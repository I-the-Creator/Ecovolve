#include <stdio.h>
#include <stdlib.h>

// this line allows for the function to be written below the main function
double cube(double num);

int main() {
  printf("Answer: %f", cube(7.0));

  return 0;
}

double cube(double num) {
  double result = num * num * num;
  return result;
}
