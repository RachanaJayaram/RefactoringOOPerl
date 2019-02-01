
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "bodyleftWORWXORleftWANDrightWNOTleftCOMMAHASH_OPrightASSIGNOPnonassocDOTDOTleftORORDORDORleftANDANDleftBITOROPleftBITANDOPnonassocRELOPleftSHIFTOPleftADDOPleftMULOPleftMATCHOPright!~rightUMINUSrightPOWOPnonassocINCREMENTDECREMENTleftDEREFADDOP ANDAND ASSIGNOP BITANDOP BITOROP BLESS BRACES_LEFT BRACES_RIGHT COMMA COMMENT DECREMENT DEREF DORDOR DOTDOT EQOP HASH_OP INCREMENT MATCHOP MULOP MY NAME NEW NUMBER OROR PACKAGE PARANTHESIS_L PARANTHESIS_R POWOP PRINT Q QQ QX RELOP RETURN SEMI SHIFT SHIFTOP STDIN STRING SUB WAND WNOT WOR WXORbody : statementlist\n            | empty          \n            statementlist : statement\n                    | statementlist statementstatement : package_dec\n                 | var_dec\n                 | function_dec\n                 | function_call\n                 | comment\n                 | cons_dec\n                 | bless_st\n                 | return_st\n                 | termtermbinop : term POWOP term\n                | term MULOP term\n                | term ADDOP term\n                | term SHIFTOP term\n                | term RELOP term\n                | term EQOP term\n                | term BITANDOP term\n                | term BITOROP term\n                | term DOTDOT term\n                | term ANDAND term\n                | term OROR term\n                | term DORDOR term\n                | term MATCHOP term\n                | term WAND term\n                | term WOR term\n                | term WXOR termtermunop : ADDOP term %prec UMINUS \n               | '!' term\n               | '~' term \n               | term INCREMENT\n               | term DECREMENT\n               | term DEREF\n               | INCREMENT term\n               | DECREMENT term\n               | WNOT termterm : termbinop\n\t   | termunop\n           | PARANTHESIS_L term PARANTHESIS_R\n           | NAME\n           | NUMBER\n           | STRING\n           | INPUT\n           | PRINT\n           | hash_exp      \n           | Q BRACES_LEFT NAME BRACES_RIGHT\n           | QQ BRACES_LEFT NAME BRACES_RIGHT\n           | QX BRACES_LEFT NAME BRACES_RIGHTpackage_dec : PACKAGE NAME SEMIcons_dec : SUB NEW set_cons blockset_cons : bless_st : BLESS PARANTHESIS_L argument PARANTHESIS_R SEMIblock : BRACES_LEFT body BRACES_RIGHTfunction_dec : SUB NAME  braces_left body braces_rightreturn_st : RETURN term SEMI function_call : NAME PARANTHESIS_L argument PARANTHESIS_R SEMIvar_dec : MY NAME ASSIGNOP term SEMI\n               | MY NAME ASSIGNOP SHIFT SEMI\n               | NAME ASSIGNOP term SEMIhash_exp : first_hash\n                | second_hashfirst_hash : PARANTHESIS_L argument PARANTHESIS_Rsecond_hash : BRACES_LEFT argument BRACES_RIGHTargument : SHIFT\n                | term\n                | argument COMMA argument\n                | argument HASH_OP argument\n                | emptyINPUT : '<' STDIN '>' comment : COMMENTbraces_left : BRACES_LEFTbraces_right : BRACES_RIGHTempty :"
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,110,111,115,117,120,121,126,131,132,133,134,135,136,137,138,140,141,],[-75,0,-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,-41,-64,-57,-65,-71,-61,-52,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'PACKAGE':([0,2,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[14,14,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,14,-73,-41,-64,-57,-65,-71,-61,-52,14,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'MY':([0,2,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[16,16,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,16,-73,-41,-64,-57,-65,-71,-61,-52,16,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'NAME':([0,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,75,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[15,15,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,62,-42,65,66,70,-72,70,-39,-40,-43,-44,-45,-46,-47,70,70,70,70,70,70,70,-62,-63,-4,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-33,-34,-35,70,70,-42,70,116,118,119,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,70,15,-73,-41,-64,70,70,-57,-65,-71,-61,-52,15,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'SUB':([0,2,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[17,17,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,17,-73,-41,-64,-57,-65,-71,-61,-52,17,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'COMMENT':([0,2,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[19,19,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,19,-73,-41,-64,-57,-65,-71,-61,-52,19,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'BLESS':([0,2,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[20,20,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,20,-73,-41,-64,-57,-65,-71,-61,-52,20,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'RETURN':([0,2,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,40,41,42,59,60,61,70,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[21,21,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-62,-63,-4,-33,-34,-35,-42,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,21,-73,-41,-64,-57,-65,-71,-61,-52,21,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'PARANTHESIS_L':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[18,18,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,64,18,-72,73,18,-39,-40,-43,-44,-45,-46,-47,18,18,18,18,18,18,18,-62,-63,-4,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-33,-34,-35,18,18,-42,18,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,18,18,-73,-41,-64,18,18,-57,-65,-71,-61,-52,18,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'NUMBER':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[24,24,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,24,-72,24,-39,-40,-43,-44,-45,-46,-47,24,24,24,24,24,24,24,-62,-63,-4,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-33,-34,-35,24,24,-42,24,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,24,24,-73,-41,-64,24,24,-57,-65,-71,-61,-52,24,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'STRING':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[25,25,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,25,-72,25,-39,-40,-43,-44,-45,-46,-47,25,25,25,25,25,25,25,-62,-63,-4,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-33,-34,-35,25,25,-42,25,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,25,25,-73,-41,-64,25,25,-57,-65,-71,-61,-52,25,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'PRINT':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[27,27,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,27,-72,27,-39,-40,-43,-44,-45,-46,-47,27,27,27,27,27,27,27,-62,-63,-4,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-33,-34,-35,27,27,-42,27,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,27,27,-73,-41,-64,27,27,-57,-65,-71,-61,-52,27,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'Q':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[29,29,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,29,-72,29,-39,-40,-43,-44,-45,-46,-47,29,29,29,29,29,29,29,-62,-63,-4,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-33,-34,-35,29,29,-42,29,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,29,29,-73,-41,-64,29,29,-57,-65,-71,-61,-52,29,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'QQ':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[31,31,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,31,-72,31,-39,-40,-43,-44,-45,-46,-47,31,31,31,31,31,31,31,-62,-63,-4,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-33,-34,-35,31,31,-42,31,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,31,31,-73,-41,-64,31,31,-57,-65,-71,-61,-52,31,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'QX':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[32,32,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,32,-72,32,-39,-40,-43,-44,-45,-46,-47,32,32,32,32,32,32,32,-62,-63,-4,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-33,-34,-35,32,32,-42,32,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,32,32,-73,-41,-64,32,32,-57,-65,-71,-61,-52,32,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'ADDOP':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,68,70,73,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,110,111,112,113,115,117,120,121,123,126,127,131,132,133,134,135,136,137,138,140,141,],[33,33,-3,-5,-6,-7,-8,-9,-10,-11,-12,45,-42,33,-72,33,-39,-40,-43,-44,-45,-46,-47,33,33,33,33,33,33,33,-62,-63,-4,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-33,-34,-35,33,33,45,-42,33,45,45,-30,-31,-32,-36,-37,45,-14,-15,-16,45,45,45,45,45,45,45,45,45,-26,45,45,45,-51,45,33,33,-73,-41,-64,33,33,-57,-65,-71,-61,45,-52,33,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'!':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[34,34,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,34,-72,34,-39,-40,-43,-44,-45,-46,-47,34,34,34,34,34,34,34,-62,-63,-4,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-33,-34,-35,34,34,-42,34,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,34,34,-73,-41,-64,34,34,-57,-65,-71,-61,-52,34,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'~':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[35,35,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,35,-72,35,-39,-40,-43,-44,-45,-46,-47,35,35,35,35,35,35,35,-62,-63,-4,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-33,-34,-35,35,35,-42,35,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,35,35,-73,-41,-64,35,35,-57,-65,-71,-61,-52,35,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'INCREMENT':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,68,70,73,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,110,111,112,113,115,117,120,121,123,126,127,131,132,133,134,135,136,137,138,140,141,],[36,36,-3,-5,-6,-7,-8,-9,-10,-11,-12,59,-42,36,-72,36,-39,-40,-43,-44,-45,-46,-47,36,36,36,36,36,36,36,-62,-63,-4,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-33,-34,-35,36,36,59,-42,36,59,59,59,59,59,None,None,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-51,59,36,36,-73,-41,-64,36,36,-57,-65,-71,-61,59,-52,36,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'DECREMENT':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,68,70,73,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,110,111,112,113,115,117,120,121,123,126,127,131,132,133,134,135,136,137,138,140,141,],[37,37,-3,-5,-6,-7,-8,-9,-10,-11,-12,60,-42,37,-72,37,-39,-40,-43,-44,-45,-46,-47,37,37,37,37,37,37,37,-62,-63,-4,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-33,-34,-35,37,37,60,-42,37,60,60,60,60,60,None,None,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-51,60,37,37,-73,-41,-64,37,37,-57,-65,-71,-61,60,-52,37,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'WNOT':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[38,38,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,38,-72,38,-39,-40,-43,-44,-45,-46,-47,38,38,38,38,38,38,38,-62,-63,-4,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-33,-34,-35,38,38,-42,38,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,38,38,-73,-41,-64,38,38,-57,-65,-71,-61,-52,38,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'<':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[39,39,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,39,-72,39,-39,-40,-43,-44,-45,-46,-47,39,39,39,39,39,39,39,-62,-63,-4,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-33,-34,-35,39,39,-42,39,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,39,39,-73,-41,-64,39,39,-57,-65,-71,-61,-52,39,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'BRACES_LEFT':([0,2,4,5,6,7,8,9,10,11,12,13,15,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,66,67,70,73,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,106,107,108,109,110,111,112,113,115,117,120,121,126,127,131,132,133,134,135,136,137,138,140,141,],[30,30,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,30,-72,30,-39,-40,-43,-44,-45,-46,-47,75,30,78,79,30,30,30,30,30,30,-62,-63,-4,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-33,-34,-35,30,30,108,-53,-42,30,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,30,30,-73,127,-41,-64,30,30,-57,-65,-71,-61,-52,30,-48,-49,-50,-58,-59,-60,-56,-74,-54,-55,]),'BRACES_RIGHT':([2,3,4,5,6,7,8,9,10,11,12,13,15,19,22,23,24,25,26,27,28,30,40,41,42,59,60,61,70,71,72,76,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,107,108,110,111,112,113,115,116,117,118,119,120,121,125,126,127,128,129,131,132,133,134,135,136,137,138,139,140,141,],[-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-13,-42,-72,-39,-40,-43,-44,-45,-46,-47,-75,-62,-63,-4,-33,-34,-35,-42,-66,-70,117,-67,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-51,-75,-73,-41,-64,-75,-75,-57,131,-65,132,133,-71,-61,138,-52,-75,-68,-69,-48,-49,-50,-58,-59,-60,-56,-74,141,-54,-55,]),'POWOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[43,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,43,-42,43,43,43,43,43,-36,-37,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-41,-64,-65,-71,43,-48,-49,-50,]),'MULOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[44,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,44,-42,44,44,-30,-31,-32,-36,-37,44,-14,-15,44,44,44,44,44,44,44,44,44,44,-26,44,44,44,44,-41,-64,-65,-71,44,-48,-49,-50,]),'SHIFTOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[46,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,46,-42,46,46,-30,-31,-32,-36,-37,46,-14,-15,-16,-17,46,46,46,46,46,46,46,46,-26,46,46,46,46,-41,-64,-65,-71,46,-48,-49,-50,]),'RELOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[47,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,47,-42,47,47,-30,-31,-32,-36,-37,47,-14,-15,-16,-17,None,47,47,47,47,47,47,47,-26,47,47,47,47,-41,-64,-65,-71,47,-48,-49,-50,]),'EQOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[48,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,48,-42,48,48,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,48,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,48,-41,-64,-65,-71,48,-48,-49,-50,]),'BITANDOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[49,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,49,-42,49,49,-30,-31,-32,-36,-37,49,-14,-15,-16,-17,-18,49,-20,49,49,49,49,49,-26,49,49,49,49,-41,-64,-65,-71,49,-48,-49,-50,]),'BITOROP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[50,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,50,-42,50,50,-30,-31,-32,-36,-37,50,-14,-15,-16,-17,-18,50,-20,-21,50,50,50,50,-26,50,50,50,50,-41,-64,-65,-71,50,-48,-49,-50,]),'DOTDOT':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[51,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,51,-42,51,51,-30,-31,-32,-36,-37,51,-14,-15,-16,-17,-18,51,-20,-21,None,-23,-24,-25,-26,51,51,51,51,-41,-64,-65,-71,51,-48,-49,-50,]),'ANDAND':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[52,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,52,-42,52,52,-30,-31,-32,-36,-37,52,-14,-15,-16,-17,-18,52,-20,-21,52,-23,52,52,-26,52,52,52,52,-41,-64,-65,-71,52,-48,-49,-50,]),'OROR':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[53,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,53,-42,53,53,-30,-31,-32,-36,-37,53,-14,-15,-16,-17,-18,53,-20,-21,53,-23,-24,-25,-26,53,53,53,53,-41,-64,-65,-71,53,-48,-49,-50,]),'DORDOR':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[54,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,54,-42,54,54,-30,-31,-32,-36,-37,54,-14,-15,-16,-17,-18,54,-20,-21,54,-23,-24,-25,-26,54,54,54,54,-41,-64,-65,-71,54,-48,-49,-50,]),'MATCHOP':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[55,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,55,-42,55,55,-30,-31,-32,-36,-37,55,-14,55,55,55,55,55,55,55,55,55,55,55,-26,55,55,55,55,-41,-64,-65,-71,55,-48,-49,-50,]),'WAND':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[56,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,56,-42,56,56,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,56,-20,-21,-22,-23,-24,-25,-26,-27,56,56,56,-41,-64,-65,-71,56,-48,-49,-50,]),'WOR':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[57,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,57,-42,57,57,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,57,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,57,-41,-64,-65,-71,57,-48,-49,-50,]),'WXOR':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[58,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,58,-42,58,58,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,58,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,58,-41,-64,-65,-71,58,-48,-49,-50,]),'DEREF':([13,15,22,23,24,25,26,27,28,40,41,59,60,61,68,70,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,123,131,132,133,],[61,-42,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,61,-42,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-41,-64,-65,-71,61,-48,-49,-50,]),'ASSIGNOP':([15,65,],[63,106,]),'NEW':([17,],[67,]),'SHIFT':([18,30,64,73,106,112,113,],[71,71,71,71,124,71,71,]),'PARANTHESIS_R':([18,22,23,24,25,26,27,28,40,41,59,60,61,64,68,69,70,71,72,73,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,105,110,111,112,113,114,117,120,128,129,131,132,133,],[-75,-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,-75,110,111,-42,-66,-70,-75,-67,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,122,-41,-64,-75,-75,130,-65,-71,-68,-69,-48,-49,-50,]),'COMMA':([18,22,23,24,25,26,27,28,30,40,41,59,60,61,64,68,69,70,71,72,73,76,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,105,110,111,112,113,114,117,120,128,129,131,132,133,],[-75,-39,-40,-43,-44,-45,-46,-47,-75,-62,-63,-33,-34,-35,-75,-67,112,-42,-66,-70,-75,112,-67,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,112,-41,-64,-75,-75,112,-65,-71,-68,-69,-48,-49,-50,]),'HASH_OP':([18,22,23,24,25,26,27,28,30,40,41,59,60,61,64,68,69,70,71,72,73,76,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,105,110,111,112,113,114,117,120,128,129,131,132,133,],[-75,-39,-40,-43,-44,-45,-46,-47,-75,-62,-63,-33,-34,-35,-75,-67,113,-42,-66,-70,-75,113,-67,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,113,-41,-64,-75,-75,113,-65,-71,-68,-69,-48,-49,-50,]),'SEMI':([22,23,24,25,26,27,28,40,41,59,60,61,62,70,74,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,110,111,117,120,122,123,124,130,131,132,133,],[-39,-40,-43,-44,-45,-46,-47,-62,-63,-33,-34,-35,103,-42,115,-30,-31,-32,-36,-37,-38,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,121,-41,-64,-65,-71,134,135,136,140,-48,-49,-50,]),'STDIN':([39,],[86,]),'>':([86,],[120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,107,127,],[1,125,139,]),'statementlist':([0,107,127,],[2,2,2,]),'empty':([0,18,30,64,73,107,112,113,127,],[3,72,72,72,72,3,72,72,3,]),'statement':([0,2,107,127,],[4,42,4,4,]),'package_dec':([0,2,107,127,],[5,5,5,5,]),'var_dec':([0,2,107,127,],[6,6,6,6,]),'function_dec':([0,2,107,127,],[7,7,7,7,]),'function_call':([0,2,107,127,],[8,8,8,8,]),'comment':([0,2,107,127,],[9,9,9,9,]),'cons_dec':([0,2,107,127,],[10,10,10,10,]),'bless_st':([0,2,107,127,],[11,11,11,11,]),'return_st':([0,2,107,127,],[12,12,12,12,]),'term':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[13,13,68,74,77,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,77,77,123,13,77,77,13,]),'termbinop':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'termunop':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'INPUT':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'hash_exp':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'first_hash':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'second_hash':([0,2,18,21,30,33,34,35,36,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,73,106,107,112,113,127,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'argument':([18,30,64,73,112,113,],[69,76,105,114,128,129,]),'braces_left':([66,],[107,]),'set_cons':([67,],[109,]),'block':([109,],[126,]),'braces_right':([125,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> statementlist','body',1,'p_body','parser.py',40),
  ('body -> empty','body',1,'p_body','parser.py',41),
  ('statementlist -> statement','statementlist',1,'p_statementlist','parser.py',46),
  ('statementlist -> statementlist statement','statementlist',2,'p_statementlist','parser.py',47),
  ('statement -> package_dec','statement',1,'p_statement','parser.py',53),
  ('statement -> var_dec','statement',1,'p_statement','parser.py',54),
  ('statement -> function_dec','statement',1,'p_statement','parser.py',55),
  ('statement -> function_call','statement',1,'p_statement','parser.py',56),
  ('statement -> comment','statement',1,'p_statement','parser.py',57),
  ('statement -> cons_dec','statement',1,'p_statement','parser.py',58),
  ('statement -> bless_st','statement',1,'p_statement','parser.py',59),
  ('statement -> return_st','statement',1,'p_statement','parser.py',60),
  ('statement -> term','statement',1,'p_statement','parser.py',61),
  ('termbinop -> term POWOP term','termbinop',3,'p_termbinop','parser.py',66),
  ('termbinop -> term MULOP term','termbinop',3,'p_termbinop','parser.py',67),
  ('termbinop -> term ADDOP term','termbinop',3,'p_termbinop','parser.py',68),
  ('termbinop -> term SHIFTOP term','termbinop',3,'p_termbinop','parser.py',69),
  ('termbinop -> term RELOP term','termbinop',3,'p_termbinop','parser.py',70),
  ('termbinop -> term EQOP term','termbinop',3,'p_termbinop','parser.py',71),
  ('termbinop -> term BITANDOP term','termbinop',3,'p_termbinop','parser.py',72),
  ('termbinop -> term BITOROP term','termbinop',3,'p_termbinop','parser.py',73),
  ('termbinop -> term DOTDOT term','termbinop',3,'p_termbinop','parser.py',74),
  ('termbinop -> term ANDAND term','termbinop',3,'p_termbinop','parser.py',75),
  ('termbinop -> term OROR term','termbinop',3,'p_termbinop','parser.py',76),
  ('termbinop -> term DORDOR term','termbinop',3,'p_termbinop','parser.py',77),
  ('termbinop -> term MATCHOP term','termbinop',3,'p_termbinop','parser.py',78),
  ('termbinop -> term WAND term','termbinop',3,'p_termbinop','parser.py',79),
  ('termbinop -> term WOR term','termbinop',3,'p_termbinop','parser.py',80),
  ('termbinop -> term WXOR term','termbinop',3,'p_termbinop','parser.py',81),
  ('termunop -> ADDOP term','termunop',2,'p_termunop','parser.py',156),
  ('termunop -> ! term','termunop',2,'p_termunop','parser.py',157),
  ('termunop -> ~ term','termunop',2,'p_termunop','parser.py',158),
  ('termunop -> term INCREMENT','termunop',2,'p_termunop','parser.py',159),
  ('termunop -> term DECREMENT','termunop',2,'p_termunop','parser.py',160),
  ('termunop -> term DEREF','termunop',2,'p_termunop','parser.py',161),
  ('termunop -> INCREMENT term','termunop',2,'p_termunop','parser.py',162),
  ('termunop -> DECREMENT term','termunop',2,'p_termunop','parser.py',163),
  ('termunop -> WNOT term','termunop',2,'p_termunop','parser.py',164),
  ('term -> termbinop','term',1,'p_term','parser.py',204),
  ('term -> termunop','term',1,'p_term','parser.py',205),
  ('term -> PARANTHESIS_L term PARANTHESIS_R','term',3,'p_term','parser.py',206),
  ('term -> NAME','term',1,'p_term','parser.py',207),
  ('term -> NUMBER','term',1,'p_term','parser.py',208),
  ('term -> STRING','term',1,'p_term','parser.py',209),
  ('term -> INPUT','term',1,'p_term','parser.py',210),
  ('term -> PRINT','term',1,'p_term','parser.py',211),
  ('term -> hash_exp','term',1,'p_term','parser.py',212),
  ('term -> Q BRACES_LEFT NAME BRACES_RIGHT','term',4,'p_term','parser.py',213),
  ('term -> QQ BRACES_LEFT NAME BRACES_RIGHT','term',4,'p_term','parser.py',214),
  ('term -> QX BRACES_LEFT NAME BRACES_RIGHT','term',4,'p_term','parser.py',215),
  ('package_dec -> PACKAGE NAME SEMI','package_dec',3,'p_package_dec','parser.py',232),
  ('cons_dec -> SUB NEW set_cons block','cons_dec',4,'p_cons_dec','parser.py',239),
  ('set_cons -> <empty>','set_cons',0,'p_set_cons','parser.py',246),
  ('bless_st -> BLESS PARANTHESIS_L argument PARANTHESIS_R SEMI','bless_st',5,'p_bless_st','parser.py',253),
  ('block -> BRACES_LEFT body BRACES_RIGHT','block',3,'p_block','parser.py',261),
  ('function_dec -> SUB NAME braces_left body braces_right','function_dec',5,'p_function_dec','parser.py',267),
  ('return_st -> RETURN term SEMI','return_st',3,'p_return_st','parser.py',274),
  ('function_call -> NAME PARANTHESIS_L argument PARANTHESIS_R SEMI','function_call',5,'p_function_call','parser.py',284),
  ('var_dec -> MY NAME ASSIGNOP term SEMI','var_dec',5,'p_var_dec','parser.py',291),
  ('var_dec -> MY NAME ASSIGNOP SHIFT SEMI','var_dec',5,'p_var_dec','parser.py',292),
  ('var_dec -> NAME ASSIGNOP term SEMI','var_dec',4,'p_var_dec','parser.py',293),
  ('hash_exp -> first_hash','hash_exp',1,'p_hash_exp','parser.py',306),
  ('hash_exp -> second_hash','hash_exp',1,'p_hash_exp','parser.py',307),
  ('first_hash -> PARANTHESIS_L argument PARANTHESIS_R','first_hash',3,'p_first_hash','parser.py',314),
  ('second_hash -> BRACES_LEFT argument BRACES_RIGHT','second_hash',3,'p_second_hash','parser.py',333),
  ('argument -> SHIFT','argument',1,'p_argument','parser.py',351),
  ('argument -> term','argument',1,'p_argument','parser.py',352),
  ('argument -> argument COMMA argument','argument',3,'p_argument','parser.py',353),
  ('argument -> argument HASH_OP argument','argument',3,'p_argument','parser.py',354),
  ('argument -> empty','argument',1,'p_argument','parser.py',355),
  ('INPUT -> < STDIN >','INPUT',3,'p_INPUT','parser.py',359),
  ('comment -> COMMENT','comment',1,'p_comment','parser.py',363),
  ('braces_left -> BRACES_LEFT','braces_left',1,'p_braces_left','parser.py',367),
  ('braces_right -> BRACES_RIGHT','braces_right',1,'p_braces_right','parser.py',372),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',377),
]
