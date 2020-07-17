#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int N, M;
int box[1001][1001];
bool visit[1001][1001];
queue<pair<int, int>> q;
int unRipedTomato;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int BFS()
{
    int day = -1;

    while (q.size())
    {
        int qSize = q.size();
        day++;

        for (int oneDay = 0; oneDay < qSize; oneDay++)
        {
            int i = q.front().first;
            int j = q.front().second;
            q.pop();

            for (int way = 0; way < 4; way++)
            {
                int ii = i + dx[way];
                int jj = j + dy[way];

                if (ii < 0 || ii > N - 1 || jj < 0 || jj > M - 1)
                    continue;

                if (!visit[ii][jj] && box[ii][jj] != -1)
                {
                    visit[ii][jj] = true;
                    unRipedTomato--;
                    q.push({ii, jj});
                }
            }
        }
    }

    return day;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int answer = 0;

    cin >> M >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> box[i][j];

            if (box[i][j] == 0)
                unRipedTomato++;
            else if (box[i][j] == 1)
            {
                visit[i][j] = true;
                q.push({i, j});
            }
        }
    }

    if (!unRipedTomato)
        cout << 0;
    else
    {
        answer = BFS();

        if (unRipedTomato)
            cout << -1;
        else
            cout << answer;
    }

    return 0;
}