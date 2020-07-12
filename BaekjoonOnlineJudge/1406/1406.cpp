#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    list<char> l;

    string init;
    cin >> init;

    for (int i = 0; i < init.size(); i++)
        l.push_back(init[i]);

    auto iter = l.end();

    int M;
    cin >> M;

    while (M--)
    {
        char order;
        cin >> order;

        if (order == 'L')
        {
            if (iter != l.begin())
                iter--;
        }
        else if (order == 'D')
        {
            if (iter != l.end())
                iter++;
        }
        else if (order == 'B')
        {
            if (iter != l.begin())
            {
                iter--;
                iter = l.erase(iter);
            }
        }
        else
        {
            char temp;
            cin >> temp;

            l.insert(iter, temp);
        }
    }

    for (auto &x : l)
        cout << x;

    return 0;
}