class Solution {
    public int mySqrt(int x) {
        long answer = 0;
        long left = 1;
        long right = Integer.MAX_VALUE;

        while (left <= right) {
            long middle = (left + right) / 2;

            if (middle * middle <= (long)x) {
                answer = middle;
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return (int)answer;
    }
}