#include "parser.h"


/*
 * Outputs the value of <number> to standard output
 */
void output_num(double number) {
	if (floorf(number) == number) {
		printf("%.0f\n", number);
	} else {
		printf("%f\n", number);
	}
}

/*
 * Parse the line if the first non space word is a 
 * number. Otherwise, return NAN
 */
double eval_num(char *line, int *i) {
	char *rest;
	double terminal_value = strtod((line + *i), &rest);
	if (strcmp((line + *i), rest) == 0) {
		return NAN;
	} else {
		strcpy((line + *i), rest);
		return terminal_value;
	}
}

/*
 * Parse syntax for builtin functions
 */
double _eval_builtin(char *line, int *i) {
	double val1 = eval_expr(line, i);
	char op[4];
	strncpy(op, (line + *i), 3);
	op[4] = '\0'; 
	*i += 3; 
	double val2 = eval_expr(line, i);
	if (strcmp(op, " + ") == 0) {
		return val1 + val2;
	} else if (strcmp(op, " - ") == 0) {
		return val1 - val2;
	} else if (strcmp(op, " * ") == 0) {
		return val1 * val2;
	} else if (strcmp(op, " / ") == 0) {
		if (val2 == 0) {
			perror("Zero Division Error");
			exit(1);
		} else {
			return val1 / val2;
		}
	}
	perror("Syntax Error: Make Sure Spacing is Accurate!");
	exit(1);
}

/*
 * Evaluates the value of a single expression as defined in README.md
 */ 
double eval_expr(char *line, int *i) {
	double num = eval_num(line, i);
	if (!isnan(num)) {
		if (line[*i] == ')') {
			*i += 1;
		}
		return num;
	}
	if (line[*i] == '(') {
		*i += 1;
		return _eval_builtin(line, i);
	}
	perror("Syntax Error -e");
	exit(1);
}


/*
 * Reads the file specified by <filename> and interprets the commands written. 
 */
void parse(const char *filename) {
	FILE *src = fopen(filename, "r");
	char *line = malloc(sizeof(char)*LINE_LEN);
	fread(line, sizeof(char), LINE_LEN, src);
	int *i = malloc(sizeof(int));
	*i = 0;
	output_num(eval_expr(line, i));
	fclose(src);
	free(line);
	free(i);
}