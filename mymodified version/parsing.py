import ply.yacc as yacc
from lexing import tokens, lexing

indent = 0

#defining the module
def p_module(p):
    '''p_module : package_dec
                | body
                | empty'''
    print("module: ",p[0:])
    p[0] = p[1]

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
                | cond_stat'''
    print("statement: ", p[0:])
    p[0] = "\t" * indent + str(p[1])

#defining the package
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
    indent+=1
    p[0] = ""

# for print statement
def p_output(p):
    '''output : KEYWORD out SEMI'''
    print(p[0:])
    p[0] = str(p[1]) + "(" + str(p[2]) + ")"


# arguments for print statement
def p_out(p):
    ''' out : VARIABLE
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
    '''argument : VARIABLE
                | STRING
                | argument COMMA argument
                | empty'''
    print(p[0:])
    p[0] = "".join(p[1:])


# defining variable declaration
def p_var_dec(p):
    '''var_dec : VARIABLE EQUALS exp SEMI
                | VARIABLE EQUALS input SEMI'''
    print(p[0:])
    p[0] = (str(p[1]) + str(p[2]) + p[3])


# right hand side of var dec
def p_exp(p):
    '''exp : NUMBER
            | VARIABLE
            | STRING
            | exp OPER exp'''
    print(p[0:])
    try:
        p[0] = "".join(p[1:])
    except:
        p[0] = str(p[1])


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
                    | KEYWORD LB for_cond RB l_braces body r_braces'''
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

def hello():
    a =[20,30,10]
    b= sorted(a)
    print(b)

# general error
def p_error(p):
    print(p)
    print("ERROR")


# empty body
def p_empty(p):
    '''empty :'''
    pass


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


