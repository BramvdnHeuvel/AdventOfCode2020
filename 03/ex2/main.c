#include <stdio.h>

int main() {
    char trees[31];
    FILE *fp = fopen("input.txt", "r");
    
    int l_x[5]          = {1, 3, 5, 7, 1};
    int l_y[5]          = {1, 1, 1, 1, 2};
    int current_x[5]    = {0, 0, 0, 0, 0};
    int current_y[5]    = {0, 0, 0, 0, 0};
    int trees_found[5]  = {0, 0, 0, 0, 0};

    // Iterate over trees
    for (int i=0; i<323; i++) {
        fscanf(fp, "%s", trees);

        for (int j=0; j<5; j++) {
            if (current_y[j] == i) {
                trees_found[j]  += (trees[current_x[j]] == '#');

                current_x[j]    = (current_x[j] + l_x[j]) % 31;
                current_y[j]    += l_y[j];
            }
        }

    }

    // Calculate the product
    int product = 1;
    for (int i=0; i<5; i++) {
        product *= trees_found[i];
    }

    printf("%d\n", product);
    return 0;
}