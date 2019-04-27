import ply.yacc as yacc
from lexer import tokens , my_lexer
from parse_constructor import *
from parse_print import *
from parse_object import *
from parse_expressions import *
from parse_functions import *
# from parse_array import *
from ctools import *
from parse_loops import *
import lookup_table
# import stage_1_parser
import constants_mod
import os

lookup_table=lookup_table.lookup.lookup_table
constants=constants_mod.constants
function_stack=['main']
output=[]
start ='start'

def p_start( p ):
    '''start : not_package
             | package END '''
    p[0]=p[1]

def p_package( p ) :
    'package : package_dec body'
    p[0]=(p[1],p[2])
    
def p_package_dec(p):
    'package_dec : PACKAGE NAME SEMI'    
    constants.package=1
    p[0]="class "  + str(p[2]) + " :"

def p_not_package(p):
    '''not_package : body '''
    global_variables=[]
    if 'called_functions' in lookup_table['main'].keys():
        called_functions=lookup_table['main']['called_functions']
        called_functions.append('main')
    else:
        called_functions=['main']
    for function in called_functions:
        for variable in sorted(lookup_table[function].keys()):
            if variable != 'called_functions' and variable!='returned' and variable!='defined':
                if 'global' in lookup_table[function][variable] :
                    if '' + variable not in global_variables:
                        global_variables.append('' + variable)
    global_variables=[variable + '=None' for variable in global_variables]
    param_str='\n'.join(global_variables)
    p[0]=["str_=lambda x: '' if x==None else str(x)"] + [param_str] + p[1]
def p_body( p ):
    '''body : statement_list
            | empty          
            '''
    p[0]=p[1]

def p_statement_list ( p ):
    '''statement_list : statement
                    | statement_list statement'''
    if len(p)==2:
        p[0]=p[1]
    else:   
        statement_list=[]
        if type(p[1])==str:
            statement_list.append(p[1])
        else:
            statement_list=p[1]
        statement_list=list(statement_list)
        statement_list.append(p[2])
        p[0]=statement_list


def p_statement(p):
    '''statement : var_dec
                 | function
                 | constructor
                 | object_creation
                 | o_func_call
                 | func_call
                 | print_st
                 | use_st
                 | comment  
                 | iterative
                 | return_st                             
            '''
    
    p[0]=p[1]



def p_use_st( p ):
    '''use_st : USE NAME SEMI
              | USE LIB STRING SEMI
              | USE NAME SEPERATOR NAME SEMI'''
    if p[3]==';':
        p[0]= "import " + p[2]

    # use folder::perlmodule    
    elif p[3]=='::':
        # p[0]= "from " + p[2]  +  " import " + p[4]
        p[0]="import " + p[2]  + "." + p[4] + " as " + p[4]

    #use lib ->to change @INC to find Perl modules in non-standard locations 
    else:
        p[0]="import sys\nsys.path.insert(0, " + p[3] + ")"

    
def p_function( p ):
    ''' function : function_dec BRACES_LEFT body function_braces_right'''
    body_st=p[3]
    if p[1]!=None:
        if type(p[3])==str:
            p[0]=(p[1],p[3] + p[4])
        
        else:
            p[0]=(p[1],body_st + [p[4]])
    else:
        p[0]=''
def p_function_dec( p ):
    '''function_dec : SUB NAME'''
    lookup_table[p[2]]['defined']-=1
    if lookup_table[p[2]]['defined']==0:
        function_stack.append(p[2])
        global_variables=[]
        if 'called_functions' in lookup_table[p[2]].keys():
            called_functions=lookup_table[p[2]]['called_functions']
            called_functions.append(p[2])
        else:
            called_functions=[p[2]]
        for function in called_functions:
            for variable in sorted(lookup_table[function].keys()):
                if variable != 'called_functions' and variable!='returned' and variable!='defined':
                    if 'global' in lookup_table[function][variable] :
                        if '' + variable not in global_variables:
                            global_variables.append('' + variable)
        print(global_variables)
        global_variables.append('*argv')
        param_str=' , '.join(global_variables)
        if constants.package==1:
            p[0]="\n" + "def " + str(p[2]) + " (self," + param_str + ") : \n" + "\targ_list=list(argv)[::-1]"
        else:
            p[0]="\n" + "def " + str(p[2]) + " (" + param_str + ") : \n" + "\targ_list=list(argv)[::-1]"
        constants.first_shift=0
    else:
        p[0]=None
        function_stack.append(p[2])

def p_var_dec( p ):
    '''var_dec :  NAME  ASSIGNOP term SEMI
                |  NAME  ASSIGNOP SHIFT SEMI
                |  NAME  ASSIGNOP o_func_call 
                |  MY NAME  ASSIGNOP term SEMI
                |  MY NAME  ASSIGNOP SHIFT SEMI
                |  MY NAME  ASSIGNOP o_func_call 
                |  LOCAL NAME  ASSIGNOP term SEMI
                |  LOCAL NAME  ASSIGNOP SHIFT SEMI
                |  LOCAL NAME  ASSIGNOP o_func_call
                |  NAME SEPERATOR NAME ASSIGNOP term SEMI
                |  NAME SEPERATOR NAME  ASSIGNOP SHIFT SEMI
                |  NAME SEPERATOR NAME  ASSIGNOP o_func_call
                '''
    rhs=""
    print(p[:])
    l=len(p)
    if l>=2 and p[l-2]=="shift":
        rhs=' arg_list.pop()'
    elif l>=2 and p[l-1]==';' :#case  var=5; needs work 
        rhs=p[l-2]
    elif l>=1:
        rhs=p[l-1]
    
    op=""
    global_list=""

    if p[1]=='my':
        lookup_table[function_stack[-1]][p[2][1:]]['last_used']='my'
        if lookup_table[function_stack[-1]][p[2][1:]]['my']==False:
            lookup_table[function_stack[-1]][p[2][1:]]['my']=True
        op="my_" + p[2][1:]
    elif p[1]=='local':
        print("\n\n",p[1:])
        lookup_table[function_stack[-1]][p[2][1:]]['last_used']='local'

        if lookup_table[function_stack[-1]][p[2][1:]]['local']==False:
            op='local_' + p[2][1:]
            lookup_table[function_stack[-1]][p[2][1:]]['local']=True
    elif p[2]=='::':
        if p[1]=='$main' and  'local' in lookup_table[function_stack[-1]][p[3]].keys() and lookup_table[function_stack[-1]][p[3]]['local']==True:
            op="" + p[3]
    else:
        op='' + p[1][1:]
    if constants.package==1 and constants.first_shift==0:
        constants.first_shift=1
        p[0]=[]    
    elif constants.package==1:
    
        p[0]=(global_list + "self." + op + ' = ' + str(rhs))
    
    else:
        p[0]=(global_list + op + ' = ' + str(rhs))

        # print("###",p[0],p[2])

def p_name(p):
    '''name : NAME'''
    print(p[1],function_stack)
    if lookup_table[function_stack[-1]][p[1][1:]]['last_used']=='my':
        p[0]-"my_" + p[1][1:]
    elif lookup_table[function_stack[-1]][p[1][1:]]['last_used']=='local':
        p[0]='local_' + p[1][1:]
    else:
        p[0]='' + p[1][1:]
def p_scope_res(p):
    '''scope_res : NAME SEPERATOR NAME''' 
    op=""
    if p[2]=='::':
        if p[1]=='$main':
            op=""
            p[0]=op + p[3]
        else :
            p[0]=p[1][1:] + '.' + p[3]     
def p_comment( p ):
    '''comment : COMMENT'''
    p[0]=p[1]


def p_braces_left( p ):
    '''braces_left : BRACES_LEFT'''

def p_braces_right( p ):
    '''braces_right : BRACES_RIGHT'''

def p_function_braces_right( p ):
    '''function_braces_right : BRACES_RIGHT'''
    if lookup_table[function_stack[-1]]['returned']==False:
        return_list=[]
        for variable in sorted(lookup_table[function_stack[-1]]):
            if variable!='called_functions' and variable!='returned' and  variable!='defined':
                if 'local' in lookup_table[function_stack[-1]][variable].keys() and 'global'in lookup_table[function_stack[-1]][variable].keys() :
                    return_list.append('' + variable)
                elif 'global'in lookup_table[function_stack[-1]][variable].keys() :
                    return_list.append('' + variable)
        return_list_str=",".join(return_list)
        if return_list!=[]:
            p[0]="return( " + return_list_str + " )"
        else:
            p[0]=''
    function_stack.pop()
def p_func_call( p ):
    '''func_call : NAME PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
    arg_list_plus=[]
    for variable in sorted(lookup_table[p[1]].keys()):
        # print(lookup_table,variable,function_stack[-1])
        if variable!='called_function' and variable!='returned'  and  variable!='defined' and 'global' in lookup_table[p[1]][variable]:
            if variable in sorted(lookup_table[function_stack[-1]]):
                if 'local' in lookup_table[function_stack[-1]][variable]:
                    arg_list_plus.append('local_' + variable)

                else:
                    arg_list_plus.append('' + variable)
            else:
                arg_list_plus.append('' + variable)

            
            
    op=""
    print('###',p[1],arg_list_plus)
    arg_list_str=' , '.join(arg_list_plus)
    if arg_list_plus!=[]:
        if str(p[3])!='':
            op="(" + arg_list_str + ')=' + str(p[1]) + '(  ' + arg_list_str + ' , ' + str(p[3]) + ' )'
        else:
            op="(" + arg_list_str + ')=' + str(p[1]) + '(  ' + arg_list_str + ' )'

    else:
        op=str(p[1]) + '(  ' + str(p[3]) + ' )'
    print('#',op)
    p[0]=op

def p_empty(p):
     'empty :'
     p[0]=''
def p_error(p):
    print("error",p)
    # p[0]="Error"

def p_return_st(p):
    '''return_st : RETURN arg_list SEMI'''
    lookup_table[function_stack[-1]]['returned']==True
    return_list=[]
    for variable in sorted(lookup_table[function_stack[-1]]):
            if variable!='called_functions' and variable!='returned'  and  variable!='defined':
                if 'local' in lookup_table[function_stack[-1]][variable].keys() and 'global'in lookup_table[function_stack[-1]][variable].keys() :
                    return_list.append('' + variable)
                elif 'global'in lookup_table[function_stack[-1]][variable].keys() :
                    return_list.append(variable)
    str_ret=' , '.join(return_list)
    if return_list!=[] and str(p[2])!='':
            p[0]="return(" + str(p[2]) + ' , ' + str_ret + ")"
    elif str(p[2])!='':
            p[0]="return(" + str(p[2]) + ")"
    else:
        p[0]='return()'
def p_string(p):
    '''string : STRING'''

    if p[1][1]=='$':
        string="\" " + p[1][1:]
        string=string.split()
    else:
        string=p[1].split()
    for i in range(len(string)):
        if string[i].find('$')!=-1:
            if  lookup_table[function_stack[-1]][string[i][1:]]['last_used']=='my':
                string[i]="\" + str_(" + 'my_' + string[i][1:] + ") + \""
            elif  lookup_table[function_stack[-1]][string[i][1:]]['last_used']=='local':
                string[i]="\" + str_(" + 'local_' + string[i][1:] + ") + \""
            else:
                string[i]="\" + str_(" + '' + string[i][1:] + ") + \""
    string=" ".join(string)
    if p[1][1]=='$':
        string=string[4:]
    p[0]=string
def my_parser():
    file_name=input()
    output_file_name=file_name.split('testing/input/')[1]


    # condition for when module to be tranlated is in a sub folder input/server/a.pm -> input/server/a.py
    if '/'  in output_file_name:
        output_path='testing/output/' + output_file_name[:output_file_name.rindex('/')]
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_file_name=output_path + output_file_name[output_file_name.rindex('/'):output_file_name.index('.')] + '.py'

    else:
        output_file_name='testing/output/' + output_file_name[:output_file_name.index('.')] + '.py'
    input_file= open ( file_name,"r")
    perl_inp=input_file.read()
    print(perl_inp)

    file = open (output_file_name,"w+")
    my_lexer(perl_inp)
    parser = yacc.yacc()
    p=parser.parse(perl_inp)
    print(p)
    p=tuple(p)

    print("\n\nParse tree :\n",p)
    
    stk=[]
    lft(p,stk)
    # stk=sorted(stk,key= lambda x: sort_func(x))

    # print("\n\n",stk)
    for statement in stk:
        file.write(statement + "\n")
    file.close()
    input_file.close()
   
def lft(p,stk,indent=0):

    if type(p)==list:
        indent  +=1
    if type(p)==str:
        # l=['\t'*indent + statement + "\t"*5 + "\t\t\t #indent=" + str(indent) for statement in p.split('\n')]
        l=['\t'*indent + statement for statement in p.split('\n')]

        stk.append('\n'.join(l))

    else:
        for node in p:
            lft(node,stk,indent)

my_parser()


