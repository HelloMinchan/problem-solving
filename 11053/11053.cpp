#include <iostream>
#include <vector>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N = 0;
	cin >> N;

	vector<int> A(N, 0);
	for (int i = 0; i < N; i++)
		cin >> A[i];

	vector<int> memoization(N, 1);
	int maxNum = 1;

	for (int i = 1; i < N; i++) {
		for (int j = 0; j < i; j++) {
			if (A[i] > A[j]) {
				if (memoization[j] + 1 > memoization[i]) {
					memoization[i] = memoization[j] + 1;

					if (memoization[i] > maxNum)
						maxNum = memoization[i];
				}
			}
		}
	}

	cout << maxNum;

	return 0;
}