import ply.yacc as yacc
from lexer import tokens , my_lexer
output=[]
indent=1
constructor_stack=[]
start ='package_dec'

def p_body( p ):
    '''body : statement_list
            | empty          
            '''

def p_statement_list ( p ):
    '''statement_list : statement
                    | statement_list statement'''

def p_statement(p):
    '''statement : var_dec
                 | function_dec
                 | comment                 
            '''

def p_package_dec( p ) :
    'package_dec : PACKAGE NAME SEMI body'
    output.append("class "+str(p[2])+" :")
    

def p_function_dec( p ):
    '''function_dec : SUB NAME  braces_left body braces_right'''

    output.append("\t"*indent+"def "+str(p[2])+" (*argv) : \n"+"\t"*(indent+1)+"i=0 ")

def p_var_dec( p ):
    '''var_dec : MY NAME EQUAL SHIFT SEMI'''
    if(p[4]=="shift"):
        if(p[2][0]=='$'):
            output.append("\t"*indent+p[2][1:]+'= argv[i]\n'+"\t"*indent+"i+=1")

def p_comment( p ):
    '''comment : COMMENT'''
    output.append(p[1]) 

def p_braces_left( p ):
    '''braces_left : BRACES_LEFT'''
    global indent
    indent+=1

def p_braces_right( p ):
    '''braces_right : BRACES_RIGHT'''
    global indent
    indent-=1

def p_empty(p):
     'empty :'
     pass

def p_error(p):
     output.append(str(p))
     output.append("Syntax error in input!")
     print(output)

def my_parser():
    input_file= open ( "input_code.pm ","r")
    perl_inp=input_file.read()
    print(perl_inp)

    file = open ("python_code.py","w+")
    
    my_lexer(perl_inp)
    parser = yacc.yacc()
    parser.parse(perl_inp)
    for statement in reversed(output):
        file.write(statement+"\n")
    file.close()
    input_file.close()

my_parser()
