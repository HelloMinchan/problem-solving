#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b)
{
    if (a.size() == b.size())
        return a < b;
    else
        return a.size() < b.size();
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;

    vector<string> words;

    for (int i = 0; i < N; i++)
    {
        string temp;
        cin >> temp;

        words.push_back(temp);
    }

    sort(words.begin(), words.end());
    words.erase(unique(words.begin(), words.end()), words.end());
    sort(words.begin(), words.end(), compare);

    for (int i = 0; i < words.size(); i++)
        cout << words[i] << '\n';

    return 0;
}