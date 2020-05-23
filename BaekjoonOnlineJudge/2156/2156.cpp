#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n = 0;
    cin >> n;

    vector<int> wines(n + 1, 0);
    for (int i = 1; i < n + 1; i++)
        cin >> wines[i];

    vector<int> memoization(n + 1, 0);
    int maxNum = 0;

    for (int i = 1; i < n + 1; i++)
    {
        if (i == 1)
        {
            memoization[1] = wines[1];
            continue;
        }
        if (i == 2)
        {
            memoization[2] = wines[1] + wines[2];
            continue;
        }

        maxNum = max(memoization[i - 3] + wines[i - 1] + wines[i], memoization[i - 2] + wines[i]);
        memoization[i] = max(maxNum, memoization[i - 1]);
    }

    cout << memoization[n];

    return 0;
}