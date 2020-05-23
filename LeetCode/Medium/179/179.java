import java.math.BigInteger;

class Solution {
    public String largestNumber(int[] nums) {
	ArrayList<String> arrlist = new ArrayList<>();
	for(int i : nums)
	    arrlist.add(Integer.toString(i));

	Comparator<String> myComparator = new Comparator<String>() {
	    int cur = 0;
	    public int compare(String o1, String o2) {
		BigInteger left = new BigInteger(o1.concat(o2));
		BigInteger right = new BigInteger(o2.concat(o1));
		if(left.compareTo(right)==-1)
		    return 1;
		else
		    return -1;  
	    }
	};
	Collections.sort(arrlist,myComparator);

	String[] arr = arrlist.toArray(new String[arrlist.size()]);
	StringBuffer sb = new StringBuffer();
	for(String i : arr)
	    sb.append(i);

	BigInteger result = new BigInteger(sb.toString());
	if(result.compareTo(BigInteger.ZERO) == 0)
	    return "0";
	else
	    return sb.toString();
    }
}
