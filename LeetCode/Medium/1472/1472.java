class Node {

    String url;
    Node next;
    Node before;

    Node() {
        url = null;
        next = null;
        before = null;
    }
    
    Node(String url) {
        this.url = url;
    }
}
class BrowserHistory {

    Node homePage = null;

    public BrowserHistory(String homepage) {
        homePage = new Node(homepage);
    }
    
    public void visit(String url) {
        Node newPage = new Node(url);
        newPage.before = homePage;

        homePage.next = newPage;
        homePage = newPage;
    }
    
    public String back(int steps) {
        int move = 0;

        while(homePage.before != null) {
            homePage = homePage.before;
            move++;

            if (move == steps) {
                break;
            }
        }

        return homePage.url;
    }
    
    public String forward(int steps) {
        int move = 0;

        while(homePage.next != null) {
            homePage = homePage.next;
            move++;

            if (move == steps) {
                break;
            }
        }

        return homePage.url;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */