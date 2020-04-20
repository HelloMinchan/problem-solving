#include <iostream>

using namespace std;

int gameboard[101][101];
long long memoization[101][101];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> gameboard[i][j];

    int ii = 0;
    int jj = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            ii = i;
            jj = j;

            for (int x = 0; x < ii; x++)
            {
                if (gameboard[x][j] == i - x)
                {
                    if (!x && !j)
                    {
                        memoization[i][j] = 1;
                        break;
                    }
                    if (memoization[x][j])
                        memoization[i][j] += memoization[x][j];
                }
            }

            for (int y = 0; y < jj; y++)
            {
                if (gameboard[i][y] == j - y)
                {
                    if (!y && !i)
                    {
                        memoization[i][j] = 1;
                        break;
                    }
                    if (memoization[i][y])
                        memoization[i][j] += memoization[i][y];
                }
            }
        }
    }

    cout << memoization[N - 1][N - 1];

    return 0;
}