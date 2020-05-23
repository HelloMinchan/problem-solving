#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct cmp
{
    bool operator()(int oldValue, int newValue)
    {
        return oldValue > newValue;
    }
};

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int ans = 0;
    int c = 0;
    cin >> c;

    int n = 0;
    priority_queue<int, vector<int>, cmp> strLength;
    int inputLength = 0;
    int length1 = 0;
    int length2 = 0;

    while (c--)
    {
        cin >> n;
        ans = 0;
        strLength = priority_queue<int, vector<int>, cmp>();

        for (int i = 0; i < n; i++)
        {
            cin >> inputLength;
            strLength.push(inputLength);
        }

        for (int i = 0; i < n - 1; i++)
        {
            length1 = strLength.top();
            strLength.pop();
            length2 = strLength.top();
            strLength.pop();

            ans += length1 + length2;
            strLength.push(length1 + length2);
        }

        cout << ans << "\n";
    }

    return 0;
}