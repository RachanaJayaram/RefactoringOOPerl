def p_object_creation( p ):
    '''object_creation : NAME ASSIGNOP NAME DEREF NEW PARANTHESIS_L arg_list PARANTHESIS_R SEMI'''
    if(p[1][0]=='$'):
        p[0]=p[1][1:] + "="+p[3]+'.'+p[3]+'('+p[7]+')'
