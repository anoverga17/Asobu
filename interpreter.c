#include "parser.h"

/*
 * The main interpreter. To test to see if the program works, run:
 * ./gai sample_programs/addition.ga
 */
int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf("Invalid Use! Expected Usage: ./gai <file_path>\n");
		return 1;
	}
	const char *src = argv[1];
	parse(src);
	return 0;
}
