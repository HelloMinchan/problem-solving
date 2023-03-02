class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }

        int[] memoization = new int[n + 1];
        memoization[1] = 1;
        memoization[2] = 2;
        
        for (int i = 3; i < n + 1; i++) {
            memoization[i] = memoization[i - 1] + memoization[i - 2];
        }

        return memoization[n];
    }
}