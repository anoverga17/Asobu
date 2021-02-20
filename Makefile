all: interpreter 

interpreter: parser.c interpreter.c
	gcc -g -Wall -Wextra -std=gnu99 -o gai parser.c interpreter.c -lm

.PHONY: clean all

clean:	
	rm gai
