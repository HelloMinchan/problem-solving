#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool compare(const pair<double, int> &a, const pair<double, int> &b)
{
    if (a.first == b.first)
    {
        if (b.second > a.second)
            return true;
        else
            return false;
    }
    else if (a.first > b.first)
        return true;
    else
        return false;
}

vector<int> solution(int N, vector<int> stages)
{
    vector<int> answer;

    vector<pair<double, int>> location;

    for (int i = 0; i < N + 2; i++)
        location.push_back({0, i});

    for (int i = 0; i < stages.size(); i++)
        location[stages[i]].first += 1.0;

    double people = stages.size();
    for (int i = 1; i < N + 1; i++)
    {
        double now = location[i].first;
        if (now == 0.0)
        {
            location[i].first = 0.0;
            continue;
        }

        people -= now;

        location[i].first = now / people;
    }

    sort(location.begin() + 1, location.end() - 1, compare);

    for (int i = 1; i < N + 1; i++)
        answer.push_back(location[i].second);

    return answer;
}