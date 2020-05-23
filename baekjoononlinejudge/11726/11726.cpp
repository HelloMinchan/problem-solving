#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n = 0;
    cin >> n;

    vector<int> memoization(n, 0);

    for (int i = 0; i < n; i++)
    {
        if (i == 0)
        {
            memoization[0] = 1;
            continue;
        }
        if (i == 1)
        {
            memoization[1] = 2;
            continue;
        }

        memoization[i] = (memoization[i - 1] + memoization[i - 2]) % 10007;
    }

    cout << memoization[n - 1];

    return 0;
}