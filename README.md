# Refactoring_oo_perl
<small>
The files perly.y and toke.c are from Perl Source Code. Will be very helpful for making the parser for project.
doc.txt is the test file.
p2p.py is the actual python file.
Usage: python p2p.py

#Rachana <br>
Check week2 files for latest code ->written by me
<br>
#Rachana 
<h5>
Week 3 used parse tree built by yacc instead of a list. This made ordering the elements easier.
</h5>
Week 4
#skanda
I have implemented all expressions. There is ternary expression left which has to be implemented. Expressions like unary preincrement/post increment which don't have support in python have been implemented as function instead. Also perl unlike python attempts to convert strings to int and proceeds with arithmentic operations. this conversion is not similar to python. That has also been implemented. <h5> All these have been implemented in ctools module. </h5>

Hashes have to be integrated from Gaurav's module. Also changes have to be made to function declaration depending on whether it is written in a package or not. Even constructors have to be properly integrated.

<h5> I have given comments whereever necessary for easy completion of the incomplete integration work of mine ! </h5>

I have uploaded 4 files. lexer.py , parser.py, ctools.py and input_code.pm. Also for easy coordination next time, I think it would be better to use uniform token names and grammer rules.


Found one bug in the code.
Skanda : In the lexing you gave higher priority to <,> when compared to <=,>= .
</small>
Current State : Inheritance - being worked on.

We now have a two stage parser. First stage generates a lookup table that is required by the second stage for translation. Necessary for local global and my. (check the 2 stage branch)
          
