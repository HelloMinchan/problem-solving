#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int sudoku[9][9];
vector<pair<int, int>> zeroList;

bool check(int k, int sudoku[][9], int x, int y)
{
    for (int i = 0; i < 9; i++)
    {
        if (sudoku[x][i] == k)
            return false;
    }
    for (int i = 0; i < 9; i++)
    {
        if (sudoku[i][y] == k)
            return false;
    }

    int ii = (x / 3) * 3;
    int jj = (y / 3) * 3;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (sudoku[ii + i][jj + j] == k)
                return false;
        }
    }
    return true;
}

void DFS(int depth)
{
    if (depth == zeroList.size())
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                cout << sudoku[i][j] << " ";
            }
            cout << "\n";
        }
        exit(0);
    }

    int x = 0;
    int y = 0;

    for (int k = 1; k <= 9; k++)
    {
        x = zeroList[depth].first;
        y = zeroList[depth].second;

        if (check(k, sudoku, x, y))
        {
            sudoku[x][y] = k;
            DFS(depth + 1);
            sudoku[x][y] = 0;
        }
    }
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cin >> sudoku[i][j];

            if (!sudoku[i][j])
                zeroList.push_back({i, j});
        }
    }

    DFS(0);

    return 0;
}