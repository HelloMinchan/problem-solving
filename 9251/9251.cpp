#include <iostream>
#include <vector>
#include <string>

using namespace std;

int memoization[1001][1001];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string str1 = "";
    string str2 = "";
    cin >> str1;
    cin >> str2;
    str1 = "0" + str1;
    str2 = "0" + str2;

    int N = str1.size();
    int M = str2.size();

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (!i || !j)
                continue;

            if (str1[i] == str2[j])
                memoization[i][j] = memoization[i - 1][j - 1] + 1;
            else
            {
                if (memoization[i - 1][j] > memoization[i][j - 1])
                {
                    memoization[i][j] = memoization[i - 1][j];
                    continue;
                }
                memoization[i][j] = memoization[i][j - 1];
            }
        }
    }

    cout << memoization[N - 1][M - 1];

    return 0;
}