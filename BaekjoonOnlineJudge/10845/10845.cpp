#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    deque<int> q;

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

            q.push_back(num);
        }
        else if (order == "empty")
            cout << q.empty() << "\n";
        else if (order == "size")
            cout << q.size() << "\n";
        else if (order == "pop")
        {
            if (q.empty())
                cout << -1 << "\n";
            else
            {
                cout << q.front() << "\n";
                q.pop_front();
            }
        }
        else if (order == "front")
        {
            if (q.empty())
                cout << -1 << "\n";
            else
                cout << q.front() << "\n";
        }
        else
        {
            if (q.empty())
                cout << -1 << "\n";
            else
                cout << q.back() << "\n";
        }
    }

    return 0;
}