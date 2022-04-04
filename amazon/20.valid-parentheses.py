#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        #method1
        # stack = []
        # for letter in s:
        #     if letter in [ "(" ,"{" , "["]:
        #         stack.append(str(letter))
        #     elif letter == ")":
        #         if not stack or stack.pop() != "(":
        #             return False
        #     elif letter == "}":
        #         if not stack or stack.pop() != "{":
        #             return False
        #     elif letter == "]":
        #         if not stack or stack.pop() != "[":
        #             return False      
        # return stack == [] 

        #method2
        stack = []
        dictt={"(":")","{":"}","[":"]"}
        for i in s:
            if i in dictt:
                stack.append(i)
            elif stack==[] or dictt[stack.pop()]!=i:
                return False
        return stack==[]



        
# @lc code=end

