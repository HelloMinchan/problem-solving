#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int N = 0;
    cin >> N;

    vector<int[3]> prices(N);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> prices[i][j];
        }
    }

    vector<int[3]> costs(N);
    int candidatePrice = 0;

    for (int i = 0; i < N; i++)
    {
        if (i == 0)
        {
            costs[i][0] = prices[i][0];
            costs[i][1] = prices[i][1];
            costs[i][2] = prices[i][2];
            continue;
        }
        for (int j = 0; j < 3; j++)
        {
            candidatePrice = 1000001;

            for (int k = 0; k < 3; k++)
            {
                if (!(j == k))
                {
                    if (candidatePrice > costs[i - 1][k])
                        candidatePrice = costs[i - 1][k];
                }
            }

            costs[i][j] = prices[i][j] + candidatePrice;
        }
    }

    cout << *min_element(costs[N - 1], costs[N - 1] + 3);

    return 0;
}