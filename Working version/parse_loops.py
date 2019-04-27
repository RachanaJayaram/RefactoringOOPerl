
def p_control_statements(p):
    '''control_statements : iterative '''
    # print("Control Statement",p[1]);
    p[0]=p[1]
    

def p_iterative(p):
    '''iterative : for_st
                 | while_st'''
                #  | do_while_st
                #  | foreach_st'''
    p[0]=p[1]

def p_for_st(p):
    '''for_st : FOR PARANTHESIS_L  NAME ASSIGNOP term SEMI NAME RELOP term SEMI NAME INCREMENT  PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT
              | FOR PARANTHESIS_L  NAME ASSIGNOP term SEMI NAME RELOP term SEMI NAME DECREMENT  PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT'''
    if (str(p[12][-2:])=="++"):
        if (p[8]=='>' or p[8]=='<' or p[8]=='!='):
            p[0]=(str(p[1])+" "+str(p[3][1:])+" in range ("+str(p[5])+","+str(p[9])+",1)"+":",[p[15]])
        else:
            p[0]=(str(p[1])+" "+str(p[3][1:])+" in range ("+str(p[5])+","+str(int(p[9])+1)+",1)"+":",[p[15]])
    else:
        if (p[8]=='>' or p[8]=='<' or p[8]=='!='):
            p[0]=(str(p[1])+" "+str(p[3][1:])+" in range ("+str(p[5])+","+str(p[9])+",-1)"+":",[p[15]])
        else:
            p[0]=(str(p[1])+" "+str(p[3][1:])+" in range ("+str(p[5])+","+str(int(p[9])+1)+",-1)"+":",[p[15]])

# #foreach $word (@data)
# def p_foreach_st(p):
#     '''foreach_st : FOREACH NAME PARANTHESIS_L NAME PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT'''
#     print(p[1])
#     p[0]=("for "+str(p[2][1:])+" in "+str(p[4][1:])+":",p[7]);

# while (condition)
def p_while_st(p):
    '''while_st : WHILE PARANTHESIS_L NAME RELOP term PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT
                | WHILE PARANTHESIS_L term PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT'''
    if len(p[1:])==7:
        p[0]=("while ("+str(p[3])+"):",[p[6]]);
    else:
        p[0]=("while ("+str(p[3][1:])+str(p[4])+str(p[5])+"):",[p[8]]);
    
    

# #do {  } while(condition);
# def p_do_while_st(p):
#     '''do_while_st : DO BRACES_LEFT body BRACES_RIGHT WHILE PARANTHESIS_L NAME RELOP NUMBER PARANTHESIS_R'''
#     print(p[1])
#     p[0]=("while ("+str(p[7][1:])+str(p[8])+str(p[9])+"):",p[3]);

# #until ($a < 1) 
# def p_until_st(p):
#     '''until_st : UNTIL PARANTHESIS_L NAME RELOP NUMBER PARANTHESIS_R BRACES_LEFT body BRACES_RIGHT'''
#     print(p[1])
#     p[0]=("while ("+str(p[3][1:])+str(p[4])+str(p[5])+"):",p[8]);
