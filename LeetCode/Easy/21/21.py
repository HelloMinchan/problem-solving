class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        
        # case1 : l1과 l2 둘 다 빈 리스트일 경우.
        if l1 == None and l2 == None:
            return None
        
        # case2 : l1 혹은 l2 둘 중 하나만 빈 리스트일 경우.
        elif l1 == None or l2 == None:
            # l1이 있다면.
            if l1:
                l3.val = l1.val
                l1 = l1.next
                
                cur = l3
                while l1:
                    temp = ListNode()
                    temp.val = l1.val
                    l1 = l1.next
                    
                    cur.next = temp
                    cur = temp
            # l2가 있다면.
            if l2:
                l3.val = l2.val
                l2 = l2.next
                
                cur = l3
                while l2:
                    temp = ListNode()
                    temp.val = l2.val
                    l2 = l2.next
                    
                    cur.next = temp
                    cur = temp
                    
            return l3
        
        # case3 : l1과 l2 둘 다 빈 리스트가 아닌 경우.        
        else:
            # l3의 첫 val값 초기화
            if l1.val <= l2.val:
                l3.val = l1.val
                l1 = l1.next
            else:
                l3.val = l2.val
                l2 = l2.next

            cur = l3
            while l1 and l2:
                temp = ListNode()

                if l1.val <= l2.val:
                    temp.val = l1.val
                    l1 = l1.next
                else:
                    temp.val = l2.val
                    l2 = l2.next

                cur.next = temp
                cur = cur.next

            if l1:
                while l1:
                    temp = ListNode()

                    temp.val = l1.val
                    l1 = l1.next
                    cur.next = temp
                    cur = cur.next
            if l2:
                while l2:
                    temp = ListNode()

                    temp.val = l2.val
                    l2 = l2.next
                    cur.next = temp
                    cur = cur.next

            return l3
