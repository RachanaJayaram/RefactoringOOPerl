use lib 'G:\\extra\\oo_perl\\Rachana_Version\\version4\\testing\\input\\';
use server::rect;
sub fibonacci
{
    print "This gets deleted";
}
sub fibonacci
{
    local $,=".\t";
    $n=shift;
    print "$n terms of the fibonacci series\n";
    local $\=".\t";
    $a=0 ;
    $b=1 ;
    print "$a ","$b ";
    for ( $i=2; $i <= $n; $i++)
    {
        $c = $a + $b;
        print "$c ";
        $a = $b ;
        $b = $c ;
    }
}

$x=2;
$y=3;
print "Constructing a rectangle of length $x and breadth $y \n";

#Constructing a rectangle of length $x and breadth $y 
$d = rect->new($x,$y);
#area and perimeter 
$area = $d->area();
$perimeter = $d->perimeter();
print "A rectangle of length $x and breadth $y \nHas area = $area \t perimeter = $perimeter \n";
$,=" ";
$\="\n";
print "Fibonacci";
fibonacci($area);


