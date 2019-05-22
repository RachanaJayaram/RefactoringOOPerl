

import ply.yacc as yacc
from lexer import tokens , my_lexer
import os

lookup_table={}
lookup_table['main']={'defined':1}
function_stack=['main']




output=[]
start ='start'

def p_start( p ):
    '''start : not_package
             | package END empty '''

def p_package( p ) :
    'package : package_dec body'
   
def p_package_dec(p):
    'package_dec : PACKAGE NAME SEMI'    

def p_not_package(p):
    '''not_package : body '''

def p_body( p ):
    '''body : statement_list
            | empty          
            '''

def p_statement_list ( p ):
    '''statement_list : statement
                    | statement_list statement'''

def p_statement(p):
    '''statement : var_dec
                 | function
                 | constructor
                 | object_creation
                 | o_func_call
                 | func_call
                 | print_st
                 | control_statements
                 | use_st
                 | comment  
                 | iterative
                 | return_st                             
            '''

def p_use_st( p ):
    '''use_st : USE NAME SEMI
              | USE LIB STRING SEMI
              | USE NAME SEPERATOR NAME SEMI'''

def p_function( p ):
    ''' function : function_dec braces_left body function_braces_right'''

def p_function_dec( p ):
    '''function_dec : SUB NAME'''
    function_stack.append(p[2])
    if p[2] not in lookup_table.keys():
        lookup_table[p[2]]={'defined':1}
    else:
        lookup_table[p[2]]['defined']+=1

    
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
    p_copy=p[:]
    if p_copy[2]=="$,":
        p_copy[2]="$sep_"
    if p_copy[2]=="$\\":
        p_copy[2]="$end_"
    if p_copy[1]=="$\\":
        p_copy[1]="$end_"
    if p_copy[1]=="$,":
        p_copy[1]="$sep_"
    if p_copy[1]=='my':
        if p_copy[2][1:] not in  lookup_table[function_stack[-1]].keys():
            lookup_table[function_stack[-1]][p_copy[2][1:]]=['my']
        else:
            lookup_table[function_stack[-1]][p_copy[2][1:]].append('my')
    elif p_copy[1]=='local':
        if p_copy[2][1:] not in  lookup_table[function_stack[-1]].keys():
            lookup_table[function_stack[-1]][p_copy[2][1:]]=['local']
        else:
            lookup_table[function_stack[-1]][p_copy[2][1:]].append('local')

    elif p_copy[2]!='::':
        if p_copy[1][1:] not in  lookup_table[function_stack[-1]].keys():
           lookup_table[function_stack[-1]][p_copy[1][1:]]=['global']
    else:
        if p_copy[1]=='$main' :
            if p_copy[3] not in  lookup_table[function_stack[-1]].keys():
                lookup_table[function_stack[-1]][p_copy[3]]=['global']
            else :
                lookup_table[function_stack[-1]][p_copy[3]].append('global')
            if p[3] not in  lookup_table['main'].keys():
                lookup_table['main'][p_copy[3]]=['global']
        

def p_name(p):
    '''name : NAME'''
    name=p[1]
    if p[1][1:]==',':
            var_name="$sep_"
    elif p[1][1:]=='\'':
            var_name="$end_"
    else:
            var_name=p[1]
    if name[1:] not in  lookup_table[function_stack[-1]].keys():
        lookup_table[function_stack[-1]][var_name[1:]]=['global']

def p_scope_res(p):
    '''scope_res : NAME SEPERATOR NAME'''
    if p[1]=='$main' :
            if p[3] not in  lookup_table[function_stack[-1]].keys():
                lookup_table[function_stack[-1]][p[3]]=['global']
            else :
                lookup_table[function_stack[-1]][p[3]].append('global')
            if p[3] not in  lookup_table['main'].keys():
                lookup_table['main'][p[3]]=['global']

def p_string(p):
    '''string : STRING'''
    string=p[1].split()
    print(string)
    try:
        if string[0][1]=='$':
            string[0]=string[0][2:]
    except:
        pass

    if "end_" not in  lookup_table[function_stack[-1]].keys():
                lookup_table[function_stack[-1]]["end_"]=['global']        
    if "sep_" not in  lookup_table[function_stack[-1]].keys():
                lookup_table[function_stack[-1]]["sep_"]=['global']        
    for i in range(len(string)):
        if string[i].find('$')!=-1:
            if string[i][1:] not in  lookup_table[function_stack[-1]].keys():
                lookup_table[function_stack[-1]][string[i][1:]]=['global']
def p_comment( p ):
    '''comment : COMMENT'''

def p_braces_left( p ):
    '''braces_left : BRACES_LEFT'''

def p_function_braces_right( p ):
    '''function_braces_right : BRACES_RIGHT'''
    function_stack.pop()

def p_braces_right( p ):
    '''braces_right : BRACES_RIGHT'''
def p_empty(p):
     'empty :'

def p_error(p):
    print("error",p)

def p_return_st(p):
    '''return_st : RETURN arg_list SEMI'''

def p_print_st(p):
    '''print_st : PRINT arg_list SEMI ''' 

def p_object_creation( p ):
    '''object_creation : NAME ASSIGNOP NAME DEREF NEW PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''

def p_control_statements(p):
    '''control_statements : iterative '''

def p_iterative(p):
    '''iterative : for_st
                 | while_st'''

def p_for_st(p):
    '''for_st : FOR PARANTHESIS_L  NAME ASSIGNOP term SEMI NAME RELOP term SEMI NAME INCREMENT  PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT
              | FOR PARANTHESIS_L  NAME ASSIGNOP term SEMI NAME RELOP term SEMI NAME DECREMENT  PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT'''

def p_while_st(p):
    '''while_st : WHILE PARANTHESIS_L NAME RELOP term PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT
                | WHILE PARANTHESIS_L term PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT'''
 
 
def p_o_func_call( p ):
    '''o_func_call : NAME DEREF NAME PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
def p_func_call( p ):
    '''func_call : NAME PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
    if 'called_functions' not in lookup_table[function_stack[-1]].keys():
        lookup_table[function_stack[-1]]['called_functions']=[p[1]]
    else:
        lookup_table[function_stack[-1]]['called_functions'].append(p[1])


def p_arg_list(p):
    '''arg_list : arg 
                | arg_list COMMA arg'''
def p_arg(p):
    '''arg : name
           | scope_res
           | var_deref
           | string 
           | NUMBER
           | empty
           | term'''

def p_var_deref(p):
    ''' var_deref : NAME DEREF BRACES_LEFT NAME BRACES_RIGHT'''

def p_constructor(p):
    '''constructor : SUB NEW braces_left constructor_body braces_right '''

def p_constructor_body(p):
    '''constructor_body : statement constructor_hash bless return_constructor'''
  
def p_constructor_hash(p):
    '''constructor_hash : MY NAME ASSIGNOP BRACES_LEFT hash_statement_list BRACES_RIGHT SEMI'''

def p_hash_statement_list(p):
    '''hash_statement_list : hash_statement
                           | hash_statement_list COMMA hash_statement'''

def p_hash_statement(p):
    '''hash_statement : NAME HASH_OP SHIFT
                      | NAME HASH_OP term '''
def p_bless(p):
    '''bless : BLESS PARANTHESIS_L  NAME COMMA NAME PARANTHESIS_R SEMI'''

def p_return_constructor(p):
    '''return_constructor : RETURN  NAME  SEMI'''

addmulop=['+','-','**','*','/','%','x','.']
match={'gt':'>','lt':'<','ge':'>=','le':'<=','eq':'==','ne':'!=','&&':'and','||':'or'}
bit=['&','|','^']
intops=['<<','>>','~'] #work only on ints
iss=lambda x: (type(x)==str) and (("'" in x) or ('"' in x)) #check if term is string
iv=lambda x: (type(x) == str) and (("$" in x) or ('%' in x) or ('@' in x) ) #check if term is variable 
start ='body'

precedence = ( #operator precedence and associativity table 
     ('left', 'WOR', 'WXOR'),
     ('left', 'WAND'),
     ('right','WNOT'),
     ('left','COMMA','HASH_OP'),
     ('right','ASSIGNOP'),
     ('nonassoc','DOTDOT'),
     ('left','OROR','DORDOR'),
     ('left','ANDAND'),
     ('left','BITOROP'),
     ('left','BITANDOP'),
     ('nonassoc','RELOP'),
     ('left','SHIFTOP'),
     ('left','ADDOP'),
     ('left','MULOP'),
     ('left','MATCHOP'),
     ('right','!','~'),
     ('right','UMINUS'),
     ('right', 'POWOP'),
     ('nonassoc','INCREMENT','DECREMENT'),
     ('left','DEREF'),
)



# binary operators
def p_termbinop(p):  
    '''termbinop : term POWOP term
                | term MULOP term
                | term ADDOP term
                | term SHIFTOP term
                | term RELOP term
                | term EQOP term
                | term BITANDOP term
                | term BITOROP term
                | term DOTDOT term
                | term ANDAND term
                | term OROR term
                | term DORDOR term
                | term MATCHOP term
                | term WAND term
                | term WOR term
                | term WXOR term'''

def p_termunop(p):
    '''termunop : ADDOP term %prec UMINUS 
               | '!' term
               | '~' term 
               | term INCREMENT
               | term DECREMENT
               | term DEREF
               | INCREMENT term
               | DECREMENT term
               | WNOT term'''

def p_term(p):
    '''term : termbinop
	       | termunop 
           | PARANTHESIS_L term PARANTHESIS_R
           | name
           | NUMBER
           | string
           | Q BRACES_LEFT NAME BRACES_RIGHT
           | QQ BRACES_LEFT NAME BRACES_RIGHT
           | var_deref
           | QX BRACES_LEFT NAME BRACES_RIGHT'''

def my_parser(file_name):
    print(file_name)
    output_file_name=file_name.split('testing/input/')[1]
    if '/'  in output_file_name:
        output_path='testing/look_up/look_up_'+output_file_name[:output_file_name.rindex('/')]
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        output_file_name=output_path+output_file_name[output_file_name.rindex('/'):output_file_name.index('.')]+'.txt'

    else:
        output_file_name='testing/look_up/look_up_'+output_file_name[:output_file_name.index('.')]+'.txt'
    
    input_file= open ( file_name,"r")
    perl_inp=input_file.read()
    perl_inp=perl_inp.replace("$,","$sep_")
    perl_inp=perl_inp.replace("$\\","$end_")
    print(perl_inp)
    file = open (output_file_name,"w+")

    my_lexer(perl_inp)
    parser = yacc.yacc()
    parser.parse(perl_inp)
    for key in lookup_table.keys():
        lookup_table[key]['returned']=False
        for key1 in lookup_table[key].keys():
            if key1!='called_functions' and key1!='returned' and key1!='defined':
                scope_list=lookup_table[key][key1]
                lookup_table[key][key1]={"last_used":'global'}
                
                for scope in scope_list:
                    lookup_table[key][key1][scope]=False
    for key in lookup_table.keys():
        file.write("\n"+str(key)+"\n")
        print("\n"+str(key))
        for key1 in lookup_table[key].keys():
            file.write(key1+':'+str(lookup_table[key][key1])+"\n")
            print(key1+':'+str(lookup_table[key][key1]))
    file.write("\n#lookup_table:"+str(lookup_table) )
    file.close()
    lookup_file = open("lookup_table.py","w+")
    lookup_file.write("class lookup:\n\tlookup_table="+str(lookup_table))
    lookup_file.close()
    input_file.close()



if __name__ == "__main__":  
    try:
        f_name=open("server/scratch_pad.txt","r")
    except: 
        f_name=open("scratch_pad.txt","r")

    f=f_name.readline()
    f_name.close()
    print(f)
    my_parser(f)