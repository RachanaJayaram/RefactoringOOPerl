print "12 terms of the fibonacci series\n";
$a=0 ;
$b=1 ;
print "$a $b ";
for ( $i=2; $i <= 12; $i++)
{
   $c = $a + $b;
   print "$c ";
   $a = $b ;
   $b = $c ;
}
print "\n";
