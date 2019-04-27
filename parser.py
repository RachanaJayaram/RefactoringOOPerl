#Dependencies
import ply.yacc as yacc
from lexer import tokens , my_lexer
import constants_mod 
from parse_expressions import *
from parse_constructor import *
from parse_print import *
from parse_object import *
from LC import *

#global access variables
constants = constants_mod.constants

#starting point
start = 'start'

def p_start(p):
    '''start : not_package
             | package'''
    p[0] = p[1]

def p_not_package(p):
    '''not_package : body'''
    p[0] = p[1]

def p_body(p):
    '''body : statement_list
            | empty'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement'''
    print("statement_list: ",p[1:])
    if len(p) == 2:
        p[0] = p[1]
    else:
        statement_list = []
        if type(p[1]) == str:
            statement_list.append(p[1])
        else:
            statement_list = p[1]
        statement_list.append(p[2])
        p[0] = statement_list

def p_statement(p):
    '''statement : var_dec
                 | function_dec
                 | constructor
                 | object_creation
                 | obj_func_call
                 | obj_variable
                 | control_statements
                 | print_st SEMI
                 | print_st
                 | use_st
                 | arg_list SEMI
                 | comment'''
    print("statemnt: ",p[1])
    p[0] = p[1]

def p_package(p):
    '''package : package_dec body'''
    p[0] = (str(p[1]),p[2])
    constants.in_package = False

def p_package_def(p):
    '''package_dec : PACKAGE NAME SEMI'''
    p[0] = "class " + str(p[2])
    constants.in_package = True


def p_use_st(p):
    '''use_st : USE NAME SEMI
    		  | USE PARENT arg_list SEMI'''
    if len(p)==4:
        p[0] = "from " + p[2] + " import *"
    else:
        temp=[]
        p[0]=""
        for i in p[3].split(","):
            p[0] += "from "+i[1:-1]+" import "+i[1:-1]+"\n"
            temp.append(i[1:-1])
        constants.inherit =','.join(temp)

def p_function_dec(p):
    '''function_dec : SUB NAME BRACES_LEFT body BRACES_RIGHT'''
    extra=""
    if constants.in_package:
        extra="self,"
    if type(p[4])!=list:
        p[4]=[p[4]]
    p[0] = ("def " + str(p[2]) + "(" + extra + "*argv):\n" + "\targ_list=list(argv)[::-1]", p[4])
    constants.first_line = 0

def p_var_dec(p):
    '''var_dec : MY NAME ASSIGNOP SHIFT SEMI
               | MY NAME ASSIGNOP term SEMI
               | MY NAME ASSIGNOP array_statement SEMI
               | MY NAME ASSIGNOP hash_statement SEMI
               | NAME ASSIGNOP SHIFT SEMI
               | NAME ASSIGNOP term SEMI
               | NAME ASSIGNOP array_statement SEMI
               | NAME ASSIGNOP hash_statement SEMI
               | sub_script ASSIGNOP term SEMI'''
    if len(p)==6:
            var_dec_helper(p, 0) #in case my is there in the declaration
    else:
            var_dec_helper(p,1)  #in case my is not there in the declaration

def p_empty(p):
    '''empty : '''
    p[0] = ""

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = p[1] + '\n'

def p_error(p):
    if p!=None:
        print("Error at Symbol ",p.value," Line no ",p.lineno," Position ",p.lexpos)

def my_parser():

    file_name = input()  # "./input/print.pm"

    output_file_name='output'+file_name[file_name.index('/',file_name.index('/')+1):file_name.index('.',1)]+'.py'
    print(output_file_name)
    input_file = open(file_name,"r")
    perl_inp = input_file.read()
    print(perl_inp)

    file = open(output_file_name,'w+')
    my_lexer(perl_inp)
    parser = yacc.yacc()
    p = parser.parse(perl_inp)
    p = list(p)
    p= reorder(p)
    p=tuple(p)
    print("\n\n Parse tree: \n",p)

    stk = []
    lft(p,stk)
    for statement in stk:
        file.write(statement+"\n")
    file.close()
    input_file.close()

def lft(p,stk,indent = 0):
    if type(p) == list:
        indent += 1
    if type(p) == str:
        l = ['\t'*indent + statement for statement in p.split('\n')]
        stk.append('\n'.join(l))
    else:
        for node in p:
            lft(node,stk,indent)

def reorder(p):
    flag=1
    for statement in p:
        if type(statement) == str:
            statement_new = statement
            if constants.inherit and ('class' in statement) and flag:
                statement_new = statement + '( '+constants.inherit+' ) :'
                flag=0
            elif constants.inherit == False and ('class' in statement):
                statement_new+= ' :'
            p[p.index(statement)] = statement_new
        if type(statement) == list:
            statement_new2=statement
            for stat in statement:
                if ('import' in stat):
                    p.insert(0, stat)
                    statement_new2.pop(statement_new2.index(stat))
            p[p.index(statement)] = statement_new2
    return p
#calling the parser function 
my_parser()

