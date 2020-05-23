#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <utility>
#include <cstdlib>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    int inputValue = 0;
    int tempValue = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> inputValue;

        if (!inputValue)
        {
            try
            {
                if (pq.empty())
                    throw 0;

                cout << pq.top().second << "\n";
                pq.pop();
            }
            catch (int e)
            {
                cout << e << "\n";
            }
        }
        else
            pq.push(make_pair(abs(inputValue), inputValue));
    }

    return 0;
}