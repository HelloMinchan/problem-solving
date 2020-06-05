#include <string>
#include <vector>
#include <cstring>
#include <iostream>
using namespace std;

bool stu[31];

int solution(int n, vector<int> lost, vector<int> reserve)
{
    int answer = 0;

    memset(stu, true, sizeof(stu));

    for (int i = 0; i < lost.size(); i++)
    {
        stu[lost[i]] = false;
        for (int j = 0; j < reserve.size(); j++)
        {
            if (lost[i] == reserve[j])
            {
                stu[lost[i]] = true;
                reserve.erase(reserve.begin() + j);
            }
        }
    }

    for (int i = 1; i < n + 1; i++)
    {
        if (!stu[i])
        {
            bool check = false;
            for (int j = 0; j < reserve.size(); j++)
            {
                if (i - 1 == reserve[j])
                {
                    reserve.erase(reserve.begin() + j);
                    check = true;
                    break;
                }
            }

            if (!check)
            {
                for (int j = 0; j < reserve.size(); j++)
                {
                    if (i + 1 == reserve[j])
                    {
                        reserve.erase(reserve.begin() + j);
                        check = true;
                        break;
                    }
                }
            }

            if (check)
            {
                answer++;
                continue;
            }

            continue;
        }
        answer++;
    }

    return answer;
}