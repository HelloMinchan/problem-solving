#include <string>
#include <vector>
#include <bitset>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2)
{
    vector<string> answer;

    for (int i = 0; i < n; i++)
    {
        bitset<16> line1(arr1[i]);
        bitset<16> line2(arr2[i]);

        string s1 = line1.to_string();
        string s2 = line2.to_string();
        string temp = "";

        for (int j = 16 - n; j < 16; j++)
        {
            if (s1[j] == '1' || s2[j] == '1')
                temp += "#";
            else
                temp += " ";
        }

        answer.push_back(temp);
    }

    return answer;
}