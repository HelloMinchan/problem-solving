#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    vector<int> russia;
    vector<int> korea;

    int member = 0;
    int rating = 0;
    int compare = 0;
    int win = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> member;

        russia.clear();
        korea.clear();
        win = 0;

        for (int j = 0; j < member; j++)
        {
            cin >> rating;
            russia.push_back(rating);
        }

        for (int j = 0; j < member; j++)
        {
            cin >> rating;
            korea.push_back(rating);
        }

        sort(russia.begin(), russia.end(), greater<int>());
        sort(korea.begin(), korea.end());

        for (int i = 0; i < member; i++)
        {
            compare = russia[i];

            if (compare > korea.back())
                continue;
            else
            {
                korea.pop_back();
                win++;
            }
        }

        cout << win << "\n";
    }

    return 0;
}