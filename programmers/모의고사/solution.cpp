#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

vector<int> solution(vector<int> answers)
{
    vector<int> answer;

    vector<vector<int>> person{
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};

    int p1 = 0, p2 = 0, p3 = 0;
    pair<int, int> score[3] = {{0, 1}, {0, 2}, {0, 3}};
    for (int i = 0; i < answers.size(); i++)
    {
        p1 = i % 5;
        p2 = i % 8;
        p3 = i % 10;

        if (answers[i] == person[0][p1])
            score[0].first++;
        if (answers[i] == person[1][p2])
            score[1].first++;
        if (answers[i] == person[2][p3])
            score[2].first++;
    }

    sort(score, score + 3, greater<pair<int, int>>());

    for (int i = 0; i < 3; i++)
    {
        if (!i)
        {
            answer.push_back(score[0].second);
            continue;
        }
        if (score[i].first == score[i - 1].first)
            answer.push_back(score[i].second);
        else
            break;
    }

    sort(answer.begin(), answer.end());

    return answer;
}