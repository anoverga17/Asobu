#include "parser.h"

/*
 * Outputs the value of <number>
 * to standard output
 */
void output_num(double number) {
	if (floorf(number) == number) {
		printf("%.0f\n", number);
	} else {
		printf("%f\n", number);
	}
}

void build_syntax_tree(Patterns *syn_tree) {
	int error;
	error = regcomp(&(syn_tree->value), "^([:digit:][:digit:]*)|([:digit:][:digit:]*[.][:digit:][:digit:]);$*", 0);
	if (error != 0) {
		perror("Error building value regex");
		exit(1);
	}
}

/*
 * Takes a string <expr> and determines
 * what operation to perform. It then
 * performs the operation and outputs 
 * the result to standard output
 */
void interpret(char *expr) {
	Patterns *syntax = malloc(sizeof(Patterns));
	build_syntax_tree(syntax);
	if (1 == regexec(&(syntax->value), expr, 0, NULL, 0)) {
		double value = strtod(expr, NULL);
		output_num(value);
	} else {
		printf("Unimplemented\n");
	}

	free(syntax);
}

/*
 * Reads the file specified by <filename>
 * and interprets the commands written. 
 */
void parse(const char *filename) {
	FILE *src = fopen(filename, "r");
	char *line = malloc(sizeof(char)*118);
	fread(line, sizeof(char), 118, src);
	interpret(line);
	fclose(src);
	free(line);
}
