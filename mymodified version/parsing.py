import ply.yacc as yacc
from lexing import tokens, lexing
import re

indent = 0
fLine = 0

# defining the body of the context
def p_body(p):
    '''body : statementlist
            | empty'''
    print("body: ", p[0:])
    p[0] = p[1]


# list of statements in the body
def p_statementlist(p):
    '''statementlist : statement
                    | statementlist statement'''
    print("statementlist: ", p[0:])
    p[0] = "\n".join(p[1:])


# defining the statement
def p_statement(p):
    '''statement : var_dec
                | function_call
                | output
                | comment
                | cond_stat
                | package_dec
                | cons_dec
                | function_def
                | return_st'''
    print("statement: ", p[0:])
    p[0] = "\t" * indent + str(p[1])

# defining the constructor
def p_cons_dec(p):
    '''cons_dec : '''

# defining the package
def p_package_dec(p):
    '''package_dec : PACKAGE KEYWORD SEMI upind body lowind NUMBER SEMI'''
    print("package: ",p[0:])
    p[0] = "class " + p[2] + ":\n" + p[5]

# for incrementing indentation
def p_upind(p):
    '''upind :'''
    global indent
    indent+=1
    p[0] = ""

# for decrementing indentation
def p_lowind(p):
    '''lowind :'''
    global indent
    indent-=1
    p[0] = ""

# defining the function definition of the class
def p_function_def(p):
    '''function_def : SUB KEYWORD block'''
    p[0] = "def " + p[2] + "(self,*argv)" + ":\n" + p[3]
    global fLine
    fLine = 0

# for print statement
def p_output(p):
    '''output : KEYWORD out SEMI'''
    print(p[0:])
    p[0] = str(p[1]) + "(" + str(p[2]) + ")"


# arguments for print statement
def p_out(p):
    ''' out : variable
            | STRING
            | out COMMA out'''
    print(p[0:])
    p[0] = "".join(p[1:])


# defining function calls
def p_function_call(p):
    ''' function_call : KEYWORD LB argument RB SEMI'''
    print(p[0:])
    p[0] = "".join(p[1:5])


# arguments for the function call
def p_argument(p):
    '''argument : variable
                | STRING
                | NUMBER
                | argument COMMA argument
                | empty'''
    print(p[0:])
    p[0] = "".join(p[1:])


# defining variable declaration
def p_var_dec(p):
    '''var_dec : scalar_var EQUALS exp SEMI
                | variable EQUALS input SEMI
                | variable EQUALS SHIFT SEMI
                | arr_var EQUALS arr_exp SEMI
                | hash_var EQUALS hash_exp SEMI'''
    print(p[0:])
    if p[3] == "shift":
        global fLine
        fLine +=1
        if fLine == 1:
            p[0] = "arg = (list(argv)[1:]).reverse()"
        else:
            p[0] = p[1] + p[2] + "arg.pop()"
    else:
        p[0] = str(p[1]) + str(p[2]) + p[3]

# variable decider
def p_variable(p):
    '''variable : scalar_var
                | arr_var
                | hash_var'''
    p[0] = p[1]

# defining scalar variable
def p_scalar_var(p):
    '''scalar_var : MY SCALAR
                | SCALAR'''
    if p[1] == "my":
        p[0] = p[2]
    else:
        p[0] = p[1]

# defining array variable
def p_arr_var(p):
    '''arr_var : MY ARRAY
                | ARRAY'''
    if p[1] == "my":
        p[0] = p[2]
    else:
        p[0] = p[1]

# defining hash variable
def p_hash_var(p):
    '''hash_var : MY HASH
                | HASH'''
    if p[1] == "my":
        p[0] = p[2]
    else:
        p[0] = p[1] 

# defining return statement
def p_return_st(p):
    '''return_st : RETURN exp SEMI'''
    p[0] = p[1] + " " + p[2]

# right hand side of var dec
def p_exp(p):
    '''exp : NUMBER
            | STRING
            | var
            | exp OPER exp'''
    print(p[0:])
    try:
        p[0] = "".join(p[1:])
    except:
        p[0] = str(p[1])

# definig the array
def p_arr_exp(p):
    '''arr_exp :  LB argument RB'''
    p[0] = "[" + p[2] + "]"

# defining the hash
def p_hash_exp(p):
    '''hash_exp : first_hash
                | second_hash'''
    p[0] = p[1]

# defining first type of hash declaration
def p_first_hash(p):
    '''first_hand : LB argument RB'''
    p[0] = "{"
    key = True
    for i in p[2].split(","):
        if key:
            p[0] = p[0] + str(i) + ":"
            key = False
        else:
            p[0] = p[0] + str(i) + ","
            key = True
    p[0] = p[:-1] + "}"

# defining second type of hash declaration
def p_second_hand(p):
    '''second_hand : LB hash_arg RB'''
    p[0] ="{"
    key = True
    for i in re.split("=>|,",p[2]):
        if key:
            p[0] = p[0] + str(i) + ":"
            key = False
        else:
            p[0] = p[0] + str(i) + ","
            key = True
    p[0] = p[:-1] + "}"
 
# defining hash argument
def p_hash_arg(p):
    '''hash_arg : STRING
                | NUMBER
                | hash_arg HASH_OP hash_arg
                | hash_arg COMMA hash_arg'''
    p[0] = "".join(p[1:])

# to handle stdin (perl input)
def p_input(p):
    '''input : ALB KEYWORD ARB'''
    print(p[0:])
    p[0] = "input()"


# defining comments
def p_comment(p):
    '''comment : COMMENT'''
    print(p[0:])
    p[0] = p[1]


# checking for conditional statements
def p_cond_stat(p):
    '''cond_stat : KEYWORD LB condition RB block
                    | KEYWORD LB for_cond RB block'''
    print(p[0:])
    p[0] = (str(p[1]) + " " + p[3] + ":\n" + str(p[6]))


# defining the arguments for 'for'
def p_for_cond(p):
    '''for_cond : VARIABLE EQUALS exp SEMI VARIABLE sign exp SEMI increment'''
    if len(p[6]) > 1:
        if p[6][0] != '!':
            p[7] = p[7] + "+1"
    p[0] = str(p[1]) + " in range(" + p[3] + "," + p[7] + "," + p[9] + ")"


# defining the increment part
def p_increment(p):
    '''increment : VARIABLE OPER OPER
                    | VARIABLE sign exp'''
    if len(p[2]) == 1:
        p[0] = p[2] + "1"
    else:
        sign = p[2][1]
        p[0] = sign + p[3]


# defing the block
def p_block(p):
    '''block : l_braces body r_braces'''
    p[0] = p[2]


# defing begining of a block
def p_l_braces(p):
    '''l_braces : LFB'''
    global indent
    indent += 1


# defining the ending of the block
def p_r_braces(p):
    '''r_braces : RFB'''
    global indent
    indent -= 1


# defining the condition for conditional statements
def p_condition(p):
    '''condition : VARIABLE sign exp'''
    print(p[0:])
    p[0] = str(p[1]) + p[2] + str(p[3])


# checking for the operators used
def p_sign(p):
    '''sign : EQUALS
            | OPER
            | ALB
            | ARB
            | sign sign'''
    print(p[0:])
    p[0] = "".join(p[1:])

# general error
def p_error(p):
    print(p)
    print("ERROR")


# empty body
def p_empty(p):
    '''empty :'''
    p[0] =  ""


# function which does the parsing
def parsing():
    inp_file = open("mymodified version/PERL/testing.pl", "r")
    inp_data = inp_file.read()
    lexing(inp_data)
    parser = yacc.yacc()
    p = parser.parse(inp_data)
    print(p)
    out_file = open("mymodified version/PERL/pyequi.py", "w+")
    for statement in p.split("\n"):
        out_file.write(statement + "\n")
    out_file.close()
    inp_file.close()


parsing()


