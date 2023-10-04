#include <stdio.h>
#include <stdlib.h>

int main() {
  // int i;
  // for(i = 1; i <= 5; i++){
  //     printf("%d\n", i);
  // }

  // int luckyNumbers[] = {4, 8, 15, 16, 23, 42}

  // int i;
  // for(i = 0; i <= 6; i++){
  //     printf("%d\n", luckyNumbers[i]);
  // }

  int nums[3][2] = {{1, 2}, {3, 4}, {5, 6}};

  // printf("%d", nums[0][0])

  int i, j;
  for (i = 0; i < 3; i++) {
    for (j = 0; j < 2; j++) {
      printf("%d,", nums[i][j]);
    }
    printf("\n");
  }

  return 0;
}
