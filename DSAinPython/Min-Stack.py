1class MinStack:
2
3    def __init__(self):
4        self.stack=[]
5        self.min_stack=[]
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        if not self.min_stack or val <= self.min_stack[-1]:
10            self.min_stack.append(val)
11
12    def pop(self) -> None:
13        if self.stack.pop()== self.min_stack[-1]:
14            self.min_stack.pop()
15        
16
17    def top(self) -> int:
18        return self.stack[-1]
19        
20
21    def getMin(self) -> int:
22        return self.min_stack[-1]
23        
24
25
26# Your MinStack object will be instantiated and called as such:
27# obj = MinStack()
28# obj.push(val)
29# obj.pop()
30# param_3 = obj.top()
31# param_4 = obj.getMin()