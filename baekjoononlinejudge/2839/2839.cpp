#include <iostream>

using namespace std;

int memoization[5001];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    int compositeNum = 0;
    int bag = 0;

    for (int i = 3; i < N + 1; i++)
    {
        if (!(i % 5))
        {
            memoization[i] = memoization[i - 5] + 1;
            continue;
        }
        else if (!(i % 3))
        {
            memoization[i] = memoization[i - 3] + 1;
            continue;
        }
        else
        {
            compositeNum = i;
            bag = 0;

            while (compositeNum % 3)
            {
                compositeNum -= 5;
                bag++;
            }

            if (!(compositeNum % 3) && compositeNum >= 3)
                memoization[i] = bag + memoization[compositeNum];
            else
                memoization[i] = -1;
        }
    }

    cout << memoization[N];

    return 0;
}