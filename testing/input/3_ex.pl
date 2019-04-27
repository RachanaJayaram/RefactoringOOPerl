
sub foo
{
	print "deleted";
}
sub foo
{
	$z=shift;
	my $y = 20;
	local $z = 30;
	print "foo before g : \n  x : $x y : $y z : $z \n"; # x: 10 y: 20 z: 30 
	g();
	print "foo  after g : \n  x : $x y : $y z : $z \n"; #x: 2 y: 20 z: 3
	print "foo global : \n y : ",  $main::y,"\n"; # y : 2

}
sub g
{
	print "g : \n  x : $x y : $y z : $z \n"; # x: 10 y :  z: 30
	$x = 2; $y = 2; $z = 3;
}
$x = 10;
print "main before foo : \n  x : $x y : $y z : $z \n"; # x: 10 y:  z:  
foo($x);
print "main after foo : \n  x : $x y : $y z : $z \n"; # x : 2 y:2 z :10
