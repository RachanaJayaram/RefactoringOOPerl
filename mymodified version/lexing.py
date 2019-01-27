import ply.lex as lex

#lexing part

# for reserved keywords
reserved = {
    'package' : 'PACKAGE',
    'sub' : 'SUB',
    'my' : 'MY',
    'shift' : 'SHIFT',
    'return' : 'RETURN',
    'new' : 'NEW',
    'bless' : 'BLESS',
    '@' : 'ARRAY',
    '%' : 'HASH'
}

#token names
tokens = [
    'NUMBER',
    'OPER',
    'SCALAR',
    'STRING',
    'HASH_OP',
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
]+list(set(reserved.values()))

#rules
t_ignore = " \t"
t_HASH_OP = r'=>' 
t_COMMA = r','
t_SEMI = r';'
t_EQUALS = r'='
t_LFB = r'{'
t_RFB = r'}'
t_RB = r'\)'
t_LB = r'\('
t_ALB = r'<'
t_ARB = r'>'
t_OPER = r'(\+|\*|/|-|%|!|&&|\|\|)'
t_COMMENT = r'\#.*'

#token definitions
def t_STRING(t):
    r'"[^"]*"'
    return t
def t_KEYWORD(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value,'KEYWORD')
    return t
def t_SHIFT(t):
    r'@_'
    return t
def t_SCALAR(t):
    r'(@|\$|%)[^ ,\t\n(){}<>;=!\+\*/-]+'
    t.type = reserved.get(str(t.value)[0],'SCALAR')
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
    lexer.input(data)
    file = open("mymodified version/PERL/lexout","w+")
    while True:
        tok = lexer.token()
        if not tok: break
        #print(tok)
        file.write(str(tok))
        file.write("\n")

inp_file = open("mymodified version/PERL/testing.pl","r")
data = inp_file.read()
lexing(data)