# Asobu

## About
This is an interpreter for Asobu, a toy programming language. The current goal 
is to implement a simple functional programming language with support for basic numeric operations and if expressions. 

## Specifications
The following is the current syntax specification for Asobu version 1.0
```
expr:
	arith_expr
	bool_expr
	'lambda' func_def
	'if' '(' bool_expr ')' ':' scope ('else' ':' scope)? 'end'
	var

arith_expr
	: INT
	| -arith_expr
	| arith_expr + arith_expr
	| arith_expr - arith_expr
	| arith_expr / arith_expr
	| arith_expr * arith_expr
	| arith_expr % arith_expr
	;

bool_expr
	: true
	| false
	| !bool_expr
	| bool_expr 'and' bool_expr
	| bool_expr 'or' bool_expr
	| arith_expr '<' arith_expr
	| expr '==' expr
	| expr '!=' expr
	;

assignment_stmt
	: 'let' varname '=' expr '\n'
	| 'func' varname func_def '\n'
	;

func_def
	: '(' param* ')' ':' scope 'end'
	;

scope:
	| assignment_stmt* expr
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

