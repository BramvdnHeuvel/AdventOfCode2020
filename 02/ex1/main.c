#include <stdio.h>
#include "main.h"

int main() {
    FILE *fp;
    int min;
    int max;
    char c;
    char buff[32];

    fp = fopen("input.txt", "r");

    int matching_pwds = 0;

    for (int i=0; i<1000; i++) {
        fscanf(fp, "%d-%d %c: %s", &min, &max, &c, buff);
        matching_pwds = matching_pwds + check_password(buff, c, min, max);
    }

    printf("%d\n", matching_pwds);
}

int check_password(char *password, char c, int min, int max) {
    int i = 0;
    int occurrences = 0;

    while (password[i] != '\0') {
        char m = password[i];
        if (c == m) {
            occurrences++;
        }

        i++;
    }

    return ((occurrences >= min) && (occurrences <= max));
}