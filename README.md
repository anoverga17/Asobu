# Asobu

## About
This is an interpreter for Asobu, a toy programming language. The current goal 
is to implement a simple functional programming language with support for basic numeric operations. 

## Specifications
The following is the current syntax specification for Asobu version 0.1 
```
Value = Num 
  
Expression = Value                    # literal expression
           | ID                       # id expression
           | Expression + Expression  # add expression (left precedence)
           | Expression - Expression  # subtract expression (left precedence)
           | Expression * Expression  # multiply expression (right precedence)
           | Expression / Expression  # divide expression (right precedence)
           | lambda ID { Expression } # lambda expression
           | Expression << Expression # apply expression (right precedence)
           | (Expression)           
           ;
```
More language features will be added in the future. 

## Running
Currently, there is only an interpreter written in Python which uses the SLY lexer and parser library.
In the future, the interpreter will be converted into C/C++ for speed and better portability.

To begin, run interpreter.py using python3 to open the Asobu language terminal. 

Currently, the terminal only accepts one line expressions. 

To exit the terminal type `quit` into the prompt. 

\
To run a file (which can be more than one line long) specify the text you are entering is a pathname by first using the
`$f` flag. Hence, your command should look similar to this: \
\
`gai (> $f ./sample/file/path/example.ga` \
\
To run an Asobu file, also ensure that it has a .ga extension or the terminal will not recognize it as a valid file.

