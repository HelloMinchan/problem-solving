import java.util.*;

class Node {
    char key;
    int childsCount = 0;
    Map<Character, Node> childs;
    
    Node (char key) {
        this.key = key;
        this.childsCount = 1;
        this.childs = new HashMap<>();
    }
}

class Trie {
    private static Node head = new Node(' ');
    private static Set<String> wordSet = new HashSet<>();
    
    static void insert(String word) {
        Node cur = head;
        wordSet.add(word);
        
        for (int i = 0; i < word.length(); i++) {
            char target = word.charAt(i);
            
            if (!cur.childs.keySet().contains(target)) {
                Node newNode = new Node(target);
                cur.childs.put(target, newNode);
                cur = newNode;
            } else {
                cur.childsCount++;
                cur = cur.childs.get(target);
            }
        }
    }
    
    static int autoComplete(String word) {
        Node cur = head;
        
        StringBuilder sb = new StringBuilder();
        int inputCount = 0;
        
        for (int i = 0; i < word.length(); i++) {
            char target = word.charAt(i);
            sb.append(target);
            
            inputCount++;
            cur = cur.childs.get(target);
            
            if (cur.childsCount == 1 && cur.childs.keySet().size() == 1) {
                if (i + 1 < word.length()) {
                    if (wordSet.contains(sb.toString())) {
                        inputCount++;
                    }
                }
                break;
            }
        }
        
        return inputCount;
    }
}

class Solution {
    public int solution(String[] words) {
        int answer = 0;
        
        Trie trie = new Trie();
        
        for (String word : words) {
            trie.insert(word);
        }
        
        for (String word : words) {
            answer += trie.autoComplete(word);
        }
        
        return answer;
    }
}