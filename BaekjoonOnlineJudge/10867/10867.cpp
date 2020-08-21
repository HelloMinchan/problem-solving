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

    vector<int> nums;

    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;

        nums.push_back(temp);
    }

    sort(nums.begin(), nums.end());

    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    sort(nums.begin(), nums.end());

    for (int i = 0; i < nums.size(); i++)
        cout << nums[i] << " ";

    return 0;
}