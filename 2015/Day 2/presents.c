#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]) {
    // Check correct number of args
    if (argc != 2) {
        printf("Usage: ./presents infile\n");
        return 1;
    }

    // Open input file
    char *infile = argv[1];
    FILE *fileptr = fopen(infile, "r");
    if (fileptr == NULL) {
        printf("Could not open %s\n", infile);
        return 1;
    }

    // Read file data line by line
    int paper = 0, ribbon = 0;
    char line[16];
    while (fgets(line, 16, fileptr) != NULL) {
        // Parse present dimensions
        int l = atoi(strtok(line, "x"));
        int w = atoi(strtok(NULL, "x"));
        int h = atoi(strtok(NULL, "x"));

        // Calculate surface area and volume
        int surfaceArea = (2 * l * w) + (2 * w * h) + (2 * h * l);
        int volume = l * w * h;

        // Calculate area and perimeter of smallest side
        int smallestArea = fmin(fmin(l * w, w * h), h * l);
        int smallestPerimeter = 2 * fmin(fmin(l + w, w + h), h + l);

        // Update needed amounts of wrapping paper and ribbon
        paper += surfaceArea + smallestArea;
        ribbon += volume + smallestPerimeter;
    }

    // Close file
    fclose(fileptr);

    // Display results
    printf("Part 1: %d\n", paper);
    printf("Part 2: %d\n", ribbon);
}