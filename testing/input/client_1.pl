
# !/usr/local/bin/perl -w -I G:\extra\oo_perl\Rachana_Version\version4\testing\input\
use lib 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\';
use server::date;
$,="\t";
$\="\n";
$d = date->new(15,8,1947);
$d->dispdate();

