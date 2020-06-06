#include <string>
#include <stack>
#include <cmath>

using namespace std;

int solution(string dr)
{
    int sum = 0;
    stack<int> s;
    int temp = 0;
    int temp2 = 0;

    for (int i = 0; i < dr.size(); i++)
    {
        if (dr[i] == '1')
        {
            s.push(dr[i] - '0');

            if (dr[i + 1] == '0')
            {
                s.pop();
                s.push(10);
                i++;
            }

            if (dr[i + 1] == 'D')
            {
                temp = s.top();
                s.pop();
                s.push(pow(temp, 2));
            }

            else if (dr[i + 1] == 'T')
            {
                temp = s.top();
                s.pop();
                s.push(pow(temp, 3));
            }
        }
        else
        {
            s.push(dr[i] - '0');

            if (dr[i + 1] == 'D')
            {
                temp = s.top();
                s.pop();
                s.push(pow(temp, 2));
            }
            else if (dr[i + 1] == 'T')
            {
                temp = s.top();
                s.pop();
                s.push(pow(temp, 3));
            }
        }
        i++;

        if (dr[i + 1] == '*' || dr[i + 1] == '#')
        {
            if (dr[i + 1] == '*')
            {
                if (s.size() == 1)
                {
                    temp = s.top();
                    s.pop();
                    s.push(temp * 2);
                }
                else
                {
                    temp2 = s.top();
                    s.pop();
                    temp = s.top();
                    s.pop();
                    temp *= 2;
                    s.push(temp);
                    temp2 *= 2;
                    s.push(temp2);
                }
            }
            else
            {
                temp = s.top();
                s.pop();
                s.push(-temp);
            }
            i++;
        }
    }

    while (!s.empty())
    {
        sum += s.top();
        s.pop();
    }

    return sum;
}