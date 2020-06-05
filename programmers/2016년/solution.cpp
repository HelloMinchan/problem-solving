#include <string>
#include <vector>
#include <deque>

using namespace std;

string solution(int a, int b)
{
    string answer = "";

    deque<string> dq;
    dq.push_back("FRI");
    dq.push_back("SAT");
    dq.push_back("SUN");
    dq.push_back("MON");
    dq.push_back("TUE");
    dq.push_back("WED");
    dq.push_back("THU");

    int day = 0;
    for (int i = 1; i < a; i++)
    {
        if (i == 2)
            day += 29;
        else if (i == 8)
            day += 31;
        else
        {
            if (i >= 9)
            {
                if (i % 2)
                    day += 30;
                else
                    day += 31;
            }
            else
            {
                if (i % 2)
                    day += 31;
                else
                    day += 30;
            }
        }
    }

    day += b;

    for (int i = 1; i < day; i++)
    {
        dq.push_back(dq.front());
        dq.pop_front();
    }

    answer = dq.front();

    return answer;
}