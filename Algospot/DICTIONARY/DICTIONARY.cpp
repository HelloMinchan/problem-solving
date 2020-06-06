#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;
vector<int> seen, order;

// 그래프(인접 행렬) 생성 함수
void makeGraph(const vector<string> &words)
{
    adj = vector<vector<int>>(26, vector<int>(26, 0));

    for (int j = 1; j < words.size(); ++j)
    {
        int i = j - 1;
        int len = min(words[i].size(), words[j].size());

        for (int k = 0; k < len; ++k)
        {
            if (words[i][k] != words[j][k])
            {
                int a = words[i][k] - 'a';
                int b = words[j][k] - 'a';

                adj[a][b] = 1;
                break;
            }
        }
    }
}

void DFS(int here)
{
    seen[here] = 1;
    for (int there = 0; there < adj.size(); ++there)
    {
        if (adj[here][there] && !seen[there])
            DFS(there);
    }

    order.push_back(here);
}

vector<int> topologicalSort()
{
    int m = adj.size();
    seen = vector<int>(m, 0);
    order.clear();

    for (int i = 0; i < m; i++)
        if (!seen[i])
            DFS(i);

    reverse(order.begin(), order.end());

    for (int i = 0; i < m; ++i)
    {
        for (int j = i + 1; j < m; ++j)
        {
            if (adj[order[j]][order[i]])
                return vector<int>();
        }
    }

    return order;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int C = 0;
    cin >> C;

    while (C--)
    {
        int N = 0;
        cin >> N;

        vector<string> words;
        string temp = "";

        for (int i = 0; i < N; ++i)
        {
            cin >> temp;
            words.push_back(temp);
        }

        makeGraph(words);

        vector<int> ans = topologicalSort();
        if (ans.empty())
            cout << "INVALID HYPOTHESIS";
        else
            for (int i = 0; i < ans.size(); i++)
                cout << char(ans[i] + 'a');
        cout << "\n";
    }

    return 0;
}