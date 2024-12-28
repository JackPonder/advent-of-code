#include <iostream>
#include <fstream>
#include <string>
#include <set>

struct Point {
    int x, y;

    bool operator<(const Point& other) const {
        if (x != other.x) {
            return x < other.x;
        }
        return y < other.y;
    }
};

int main(int argc, char *argv[]) {
    // Check correct number of args
    if (argc != 2) {
        std::cout << "Usage: ./houses infile\n";
        return 1;
    }

    // Open input file
    std::string infile = argv[1];
    std::ifstream file(infile);
    if (!file.is_open()) {
        std::cout << "Could not open " << infile << "\n";
        return 1;
    }

    // Keep track of current Santa positions and all visited positions
    Point santas[2] = {{0, 0}, {0, 0}};
    std::set<Point> visited{santas[0]};

    // Read file one character at a time
    char c, i = 0;
    while (file.get(c)) {
        // Update current position
        if (c == '^') {
            santas[i].y += 1;
        } else if (c == '>') {
            santas[i].x += 1;
        } else if (c == 'v') {
            santas[i].y -= 1;
        } else if (c == '<') {
            santas[i].x -= 1;
        }

        // Mark new position as visted
        visited.insert(santas[i]);

        // ALternate movements between santas
        i = !i;
    }

    // Close file
    file.close();

    // Display results
    std::cout << "Part 2: " << visited.size() << "\n";
}