#include <iostream>

using namespace std;

bool isPossible(int rise, int oneDayRise, int destination, int day)
{
    int remainingDistanceOnTheLastDay = destination - oneDayRise * day;

    if (rise >= remainingDistanceOnTheLastDay)
        return true;
    return false;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int A = 0, B = 0, V = 0;
    cin >> A >> B >> V;

    if (A == V)
    {
        cout << 1;
        return 0;
    }

    int oneDayRise = A - B;
    int left = 1;
    int right = V;
    int mid = 0;
    int result = 0;

    while (left <= right)
    {
        mid = (left + right) / 2;

        if (isPossible(A, oneDayRise, V, mid))
        {
            right = mid - 1;
            result = mid;
        }
        else
            left = mid + 1;
    }

    cout << result + 1;

    return 0;
}