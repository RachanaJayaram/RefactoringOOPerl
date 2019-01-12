import ply.lex as lex
import ply.yacc as yacc
s1="int x;"
s='''
package date; '''

reserved={
    
    'package':'PACKAGE',
    'sub':'SUB',
    'new':'NEW',
    'my':'MY',
    'shift':'SHIFT',
    'bless':'BLESS',
    'return':'RETURN',
    'print':'PRINT'

}

tokens=['name','number','equals','para_l','para_r','semi','c_l','c_r']+list(reserved.values())
t_ignore = ' \t\n'

t_para_l=r'\('
t_para_r=r'\)'

#
t_c_l=r'\{'
t_c_r=r'\}'
t_semi=r';'
t_equals = r'='
#t_name=r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
def t_number(t):
 r'\d+'
 t.value = int(t.value)
 return t
def t_name(t):
    r'[$@%][a-zA-Z0-9_]*'
    t.type=reserved.get(t.value,'name')
    return(t)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer=lex.lex() 
lex.input(s)
while True:
 tok = lex.token()
 if not tok: break
 else : print(tok,"\n")

