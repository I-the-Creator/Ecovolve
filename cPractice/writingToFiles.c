#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
  // FILE * fpointer = fopen("employees.txt", "w");
  // fprintf(fpointer, "Jim, Salesmen\nPam, Receptionist\nOscar, Accounting");
  FILE *fpointer = fopen("employees.txt", "a");

  fprintf(fpointer, "Kelly, Customer Service");

  fclose(fpointer);
  return 0;
}
