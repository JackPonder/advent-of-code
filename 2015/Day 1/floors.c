#include <stdio.h>

int main(int argc, char *argv[]) {
    // Check correct number of args
    if (argc != 2) {
        printf("Usage: ./floors infile\n");
        return 1;
    }

    // Open input file
    char *infile = argv[1];
    FILE *fileptr = fopen(infile, "r");
    if (fileptr == NULL) {
        printf("Could not open %s\n", infile);
        return 1;
    }

    // Read file data one character at a time
    int floor = 0, pos = -1;
    for (unsigned i = 1; ; i++) {
        // Get next character in file
        char c = fgetc(fileptr);

        // Stop once end of file is reached
        if (c == EOF) {
            break;
        }

        // Update floor number
        if (c == '(') {
            floor += 1;
        } else if (c == ')') {
            floor -= 1;
        }

        // Save position of first character that reaches the basement
        if (pos == -1 && floor == -1) {
            pos = i;
        }
    }

    // Display results
    printf("Part 1: %d\n", floor);
    printf("Part 2: %d\n", pos);
}