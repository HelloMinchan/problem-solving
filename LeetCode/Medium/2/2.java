/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.math.BigInteger;

class Solution {
    //리스트의 값들을 역순으로 된 하나의 값으로 만들어 반환하는 메서드
    public static BigInteger generNum(ListNode list) {
	ListNode temp = new ListNode(0);
	temp = list;

	StringBuffer num = new StringBuffer();

	while(temp != null) {
	    num.append(Integer.toString(temp.val));
	    temp = temp.next;
	}

	//long 타입 보다 큰 수를 대비해 BigInteger 클래스 사용
	BigInteger n = new BigInteger(num.reverse().toString());

	return n;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	ListNode head = null;

	String num = (generNum(l1).add(generNum(l2))).toString();

	//반환할 리스트에 역순으로 삽입
	for(int i = num.length() - 1; i >= 0; i--) {
	    ListNode temp = new ListNode(num.charAt(i)- '0');

	    if(head == null)
		head = temp;
	    else {
		ListNode cur = head;
		while(cur.next != null) {
		    cur = cur.next;
		}
		cur.next = temp;
	    }
	}

	return head;
    }
}
