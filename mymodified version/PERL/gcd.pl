#program to find gcd of two numbers
print "Enter number 1: ";
$p = <STDIN>;
chomp($p);
print "Enter number 2: ";
$q = <STDIN>;
chomp($q);
while($q!=0)
{
  $r = $p % $q;
  $p = $q;
  $q = $r;
}
print "The gcd is: ",$p;
