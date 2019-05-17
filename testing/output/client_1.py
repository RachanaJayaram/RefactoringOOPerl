str_=lambda x: '' if x==None else str(x)

# !/usr/local/bin/perl -w -I G:\extra\oo_perl\Rachana_Version\version4\testing\input\
import sys
sys.path.insert(0, 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\')
import server.date as date
d=date.date(15,8,1947)
d.dispdate()
