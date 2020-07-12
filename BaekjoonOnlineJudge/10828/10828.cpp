#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<int> s;

    int N;
    cin >> N;

    while (N--)
    {
        string order;
        cin >> order;

        if (order == "push")
        {
            int num;
            cin >> num;

            s.push(num);
        }
        else if (order == "top")
        {
            if (s.empty())
                cout << -1 << "\n";
            else
                cout << s.top() << "\n";
        }
        else if (order == "empty")
            cout << s.empty() << "\n";
        else if (order == "size")
            cout << s.size() << "\n";
        else
        {
            if (s.empty())
                cout << -1 << "\n";
            else
            {
                cout << s.top() << "\n";
                s.pop();
            }
        }
    }

    return 0;
}