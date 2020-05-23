#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int triangle[101][101];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int C = 0;
    cin >> C;

    int n = 0;
    while (C--)
    {
        cin >> n;
        memset(triangle, 0, sizeof(triangle));

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < i + 1; j++)
            {
                cin >> triangle[i][j];

                if (i >= 1)
                {
                    if (j == 0)
                        triangle[i][j] += triangle[i - 1][j];
                    else if (j == i)
                        triangle[i][j] += triangle[i - 1][j - 1];
                    else
                        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1]);
                }
            }
        }

        cout << *max_element(&triangle[n - 1][0], &triangle[n - 1][n + 1]) << "\n";
    }

    return 0;
}