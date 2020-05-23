#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    priority_queue<int, vector<int>, greater<int>> pq;

    int inputValue = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> inputValue;
        pq.push(inputValue);
    }

    int minCompareCount = 0;
    int compareCountA = 0;
    int compareCountB = 0;
    for (int i = 0; i < N - 1; i++)
    {
        compareCountA = pq.top();
        pq.pop();
        compareCountB = pq.top();
        pq.pop();

        pq.push(compareCountA + compareCountB);
        minCompareCount += compareCountA + compareCountB;
    }

    cout << minCompareCount;

    return 0;
}