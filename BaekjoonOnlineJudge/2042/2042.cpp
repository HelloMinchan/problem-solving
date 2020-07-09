#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

long long init(vector<long long> &arr, vector<long long> &tree, int node, int start, int end)
{
    if (start == end)
        return tree[node] = arr[start];
    else
        return tree[node] = init(arr, tree, node * 2, start, (start + end) / 2) + init(arr, tree, node * 2 + 1, (start + end) / 2 + 1, end);
}

long long modify(vector<long long> &tree, int node, int start, int end, long long target, long long change)
{
    if (end < target or target < start)
        return tree[node];
    if (start == end)
        return tree[node] = change;

    return tree[node] = modify(tree, node * 2, start, (start + end) / 2, target, change) + modify(tree, node * 2 + 1, (start + end) / 2 + 1, end, target, change);
}

long long getSum(vector<long long> &tree, int node, int start, int end, long long left, long long right)
{
    if (end < left or right < start)
        return 0;
    if (left <= start and end <= right)
        return tree[node];

    return getSum(tree, node * 2, start, (start + end) / 2, left, right) + getSum(tree, node * 2 + 1, (start + end) / 2 + 1, end, left, right);
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M, K;
    cin >> N >> M >> K;

    vector<long long> arr(N + 1);

    for (int i = 1; i < N + 1; i++)
        cin >> arr[i];

    int h = ceil(log2(N));
    int tree_size = (1 << (h + 1));

    vector<long long> tree(tree_size);

    init(arr, tree, 1, 1, N);

    for (int i = 0; i < M + K; i++)
    {
        long long a, b, c;
        cin >> a >> b >> c;

        if (a == 1)
            modify(tree, 1, 1, N, b, c);
        else
            cout << getSum(tree, 1, 1, N, b, c) << "\n";
    }

    return 0;
}