#include <iostream>

using namespace std;

int n;
int bambooForest[501][501];
int memoization[501][501];
int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};
int maxAliveDay = 0;

int DFS(int i, int j)
{
    if (memoization[i][j])
        return memoization[i][j];

    memoization[i][j] = 1;
    int ii = 0;
    int jj = 0;
    int day = 0;

    for (int way = 0; way < 4; way++)
    {
        ii = i + dx[way];
        jj = j + dy[way];

        if (ii < 0 || ii > n - 1 || jj < 0 || jj > n - 1)
            continue;

        if (bambooForest[i][j] < bambooForest[ii][jj])
        {
            day = DFS(ii, jj) + 1;
            if (memoization[i][j] < day)
                memoization[i][j] = day;
        }
    }

    return memoization[i][j];
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> bambooForest[i][j];

    int aliveDay = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            aliveDay = DFS(i, j);

            if (maxAliveDay < aliveDay)
                maxAliveDay = aliveDay;
        }
    }

    cout << maxAliveDay;

    return 0;
}