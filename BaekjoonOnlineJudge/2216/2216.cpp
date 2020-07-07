#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int INF = -2147483647;
int A, B, C;
string X, Y;
int memoization[3001][3001];

int DFS(int s1, int s2) {
	if (s1 >= X.size())
		return B * (Y.size() - s2);
	if (s2 >= Y.size())
		return B * (X.size() - s1);

	int &score = memoization[s1][s2];
	if (score != INF)
		return score;
	
	if (X[s1] == Y[s2])
		score = max(score, A + DFS(s1 + 1, s2 + 1));
	else
		score = max(score, C + DFS(s1 + 1, s2 + 1));

	score = max(score, max(B + DFS(s1 + 1, s2), B + DFS(s1, s2 + 1)));

	return score;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> A >> B >> C;	
	cin >> X;
	cin >> Y;

	fill(&memoization[0][0], &memoization[X.size() - 1][Y.size()],INF);

	cout << DFS(0, 0) << "\n";
}