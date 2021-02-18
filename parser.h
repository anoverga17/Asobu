#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <regex.h>

typedef struct {
	regex_t value;
	regex_t addition;
	regex_t subtraction;
	regex_t multiplication;
	regex_t division;
} Patterns;

void parse(const char *filename);