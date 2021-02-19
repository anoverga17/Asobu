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

void printlin(char *line, int *i) {
	printf("<<< To be Parsed >>>\n");
	int j = *i;
	while (line[j] != '\0') {
		printf("%c", line[j]);
		j++;
	}
	printf("\n<<< End >>>\n");
}

/*
 * Evaluates the value of a single term as defined in README.md
 */ 
double eval_term(char *line, int *i) {
	int num = line[*i];
	int isnum = isdigit(num);
	if (isnum) {
		double value = strtod((line + *i), NULL);
		int dot = 0;
		while (isnum || (line[*i] == '.' && dot == 0)) {
			*i += 1;
			num = line[*i];
			isnum = isdigit(num);
			if (line[*i] == '.') {
				dot = 1;
			}
		}
		return value;
	} else if (line[*i] == '('){
		*i += 1;
		double evaluated = eval_expr(line, i);
		if (line[*i] == ')') {
			return evaluated;
		} 
	} 
	perror("Invalid Syntax");
	exit(1);
}

/*
 * Evaluates the value of a single expression as defined in README.md
 */ 
double eval_expr(char *line, int *i) {
	double result = eval_term(line, i);
	int add = -1;
	while ((line[*i] != '\0') && (line[*i] != '\n') && (line[*i] != '\t') && (line[*i] != ')')) {
		char c = line[*i];
		*i += 1;
 		switch (c) {
			case '+':
				add = 1;
				break;
			case '-':
				add = 0;
				break;
			case ' ':
				break;
			default:
				*i -= 1;
				if (add == 1) {
					return result + eval_term(line, i);
				} else if (add == 0) {
					return result - eval_term(line, i);
				} else {
					perror("Syntax Error Not a Valid Operation");
					exit(1);
				}
				break;
		}
	}
	return result;
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
}
