#include <stdio.h>
#include <stdlib.h>

int main() {

    int age = 30;
    int * pAge = &age;

    // printf("%p", &pAge);
    printf("%d", *&*&*&*&*&*&*&*&*&*&pAge);
    return 0;
}