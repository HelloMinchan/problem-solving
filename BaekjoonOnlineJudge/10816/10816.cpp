#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<int> cards;

    for (int i = 0; i < N; i++)
    {
        int card;
        cin >> card;

        cards.push_back(card);
    }

    sort(cards.begin(), cards.end());

    int M;
    cin >> M;

    for (int i = 0; i < M; i++)
    {
        int card;
        cin >> card;

        int left, right;
        left = lower_bound(cards.begin(), cards.end(), card) - cards.begin();
        right = upper_bound(cards.begin(), cards.end(), card) - cards.begin();

        cout << right - left << " ";
    }

    return 0;
}