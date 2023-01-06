class Node {

    int val;
    Node next;

    Node(int val) {
        this.val = val;
        next = null;
    }
}

class MyLinkedList {    

    Node head;

    public MyLinkedList() {
        this.head = null;
    }
    
    public int get(int index) {
        Node curNode = head;

        if (curNode == null) {
            return -1;
        }

        if (index == 0) {
            return curNode.val;
        }
        
        int move = 0;
        while (curNode.next != null) {
            curNode = curNode.next;
            move++;

            if (move == index) {
                return curNode.val;
            }
        }

        return -1;
    }
    
    public void addAtHead(int val) {
        Node newNode = new Node(val);
        newNode.next = head;
        head = newNode;
    }
    
    public void addAtTail(int val) {
        Node curNode = head;
        Node newNode = new Node(val);

        if (curNode == null) {
            head = newNode;
            return;
        }

        while (curNode.next != null) {
            curNode = curNode.next;
        }

        curNode.next = newNode;
    }
    
    public void addAtIndex(int index, int val) {
        Node curNode = head;
        Node newNode = new Node(val);
        
        if (curNode == null) {
            if (index == 0) {
                newNode.next= curNode;
                head = newNode;

                return;
            }
            return;
        }

        if (index == 0) {
            newNode.next= curNode;
            head = newNode;
            return;
        }
        if (index == 1) {
            newNode.next = curNode.next;
            curNode.next = newNode;

            return;
        }
        
        int move = 1;
        while (curNode.next != null) {
            curNode = curNode.next;
            move++;

            if (move == index) {        
                newNode.next = curNode.next;
                curNode.next = newNode;

                return;
            }
        }
    }
    
    public void deleteAtIndex(int index) {
        Node curNode = head;

        if (index == 0) {
            head = curNode.next;
            
            return;
        }
        
        Node beforeNode = null;
        int move = 0;
        while (curNode.next != null) {
            beforeNode = curNode;
            curNode = curNode.next;
            move++;

            if (move == index) {        
                beforeNode.next = curNode.next;

                return;
            }
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */