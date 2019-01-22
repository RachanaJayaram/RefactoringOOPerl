import ply.lex as lex

#lexing part
#token names
tokens = (
    'NUMBER',
    'OPER',
    'VARIABLE',
    'STRING',
    'COMMA',
    'SEMI',
    'EQUALS',
    'newl',
    'KEYWORD',
    'LFB',
    'RFB',
    'COMMENT',
    'LB',
    'RB',
    'ALB',
    'ARB'
)

#rules
t_ignore = " \t"
t_COMMA = r','
t_SEMI = r';'
t_EQUALS = r'='
t_LFB = r'{'
t_RFB = r'}'
t_RB = r'\)'
t_LB = r'\('
t_ALB = r'<'
t_ARB = r'>'
t_OPER = r'(\+|\*|/|-|%|!)'
t_COMMENT = r'\#.*'

#token definitions
def t_STRING(t):
    r'"[^"]*"'
    return t
def t_KEYWORD(t):
    r'[a-zA-Z]+'
    return t
def t_VARIABLE(t):
    r'(@|\$|%)[^ \t\n(){}<>;=!\+\*/-]+'
    t.value = str(t.value)[1:]
    return t
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newl(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Illegal character '%s'"%t.value[0])
    t.lexer.skip(1)

def lexing(data):
    lexer = lex.lex()
    #testing
    lexer.input(data);
    file = open("./PERL/lexout","w+")
    while True:
        tok = lexer.token()
        if not tok: break
        #print(tok)
        file.write(str(tok))
        file.write("\n")

