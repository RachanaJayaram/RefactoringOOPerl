
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "bodyleftWORWXORleftWANDrightWNOTleftCOMMAHASH_OPrightASSIGNOPnonassocDOTDOTleftORORDORDORleftANDANDleftBITOROPleftBITANDOPnonassocRELOPleftSHIFTOPleftADDOPleftMULOPleftMATCHOPright!~rightUMINUSrightPOWOPnonassocINCREMENTDECREMENTleftDEREFADDOP ANDAND ASSIGNOP BITANDOP BITOROP BLESS BRACES_LEFT BRACES_RIGHT COMMA COMMENT DECREMENT DEREF DORDOR DOTDOT EQOP HASH_OP INCREMENT MATCHOP MULOP MY NAME NEW NUMBER OROR PACKAGE PARANTHESIS_L PARANTHESIS_R POWOP PRINT Q QQ QX RELOP RETURN SEMI SHIFT SHIFTOP STDIN STRING SUB WAND WNOT WOR WXORbody : statementlist\n            | empty          \n            statementlist : statement\n                    | statementlist statementstatement : package_dec           \n                 | var_dec\n                 | function_dec\n                 | function_call\n                 | comment\n                 | cons_dec\n                 | bless_st\n                 | return_st\n                 | term\n                 | package_endtermbinop : term POWOP term\n                | term MULOP term\n                | term ADDOP term\n                | term SHIFTOP term\n                | term RELOP term\n                | term EQOP term\n                | term BITANDOP term\n                | term BITOROP term\n                | term DOTDOT term\n                | term ANDAND term\n                | term OROR term\n                | term DORDOR term\n                | term MATCHOP term\n                | term WAND term\n                | term WOR term\n                | term WXOR termtermunop : ADDOP term %prec UMINUS \n               | '!' term\n               | '~' term \n               | term INCREMENT\n               | term DECREMENT\n               | term DEREF\n               | INCREMENT term\n               | DECREMENT term\n               | WNOT termterm : termbinop\n\t       | termunop\n           | hash_exp \n           | PARANTHESIS_L term PARANTHESIS_R\n           | NAME\n           | NUMBER\n           | STRING\n           | INPUT\n           | PRINT     \n           | Q BRACES_LEFT NAME BRACES_RIGHT\n           | QQ BRACES_LEFT NAME BRACES_RIGHT\n           | QX BRACES_LEFT NAME BRACES_RIGHTpackage_dec : PACKAGE NAME SEMIpackage_end : NUMBER SEMIcons_dec : SUB NEW set_cons blockset_cons : bless_st : BLESS PARANTHESIS_L argument PARANTHESIS_R SEMIblock : braces_left body BRACES_RIGHTfunction_dec : SUB NAME  blockreturn_st : RETURN term SEMI function_call : NAME PARANTHESIS_L argument PARANTHESIS_R SEMIvar_dec : my NAME ASSIGNOP term SEMI\n               | my NAME ASSIGNOP SHIFT SEMImy : MY\n            | emptyhash_exp : first_hash\n                | second_hashfirst_hash : PARANTHESIS_L argument PARANTHESIS_Rsecond_hash : BRACES_LEFT argument BRACES_RIGHTargument : SHIFT\n                | term\n                | argument COMMA argument\n                | argument HASH_OP argument\n                | emptyINPUT : '<' STDIN '>' comment : COMMENTbraces_left : BRACES_LEFTempty :"
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[-77,0,-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'NAME':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,31,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,79,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[16,16,-64,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,65,-44,67,68,72,-75,72,-40,-41,-42,-45,-46,-47,-48,72,-63,72,72,72,72,72,72,-65,-66,-4,-64,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-34,-35,-36,72,-44,-45,72,-53,120,122,123,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,72,-58,16,-76,-43,-67,72,72,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'PACKAGE':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[15,15,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,15,-76,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'SUB':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[18,18,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,18,-76,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'COMMENT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[20,20,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,20,-76,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'BLESS':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[21,21,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,21,-76,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'RETURN':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[22,22,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,22,-76,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'PARANTHESIS_L':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,21,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[19,19,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,66,19,-75,76,19,-40,-41,-42,-45,-46,-47,-48,19,19,19,19,19,19,19,-65,-66,-4,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-34,-35,-36,19,-44,-45,19,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,19,-58,19,-76,-43,-67,19,19,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'NUMBER':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[26,26,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,73,-75,73,-40,-41,-42,-45,-46,-47,-48,73,73,73,73,73,73,73,-65,-66,-4,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,-34,-35,-36,73,-44,-45,73,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,73,-58,26,-76,-43,-67,73,73,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'STRING':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[27,27,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,27,-75,27,-40,-41,-42,-45,-46,-47,-48,27,27,27,27,27,27,27,-65,-66,-4,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-34,-35,-36,27,-44,-45,27,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,27,-58,27,-76,-43,-67,27,27,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'PRINT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[29,29,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,29,-75,29,-40,-41,-42,-45,-46,-47,-48,29,29,29,29,29,29,29,-65,-66,-4,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-34,-35,-36,29,-44,-45,29,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,29,-58,29,-76,-43,-67,29,29,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'Q':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[30,30,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,30,-75,30,-40,-41,-42,-45,-46,-47,-48,30,30,30,30,30,30,30,-65,-66,-4,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-34,-35,-36,30,-44,-45,30,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,30,-58,30,-76,-43,-67,30,30,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'QQ':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[32,32,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,32,-75,32,-40,-41,-42,-45,-46,-47,-48,32,32,32,32,32,32,32,-65,-66,-4,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-34,-35,-36,32,-44,-45,32,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,32,-58,32,-76,-43,-67,32,32,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'QX':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[33,33,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,33,-75,33,-40,-41,-42,-45,-46,-47,-48,33,33,33,33,33,33,33,-65,-66,-4,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-34,-35,-36,33,-44,-45,33,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,33,-58,33,-76,-43,-67,33,33,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'MY':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,41,42,44,62,63,64,72,73,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,119,121,124,129,133,134,135,136,137,138,139,140,],[34,34,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-65,-66,-4,-34,-35,-36,-44,-45,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,34,-76,-43,-67,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'ADDOP':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,70,72,73,76,77,78,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,126,129,133,134,135,136,137,138,139,140,],[35,35,-3,-5,-6,-7,-8,-9,-10,-11,-12,48,-14,-44,35,-75,35,-40,-41,-42,-45,-46,-47,-48,35,35,35,35,35,35,35,-65,-66,-4,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-34,-35,-36,35,48,-44,-45,35,48,-53,48,-31,-32,-33,-37,-38,48,-15,-16,-17,48,48,48,48,48,48,48,48,48,-27,48,48,48,-52,35,-58,35,-76,-43,-67,35,35,-59,-68,-74,48,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'!':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[36,36,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,36,-75,36,-40,-41,-42,-45,-46,-47,-48,36,36,36,36,36,36,36,-65,-66,-4,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-34,-35,-36,36,-44,-45,36,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,36,-58,36,-76,-43,-67,36,36,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'~':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[37,37,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,37,-75,37,-40,-41,-42,-45,-46,-47,-48,37,37,37,37,37,37,37,-65,-66,-4,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-34,-35,-36,37,-44,-45,37,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,37,-58,37,-76,-43,-67,37,37,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'INCREMENT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,70,72,73,76,77,78,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,126,129,133,134,135,136,137,138,139,140,],[38,38,-3,-5,-6,-7,-8,-9,-10,-11,-12,62,-14,-44,38,-75,38,-40,-41,-42,-45,-46,-47,-48,38,38,38,38,38,38,38,-65,-66,-4,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-34,-35,-36,38,62,-44,-45,38,62,-53,62,62,62,62,None,None,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-52,38,-58,38,-76,-43,-67,38,38,-59,-68,-74,62,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'DECREMENT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,70,72,73,76,77,78,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,126,129,133,134,135,136,137,138,139,140,],[39,39,-3,-5,-6,-7,-8,-9,-10,-11,-12,63,-14,-44,39,-75,39,-40,-41,-42,-45,-46,-47,-48,39,39,39,39,39,39,39,-65,-66,-4,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-34,-35,-36,39,63,-44,-45,39,63,-53,63,63,63,63,None,None,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-52,39,-58,39,-76,-43,-67,39,39,-59,-68,-74,63,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'WNOT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[40,40,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,40,-75,40,-40,-41,-42,-45,-46,-47,-48,40,40,40,40,40,40,40,-65,-66,-4,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-34,-35,-36,40,-44,-45,40,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,40,-58,40,-76,-43,-67,40,40,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'<':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,31,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[43,43,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,43,-75,43,-40,-41,-42,-45,-46,-47,-48,43,43,43,43,43,43,43,-65,-66,-4,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-34,-35,-36,43,-44,-45,43,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,43,-58,43,-76,-43,-67,43,43,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'BRACES_LEFT':([0,2,4,5,6,7,8,9,10,11,12,13,14,16,19,20,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,69,72,73,76,78,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,117,119,121,124,129,133,134,135,136,137,138,139,140,],[31,31,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,31,-75,31,-40,-41,-42,-45,-46,-47,-48,79,31,82,83,31,31,31,31,31,31,-65,-66,-4,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-34,-35,-36,31,112,-55,-44,-45,31,-53,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,31,-58,31,-76,112,-43,-67,31,31,-59,-68,-74,-54,-49,-50,-51,-60,-61,-62,-57,-56,]),'BRACES_RIGHT':([2,3,4,5,6,7,8,9,10,11,12,13,14,16,20,23,24,25,26,27,28,29,31,41,42,44,62,63,64,72,73,74,75,78,80,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,110,111,112,114,115,116,117,119,120,121,122,123,124,128,129,130,131,133,134,135,136,137,138,139,140,],[-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-44,-75,-40,-41,-42,-45,-46,-47,-48,-77,-65,-66,-4,-34,-35,-36,-44,-45,-69,-73,-53,121,-70,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-52,-58,-77,-76,-43,-67,-77,-77,-59,133,-68,134,135,-74,139,-54,-71,-72,-49,-50,-51,-60,-61,-62,-57,-56,]),'POWOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[46,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,46,-44,-45,46,46,46,46,46,-37,-38,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-43,-67,-68,-74,46,-49,-50,-51,]),'MULOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[47,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,47,-44,-45,47,47,-31,-32,-33,-37,-38,47,-15,-16,47,47,47,47,47,47,47,47,47,47,-27,47,47,47,-43,-67,-68,-74,47,-49,-50,-51,]),'SHIFTOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[49,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,49,-44,-45,49,49,-31,-32,-33,-37,-38,49,-15,-16,-17,-18,49,49,49,49,49,49,49,49,-27,49,49,49,-43,-67,-68,-74,49,-49,-50,-51,]),'RELOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[50,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,50,-44,-45,50,50,-31,-32,-33,-37,-38,50,-15,-16,-17,-18,None,50,50,50,50,50,50,50,-27,50,50,50,-43,-67,-68,-74,50,-49,-50,-51,]),'EQOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[51,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,51,-44,-45,51,51,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,51,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-43,-67,-68,-74,51,-49,-50,-51,]),'BITANDOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[52,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,52,-44,-45,52,52,-31,-32,-33,-37,-38,52,-15,-16,-17,-18,-19,52,-21,52,52,52,52,52,-27,52,52,52,-43,-67,-68,-74,52,-49,-50,-51,]),'BITOROP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[53,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,53,-44,-45,53,53,-31,-32,-33,-37,-38,53,-15,-16,-17,-18,-19,53,-21,-22,53,53,53,53,-27,53,53,53,-43,-67,-68,-74,53,-49,-50,-51,]),'DOTDOT':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[54,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,54,-44,-45,54,54,-31,-32,-33,-37,-38,54,-15,-16,-17,-18,-19,54,-21,-22,None,-24,-25,-26,-27,54,54,54,-43,-67,-68,-74,54,-49,-50,-51,]),'ANDAND':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[55,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,55,-44,-45,55,55,-31,-32,-33,-37,-38,55,-15,-16,-17,-18,-19,55,-21,-22,55,-24,55,55,-27,55,55,55,-43,-67,-68,-74,55,-49,-50,-51,]),'OROR':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[56,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,56,-44,-45,56,56,-31,-32,-33,-37,-38,56,-15,-16,-17,-18,-19,56,-21,-22,56,-24,-25,-26,-27,56,56,56,-43,-67,-68,-74,56,-49,-50,-51,]),'DORDOR':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[57,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,57,-44,-45,57,57,-31,-32,-33,-37,-38,57,-15,-16,-17,-18,-19,57,-21,-22,57,-24,-25,-26,-27,57,57,57,-43,-67,-68,-74,57,-49,-50,-51,]),'MATCHOP':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[58,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,58,-44,-45,58,58,-31,-32,-33,-37,-38,58,-15,58,58,58,58,58,58,58,58,58,58,58,-27,58,58,58,-43,-67,-68,-74,58,-49,-50,-51,]),'WAND':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[59,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,59,-44,-45,59,59,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,59,-21,-22,-23,-24,-25,-26,-27,-28,59,59,-43,-67,-68,-74,59,-49,-50,-51,]),'WOR':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[60,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,60,-44,-45,60,60,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,60,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-43,-67,-68,-74,60,-49,-50,-51,]),'WXOR':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[61,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,61,-44,-45,61,61,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,61,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-43,-67,-68,-74,61,-49,-50,-51,]),'DEREF':([13,16,23,24,25,26,27,28,29,41,42,62,63,64,70,72,73,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,126,133,134,135,],[64,-44,-40,-41,-42,-45,-46,-47,-48,-65,-66,-34,-35,-36,64,-44,-45,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-43,-67,-68,-74,64,-49,-50,-51,]),'NEW':([18,],[69,]),'SHIFT':([19,31,66,76,109,116,117,],[74,74,74,74,127,74,74,]),'PARANTHESIS_R':([19,23,24,25,27,28,29,41,42,62,63,64,66,70,71,72,73,74,75,76,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,114,115,116,117,118,121,124,130,131,133,134,135,],[-77,-40,-41,-42,-46,-47,-48,-65,-66,-34,-35,-36,-77,114,115,-44,-45,-69,-73,-77,-70,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,125,-43,-67,-77,-77,132,-68,-74,-71,-72,-49,-50,-51,]),'COMMA':([19,23,24,25,27,28,29,31,41,42,62,63,64,66,70,71,72,73,74,75,76,80,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,114,115,116,117,118,121,124,130,131,133,134,135,],[-77,-40,-41,-42,-46,-47,-48,-77,-65,-66,-34,-35,-36,-77,-70,116,-44,-45,-69,-73,-77,116,-70,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,116,-43,-67,-77,-77,116,-68,-74,-71,-72,-49,-50,-51,]),'HASH_OP':([19,23,24,25,27,28,29,31,41,42,62,63,64,66,70,71,72,73,74,75,76,80,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,114,115,116,117,118,121,124,130,131,133,134,135,],[-77,-40,-41,-42,-46,-47,-48,-77,-65,-66,-34,-35,-36,-77,-70,117,-44,-45,-69,-73,-77,117,-70,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,117,-43,-67,-77,-77,117,-68,-74,-71,-72,-49,-50,-51,]),'SEMI':([23,24,25,26,27,28,29,41,42,62,63,64,65,72,73,77,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,114,115,121,124,125,126,127,132,133,134,135,],[-40,-41,-42,78,-46,-47,-48,-65,-66,-34,-35,-36,107,-44,-45,119,-31,-32,-33,-37,-38,-39,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-43,-67,-68,-74,136,137,138,140,-49,-50,-51,]),'STDIN':([43,],[90,]),'ASSIGNOP':([67,],[109,]),'>':([90,],[124,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,111,],[1,128,]),'statementlist':([0,111,],[2,2,]),'empty':([0,2,19,31,66,76,111,116,117,],[3,45,75,75,75,75,3,75,75,]),'statement':([0,2,111,],[4,44,4,]),'package_dec':([0,2,111,],[5,5,5,]),'var_dec':([0,2,111,],[6,6,6,]),'function_dec':([0,2,111,],[7,7,7,]),'function_call':([0,2,111,],[8,8,8,]),'comment':([0,2,111,],[9,9,9,]),'cons_dec':([0,2,111,],[10,10,10,]),'bless_st':([0,2,111,],[11,11,11,]),'return_st':([0,2,111,],[12,12,12,]),'term':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[13,13,70,77,81,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,81,81,126,13,81,81,]),'package_end':([0,2,111,],[14,14,14,]),'my':([0,2,111,],[17,17,17,]),'termbinop':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'termunop':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'hash_exp':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'INPUT':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'first_hash':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'second_hash':([0,2,19,22,31,35,36,37,38,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,76,109,111,116,117,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'argument':([19,31,66,76,116,117,],[71,80,108,118,130,131,]),'block':([68,113,],[110,129,]),'braces_left':([68,113,],[111,111,]),'set_cons':([69,],[113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> statementlist','body',1,'p_body','parser.py',48),
  ('body -> empty','body',1,'p_body','parser.py',49),
  ('statementlist -> statement','statementlist',1,'p_statementlist','parser.py',54),
  ('statementlist -> statementlist statement','statementlist',2,'p_statementlist','parser.py',55),
  ('statement -> package_dec','statement',1,'p_statement','parser.py',61),
  ('statement -> var_dec','statement',1,'p_statement','parser.py',62),
  ('statement -> function_dec','statement',1,'p_statement','parser.py',63),
  ('statement -> function_call','statement',1,'p_statement','parser.py',64),
  ('statement -> comment','statement',1,'p_statement','parser.py',65),
  ('statement -> cons_dec','statement',1,'p_statement','parser.py',66),
  ('statement -> bless_st','statement',1,'p_statement','parser.py',67),
  ('statement -> return_st','statement',1,'p_statement','parser.py',68),
  ('statement -> term','statement',1,'p_statement','parser.py',69),
  ('statement -> package_end','statement',1,'p_statement','parser.py',70),
  ('termbinop -> term POWOP term','termbinop',3,'p_termbinop','parser.py',75),
  ('termbinop -> term MULOP term','termbinop',3,'p_termbinop','parser.py',76),
  ('termbinop -> term ADDOP term','termbinop',3,'p_termbinop','parser.py',77),
  ('termbinop -> term SHIFTOP term','termbinop',3,'p_termbinop','parser.py',78),
  ('termbinop -> term RELOP term','termbinop',3,'p_termbinop','parser.py',79),
  ('termbinop -> term EQOP term','termbinop',3,'p_termbinop','parser.py',80),
  ('termbinop -> term BITANDOP term','termbinop',3,'p_termbinop','parser.py',81),
  ('termbinop -> term BITOROP term','termbinop',3,'p_termbinop','parser.py',82),
  ('termbinop -> term DOTDOT term','termbinop',3,'p_termbinop','parser.py',83),
  ('termbinop -> term ANDAND term','termbinop',3,'p_termbinop','parser.py',84),
  ('termbinop -> term OROR term','termbinop',3,'p_termbinop','parser.py',85),
  ('termbinop -> term DORDOR term','termbinop',3,'p_termbinop','parser.py',86),
  ('termbinop -> term MATCHOP term','termbinop',3,'p_termbinop','parser.py',87),
  ('termbinop -> term WAND term','termbinop',3,'p_termbinop','parser.py',88),
  ('termbinop -> term WOR term','termbinop',3,'p_termbinop','parser.py',89),
  ('termbinop -> term WXOR term','termbinop',3,'p_termbinop','parser.py',90),
  ('termunop -> ADDOP term','termunop',2,'p_termunop','parser.py',165),
  ('termunop -> ! term','termunop',2,'p_termunop','parser.py',166),
  ('termunop -> ~ term','termunop',2,'p_termunop','parser.py',167),
  ('termunop -> term INCREMENT','termunop',2,'p_termunop','parser.py',168),
  ('termunop -> term DECREMENT','termunop',2,'p_termunop','parser.py',169),
  ('termunop -> term DEREF','termunop',2,'p_termunop','parser.py',170),
  ('termunop -> INCREMENT term','termunop',2,'p_termunop','parser.py',171),
  ('termunop -> DECREMENT term','termunop',2,'p_termunop','parser.py',172),
  ('termunop -> WNOT term','termunop',2,'p_termunop','parser.py',173),
  ('term -> termbinop','term',1,'p_term','parser.py',213),
  ('term -> termunop','term',1,'p_term','parser.py',214),
  ('term -> hash_exp','term',1,'p_term','parser.py',215),
  ('term -> PARANTHESIS_L term PARANTHESIS_R','term',3,'p_term','parser.py',216),
  ('term -> NAME','term',1,'p_term','parser.py',217),
  ('term -> NUMBER','term',1,'p_term','parser.py',218),
  ('term -> STRING','term',1,'p_term','parser.py',219),
  ('term -> INPUT','term',1,'p_term','parser.py',220),
  ('term -> PRINT','term',1,'p_term','parser.py',221),
  ('term -> Q BRACES_LEFT NAME BRACES_RIGHT','term',4,'p_term','parser.py',222),
  ('term -> QQ BRACES_LEFT NAME BRACES_RIGHT','term',4,'p_term','parser.py',223),
  ('term -> QX BRACES_LEFT NAME BRACES_RIGHT','term',4,'p_term','parser.py',224),
  ('package_dec -> PACKAGE NAME SEMI','package_dec',3,'p_package_dec','parser.py',244),
  ('package_end -> NUMBER SEMI','package_end',2,'p_package_end','parser.py',251),
  ('cons_dec -> SUB NEW set_cons block','cons_dec',4,'p_cons_dec','parser.py',258),
  ('set_cons -> <empty>','set_cons',0,'p_set_cons','parser.py',265),
  ('bless_st -> BLESS PARANTHESIS_L argument PARANTHESIS_R SEMI','bless_st',5,'p_bless_st','parser.py',271),
  ('block -> braces_left body BRACES_RIGHT','block',3,'p_block','parser.py',277),
  ('function_dec -> SUB NAME block','function_dec',3,'p_function_dec','parser.py',284),
  ('return_st -> RETURN term SEMI','return_st',3,'p_return_st','parser.py',297),
  ('function_call -> NAME PARANTHESIS_L argument PARANTHESIS_R SEMI','function_call',5,'p_function_call','parser.py',305),
  ('var_dec -> my NAME ASSIGNOP term SEMI','var_dec',5,'p_var_dec','parser.py',312),
  ('var_dec -> my NAME ASSIGNOP SHIFT SEMI','var_dec',5,'p_var_dec','parser.py',313),
  ('my -> MY','my',1,'p_my','parser.py',343),
  ('my -> empty','my',1,'p_my','parser.py',344),
  ('hash_exp -> first_hash','hash_exp',1,'p_hash_exp','parser.py',348),
  ('hash_exp -> second_hash','hash_exp',1,'p_hash_exp','parser.py',349),
  ('first_hash -> PARANTHESIS_L argument PARANTHESIS_R','first_hash',3,'p_first_hash','parser.py',354),
  ('second_hash -> BRACES_LEFT argument BRACES_RIGHT','second_hash',3,'p_second_hash','parser.py',371),
  ('argument -> SHIFT','argument',1,'p_argument','parser.py',389),
  ('argument -> term','argument',1,'p_argument','parser.py',390),
  ('argument -> argument COMMA argument','argument',3,'p_argument','parser.py',391),
  ('argument -> argument HASH_OP argument','argument',3,'p_argument','parser.py',392),
  ('argument -> empty','argument',1,'p_argument','parser.py',393),
  ('INPUT -> < STDIN >','INPUT',3,'p_INPUT','parser.py',397),
  ('comment -> COMMENT','comment',1,'p_comment','parser.py',401),
  ('braces_left -> BRACES_LEFT','braces_left',1,'p_braces_left','parser.py',405),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',410),
]