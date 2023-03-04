import java.util.*;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        Deque<Integer> nums1Queue = new LinkedList<>();
        Queue<Integer> nums2Queue = new LinkedList<>();
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            nums1Queue.add(nums1[i]);
        }

        for (int num: nums2) {
            nums2Queue.add(num);
        }

        while (!nums1Queue.isEmpty() && !nums2Queue.isEmpty()) {
            if (nums1Queue.peek() < nums2Queue.peek()) {
                answer.add(nums1Queue.poll());
            } else {
                answer.add(nums2Queue.poll());
            }
        }

        while(!nums1Queue.isEmpty()) {
            answer.add(nums1Queue.poll());
        }

        while(!nums2Queue.isEmpty()) {
            answer.add(nums2Queue.poll());
        }

        for (int i = 0; i < answer.size(); i++) {
            nums1[i] = answer.get(i);
        }
    }
}