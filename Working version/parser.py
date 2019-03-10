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
    p[0] = "class " + str(p[2]) + ":"
    constants.in_package = True
    

def p_use_st(p):
    '''use_st : USE NAME SEMI'''
    p[0] = "import " + p[2]

def p_function_dec(p):
    '''function_dec : SUB NAME BRACES_LEFT body BRACES_RIGHT'''
    extra=""
    if constants.in_package:
        extra="self,"
    p[0] = ("\n" + "def " + str(p[2]) + "(" + extra + "*argv):\n" + "\targ_list=list(argv)[::-1]", p[4])
    constants.first_line = 0

def p_var_dec(p):
    '''var_dec : my NAME ASSIGNOP SHIFT SEMI
               | my NAME ASSIGNOP term SEMI
               | NAME ASSIGNOP SHIFT SEMI
               | NAME ASSIGNOP term SEMI'''
    if len(p)==6:
        if str(p[4]) == "shift":
            if constants.in_package == True and constants.first_line == 0:
                constants.first_line = 1
                p[0] = []
            else:
                if p[2][0] == '$':
                    p[0] = ('self.' + p[2][1:] + '=arg_list.pop()')
        else:
            if p[2][0] == '$':
                if p[3] == '+=' or p[3] == '-=' or p[3] == '/=' or p[3] == '%=' or p[3] == '**=' or p[3] == '&=' or p[3] == '^=' or p[3] == '|=' or p[3] == '>>=' or p[3] == '<<=':
                    p[0] = p[2][1:] + p[3] + str(p[4])
                elif p[3] == '&&=' or p[3] == '//=' or p[3] == '||=':
                    if p[3] == '&&=':
                        p[0] = p[2][1:]+" = "+p[2][1:]+" and "+str(p[4])
                    if p[3] == '//=':
                        p[0] = p[2][1:]+" = "+"dor( "+p[2][1:]+" , "+str(p[4])+" )"
                    else:
                        p[0] = p[2][1:]+" = "+p[2][1:]+" or "+str(p[4])
                elif p[3] == '&.=' or p[3] == '^.=' or p[3] == '|.=':
                    p[0] = p[2][1:]+" = " + "strbitwise( "+p[2][1:]+" , "+p[3][0]+" , "+str(p[4])+" )"
                else:
                    if p[3] == '.=':
                        p[0] = p[2][1:] + " += " + str(p[4])
                    elif p[3] == 'x=':
                        p[0] = p[2][1:] + " *= " + str(p[4])
                    else:
                        p[0] = p[2][1:] + " = " + str(p[4])

            else:
                p[0] = p[2] + '=' + str(p[4])
    else:
        if str(p[3]) == "shift":
            if constants.in_package == True and constants.first_line == 0:
                constants.first_line = 1
                p[0] = []
            else:
                if p[1][0] == '$':
                    p[0] = ('self.' + p[1][1:] + '=arg_list.pop()')
        else:
            if p[1][0] == '$':
                if p[2] == '+=' or p[2] == '-=' or p[2] == '/=' or p[2] == '%=' or p[2] == '**=' or p[2] == '&=' or p[2] == '^=' or p[2] == '|=' or p[2] == '>>=' or p[2] == '<<=':
                    p[0] = p[1][1:] + p[2] + str(p[3])
                elif p[2] == '&&=' or p[2] == '//=' or p[2] == '||=':
                    if p[2] == '&&=':
                        p[0] = p[1][1:]+" = "+p[1][1:]+" and "+str(p[3])
                    if p[2] == '//=':
                        p[0] = p[1][1:]+" = " + \
                            "dor( "+p[1][1:]+" , "+str(p[3])+" )"
                    else:
                        p[0] = p[1][1:]+" = "+p[1][1:]+" or "+str(p[3])
                elif p[3] == '&.=' or p[3] == '^.=' or p[3] == '|.=':
                    p[0] = p[1][1:]+" = " + \
                        "strbitwise( "+p[1][1:]+" , " + \
                                    p[2][0]+" , "+str(p[3])+" )"
                else:
                    if p[2] == '.=':
                        p[0] = p[1][1:] + " += " + str(p[3])
                    elif p[2] == 'x=':
                        p[0] = p[1][1:] + " *= " + str(p[3])
                    else:
                        p[0] = p[1][1:] + " = " + str(p[3])

            else:
                p[0] = p[2] + '=' + str(p[4])

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
    p = tuple(p)
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


#calling the parser function 
my_parser()

