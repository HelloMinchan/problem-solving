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
    int triangle[501][501];

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cin >> triangle[i][j];
        }
    }

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            if (j == 0)
                triangle[i][j] += triangle[i - 1][j];
            else if (j == i)
                triangle[i][j] += triangle[i - 1][j - 1];
            else
            {
                if (triangle[i - 1][j] > triangle[i - 1][j - 1])
                    triangle[i][j] += triangle[i - 1][j];
                else
                    triangle[i][j] += triangle[i - 1][j - 1];
            }
        }
    }

    cout << *max_element(triangle[n - 1], triangle[n - 1] + n + 1);

    return 0;
}