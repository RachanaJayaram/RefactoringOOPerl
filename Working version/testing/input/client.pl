
# !/usr/local/bin/perl -w -I G:\extra\oo_perl\Rachana_Version\version4\testing\input\
use lib 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\';
use server::rect;

$x=10;
$y=15;
print "Constructing a rectangle of length $x and breadth $y \n";

#Constructing a rectangle of length $x and breadth $y 
$d = rect->new($x,$y);
$d->area();

#area and perimeter 
$area = $d->area();
$perimeter = $d->perimeter();

print "A rectangle of length $x and breadth $y \nHas area = $area \t perimeter = $perimeter \n";


