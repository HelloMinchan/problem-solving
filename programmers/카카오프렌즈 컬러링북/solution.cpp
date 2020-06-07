#include <vector>
#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int max_size_of_one_area;
vector<vector<bool>> visit;

void BFS(int color, int dx[], int dy[], vector<vector<int>> &picture, int m, int n, int x, int y)
{
    queue<pair<int, int>> q;

    q.push({x, y});

    int i = 0, j = 0;
    int ii = 0, jj = 0;
    int count = 0;

    while (!q.empty())
    {
        i = q.front().first;
        j = q.front().second;

        q.pop();

        if (visit[i][j])
            continue;

        visit[i][j] = true;
        count++;

        for (int way = 0; way < 4; way++)
        {
            ii = i + dx[way];
            jj = j + dy[way];

            if (ii < 0 || ii > m - 1 || jj < 0 || jj > n - 1)
                continue;

            if (picture[ii][jj] != color)
                continue;

            q.push({ii, jj});
        }
    }

    if (max_size_of_one_area < count)
        max_size_of_one_area = count;
}

vector<int> solution(int m, int n, vector<vector<int>> picture)
{
    max_size_of_one_area = 0;

    visit = vector<vector<bool>>(m, vector<bool>(n, false));
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    int count = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (picture[i][j] != 0 && !visit[i][j])
            {
                BFS(picture[i][j], dx, dy, picture, m, n, i, j);
                count++;
            }
        }
    }

    vector<int> answer(2);
    answer[0] = count;
    answer[1] = max_size_of_one_area;
    return answer;
}