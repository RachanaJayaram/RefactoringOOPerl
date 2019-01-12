import ply.lex as lex
import ply.yacc as yacc

file=open("date.pm","r")
s=file.read()
s='''   
    sub try
    {
    
    }
  '''
reserved={
    'package':'PACKAGE',
    'sub':'SUB',
    'my':'MY',
    'shift':'SHIFT',
    'return':'RETURN',
    'print':'PRINT'
}

tokens=['STRING','COMMA','NAME','SEMI','BRACES_LEFT','BRACES_RIGHT','COMMENT','EQUAL','PARANTHESIS_L','PARANTHESIS_R','NUMBER','DEREF','HASH_OP']+list(reserved.values())
#print(tokens)
t_STRING= r'"(.*?)"'       
t_COMMA=r','
t_ignore = ' \t\n'
t_SEMI = r';'
t_BRACES_LEFT = r'\{' 
t_BRACES_RIGHT = r'\}'
t_EQUAL = r'='
t_PARANTHESIS_L = r'\('
t_PARANTHESIS_R = r'\)'
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_NAME(t):
    r'[a-zA-Z$@%][a-zA-Z0-9_]*'
    t.type=reserved.get(t.value,'NAME')
    return(t)

t_DEREF = r'->'
t_HASH_OP = r'=>'
t_COMMENT = r'\#.*'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer=lex.lex() 
lex.input(s)
#print(s)
while True:
    tok = lex.token()
    if not tok: break
    else : print(tok,"\n")


class_name=[]

def p_body(p):
    '''body : package_dec
            | var_dec
            | function_dec
            | hash_dec
            | empty'''
 #   print("list_of_p",list(p))

def p_var_dec( p ):
    '''var_dec : MY NAME EQUAL SHIFT SEMI
               | MY NAME EQUAL BRACES_LEFT hash_dec BRACES_RIGHT SEMI'''
#    print("var",list(p))
    if(p[4]=="shift"):
        if(p[2][0]=='$'):
            print("\t\t",p[2][1:],'= argv[i+=1]')
def p_package_dec( p ) :
    'package_dec : PACKAGE NAME SEMI body '
    class_name.append(p[2])
    print("class",p[2],":")
 #   print("!!!!!",list(p))
def p_function_dec( p ):
    '''function_dec : SUB NAME  BRACES_LEFT hash_dec BRACES_RIGHT
                    | SUB NAME  BRACES_LEFT empty BRACES_RIGHT
                    | SUB NAME  BRACES_LEFT var_dec BRACES_RIGHT'''
    if(p[2]=="new"):
 #       print(class_name)
        print("\tdef",class_name[len(class_name)-1],"(*argv):")
    else: 
        print("\tdef",p[2] ,"(*argv):");
    print("\t\t i=-1")

def p_hash_dec( p ):
    '''hash_dec : NAME HASH_OP SHIFT BRACES_RIGHT SEMI 
                | NAME HASH_OP SHIFT COMMA hash_dec'''
    if(p[4]=='BRACES_RIGHT'):
        print("\t\t",p[1],'=argv[i++]')
def p_empty(p):
     'empty :'
     pass
def p_error(p):
     print("####",p)
     print("Syntax error in input!")
parser = yacc.yacc()

res = parser.parse(s) # the input
