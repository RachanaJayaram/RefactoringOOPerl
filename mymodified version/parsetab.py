
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALB ARB COMMA COMMENT EQUALS KEYWORD LB LFB MY NEW NUMBER OPER PACKAGE RB RETURN RFB SEMI SHIFT STRING SUB VARIABLE newlbody : statementlist\n            | emptystatementlist : statement\n                    | statementlist statementstatement : var_dec\n                | function_call\n                | output\n                | comment\n                | cond_stat\n                | package_dec\n                | function_def\n                | return_stpackage_dec : PACKAGE KEYWORD SEMI upind body lowind NUMBER SEMIupind :lowind :function_def : SUB KEYWORD blockoutput : KEYWORD out SEMI out : VARIABLE\n            | STRING\n            | out COMMA out function_call : KEYWORD LB argument RB SEMIargument : VARIABLE\n                | STRING\n                | argument COMMA argument\n                | emptyvar_dec : variable EQUALS exp SEMI\n                | variable EQUALS input SEMI\n                | variable EQUALS SHIFT SEMIvariable : MY VARIABLE\n                | VARIABLEreturn_st : RETURN exp SEMIexp : NUMBER\n            | VARIABLE\n            | STRING\n            | exp OPER expinput : ALB KEYWORD ARBcomment : COMMENTcond_stat : KEYWORD LB condition RB block\n                    | KEYWORD LB for_cond RB blockfor_cond : VARIABLE EQUALS exp SEMI VARIABLE sign exp SEMI incrementincrement : VARIABLE OPER OPER\n                    | VARIABLE sign expblock : l_braces body r_bracesl_braces : LFBr_braces : RFBcondition : VARIABLE sign expsign : EQUALS\n            | OPER\n            | ALB\n            | ARB\n            | sign signempty :'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,15,21,44,47,50,52,53,54,70,73,74,80,81,87,],[-52,0,-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-16,-31,-26,-27,-28,-21,-38,-39,-43,-45,-13,]),'KEYWORD':([0,2,4,5,6,7,8,9,10,11,12,15,16,17,21,37,44,46,47,48,49,50,52,53,54,66,70,73,74,80,81,87,],[14,14,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,27,28,-4,55,-17,-14,-16,14,-44,-31,-26,-27,-28,14,-21,-38,-39,-43,-45,-13,]),'COMMENT':([0,2,4,5,6,7,8,9,10,11,12,15,21,44,46,47,48,49,50,52,53,54,66,70,73,74,80,81,87,],[15,15,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-14,-16,15,-44,-31,-26,-27,-28,15,-21,-38,-39,-43,-45,-13,]),'PACKAGE':([0,2,4,5,6,7,8,9,10,11,12,15,21,44,46,47,48,49,50,52,53,54,66,70,73,74,80,81,87,],[16,16,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-14,-16,16,-44,-31,-26,-27,-28,16,-21,-38,-39,-43,-45,-13,]),'SUB':([0,2,4,5,6,7,8,9,10,11,12,15,21,44,46,47,48,49,50,52,53,54,66,70,73,74,80,81,87,],[17,17,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-14,-16,17,-44,-31,-26,-27,-28,17,-21,-38,-39,-43,-45,-13,]),'RETURN':([0,2,4,5,6,7,8,9,10,11,12,15,21,44,46,47,48,49,50,52,53,54,66,70,73,74,80,81,87,],[18,18,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-14,-16,18,-44,-31,-26,-27,-28,18,-21,-38,-39,-43,-45,-13,]),'MY':([0,2,4,5,6,7,8,9,10,11,12,15,21,44,46,47,48,49,50,52,53,54,66,70,73,74,80,81,87,],[19,19,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-14,-16,19,-44,-31,-26,-27,-28,19,-21,-38,-39,-43,-45,-13,]),'VARIABLE':([0,2,4,5,6,7,8,9,10,11,12,14,15,18,19,21,22,23,44,45,46,47,48,49,50,51,52,53,54,57,60,61,62,63,64,66,70,73,74,75,77,80,81,82,86,87,89,92,93,],[20,20,-3,-5,-6,-7,-8,-9,-10,-11,-12,25,-37,31,33,-4,31,41,-17,25,-14,-16,20,-44,-31,31,-26,-27,-28,72,31,31,-48,-49,-50,20,-21,-38,-39,-51,-47,-43,-45,84,31,-13,90,-48,31,]),'RFB':([2,3,4,5,6,7,8,9,10,11,12,15,21,44,47,48,49,50,52,53,54,67,70,73,74,80,81,87,],[-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,-4,-17,-16,-52,-44,-31,-26,-27,-28,81,-21,-38,-39,-43,-45,-13,]),'NUMBER':([2,3,4,5,6,7,8,9,10,11,12,15,18,21,22,44,46,47,50,51,52,53,54,60,61,62,63,64,66,70,73,74,75,77,79,80,81,83,86,87,92,93,],[-1,-2,-3,-5,-6,-7,-8,-9,-10,-11,-12,-37,30,-4,30,-17,-14,-16,-31,30,-26,-27,-28,30,30,-48,-49,-50,-52,-21,-38,-39,-51,-47,-15,-43,-45,85,30,-13,-48,30,]),'EQUALS':([13,20,33,41,60,61,62,63,64,75,77,84,86,90,92,93,],[22,-30,-29,61,77,-47,-48,-49,-50,77,-47,77,77,77,-48,77,]),'LB':([14,],[23,]),'STRING':([14,18,22,23,45,51,57,60,61,62,63,64,75,77,86,92,93,],[26,32,32,42,26,32,42,32,32,-48,-49,-50,-51,-47,32,-48,32,]),'SHIFT':([22,],[36,]),'ALB':([22,41,60,61,62,63,64,75,77,84,86,90,92,93,],[37,63,63,-47,-48,-49,-50,63,-47,63,63,63,-48,63,]),'RB':([23,30,31,32,38,39,40,41,42,43,57,68,71,72,76,91,94,95,],[-52,-32,-33,-34,56,58,59,-22,-23,-25,-52,-35,-24,-22,-46,-40,-41,-42,]),'COMMA':([23,24,25,26,38,41,42,43,57,65,71,72,],[-52,45,-18,-19,57,-22,-23,-25,-52,45,57,-22,]),'SEMI':([24,25,26,27,29,30,31,32,34,35,36,56,65,68,69,78,85,88,],[44,-18,-19,46,50,-32,-33,-34,52,53,54,70,-20,-35,-36,82,87,89,]),'LFB':([28,58,59,],[49,49,49,]),'OPER':([29,30,31,32,34,41,60,61,62,63,64,68,75,76,77,78,84,86,88,90,92,93,95,],[51,-32,-33,-34,51,62,62,-47,-48,-49,-50,51,62,51,-47,51,62,62,51,92,94,62,51,]),'ARB':([41,55,60,61,62,63,64,75,77,84,86,90,92,93,],[64,69,64,-47,-48,-49,-50,64,-47,64,64,64,-48,64,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,48,66,],[1,67,79,]),'statementlist':([0,48,66,],[2,2,2,]),'empty':([0,23,48,57,66,],[3,43,3,43,3,]),'statement':([0,2,48,66,],[4,21,4,4,]),'var_dec':([0,2,48,66,],[5,5,5,5,]),'function_call':([0,2,48,66,],[6,6,6,6,]),'output':([0,2,48,66,],[7,7,7,7,]),'comment':([0,2,48,66,],[8,8,8,8,]),'cond_stat':([0,2,48,66,],[9,9,9,9,]),'package_dec':([0,2,48,66,],[10,10,10,10,]),'function_def':([0,2,48,66,],[11,11,11,11,]),'return_st':([0,2,48,66,],[12,12,12,12,]),'variable':([0,2,48,66,],[13,13,13,13,]),'out':([14,45,],[24,65,]),'exp':([18,22,51,60,61,86,93,],[29,34,68,76,78,88,95,]),'input':([22,],[35,]),'argument':([23,57,],[38,71,]),'condition':([23,],[39,]),'for_cond':([23,],[40,]),'block':([28,58,59,],[47,73,74,]),'l_braces':([28,58,59,],[48,48,48,]),'sign':([41,60,75,84,86,90,93,],[60,75,75,86,75,93,75,]),'upind':([46,],[66,]),'r_braces':([67,],[80,]),'lowind':([79,],[83,]),'increment':([89,],[91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> statementlist','body',1,'p_body','parsing.py',18),
  ('body -> empty','body',1,'p_body','parsing.py',19),
  ('statementlist -> statement','statementlist',1,'p_statementlist','parsing.py',26),
  ('statementlist -> statementlist statement','statementlist',2,'p_statementlist','parsing.py',27),
  ('statement -> var_dec','statement',1,'p_statement','parsing.py',34),
  ('statement -> function_call','statement',1,'p_statement','parsing.py',35),
  ('statement -> output','statement',1,'p_statement','parsing.py',36),
  ('statement -> comment','statement',1,'p_statement','parsing.py',37),
  ('statement -> cond_stat','statement',1,'p_statement','parsing.py',38),
  ('statement -> package_dec','statement',1,'p_statement','parsing.py',39),
  ('statement -> function_def','statement',1,'p_statement','parsing.py',40),
  ('statement -> return_st','statement',1,'p_statement','parsing.py',41),
  ('package_dec -> PACKAGE KEYWORD SEMI upind body lowind NUMBER SEMI','package_dec',8,'p_package_dec','parsing.py',47),
  ('upind -> <empty>','upind',0,'p_upind','parsing.py',53),
  ('lowind -> <empty>','lowind',0,'p_lowind','parsing.py',60),
  ('function_def -> SUB KEYWORD block','function_def',3,'p_function_def','parsing.py',67),
  ('output -> KEYWORD out SEMI','output',3,'p_output','parsing.py',74),
  ('out -> VARIABLE','out',1,'p_out','parsing.py',81),
  ('out -> STRING','out',1,'p_out','parsing.py',82),
  ('out -> out COMMA out','out',3,'p_out','parsing.py',83),
  ('function_call -> KEYWORD LB argument RB SEMI','function_call',5,'p_function_call','parsing.py',90),
  ('argument -> VARIABLE','argument',1,'p_argument','parsing.py',97),
  ('argument -> STRING','argument',1,'p_argument','parsing.py',98),
  ('argument -> argument COMMA argument','argument',3,'p_argument','parsing.py',99),
  ('argument -> empty','argument',1,'p_argument','parsing.py',100),
  ('var_dec -> variable EQUALS exp SEMI','var_dec',4,'p_var_dec','parsing.py',107),
  ('var_dec -> variable EQUALS input SEMI','var_dec',4,'p_var_dec','parsing.py',108),
  ('var_dec -> variable EQUALS SHIFT SEMI','var_dec',4,'p_var_dec','parsing.py',109),
  ('variable -> MY VARIABLE','variable',2,'p_variable','parsing.py',123),
  ('variable -> VARIABLE','variable',1,'p_variable','parsing.py',124),
  ('return_st -> RETURN exp SEMI','return_st',3,'p_return_st','parsing.py',132),
  ('exp -> NUMBER','exp',1,'p_exp','parsing.py',137),
  ('exp -> VARIABLE','exp',1,'p_exp','parsing.py',138),
  ('exp -> STRING','exp',1,'p_exp','parsing.py',139),
  ('exp -> exp OPER exp','exp',3,'p_exp','parsing.py',140),
  ('input -> ALB KEYWORD ARB','input',3,'p_input','parsing.py',150),
  ('comment -> COMMENT','comment',1,'p_comment','parsing.py',157),
  ('cond_stat -> KEYWORD LB condition RB block','cond_stat',5,'p_cond_stat','parsing.py',164),
  ('cond_stat -> KEYWORD LB for_cond RB block','cond_stat',5,'p_cond_stat','parsing.py',165),
  ('for_cond -> VARIABLE EQUALS exp SEMI VARIABLE sign exp SEMI increment','for_cond',9,'p_for_cond','parsing.py',172),
  ('increment -> VARIABLE OPER OPER','increment',3,'p_increment','parsing.py',181),
  ('increment -> VARIABLE sign exp','increment',3,'p_increment','parsing.py',182),
  ('block -> l_braces body r_braces','block',3,'p_block','parsing.py',192),
  ('l_braces -> LFB','l_braces',1,'p_l_braces','parsing.py',198),
  ('r_braces -> RFB','r_braces',1,'p_r_braces','parsing.py',205),
  ('condition -> VARIABLE sign exp','condition',3,'p_condition','parsing.py',212),
  ('sign -> EQUALS','sign',1,'p_sign','parsing.py',219),
  ('sign -> OPER','sign',1,'p_sign','parsing.py',220),
  ('sign -> ALB','sign',1,'p_sign','parsing.py',221),
  ('sign -> ARB','sign',1,'p_sign','parsing.py',222),
  ('sign -> sign sign','sign',2,'p_sign','parsing.py',223),
  ('empty -> <empty>','empty',0,'p_empty','parsing.py',235),
]
