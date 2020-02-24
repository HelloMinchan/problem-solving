import java.util.Scanner;

class Node {
    public int data;
    public Node nextNode;

    public Node(int data) {
        this.data = data;
        this.nextNode = null;
    }

    public void linkNode(Node node) {
        this.nextNode = node;
    }

    public int getData() {
        return this.data;
    }

    public Node getNextNode() {
        return this.nextNode;
    }
}

class Stack {
    static int size;
    Node top;

    Stack() {
        this.top = null;
        this.size++;
    }

    public void push(int data) {
        Node node = new Node(data);
        node.linkNode(top);
        top = node;
    }

    public int pop() {
        if (isEmpty())
            throw new ArrayIndexOutOfBoundsException();
        else {
            int temp = top.data;
            top = top.getNextNode();
            this.size--;
            return temp;
        }
    }

    public boolean isEmpty() {
        return top == null;
    }

    public int top() {
        return top.getData();
    }
}

public class Main {
    

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Stack st = new Stack();
        String order_str = "";
        int order_num = 0;

        int N = sc.nextInt();
        for(int i=0;i<N;i++) {
            order_str = sc.next();

            if(order_str.equals("push") == true) {
                order_num = sc.nextInt();
                st.push(order_num);
            }
            else if(order_str.equals("pop") == true) {
                System.out.println(st.pop());
            }
            else if(order_str.equals("size") == true) {
                System.out.println(st.size);
            }
            else if(order_str.equals("empty") == true) {
                if(st.isEmpty()) {
                    System.out.println(1);
                }
                else {
                    System.out.println(0);
                }
            }
            else {
                System.out.println(st.top());
            }
        }

        sc.close();
    }   
}
