#variables
import constants_mod
constants = constants_mod.constants
addmulop=['+','-','**','*','/','%']
match={'gt':'>','lt':'<','ge':'>=','le':'<=','eq':'==','ne':'!=','&&':'and','||':'or'}
bit=['&','|','^']
intops=['<<','>>','~'] #work only on ints
iss=lambda x: (type(x)==str) and (("'" in x) or ('"' in x)) #check if term is string
iv=lambda x: (type(x) == str) and (("$" in x) or ('%' in x) or ('@' in x) ) #check if term is variable 

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
     ('nonassoc', 'INCREMENT', 'DECREMENT'),
     ('left','DEREF'),
)

#Expressions Grammer

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
        if p[2] in match:
            p[0]=p[1]+" "+match[p[2]]+" "+p[3]
        elif p[2] in match.values():
            p[0] = p[1]+" "+p[2]+" "+p[3]
        elif p[2]=='cmp' or p[2]=='<=>':
            p[0]="cmp( "+p[1]+","+p[3]+" )"
        elif (p[2] in addmulop):
            if iss(p[1]) and iss(p[3]):
                p[0] = "str2float( "+p[1]+") "+str(p[2])+" str2float( "+p[3]+" )"
            else :
                p[0] = str(p[1])+" "+p[2]+" "+str(p[3])
        elif (p[2] in bit):
            if iss(p[1]) and iss(p[3]):
                p[0] = "strbitwise( "+p[1]+","+p[2]+","+p[3]+" )"
            else :
                p[0] = "int("+str(p[1])+") "+p[2]+" int("+str(p[3])+")"
        elif p[2]=='.':
            p[0] = p[1]+" + "+p[3]
        elif p[2] == 'x':
            p[0] = p[1]+" * "+p[3]
        elif p[2] in intops:
            if iss(p[1]) and iss(p[3]):
                p[2] = "str2int( "+p[1]+") "+p[2]+" str2int( "+p[3]+" )"
            else :
                p[0] = "int("+str(p[1])+") "+p[2]+" int("+str(p[3])+")"
        elif p[2] == 'and':
            p[0] = str(p[1])+" "+" and "+" "+str(p[3])
        elif p[2] == 'or':
            p[0] = str(p[1])+" "+" or "+" "+str(p[3])
        elif p[2] == 'xor':
            p[0] = str(p[1])+" "+" ^ "+" "+str(p[3])

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
           | PARANTHESIS_L term PARANTHESIS_R
           | NAME
           | SCALAR NAME
           | NUMBER
           | STRING
           | var_deref
           | sub_script
           | term '?' term ':' term   
           | Q BRACES_LEFT NAME BRACES_RIGHT
           | QQ BRACES_LEFT NAME BRACES_RIGHT
           | QX BRACES_LEFT NAME BRACES_RIGHT'''
    if p[1]=='(':
        p[0]="("+str(p[2])+")"
    elif len(p)==5:
        if ('q' in p[1]):  # for quote like operators
            p[0]="'"+p[3]+"'"
        elif ('qq' in p[1]):
            p[0]="\""+p[3]+"\""
        elif ('qx' in p[1]):
            p[0]="`"+p[3]+"`"
    elif len(p)==6:
        p[0]=str(p[3])+" if "+str(p[1])+" else "+str(p[5])
    elif len(p)==3:
        p[0] = "len( "+p[2][1:]+")"
    else :
        p[0]=p[1]

def var_dec_helper(p, i):
        if p[2-i][0] == '$': #in case of scalars
            if str(p[4-i]) == "shift":
                if constants.in_package == True and constants.first_line == 0:
                    constants.first_line = 1
                    p[0] = []
                else:
                    p[0] = ('self.' + p[2-i][1:] + '=arg_list.pop()')
            else :
                var_dec_scalar_helper(p,i)
        elif p[2-i][0] == '@': #in case of arrays
            p[0] = p[2-i][1:] + '=' + str(p[4-i])
        elif '[' in p[2-i]:  #in case of initialization for a particular index of array
            p1 = p[2-i].split('[')
            p[0] = "insert_into( "+p1[0]+" , "+p1[1].split(']')[0]+" , "+str(p[3])+" )"
        elif p[2-i][0] == '%': #in case of hashes
            p[0] = p[2-i][1:] + '=' + str(p[4-i])
        else:
            p[0] = p[2-i][1:] + '=' + str(p[4-i])


def var_dec_scalar_helper(p, i):
    if p[3-i] in ['+=', '-=', '/=', '%=', '**=', '&=', '^=', '|=', '>>=', '<<=']:
        p[0] = p[2-i][1:] + p[3-i] + str(p[4-i])
    elif p[3-i] in ['&&=', '//=', '||=']:
        if p[3-i] == '&&=':
            p[0] = p[2-i][1:]+" = "+p[2-i][1:]+" and "+str(p[4-i])
        if p[3-i] == '//=':
            p[0] = p[2-i][1:]+" = " + "dor( "+p[2-i][1:]+" , "+str(p[4-i])+" )"
        else:
            p[0] = p[2-i][1:]+" = "+p[2-i][1:]+" or "+str(p[4-i])
    elif p[3-i] in ['&.=', '^.=', '|.=']:
        p[0] = p[2-i][1:]+" = " + "strbitwise( "+p[2-i][1:]+" , " + p[3-i][0]+" , "+str(p[4-i])+" )"
    else:
        if p[3-i] == '.=':
            p[0] = p[2-i][1:] + " += " + str(p[4-i])
        elif p[3-i] == 'x=':
            p[0] = p[2-i][1:] + " *= " + str(p[4-i])
        else:
            if '@' in str(p[4-i]):
                p[0] = "len( "+p[4-i][1:]+")"
            else:
                p[0] = p[2-i][1:] + " = " + str(p[4-i])
