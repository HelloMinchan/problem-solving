#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <cstdlib>

using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N = 0;
    cin >> N;

    int middleValue = 0;
    priority_queue<int> smallPQ;
    int smallPQCount = 0;
    priority_queue<int, vector<int>, greater<int>> bigPQ;
    int bigPQCount = 0;

    int tempValue = 0;
    int inputValue = 0;

    for (int i = 0; i < N; i++)
    {
        cin >> inputValue;

        if (!i)
        {
            middleValue = inputValue;
            cout << middleValue << "\n";
            continue;
        }

        if (inputValue >= middleValue)
        {
            smallPQ.push(middleValue);
            smallPQCount++;

            if (!abs(smallPQCount - bigPQCount))
            {
                bigPQ.push(inputValue);
                middleValue = bigPQ.top();
                bigPQ.pop();
                cout << middleValue << "\n";
            }
            else if (abs(smallPQCount - bigPQCount) == 2)
            {
                tempValue = smallPQ.top();
                smallPQ.pop();
                smallPQCount--;
                bigPQ.push(inputValue);
                bigPQCount += 1;
                bigPQ.push(tempValue);
                middleValue = bigPQ.top();
                bigPQ.pop();
                cout << middleValue << "\n";
            }
            else
            {
                cout << middleValue << "\n";
                bigPQ.push(inputValue);
                middleValue = bigPQ.top();
                bigPQ.pop();
            }
        }
        else
        {
            bigPQ.push(middleValue);
            bigPQCount++;

            if (!abs(smallPQCount - bigPQCount))
            {
                smallPQ.push(inputValue);
                middleValue = smallPQ.top();
                smallPQ.pop();
                cout << middleValue << "\n";
            }
            else if (abs(smallPQCount - bigPQCount) == 2)
            {
                tempValue = bigPQ.top();
                bigPQ.pop();
                bigPQCount--;
                smallPQ.push(inputValue);
                smallPQCount += 1;
                smallPQ.push(tempValue);
                middleValue = smallPQ.top();
                smallPQ.pop();
                cout << middleValue << "\n";
            }
            else
            {
                smallPQ.push(inputValue);
                middleValue = smallPQ.top();
                smallPQ.pop();
                cout << middleValue << "\n";
            }
        }
    }

    return 0;
}