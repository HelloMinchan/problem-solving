class Node:
    def __init__(self, data, forward=None, back=None):
        self.data = data
        self.forward = forward
        self.back = back


class BrowserHistory:
    root = None

    def __init__(self, homepage: str):
        BrowserHistory.root = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        new_node.back = BrowserHistory.root
        BrowserHistory.root.forward = new_node
        BrowserHistory.root = new_node

    def back(self, steps: int) -> str:
        cur_step = 0

        while BrowserHistory.root.back != None:
            cur_step += 1

            BrowserHistory.root = BrowserHistory.root.back

            if cur_step == steps:
                break

        return BrowserHistory.root.data

    def forward(self, steps: int) -> str:
        cur_step = 0

        while BrowserHistory.root.forward != None:
            cur_step += 1

            BrowserHistory.root = BrowserHistory.root.forward

            if cur_step == steps:
                break

        return BrowserHistory.root.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
