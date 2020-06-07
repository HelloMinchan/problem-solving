#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(string skill, vector<string> skill_trees)
{
    set<char> s;

    for (int i = 0; i < skill.size(); i++)
        s.insert(skill[i]);

    int answer = 0;

    for (int i = 0; i < skill_trees.size(); i++)
    {
        int seq = 0;
        bool isPossible = true;

        for (int j = 0; j < skill_trees[i].size(); j++)
        {
            if (s.count(skill_trees[i][j]))
            {
                if (skill_trees[i][j] != skill[seq])
                {
                    isPossible = false;
                    break;
                }
                seq++;
            }

            if (!isPossible)
                break;
        }

        if (isPossible)
            answer++;
    }

    return answer;
}