#include <iostream>
using namespace std;
int main(void)
{
	int a, b;
	cin >> a >> b;
	cout << fixed;
	cout.precision(9);
	cout << (double)a / b << endl;
}