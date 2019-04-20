import ply.lex as lex
reserved={
    'package':'PACKAGE',
    'sub':'SUB',
    'use' : 'USE',
    'my':'MY',
    'shift':'SHIFT',
    'return':'RETURN',
    'print':'PRINT',
    'new':'NEW',
    'not':'WNOT',
    'xor':'WXOR',
    'and':'WAND',
    'or':'WOR',
    'q':"Q",
    "qq":"QQ",
    "qx":"QX",
    'bless': 'BLESS',
    'qw':'QW',
    'for':'FOR',
    'while':'WHILE',
    'do':'DO',
    'until':'UNTIL',
    'foreach':'FOREACH',
    'if':'IF',
    'elsif':'ELSIF',
    'unless':'UNLESS',
    'else':'ELSE',
    'parent':'PARENT',
    'DESTROY':'destroy',
    'scalar' : 'SCALAR'
}

literals=['!','~','x','>','<',':','?','[',']']

tokens = ['STRING', 'RANGE', 'COMMA', 'SEMI', 'BRACES_LEFT', 'BRACES_RIGHT', 'PARANTHESIS_L', 'PARANTHESIS_R', 'HASH_OP', 'DEREF', 'COMMENT', 'NUMBER', 'NAME', 'POWOP', 'ASSIGNOP',
          'MULOP', 'ADDOP', 'SHIFTOP', 'RELOP', 'EQOP', 'BITANDOP', 'BITOROP', 'DOTDOT', 'ANDAND', 'OROR', 'DORDOR', 'MATCHOP', 'INCREMENT', 'DECREMENT']+list(reserved.values())

t_ignore = ' \t'
t_STRING = r""""([^"\\]|\\.|\\\n)*"|'([^'\\]|\\.|\\\n)*'"""
t_COMMA = r','
t_SEMI = r';'
t_BRACES_LEFT = r'\{' 
t_BRACES_RIGHT = r'\}'
t_PARANTHESIS_L = r'\('
t_PARANTHESIS_R = r'\)'
t_COMMENT = r'\#.*'


def t_DOTDOT(t):
     r'(\.\.)'
     return t

def t_DEREF(t):
    r'->'
    return t

def t_HASH_OP(t):
     r'=>'
     return t

def t_INCREMENT(t):
     r'\+\+'
     return t

def t_NAME(t):
    r'[$@%]?[a-zA-Z][a-zA-Z0-9_]*'
    t.value=t.value
    t.type=reserved.get(t.value,'NAME')
    return t
    
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_DECREMENT(t):
     r'--'
     return t

def t_SHIFTOP(t):
     r'(<<)|(>>)'
     return t


def t_DORDOR(t):
     r'//'
     return t
def t_RELOP(t):
     r'(>=)|(<=)|(>)|(<)|(gt)|(lt)|(le)|(ge)'
     return t

def t_EQOP(t):
     r'(==)|(eq)|(!=)|(<=>)|(ne)|(cmp)|(~~)'
     return t

def t_NUMBER(t):
    r'[-+]?((0[xX]){1}[0-9a-fA-Z]*\.?[0-9a-fA-Z]+([p][-+]?[0-9]+)?)|((0[xX]){0}[0-9]*)\.?[0-9]+([eE][-+]?[0-9]+)?'
    if ('x' in t.value) and ("p" in t.value) :
        t.value = float.fromhex(t.value)
    elif ('x' in t.value):
        t.value = int(t.value,16)
    elif ("." in t.value) or ("e" in t.value) or ("E" in t.value):
        t.value=float(t.value)
    else:
        t.value = int(t.value)
    return t
 
def t_ASSIGNOP(t):
     r'''(=)|(\+=)|(-=)|(\*=)|(\*\*=)|(/=)|(%=)|(&=)|(//=)|(&&=)|(\|=)|(\|\|=)|(\^=)|(x=)|(\.=)|(&\.=)|(\|\.=)|(\^\.=)|(>>=)|(<<=)'''
     return t
def t_POWOP(t):
     r'\*\*'
     return t
def t_MULOP(t):
     r'(\*)|(/)|(%)'
     return t
def t_ADDOP(t):
     r'''(\+)|(-)|(\.)'''
     return t
def t_ANDAND(t):
     r'&&'
     return t
def t_OROR(t):
     r'\|\|'
     return t
def t_BITANDOP(t):
     r'&'
     return t
def t_BITOROP(t):
     r'(\|)|(\^)'
     return t
def t_MATCHOP(t):
     r'(~=)|(!~)'
     return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex() 

def my_lexer(perl_inp):
    file = open ("my_lexer_op","w+")
    lex.input(perl_inp)
    while True:
        tok = lex.token()
        if not tok: break
        else : 
               #print(str(tok))
               file.write(str(tok))
               file.write("\n")  


#perl_inp = open("./input/print.pm")
#perl_inp=perl_inp.read()
#my_lexer(perl_inp)
