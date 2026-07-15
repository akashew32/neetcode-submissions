class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        temp = self.curr
        self.curr.next = Node(url)
        self.curr = self.curr.next
        self.curr.prev = temp
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
        return self.curr.data
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
        return self.curr.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None