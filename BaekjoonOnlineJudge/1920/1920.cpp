#include <iostream>
#include <map>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    map<int, int> hash_map;

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int value;
        cin >> value;

        hash_map[value] = 1;
    }

    int M;
    cin >> M;

    for (int i = 0; i < M; i++)
    {
        int value;
        cin >> value;
        if (hash_map.end() != hash_map.find(value))
            cout << 1 << "\n";
        else
            cout << 0 << "\n";
    }

    return 0;
}