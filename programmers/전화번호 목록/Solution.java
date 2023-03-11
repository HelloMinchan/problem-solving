import java.util.*;

class Node {
    char key;
    HashMap<Character, Node> childs;
    
    Node(char key, HashMap<Character, Node> childs) {
        this.key = key;
        this.childs = childs;
    }
        
}

class Trie {
    private static Node head = new Node(' ', new HashMap<>());
    
    static boolean insert(String phoneNumber) {
        boolean isPrefix = true;
        
        Node currentNode = head;
        
        for (int i = 0; i < phoneNumber.length(); i++) {
            char number = phoneNumber.charAt(i);
            
            if (!currentNode.childs.containsKey(number)) {
                isPrefix = false;
                Node newNode = new Node(number, new HashMap<>());
                currentNode.childs.put(number, newNode);
                currentNode = newNode;
            } else {
                currentNode = currentNode.childs.get(number);
            }
        }
        
        return isPrefix;
    }
}

class Solution {
    public boolean solution(String[] phoneBooks) {
        Arrays.sort(phoneBooks, (pb1, pb2) -> pb2.length() - pb1.length());
        
        Trie trie = new Trie();
        
        for (String phoneBook : phoneBooks) {
            if(trie.insert(phoneBook)) {
                return false;
            }
        }
        
        return true;
    }
}