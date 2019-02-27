package date;
sub new {
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
sub dispdate{
    my $self=shift;
    print  $self->{dd}, "//",$self->{mm},"//",$self->{yy},'=',$self->{dd}+$self->{mm}+$self->{yy};
    print  $self->{dd}, "//",$self->{mm},"//",$self->{yy},'=',$self->{dd}+$self->{mm}-$self->{yy};
    print  $self->{dd}, "//",$self->{mm},"//",$self->{yy},'=',$self->{dd}+$self->{mm}*$self->{yy};
    print  $self->{dd}, "//",$self->{mm},"//",$self->{yy},'=',$self->{dd}+$self->{mm}/$self->{yy};
}
sub  dispdate2{
    my $self=shift;
    print  $self->{dd}, "//",$self->{mm},"//",$self->{yy},'=',$self->{dd}+$self->{mm}/$self->{yy};
    print  $self->{dd}, "//",$self->{mm},"//",$self->{yy},'=',$self->{dd}+$self->{mm}*$self->{yy};
}
