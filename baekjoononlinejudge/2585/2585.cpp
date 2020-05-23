#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <cstring>
#include <cmath>

using namespace std;

int n, k;
bool visit[1001];

bool BFS(const vector<pair<int, int>> &airport, int vertex, int fuel)
{
    memset(visit, false, sizeof(visit));
    int landingCount = 0;
    int arrivedVertex = 0;
    double distance = 0.0;
    double distanceForDestination = 0.0;
    int qSize = 0;
    queue<int> q;
    q.push(vertex);

    while (!q.empty())
    {
        if (landingCount > k)
            return false;

        qSize = q.size();
        for (int i = 0; i < qSize; i++)
        {
            arrivedVertex = q.front();
            q.pop();

            if (!visit[arrivedVertex])
            {
                visit[arrivedVertex] = true;

                for (int j = 1; j < n + 1; j++)
                {
                    distance = sqrt(pow(airport[arrivedVertex].first - airport[j].first, 2) + pow(airport[arrivedVertex].second - airport[j].second, 2));

                    if (distance <= fuel)
                    {
                        distanceForDestination = sqrt(pow(10000 - airport[j].first, 2) + pow(10000 - airport[j].second, 2));

                        if (distanceForDestination <= fuel)
                            return true;

                        q.push(j);
                    }
                }
            }
        }

        landingCount++;
    }

    return false;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> k;

    vector<pair<int, int>> airport(n + 1, make_pair(0, 0));
    for (int i = 1; i < n + 1; i++)
        cin >> airport[i].first >> airport[i].second;

    int left = 0;
    int right = 10000;
    int mid = 0;
    int result = 0;

    while (left <= right)
    {
        mid = (left + right) / 2;

        if (BFS(airport, 0, mid * 10))
        {
            result = mid;
            right = mid - 1;
        }
        else
            left = mid + 1;
    }

    cout << result;

    return 0;
}