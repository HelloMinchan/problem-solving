#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int stairNum = 0;

    cin >> stairNum;

    vector<int> stairs(stairNum, 0);
    vector<int> memoization(stairNum, 0);

    for (int i = 0; i < stairNum; i++)
        cin >> stairs[i];

    if (stairNum == 1)
    {
        cout << stairs[0];
        exit(0);
    }
    if (stairNum == 2)
    {
        cout << stairs[0] + stairs[1];
        exit(0);
    }

    for (int i = 0; i < stairNum; i++)
    {
        if (!i)
            memoization[0] = stairs[0];
        else if (i == 1)
            memoization[1] = stairs[0] + stairs[1];
        else if (i == 2)
        {
            if (stairs[0] + stairs[2] > stairs[1] + stairs[2])
                memoization[2] = stairs[0] + stairs[2];
            else
                memoization[2] = stairs[1] + stairs[2];
        }
        else
        {
            if (stairs[i] + stairs[i - 1] + memoization[i - 3] > stairs[i] + memoization[i - 2])
                memoization[i] = stairs[i] + stairs[i - 1] + memoization[i - 3];
            else
                memoization[i] = stairs[i] + memoization[i - 2];
        }
    }

    cout << memoization[stairNum - 1];

    return 0;
}