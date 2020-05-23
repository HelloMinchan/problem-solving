#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n = 0;
    cin >> n;

    vector<int> nums(n, 0);
    vector<int> memoization(n, 0);
    int maxNum = -1001;

    for (int i = 0; i < n; i++)
        cin >> nums[i];

    for (int i = 0; i < n; i++)
    {
        if (!i)
        {
            maxNum = memoization[0] = nums[0];
            continue;
        }

        if (nums[i] < 0)
        {
            if (memoization[i - 1] > 0)
            {
                if (memoization[i - 1] + nums[i] > 0)
                    memoization[i] = memoization[i - 1] + nums[i];
                else
                    memoization[i] = nums[i];
            }
            else
                memoization[i] = nums[i];
        }
        else
        {
            if (memoization[i - 1] > 0)
                memoization[i] = memoization[i - 1] + nums[i];
            else
                memoization[i] = nums[i];
        }

        if (maxNum < memoization[i])
            maxNum = memoization[i];
    }

    cout << maxNum;

    return 0;
}