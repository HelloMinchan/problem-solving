class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0)
            return "";
        else if(strs.length == 1)
            return strs[0];
        
        int min = 2147483647;
        boolean common = true;
        char temp = ' ';
        
        for(int i =0;i<strs.length;i++) {
            if(min>strs[i].length())
                min = strs[i].length();
        }
        System.out.println(min);
        StringBuffer sb = new StringBuffer("");
        
        for(int i=0;i<min;i++) {
            if(common == true) {
                for(int j=0;j<strs.length-1;j++) {
                    temp = strs[j].charAt(i);
                    if(strs[j].charAt(i)!=strs[j+1].charAt(i)) {
                        common = false;
                        break;
                    }
                }
                if(common == true)
                    sb.append(temp);
            }
        }
        
        return sb.toString();
    }
}
