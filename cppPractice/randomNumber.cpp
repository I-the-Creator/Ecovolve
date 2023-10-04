#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

int main() {
  // long elapsedSeconds = time(0); // Jan 1 1970
  // srand(elapsedSeconds);
  // int number = rand() % 10;
  // cout << elapsedSeconds;
  // return 0;
  const int minValue = 1;
  const short maxValue = 6;

  srand(time(0));
  short first = (rand() % (maxValue - minValue + 1)) + minValue;
  short second = (rand() % (maxValue - minValue + 1)) + minValue;

  cout << first << ", " << second;

  return 0;
}
