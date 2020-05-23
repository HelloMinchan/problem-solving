#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int sequence[501];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int C = 0;
    cin >> C;

    int N = 0;
    vector<int> LIS;
    int length = 0;
    vector<int>::iterator low;

    while (C--)
    {
        cin >> N;
        length = 0;
        memset(sequence, 0, sizeof(sequence));
        LIS.clear();
        LIS.push_back(0);

        for (int i = 0; i < N; i++)
            cin >> sequence[i];

        for (int i = 0; i < N; i++)
        {
            if (sequence[i] > LIS[length])
            {
                LIS.push_back(sequence[i]);
                length++;
                continue;
            }

            low = lower_bound(LIS.begin(), LIS.end(), sequence[i]);

            LIS[low - LIS.begin()] = sequence[i];
        }

        cout << length << "\n";
    }

    return 0;
}