#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <cstring>

using namespace std;

vector<int> solution(string s)
{
    struct cmp
    {
        bool operator()(pair<int, int> oldValue, pair<int, int> newValue)
        {
            return oldValue.second > newValue.second;
        }
    };
    vector<int> answer;
    vector<int> temp;
    int sLength = s.size();
    queue<char> q;
    string tempNum = "";
    bool isPop = false;
    string value = "";
    vector<pair<int, int>> hash;

    for (int i = 0; i < sLength; i++)
    {
        tempNum = "";

        if (s[i] != '{' && s[i] != '}')
            q.push(s[i]);

        if (s[i] == '}')
        {
            isPop = false;

            while (q.size())
            {
                isPop = true;
                value = q.front();
                q.pop();

                if (value != ",")
                    tempNum += value;
                else
                {
                    if (tempNum != "")
                    {
                        temp.push_back(stoi(tempNum));
                        tempNum = "";
                    }
                }
            }

            if (isPop && tempNum != "")
                temp.push_back(stoi(tempNum));
        }
    }

    for (int i = 0; i < 100001; i++)
        hash.push_back({i, 0});

    for (int i = 0; i < temp.size(); i++)
        hash[temp[i]].second++;

    sort(hash.begin(), hash.end(), cmp());

    for (int i = 0; i < 100001; i++)
    {
        if (!hash[i].second)
            break;
        answer.push_back(hash[i].first);
    }

    return answer;
}