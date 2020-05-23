#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int X = 0;
    cin >> X;

    int temp = 0;
    int diff = 0;
    int i = 1;

    while (X > temp)
    {
        temp += i;
        i++;
    }

    i--;
    diff = temp - X;

    if (!(i % 2))
        cout << i - diff << "/" << 1 + diff;
    else
        cout << 1 + diff << "/" << i - diff;

    return 0;
}