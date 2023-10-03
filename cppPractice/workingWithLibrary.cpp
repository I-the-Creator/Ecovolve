#include <iostream>
#include <cmath>

using namespace std;

// int main()
// {
//     double result = pow(2, 3);
//     // double result = floor(1.2);
//     cout << result;
//     return 0;
// }

int main()
{
    cout << "Enter radius: ";
    double radius;
    cin >> radius;
    const double pi = 3.14;
    double area = pi * pow(radius, 2);
    cout << area;
    return 0;
}