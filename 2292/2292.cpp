#include <iostream>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int num = 1;
    int i = 1;
    int target = 0;
    cin >> target;

    while (true)
    {
        if (target > num)
        {
            num += 6 * i;
            i += 1;
            continue;
        }
        break;
    }

    cout << i;

    return 0;
}