#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    # def __init__(self):
    #     self.stack=[]

    # def push(self, val: int) -> None:
    #     self.stack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop() 

    # def top(self) -> int:
    #     return self.stack[-1]
        

    # def getMin(self) -> int:
    #     minnum = self.stack[0]
    #     for item in self.stack:
    #         if item < minnum:
    #             minnum = item
    #     return minnum

    def __init__(self):
        self.stack=[]
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            self.min.append(min(val,self.min[-1]))
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.stack.pop() 
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

