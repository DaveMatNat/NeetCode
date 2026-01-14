"""
Evaluate Reverse Polish Notation
LeetCode 150

Problem: 

Approach:

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def evalRPN(self, tokens: list) -> int:
        symbols = "+-*/"
        res = 0
        stack = []
        
        for t in tokens:
            if t in symbols:
                # Pop two operands (order matters: second pop is left operand)
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                elif t == "/":
                    # Truncate toward zero for division
                    res = int(a / b)
                
                # Push result back onto stack
                stack.append(res)
            else:
                # If it's a number, push it onto the stack
                stack.append(int(t))
        
        # Final result is the only element left in stack
        return stack.pop()


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    print(solution.evalRPN(["2","1","+","3","*"]))
    print(solution.evalRPN(["4","13","5","/","+"]))
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    # TODO: Add test cases
    pass
