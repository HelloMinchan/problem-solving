import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        Integer[] boxedNumbers = Arrays.stream(numbers).boxed().toArray(Integer[]::new);
        Arrays.sort(boxedNumbers, (n1, n2) -> {
            String number1 = String.valueOf(n1);
            String number2 = String.valueOf(n2);
            
            if (number1.length() == number2.length()) {
                return number2.compareTo(number1);
            } else {
                return (number2+number1).compareTo(number1+number2);
            }
        });
        
        StringBuilder sb = new StringBuilder();
        for (int number : boxedNumbers) {
            sb.append(number);
        }
        
        while (sb.charAt(0) == '0' && sb.length() > 1) {
            sb.deleteCharAt(0);
        }
        
        return sb.toString();
    }
}