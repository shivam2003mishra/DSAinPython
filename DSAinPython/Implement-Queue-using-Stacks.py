1class MyQueue:
2
3    def __init__(self):
4        self.in_stack=[]
5        self.out_stack=[]
6
7    def push(self, x: int) -> None:
8        self.in_stack.append(x)
9
10    def pop(self) -> int:
11        if not self.out_stack:
12            while self.in_stack:
13                self.out_stack.append(self.in_stack.pop())
14        return self.out_stack.pop()
15
16    def peek(self) -> int:
17        if not self.out_stack:
18            while self.in_stack:
19                self.out_stack.append(self.in_stack.pop())
20        return self.out_stack[-1]
21        
22
23    def empty(self) -> bool:
24        return not self.in_stack and not self.out_stack
25        
26
27
28# Your MyQueue object will be instantiated and called as such:
29# obj = MyQueue()
30# obj.push(x)
31# param_2 = obj.pop()
32# param_3 = obj.peek()
33# param_4 = obj.empty()