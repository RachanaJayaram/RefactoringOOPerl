package date;
sub new{
    my $class = shift;
    my %self =
    {
        "dd" => shift,
        "mm" => shift,
        "yy" => shift
    };
    bless($self, $class);
    return $self;
}

sub dispdate
{
    my $self = shift;
    my $date = shift;
}
1;