#include <iostream>

using namespace std;

int memoization[1001][1001];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0, K = 0;
    cin >> N >> K;

    for (int i = 1; i < N + 1; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            if (i == j || !j)
            {
                memoization[i][j] = 1;
                continue;
            }
            memoization[i][j] = (memoization[i - 1][j - 1] + memoization[i - 1][j]) % 10007;
        }
    }

    cout << memoization[N][K];

    return 0;
}