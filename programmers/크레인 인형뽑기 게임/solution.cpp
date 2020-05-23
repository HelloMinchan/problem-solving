#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int answer = 0;
    int m = 0;
    
    stack<int> s;
    s.push(0);
    
    int beforeNum = 0;
    bool isPush = false;
    
    for (int i = 0; i< moves.size();i++) {
        m = moves[i];
        isPush = false;
        
        for (int j =0; j<board[0].size();j++) {
            if (board[j][m-1] != 0) {
                isPush = true;
                s.push(board[j][m-1]);
                board[j][m-1] = 0;
                break;
            }
        }
        
        if (isPush && s.top() == beforeNum) {
            s.pop();
            s.pop();
            answer+=2;
        }    

        beforeNum = s.top();
    }
    
    return answer;
}