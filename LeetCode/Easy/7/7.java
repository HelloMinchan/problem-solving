class Solution {
    public int reverse(int x) {
        StringBuffer r = null;
        if (x == 0)
            return 0;
        else if (x > 0) {
            r = new StringBuffer(Integer.toString(x));
            try {
                return Integer.parseInt((r.reverse().toString()));   
            } catch(NumberFormatException e) {
                return 0;
            }
        }
        else {
            r = new StringBuffer((Integer.toString(x)).substring(1));
            try {
                return (Integer.parseInt((r.reverse().toString())) * -1);
            } catch(NumberFormatException e) {
                return 0;
            }
        }
    }
}
