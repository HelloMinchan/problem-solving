#include <iostream>
#include <algorithm>

using namespace std;

int memoization[1001][1001];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    int prices[1001] = {
        0,
    };
    for (int i = 1; i < N + 1; i++)
        cin >> prices[i];

    for (int i = 1; i < N + 1; i++)
        for (int j = 1; j < i + 1; j++)
            memoization[i][j] = prices[j] + *max_element(memoization[i - j], memoization[i - j] + (i - j + 1));

    cout << *max_element(memoization[N], memoization[N] + (N + 1));

    return 0;
}