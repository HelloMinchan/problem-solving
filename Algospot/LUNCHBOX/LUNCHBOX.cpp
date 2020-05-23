#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>

using namespace std;

struct cmp
{
    bool operator()(pair<int, int> oldValue, pair<int, int> newValue)
    {
        return oldValue.second > newValue.second;
    }
};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T = 0;
    cin >> T;

    int N = 0;
    vector<int> microwaveTime, eatingTime;
    vector<pair<int, int>> total;
    int eachTime = 0;

    while (T--)
    {
        cin >> N;
        int time = 0;
        int remainingEatingTime = 0;

        microwaveTime.clear();
        eatingTime.clear();
        total.clear();

        for (int i = 0; i < N; i++)
        {
            cin >> eachTime;
            microwaveTime.push_back(eachTime);
        }
        for (int i = 0; i < N; i++)
        {
            cin >> eachTime;
            eatingTime.push_back(eachTime);
        }
        for (int i = 0; i < N; i++)
        {
            time += microwaveTime[i];
            total.push_back({microwaveTime[i], eatingTime[i]});
        }

        sort(total.begin(), total.end(), cmp());

        for (int i = 0; i < N; i++)
        {
            remainingEatingTime -= total[i].first;
            remainingEatingTime = max(total[i].second, remainingEatingTime);
        }

        time += remainingEatingTime;

        cout << time << "\n";
    }

    return 0;
}