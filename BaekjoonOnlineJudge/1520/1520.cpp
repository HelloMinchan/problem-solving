#include <iostream>
#include <cstring>

using namespace std;

int N, M;
int MAP[501][501];
int memoization[501][501];
int dx[4] = {0, 0, 1, -1}, dy[4] = {1, -1, 0, 0};

int DFS(int i, int j)
{
    if (!i && !j)
        return 1;
    if (i < 0 || i >= N || j < 0 || j >= M)
        return 0;
    if (memoization[i][j] != -1)
        return memoization[i][j];

    memoization[i][j] = 0;

    int ii = 0;
    int jj = 0;

    for (int way = 0; way < 4; way++)
    {
        ii = i + dx[way];
        jj = j + dy[way];

        if (ii < 0 || ii >= N || jj < 0 || jj >= M)
            continue;

        if (MAP[ii][jj] > MAP[i][j])
            memoization[i][j] += DFS(ii, jj);
    }

    return memoization[i][j];
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> MAP[i][j];

    memset(memoization, -1, sizeof(memoization));

    cout << DFS(N - 1, M - 1);

    return 0;
}