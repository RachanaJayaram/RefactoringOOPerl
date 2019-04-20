#defining the constructor logics

def p_constructor(p):
    '''constructor : SUB NEW BRACES_LEFT constructor_body BRACES_RIGHT'''
    output = "\n" + "def __init__(self,*argv) : \n"
    output += "\t" + "arg_list = list(argv)[::-1]\n"
    output += "\t" + "self.__dict__.update("
    p[0] = output + p[4] + ')'

def p_constructor_body(p):
    '''constructor_body : statement constructor_hash bless_st return_constructor'''
    p[0] = p[2]

def p_constructor_hash(p):
    '''constructor_hash : my NAME ASSIGNOP hash_statement SEMI'''  # can remove it and add it to var_dec itself. Try it
    p[0] = p[5]


def p_hash_statement(p):
    '''hash_statement : BRACES_LEFT hash_statement_list BRACES_RIGHT'''
    p[0] = '{ '+p[2]+' }'


def p_hash_statement_list(p):  
    '''hash_statement_list : hash_statement_part
                           | hash_statement_list COMMA hash_statement_part'''
    p[0] = ''.join(p[1:]) 

def p_hash_statement_part(p):
    '''hash_statement_part : NAME HASH_OP SHIFT
                      | NAME HASH_OP term'''
    if p[3] == "shift":
        p[0] = "'" + p[1] + "':arg_list.pop()"
    else:
        p[0] = "'" + p[1] + "':" +p[3]

def p_bless_st(p):
    '''bless_st : BLESS PARANTHESIS_L NAME COMMA NAME PARANTHESIS_R SEMI'''

def p_return_constructor(p):
    '''return_constructor : RETURN NAME SEMI'''

