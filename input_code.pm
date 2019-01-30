package date;
sub hello {
    my $class = shift;
   # my %self =
    #{
     #   "dd" => shift,
      #  "mm" => shift,
       # "yy" => shift
    #};
    #the hash is not working. have to fix the errors
    bless($self, $class);
    return $self;
}

sub dispdate
{
    my $self = shift;
    my $date = shift;
}

   
