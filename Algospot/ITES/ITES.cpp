#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio;
    cin.tie(NULL);
    cout.tie(NULL);

    int C = 0;
    cin >> C;

    int K = 0, N = 0;

    while (C--)
    {
        long long prevSignal = 1983;
        int nowSignal = 0;
        int sumSignal = 0;
        int ans = 0;
        queue<int> q;

        cin >> K >> N;

        while (N--)
        {
            nowSignal = (int)(prevSignal % 10000 + 1);
            sumSignal += nowSignal;
            q.push(nowSignal);

            while (sumSignal > K)
            {
                sumSignal -= q.front();
                q.pop();
            }

            if (sumSignal == K)
                ans++;

            prevSignal = (prevSignal * 214013 + 2531011) % (long long)(pow(2, 32));
        }

        cout << ans << "\n";
    }

    return 0;
}