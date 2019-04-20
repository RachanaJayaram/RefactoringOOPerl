package child;
use parent 'parent','grandparent';
sub hi
{
  $name = "skanda";
  print "hello"."$name";
}