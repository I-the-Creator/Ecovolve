#include <iostream>

int main() {
    // double x = 10;
    // int y = 3;
    // double z = x / y;
    // std::cout << z;
    // return 0;

    int x = 10;
    int y = x++;    // x = 11, y = 10
    int z = ++x;    // x = 11, z = 11

    std::cout << y;
    return 0;
}