def p_object_creation(p):
    '''object_creation : NAME ASSIGNOP NAME DEREF NEW PARANTHESIS_L arg_list PARANTHESIS_R SEMI
                       | MY NAME ASSIGNOP NAME DEREF NEW PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
    if p[1][0] == 10:
        p[0] = p[1][1:] + " = " + p[3] + '.' + p[3] + '(' + p[7] + ')'
    else:
        p[0] = p[2][1:] + ' = ' + p[4] + '(' + p[8] + ')'  

def p_obj_func_call(p):
    '''obj_func_call : NAME DEREF NAME PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
    if p[1][0] == '$':
        p[0] = p[1][1:] + '.' + p[3] + '(' + p[5] + ')'

def p_obj_variable(p):
        '''obj_variable : NAME DEREF NAME SEMI'''
        p[0] = p[1][1:] + '.' + p[3]