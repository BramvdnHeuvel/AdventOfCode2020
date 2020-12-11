#include <stdio.h>

int main() {
    FILE *fp;
    int getallen[200];

    fp = fopen("input.txt", "r");

    for (int i=0; i<200; i++) {
        // Read line from file
        fscanf(fp, "%d", &(getallen[i]));

        // Evaluate if the current number already meets
        // the requirement with any of the previous
        // numbers
        for (int j=0; j<i; j++) {
            for (int k=0; k<j; k++) {
                int sum = getallen[i] + getallen[j] + getallen[k];

                if (sum == 2020) {
                    int product = getallen[i] * getallen[j] * getallen[k];

                    printf("%d\n", product);
                    return 0;
                }
            }
        }
    }

    return 1;
}