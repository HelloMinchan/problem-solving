#include <iostream>

using namespace std;

int dailyCost[1001];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cout.setf(ios::fixed);
    cout.precision(8);

    int C = 0;
    cin >> C;

    int N = 0, L = 0;
    int day = 0;
    int rentCost = 0;
    double minRentCost = 0.0;
    while (C--)
    {
        cin >> N >> L;
        minRentCost = 987654321.0;

        for (int i = 0; i < N; i++)
            cin >> dailyCost[i];

        for (int i = 0; i <= N - L; i++)
        {
            day = 1;
            rentCost = 0;
            for (int j = i; j < N; j++)
            {
                rentCost += dailyCost[j];

                if (day >= L)
                {
                    if (minRentCost > rentCost / (double)day)
                        minRentCost = rentCost / (double)day;
                }

                day++;
            }
        }

        cout << minRentCost << "\n";
    }

    return 0;
}