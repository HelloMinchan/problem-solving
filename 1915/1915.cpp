#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int arr[1001][1001];

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int n = 0, m = 0;
	cin >> n >> m;

	string temp = "";
	for (int i = 0; i < n; i++) {
		temp = "";
		cin >> temp;
		for (int j = 0; j < m; j++)
			arr[i][j] = temp[j] - '0';
	}
	
	int dx[4] = { -1,0,-1 }, dy[4] = { 0,-1,-1 };
	int maxLength = 0;

	vector<int> length;
	int countLength = 0;
	int minLength = 0;
	int ii = 0;
	int jj = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] == 1) {
				length.clear();

				for (int way = 0; way < 3; way++) {
					ii = i + dx[way];
					jj = j + dy[way];

					if (ii < 0 or ii > n - 1 or jj < 0 or jj > m - 1)
						continue;
					if (arr[ii][jj] and arr[ii][jj] != 0)
						length.push_back(arr[ii][jj]);

					countLength = length.size();
				}

				if (countLength)
					minLength = *min_element(length.begin(), length.end());
				else
					minLength = 0;

				if (countLength == 3)
					arr[i][j] = minLength + 1;
				else
					arr[i][j] = arr[i][j];
				
				if (maxLength < arr[i][j])
					maxLength = arr[i][j];
			}	
		}
	}
	
	cout << pow(maxLength, 2);

	return 0;
}