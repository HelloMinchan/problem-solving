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

    int N = str2.size();
    int M = str1.size();

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (!i || !j)
                continue;

            if (str1[j] == str2[i])
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

    int lcsLength = memoization[N - 1][M - 1];
    vector<char> stack;

    for (int i = N - 1; i > 0; i--)
    {
        for (int j = 0; j < M; j++)
        {
            if (memoization[i][j] == lcsLength)
            {
                if (str1[j] == str2[i])
                {
                    stack.push_back(str1[j]);
                    lcsLength--;
                    break;
                }
            }
        }
    }

    lcsLength = memoization[N - 1][M - 1];
    cout << lcsLength << '\n';
    for (int i = 0; i < lcsLength; i++)
    {
        cout << stack.back();
        stack.pop_back();
    }

    return 0;
}