import java.math.*;

class Solution {
    public int[] plusOne(int[] digits) {
        StringBuilder sb = new StringBuilder();
        for (int digit : digits) {
            sb.append(digit);
        }

        BigInteger largeNumber = new BigInteger(sb.toString());
        String largeNumberString = largeNumber.add(BigInteger.ONE).toString();

        int[] answer = new int[largeNumberString.length()];
        for (int i = 0; i < largeNumberString.length(); i++) {
            answer[i] = Character.getNumericValue(largeNumberString.charAt(i));
        }

        return answer;
    }
}