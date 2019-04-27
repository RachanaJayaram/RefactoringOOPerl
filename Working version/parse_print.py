def p_print_st(p):
    '''print_st : PRINT arg_list SEMI ''' 
    p[0]="print( "+p[2]+",end='',sep='' )"