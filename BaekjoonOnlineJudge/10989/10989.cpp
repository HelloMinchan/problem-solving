#include <iostream>
#define MAX 10'001

using namespace std;

int nums[MAX];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int index;
        cin >> index;
        nums[index] += 1;
    }

    for (int i = 1; i < MAX; i++)
        for (int j = 0; j < nums[i]; j++)
            cout << i << "\n";

    return 0;
}