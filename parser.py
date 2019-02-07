# Dependencies
import ply.yacc as yacc
from lexer import tokens , my_lexer
import re

# variables
output=[]
stack=[]
addmulop=['+','-','**','*','/','%','x','.']
match={'gt':'>','lt':'<','ge':'>=','le':'<=','eq':'==','ne':'!=','&&':'and','||':'or'}
bit=['&','|','^']
intops=['<<','>>','~'] #work only on ints
iss=lambda x: (type(x)==str) and (("'" in x) or ('"' in x)) #check if term is string
iv=lambda x: (type(x) == str) and (("$" in x) or ('%' in x) or ('@' in x) ) #check if term is variable 
start ='body'

# in variables
indent = 0
pac = False
incons = False
inpac = False
fline = 0

precedence = ( #operator precedence and associativity table 
     ('left', 'WOR', 'WXOR'),
     ('left', 'WAND'),
     ('right','WNOT'),
     ('left','COMMA','HASH_OP'),
     ('right','ASSIGNOP'),
     ('nonassoc','DOTDOT'),
     ('left','OROR','DORDOR'),
     ('left','ANDAND'),
     ('left','BITOROP'),
     ('left','BITANDOP'),
     ('nonassoc','RELOP'),
     ('left','SHIFTOP'),
     ('left','ADDOP'),
     ('left','MULOP'),
     ('left','MATCHOP'),
     ('right','!','~'),
     ('right','UMINUS'),
     ('right', 'POWOP'),
     ('nonassoc','INCREMENT','DECREMENT'),
     ('left','DEREF'),
)

# Grammer
def p_body( p ):
    '''body : statementlist
            | empty          
            '''
    print("body:")
    p[0]=p[1]

def p_statementlist(p):
    '''statementlist : statement
                    | statementlist statement'''
    print("list:",p[1:])
    p[0] = "\n".join(p[1:])

# all types of statements

def p_statement(p):
    '''statement : package_dec           
                 | var_dec
                 | function_dec
                 | function_call
                 | comment
                 | cons_dec
                 | bless_st
                 | return_st
                 | term
                 | package_end'''
    global pac
    if pac:
        pac =False
        ind = 0
    else:
        ind = indent
    print("statement:",p[1:])
    p[0]= "\t"*ind + str(p[1])

# binary operators
def p_termbinop(p):  
    '''termbinop : term POWOP term
                | term MULOP term
                | term ADDOP term
                | term SHIFTOP term
                | term RELOP term
                | term EQOP term
                | term BITANDOP term
                | term BITOROP term
                | term DOTDOT term
                | term ANDAND term
                | term OROR term
                | term DORDOR term
                | term MATCHOP term
                | term WAND term
                | term WOR term
                | term WXOR term'''

    if p[2] == '//' and iv(p[1]) and iv(p[3]):
            if iss(p[1]):
                a=p[1][2:-1]
            else:
                a=p[1][1:]
            if iss(p[3]):
                b = p[3][2:-1]
            else:
                b = p[3][1:]
            
            p[0] = "dor( "+a+" , "+b+" )"

    elif p[2] == '//' and ((not iv(p[1])) or (not iv(p[3]))):
        raise Exception("Syntax Error")

    else :
        if iss(p[1]) and iv(p[1]):
            p[1]=p[1][2:-1]
        elif iv(p[1]):
            p[1]=p[1][1:]
        if iss(p[3]) and iv(p[3]):
            p[3]= p[3][2:-1]
        elif iv(p[3]):
            p[3]= p[3][1:]
        if iss(p[1]) and iss(p[3]):
            if p[2] in match:
                p[0]=p[1]+" "+match[p[2]]+" "+p[3]
            elif p[2] in match.values():
                p[0] = p[1]+" "+p[2]+" "+p[3]
            elif p[2]=='cmp' or p[2]=='<=>':
                p[0]="cmp( "+p[1]+","+p[3]+" )"
            elif (p[2] in addmulop):
                p[0] = "str2float( "+p[1]+") "+str(p[2])+" str2float( "+p[3]+" )"
            elif (p[2] in bit):
                p[0] = "strbitwise( "+p[1]+","+p[2]+","+p[3]+" )"
            elif p[2]=='.':
                p[0] = p[1]+" + "+p[3]
            elif p[2] == 'x':
                p[0] = p[1]+" * "+p[3]
            elif p[2] in intops:
                p[2] = "str2int( "+p[1]+") "+p[2]+" str2int( "+p[3]+" )"
            elif p[2] == 'and':
                p[0] = str(p[1])+" "+" and "+" "+str(p[3])
            elif p[2] == 'or':
                p[0] = str(p[1])+" "+" or "+" "+str(p[3])
            elif p[2] == 'xor':
                p[0] = str(p[1])+" "+" ^ "+" "+str(p[3])
        else:
            if p[2] in match:
                p[0] = str(p[1])+" "+match[p[2]]+" "+str(p[3])
            elif p[2] in match.values():
                 p[0] = p[1]+" "+p[2]+" "+p[3]
            elif p[2] == 'cmp' or p[2] == '<=>':
                p[0] = "cmp( "+p[1]+","+p[3]+" )"
            elif (p[2] in addmulop):
                    p[0] = str(p[1])+" "+p[2]+" "+str(p[3])
            elif (p[2] in bit):
                p[0] = "int("+str(p[1])+") "+p[2]+" int("+str(p[3])+")"
            elif p[2] == '.':
                p[0] = p[1]+" + "+p[3]
            elif p[2] == 'x':
                p[0] = p[1]+" * "+p[3]
            elif p[2] in intops:
                p[0] = "int("+str(p[1])+") "+p[2]+" int("+str(p[3])+")"
            elif p[2] == 'and':
                p[0] = str(p[1])+" "+"and"+" "+str(p[3])
            elif p[2] == 'or':
                p[0] = str(p[1])+" "+"or"+" "+str(p[3])
            elif p[2] == 'xor':
                p[0] = str(p[1])+" "+"^"+" "+str(p[3])

# unary operators
def p_termunop(p):
    '''termunop : ADDOP term %prec UMINUS 
               | '!' term
               | '~' term 
               | term INCREMENT
               | term DECREMENT
               | term DEREF
               | INCREMENT term
               | DECREMENT term
               | WNOT term'''
    if iss(p[1]) and iv(p[1]):
        p[1] = p[1][2:-1]
    elif iv(p[1]):
        p[1] = p[1][1:]
    if iss(p[2]) and iv(p[2]):
        p[2] = p[2][2:-1]
    elif iv(p[2]):
        p[2] = p[2][1:]
    if p[1]=='!':
        p[0]='not '+str(p[2])
    elif p[1] == '-':
        if iss(p[2]):
            p[0]="-"+str(p[2][1:-1])
        else:
            p[0]= "-"+str(p[2])
    elif p[1]=='+':
        if iss(p[2]):
            p[0] = str(p[2][1:-1])
        else:
            p[0] = str(p[2])
    elif p[1]=='~':
        p[0] = "~str2int("+str(p[2])+")"
    elif p[1]=='++':
        p[0]="PreIncrement('"+str(p[2])+"',locals())" # found in ctools module
    elif p[1] == '--':
        p[0]="PreDecrement('"+str(p[2])+"',locals())"
    elif p[2] == '++':
        p[0]="PostIncrement('"+str(p[1])+"',locals())"
    elif p[2] == '--':
        p[0]="PostDecrement('"+str(p[1])+"',locals())"
    else:
        p[0] = 'not '+str(p[2])

        

#all the various types of terms


def p_term(p):
    '''term : termbinop
	       | termunop
           | hash_exp 
           | PARANTHESIS_L term PARANTHESIS_R
           | NAME
           | NUMBER
           | STRING
           | INPUT
           | PRINT     
           | Q BRACES_LEFT NAME BRACES_RIGHT
           | QQ BRACES_LEFT NAME BRACES_RIGHT
           | QX BRACES_LEFT NAME BRACES_RIGHT'''
 	#can integrate the ternary operator here
    if p[1]=='(':
        p[0]="("+str(p[2])+")"
    elif len(p)==5:
        if ('q' in p[1]):  # for quote like operators
            p[0]="'"+p[3]+"'"
        elif ('qq' in p[1]):
            p[0]="\""+p[3]+"\""
        elif ('qx' in p[1]):
            p[0]="`"+p[3]+"`"
    # this elif will always fail
    elif len(p)==4 and (p[2]==',' or p[2]=='=>'):
        p[0]=str(p[1])+p[2]+str(p[3]) 
    else :
        p[0]=p[1]

# object oriented part
# defining the package
def p_package_dec( p ) :
    'package_dec : PACKAGE NAME SEMI'
    global indent, inpac, pac
    indent += 1
    inpac = True
    pac = True
    p[0] = "class "+str(p[2])+" :"

# defining end of package
def p_package_end(p):
    '''package_end : NUMBER SEMI'''
    p[0] = ""
    global inpac
    inpac = False

# defining the constructor
def p_cons_dec(p):
    '''cons_dec : SUB NEW set_cons block'''
    p[0] = "def __init__(self,*argv):\n" + p[4]
    global incons
    incons = False

# defining that we are part of constructor
def p_set_cons(p):
    '''set_cons : ''' 
    global incons
    incons = True

# defining the blessing part
def p_bless_st(p):
    '''bless_st : BLESS PARANTHESIS_L argument PARANTHESIS_R SEMI'''
    #print("bless_st: ", p[0:])
    p[0] = ""

# defing the block
def p_block(p):
    '''block : braces_left body BRACES_RIGHT'''
    #print("block: ", p[0:])
    p[0] = p[2]
    global indent
    indent -= 1

def p_function_dec( p ):
    '''function_dec : SUB NAME  block'''
    # modifications have to be made here for functions written without using packages
    # the required modifications
    if inpac:
        extra = "self,"
    else:
        extra = ""
    p[0] = "def " + str(p[2]) + "(" + extra + "argv):\n" + p[3]
    global fline
    fline = 0

# defining return statement
def p_return_st(p):
    '''return_st : RETURN term SEMI'''
    if not incons:
        p[0] = p[1] + " " + p[2][1:]
    else:
        p[0] = ""

# defining function calls
def p_function_call(p):
    ''' function_call : NAME PARANTHESIS_L argument PARANTHESIS_R SEMI'''
    p[0] = "".join(p[1:5])


    

def p_var_dec( p ):
    '''var_dec : my NAME ASSIGNOP term SEMI
               | my NAME ASSIGNOP SHIFT SEMI'''
               #| NAME ASSIGNOP term SEMI
    """if len(p)==6 and p[4]=='shift':
        if(p[2][0]=='$'):
            p[0]="\t"*indent+p[2][1:]+' = argv[i]\n'+"\t"*indent+"i+=1" # have to add support for hashes here
    if len(p)==6 and p[4]!='shift':
        if(p[2][0]=='$'):
            p[0]="\t"*indent+p[2][1:]+" "+p[3]+" "+str(p[4])
    else:
        if(p[1][0] == '$'):
            p[0]="\t"*indent+p[1][1:]+" "+p[2]+" "+str(p[3])"""
    if p[4] == 'shift':
        global fline
        fline += 1
        if (fline == 1 and inpac and incons) or (fline == 1 and not inpac):
            p[0] = "arg = list(argv).reverse()"
        elif fline == 1 and inpac:
            p[0] = p[2][1:] + p[3] + "self\n" + "\t"*indent
            p[0] += "arg = list(argv).reverse()" 
        elif incons and p[2][0] == "$":
            p[0] = "self." + p[2][1:] + p[3] + "arg.pop()"
        elif incons:
            p[0] = "self." + p[2][1:] + p[3] + p[4]
        else:
            p[0] = p[2][1:] + p[3] + "arg.pop()"
    elif incons:
        if p[2][0] == "%":
            assign = ""
            i = 1
            for j in re.split(":|,",p[4][1:-1]):
                if i%2 == 1:
                    assign += "self." + j.replace("\"","") + "="
                else:
                    assign += j + "\n" + "\t"*indent
                i += 1
            p[0] = assign
        else:
            p[0] = "self." + p[2][1:] + p[3] + p[4]
    else:
        p[0] = p[2][1:] + p[3] + p[4]
        

# defining my
def p_my(p):
    '''my : MY
            | empty'''
    p[0] = p[1]

def p_hash_exp(p):
    '''hash_exp : first_hash
                | second_hash'''
    p[0] = p[1]

# defining first type of hash declaration
def p_first_hash(p):
    '''first_hash : PARANTHESIS_L argument PARANTHESIS_R'''
    p[0] = "{"
    key = True
    for i in p[2].split(","):
        if key:
            p[0] = p[0] + str(i) + ":"
            key = False
        else:
            if i == "shift":
                p[0] = p[0] + "arg.pop(),"
            else:
                p[0] = p[0] + str(i) + ","
            key = True
    p[0] = p[0][:-1] + "}"

# defining second type of hash declaration
def p_second_hash(p):
    '''second_hash : BRACES_LEFT argument BRACES_RIGHT'''
    p[0] = "{"
    key = True
    for i in re.split("=>|,", p[2]):
        if key:
            p[0] = p[0] + str(i) + ":"
            key = False
        else:
            if i == "shift":
                p[0] = p[0] + "arg.pop(),"
            else:
                p[0] = p[0] + str(i) + ","
            key = True
    p[0] = p[0][:-1] + "}"
# arguments for the function call


def p_argument(p):
    '''argument : SHIFT
                | term
                | argument COMMA argument
                | argument HASH_OP argument
                | empty'''
    p[0] = "".join(str(x) for x in p[1:])

def p_INPUT(p):
    '''INPUT : '<' STDIN '>' '''
    p[0] = "input()"

def p_comment( p ):
    '''comment : COMMENT'''
    p[0] = p[1]

def p_braces_left( p ):
    '''braces_left : BRACES_LEFT'''
    global indent
    indent += 1

def p_empty(p):
     'empty :'
     pass

def p_error(p):
    if p!=None:
        print("Error at Symbol ",p.value," Line no ",p.lineno," Position ",p.lexpos)



def my_parser():
    input_file= open ( "input_code.pm ","r")
    perl_inp=input_file.read()
    my_lexer(perl_inp)
    #file = open ("python_code.py","w+")
    parser = yacc.yacc()
    p=parser.parse(perl_inp)
    print("from ctools import *\n"+p) #ctools is the module which supports a number of operations which are not supported in python like ++,-- , // etc
    #file.close()
    input_file.close()
   


        

my_parser()

