import ply.lex as lex
reserved={
    'package':'PACKAGE',
    'sub':'SUB',
    'my':'MY',
    'shift':'SHIFT',
    'return':'RETURN',
    'print':'PRINT',
    'new':'NEW'
}

tokens=['STRING','COMMA','SEMI','BRACES_LEFT','BRACES_RIGHT','EQUAL','PARANTHESIS_L','PARANTHESIS_R','HASH_OP','DEREF','COMMENT',
        'NUMBER','NAME']+list(reserved.values())

t_ignore = ' \t\n'

t_STRING = r'"(.*?)"'       
t_COMMA = r','
t_SEMI = r';'
t_BRACES_LEFT = r'\{' 
t_BRACES_RIGHT = r'\}'
t_EQUAL = r'='
t_PARANTHESIS_L = r'\('
t_PARANTHESIS_R = r'\)'
t_DEREF = r'->'
t_HASH_OP = r'=>'
t_COMMENT = r'\#.*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z$@%][a-zA-Z0-9_]*'
    t.type=reserved.get(t.value,'NAME')
    return(t)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex() 

def my_lexer(perl_inp):
    file = open ("my_lexer_op","a+")
    lex.input(perl_inp)
    while True:
        tok = lex.token()
        if not tok: break
        else : 
            file.write(str(tok))
            file.write("\n")    
