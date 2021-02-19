#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#ifndef LINE_LEN
#define LINE_LEN 118
#endif

double eval_term(char *line, int *i);
double eval_expr(char *line, int *i);
void parse(const char *filename);