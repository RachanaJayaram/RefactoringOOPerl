
def p_o_func_call( p ):
    '''o_func_call : NAME DEREF NAME PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
    if(p[1][0]=='$'):
        p[0]=p[1][1:] + "."+p[3]+'('+p[5]+')'



def p_arg_list(p):
    '''arg_list : arg 
                | arg_list COMMA arg'''
    p[0]=p[1]
    for arg in p[2:]:
        if arg!=',':
            p[0]+=","+arg

def p_arg(p):
    '''arg : name
           | var_deref
           | scope_res
           | string 
           | NUMBER
           | empty
           | term'''
    try:
            p[0]=p[1]
    except:
        p[0]=str(p[1])


def p_var_deref(p):
    ''' var_deref : NAME DEREF BRACES_LEFT NAME BRACES_RIGHT'''
    if(p[1][0]=='$'):
        p[0]=p[1][1:]+'.'+p[4]
    else:
        p[0]=p[1]+'.'+p[4]
