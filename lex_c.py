import ply.lex as lex
import ply.yacc as yacc
s1="int x;"
s='''
class a
{
    class b
    {

    }
} '''

reserved={
    'class':'class',
    'void':'void',
    'int':'int' ,
    'string':'string'

}

tokens=['class','name','number','void','equals','para_l','para_r','semi','string','int','c_l','c_r']
t_ignore = ' \t\n'

t_para_l=r'\('
t_para_r=r'\)'
t_void=r'void'
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
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type=reserved.get(t.value,'name')
    return(t)

lexer=lex.lex() 
lex.input(s)
while True:
 tok = lex.token()
 if not tok: break
 else : print(tok,"\n")



def p_body(p):
    '''body : class_dec
          | var_dec
          | empty'''
    print(list(p))
def p_class_declaration( p ) :
    'class_dec : class name c_l body c_r'
    print("class",p[2])
    print("!!!!!",list(p))
def p_empty(p):
     'empty :'
     pass
 
def p_var_declaration( p ):
    '''var_dec : int name semi'''
    print(p[2])
def p_error(p):
     print("!!!!!",p)
     print("Syntax error in input!")
 
 # Build the parser
parser = yacc.yacc()

res = parser.parse(s) # the input
#res = parser.parse("class namespace{int id; void thing();}") # the input
print(res)
