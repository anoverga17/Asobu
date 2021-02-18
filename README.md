# Asobu

## About
This is an interpreter for Asobu, a toy programming language. The compiler is called gai. The current goal 
is to implement a simple functional programming language with support for basic numeric operations. 

## Specifications
The following is the current syntax specification for Asobu version 0.01 
```
Value = Num 
  
Expression = Value; |
             (Expression + Expression); |
             (Expression - Expression); |
             (Expression * Expression); |
             (Expression / Expression); |
```
**Currently only plain values can be evaluated. The functions do not yet work.**
More language features will be added in the future. 

## Running
To run a program from the Asobu directory, simply call in a terminal: \
\
`./gai <file_path>` \
\
Please note that the gai binary file works only for linux and macOS. \
By convention, Asobu files end with a .ga extension.
