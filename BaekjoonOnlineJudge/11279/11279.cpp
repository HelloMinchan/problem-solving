#include <iostream>
#include <queue>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio;
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    priority_queue<int> pq;

    int value = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> value;

        if (!value)
        {
            try
            {
                if (!pq.size())
                    throw 0;
                cout << pq.top() << "\n";
                pq.pop();
            }
            catch (int e)
            {
                cout << e << "\n";
            }
        }
        else
            pq.push(value);
    }

    return 0;
}