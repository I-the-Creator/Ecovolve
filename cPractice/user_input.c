#include <stdio.h>
#include <stdlib.h>

int main() {
  double gpa;
  printf("Enter your gpa: ");
  scanf("%lf", &gpa);
  printf("You gpa is %f", gpa);

  char grade;
  printf("Enter your grade: ");
  scanf("%c", &grade);
  printf("You grade is %c", grade);

  char name[20];
  printf("Enter your name: ");
  fgets(name, 20, stdin);
  printf("You name is %s", name);

  return 0;
}
