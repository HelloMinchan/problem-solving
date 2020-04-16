#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, k;
    cin >> n >> k;

    vector<int> values(n, 0);
    for (int i = 0; i < n; i++)
        cin >> values[i];

    vector<int> memoization(k + 1, 0);
    memoization[0] = 1;

    for (int i = 0; i < n; i++)
        for (int j = 1; j < k + 1; j++)
            if (j - values[i] >= 0)
                memoization[j] += memoization[j - values[i]];

    cout << memoization[k];

    return 0;
}