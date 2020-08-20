#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int> a, pair<int, int> b)
{
    if (a.second == b.second)
        return a.first < b.first;
    else
        return a.second < b.second;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, int>> coords;

    for (int i = 0; i < N; i++)
    {
        int t1, t2;
        cin >> t1 >> t2;

        coords.push_back({t1, t2});
    }

    sort(coords.begin(), coords.end(), compare);

    for (int i = 0; i < coords.size(); i++)
        cout << coords[i].first << " " << coords[i].second << '\n';

    return 0;
}