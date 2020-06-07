#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
    int time = 0;
    queue<int> q;
    int sum = 0;
    int i = 0;

    while (1)
    {
        time++;

        if (q.size() == bridge_length)
        {
            sum -= q.front();
            q.pop();
        }

        if (sum + truck_weights[i] <= weight)
        {
            if (i == truck_weights.size() - 1)
            {
                time += bridge_length;
                break;
            }

            q.push(truck_weights[i]);
            sum += truck_weights[i];
            i++;
        }
        else
            q.push(0);
    }

    return time;
}