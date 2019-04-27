package rect;
sub new 
{
    my $class = shift;
    my $self =
    {
        length=>shift,
        breadth=>shift
    };
    bless($self,$class);
    return $self;

}

sub area 
{
    my $self=shift;
    return $self->{length}*$self->{breadth};
}

sub perimeter
{
    my $self=shift;
    return $self->{length}*2+$self->{breadth}*2;   
}
1;