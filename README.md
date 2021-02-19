# Asobu

## About
This is an interpreter for Asobu, a toy programming language. The compiler is called gai. The current goal 
is to implement a simple functional programming language with support for basic numeric operations. 

## Specifications
The following is the current syntax specification for Asobu version 0.01 
```
Value = Num 

Term =  Num 
       |(Expression)
  
Expression = Term
            | Expression + Term 
            | Expression - Term 
```
Currently only binary addition/subtraction can be evaluated. **Multiple nested expressions is not yet supported** \
More language features will be added in the future. 

## Running
To run a program from the Asobu directory, simply call in a terminal: \
\
`./gai <file_path>` \
\
Please note that the gai binary file works only for linux and macOS. \
By convention, Asobu files end with a .ga extension.
