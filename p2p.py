import ply.lex as lex
import ply.yacc as yacc
from functools import reduce
reserved = {
    'package': 'PACKAGE',
    'sub': 'SUB',
    'my': 'MY',
    'shift': 'SHIFT',
    'return': 'RETURN',
    'print': 'PRINT'
}

class scope:
    scope_name="temp"
    scope_type="global" 
    statements=[""]

tokens = ['STRING', 'COMMA', 'NAME', 'SEMI', 'BRACES_LEFT', 'BRACES_RIGHT', 'COMMENT', 'EQUAL',
          'PARANTHESIS_L', 'PARANTHESIS_R', 'NUMBER', 'DEREF', 'HASH_OP',]+list(reserved.values())
#print(tokens)
#t_STRING = r'"(.*?)"'
t_COMMA = r','
t_ignore = '(" ")*?(\t)'
t_SEMI = r';'
t_BRACES_LEFT = r'\{'
t_BRACES_RIGHT = r'\}'
t_EQUAL = r'='
t_PARANTHESIS_L = r'\('
t_PARANTHESIS_R = r'\)'

identifiers={"function_names":[],"var_names":[],"hash_names":[],"package_names":[]}
statements=[]
no_statements=0
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_STRING(t):
    r"'([^\\']+|\\'|\\\\)*'" 
    t.value = t.value[1:-1].decode("string-escape")  
    return t

def t_NAME(t):
    r'[a-zA-Z$@%][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return(t)


t_DEREF = r'->'
t_HASH_OP = r'=>'
t_COMMENT = r'\#.*'

    
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
with open("doc.txt") as f_in:
    lines = [line.rstrip() for line in f_in]
    lines = list(line for line in lines if line)
    s = reduce(lambda x,y:x+'\n'+y,lines)
#print(s)

lex.input(s)

"""while True:
    tok = lex.token()
    if not tok:
        break
    else:
        print(tok)"""

def p_statements(p):
    '''statements : function_dec statements
                  | var_dec statements
                  | empty'''
def p_def(p):
    "def :"
    global temp
    temp=scope()

def p_function_dec(p):
    '''function_dec : SUB NAME BRACES_LEFT def statements BRACES_RIGHT'''
    global temp
    temp.statements[0]="def "+p[2]+"(*argv):\n\ti=1"
    for i in temp.statements:
        if i!=temp.statements[0]:
            print("\t"+i)
        else:
            print(i)
    del temp

def p_var_dec(p):
    '''var_dec : NAME EQUAL NUMBER SEMI'''
    global temp
    s=p[1][1:]+'='+str(p[3])
    try:
        temp.statements.append(s)
    except:
        print(s)
    


def p_empty(p):
     'empty :'
     pass


def p_error(p):
     print(p.value,"in line no",p.lineno,"is Syntax error")


parser = yacc.yacc()

res = parser.parse(s,tracking=True)  # the input

