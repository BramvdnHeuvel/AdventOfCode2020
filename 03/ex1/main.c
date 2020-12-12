#include <stdio.h>

void load_trees(char **array);

int main() {
    char trees[31];
    FILE *fp = fopen("input.txt", "r");
    
    int x = 0;
    int y = 0;
    int trees_found = 0;

    // Iterate over trees
    for (int i=0; i<323; i++) {
        fscanf(fp, "%s", trees);

        if (y==i) {
            trees_found = trees_found + (trees[x] == '#');

            x = (x + 3) % 31;
            y = y + 1;
        }
    }

    printf("%d\n", trees_found);
    return 0;
}