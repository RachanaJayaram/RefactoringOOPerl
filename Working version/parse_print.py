def p_print_st(p):
    '''print_st : PRINT arg_list SEMI'''
    p[0] = "print(" + p[2] + ",end='')"

def p_arg_list(p):
    '''arg_list : arg
                | arg_list COMMA arg'''
    p[0] = p[1]
    for arg in p[2:]:
        if arg != ',':
            p[0] += "," + arg

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
