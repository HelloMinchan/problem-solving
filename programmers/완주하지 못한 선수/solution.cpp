#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string solution(vector<string> participant, vector<string> completion)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string answer = "";

    multiset<string> s1;
    multiset<string> s2;

    for (int i = 0; i < participant.size(); i++)
        s1.insert(participant[i]);

    for (int i = 0; i < completion.size(); i++)
        s2.insert(completion[i]);

    for (int i = 0; i < participant.size(); i++)
    {
        if (s1.count(participant[i]) != s2.count(participant[i]))
            answer = participant[i];
    }

    return answer;
}