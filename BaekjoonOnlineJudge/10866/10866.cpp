#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    deque<int> dq;

    int N;
    cin >> N;

    while (N--)
    {
        string order;
        cin >> order;

        if (order == "push_front")
        {
            int num;
            cin >> num;

            dq.push_front(num);
        }
        else if (order == "push_back")
        {
            int num;
            cin >> num;

            dq.push_back(num);
        }
        else if (order == "empty")
            cout << dq.empty() << "\n";
        else if (order == "size")
            cout << dq.size() << "\n";
        else if (order == "pop_front")
        {
            if (dq.empty())
                cout << -1 << "\n";
            else
            {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        }
        else if (order == "pop_back")
        {
            if (dq.empty())
                cout << -1 << "\n";
            else
            {
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        }
        else if (order == "front")
        {
            if (dq.empty())
                cout << -1 << "\n";
            else
                cout << dq.front() << "\n";
        }
        else
        {
            if (dq.empty())
                cout << -1 << "\n";
            else
                cout << dq.back() << "\n";
        }
    }

    return 0;
}