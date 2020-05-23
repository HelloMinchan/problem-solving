#include <iostream>
#include <vector>

using namespace std;

int children[201];

int main(void)
{
    ios_base::sync_with_stdio;
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> children[i];

    vector<int> LIS;
    LIS.push_back(0);
    int length = 0;

    int left = 0;
    int right = 0;
    int mid = 0;

    for (int i = 0; i < N; i++)
    {
        if (children[i] > LIS[length])
        {
            LIS.push_back(children[i]);
            length++;
        }
        else
        {
            left = 0;
            right = length;

            while (left < right)
            {
                mid = (left + right) / 2;

                if (LIS[mid] >= children[i])
                    right = mid;
                else
                    left = mid + 1;
            }

            LIS[right] = children[i];
        }
    }

    cout << N - length;

    return 0;
}