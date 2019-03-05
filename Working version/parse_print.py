fileHandles=['a']
def p_print_st(p):
    '''print_st : PRINT HANDLE
                | PRINT PARANTHESIS_L HANDLE PARANTHESIS_R'''
    if len(p)==5:
        if p[3][0] in fileHandles:
            p[0] = "print( " + p[3][1] + " , end = '', file = "+p[3][0]+" )"
        else :
            p[0] = "print( " + p[3][1] + " , end = '' )"
    elif len(p) == 3:
        if p[2][0] in fileHandles:
            p[0] = "print( " + p[2][1] + " , end = '', file = "+p[2][0]+" )"
        else:
            p[0] = "print( " + p[2][1] + " , end = '' )"
    else:
        temp = p[2][1:-1] 
        p[0] = "print( " + temp + " , end = '')"

def p_HANDLE(p):
    '''HANDLE : arg_list
              | NAME arg_list'''
    if len(p)==3:
        if "," not in p[2][1:2]:
            p[0] = ((p[1] if '$' not in p[1][0:1] else p[1][1:]),p[2])
        else:
            p[0] = ("", p[1]+p[2])
    else :
        p[0]=("",p[1])

def p_arg_list(p):
    '''arg_list : arg
                | arg_list COMMA arg'''
    p[0] = p[1]
    for arg in p[2:]:
        if arg != ',':
            p[0] += " , " + arg
def p_arg(p):
    '''arg : term 
           | empty'''
    try:
        if p[1][0] == '$':
            p[0] = p[1][1:]
        else:
            p[0] = p[1]
    except:
        p[0] = str(p[1])

def p_var_deref(p):
    '''var_deref : NAME DEREF BRACES_LEFT NAME BRACES_RIGHT'''
    if p[1][0] == '$':
        p[0] = p[1][1:] + '.' + p[4]
    else:
        p[0] = p[1] + '.' + p[4]

def p_variable(p):
    '''variable : MY NAME
          | NAME'''
    if len(p) > 2 :
        p[0] = p[2]
    else:
        p[0] = p[1]
