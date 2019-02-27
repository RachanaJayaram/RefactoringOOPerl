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

def p_my(p):
    '''my : MY
          | empty'''

def p_block(p):
    '''block : braces_left body braces_right'''
    p[0] = p[2]

def p_braces_left(p):
    '''braces_left : BRACES_LEFT'''

def p_braces_right(p):
    '''braces_right : BRACES_RIGHT'''