#include <iostream>
#include <vector>

using namespace std;

int A[1000001];

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> A[i];

    vector<int> LIS;
    LIS.push_back(0);

    int length = 0;
    int left = 0;
    int right = 0;
    int mid = 0;

    for (int i = 0; i < N; i++)
    {
        if (A[i] > LIS.back())
        {
            LIS.push_back(A[i]);
            length++;
        }
        else
        {
            left = 0;
            right = LIS.size();

            while (right - left > 0)
            {
                mid = (left + right) / 2;

                if (LIS[mid] < A[i])
                    left = mid + 1;
                else
                    right = mid;
            }

            LIS[right] = A[i];
        }
    }

    cout << length;

    return 0;
}