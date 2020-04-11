#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;
int N, T;
vector<int> arr, tempArr, result;

bool investigate(int gap)
{
    tempArr.clear();
    tempArr.resize(N, 0);
    copy(arr.begin(), arr.end(), tempArr.begin());
    int operCount = 0;

    for (int i = 0; i < N - 1; i++)
    {
        if (tempArr[i + 1] - tempArr[i] > gap)
        {
            operCount += tempArr[i + 1] - (tempArr[i] + gap);
            tempArr[i + 1] = tempArr[i] + gap;
        }
    }

    for (int i = N - 1; i > 0; i--)
    {
        if (tempArr[i - 1] - tempArr[i] > gap)
        {
            operCount += tempArr[i - 1] - (tempArr[i] + gap);
            tempArr[i - 1] = tempArr[i] + gap;
        }
    }

    if (operCount <= T)
        return true;
    return false;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> T;
    arr.resize(N, 0);
    result.resize(N, 0);

    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int left = 0;
    int right = 1000000000;
    int mid = 0;

    while (left <= right)
    {
        mid = (left + right) / 2;

        if (investigate(mid))
        {
            copy(tempArr.begin(), tempArr.end(), result.begin());
            right = mid - 1;
        }
        else
            left = mid + 1;
    }

    for (int i = 0; i < N; i++)
        cout << result[i] << " ";

    return 0;
}