#include <stdio.h>
#include <stdlib.h>

int main() {
  char characterName[] = "John";
  int characterAge = 35;
  printf("Sir %s is %d\n", characterName, characterAge);
  characterAge = 60;
  printf("Sir %s is %d", characterName, characterAge);

  return 0;
}
