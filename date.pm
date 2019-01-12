#!/usr/local/bin/perl -w -I C:\Users\Rachana\Desktop\try\perl\
package date;
sub new
{
my $class = shift;
my $self =
{
dd => shift,
mm => shift,
yy => shift

};
bless($self, $class);
return $self;
}

sub dispdate
{
my $self = shift;
print $self->{dd}, " ", $self->{mm},
" ", $self->{yy}, "\n";

}

1;