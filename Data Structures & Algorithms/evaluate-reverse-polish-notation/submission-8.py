class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            stack.append(i)
            if i == "+":
                # pop twice
                # add
                # push
                stack.pop()
                p1 = int(stack.pop())
                p2 = int(stack.pop())
                prod = p1 + p2
                stack.append(prod)
            elif i == "-":
                stack.pop()
                p1 = int(stack.pop())
                p2 = int(stack.pop())
                prod = p2 - p1
                stack.append(prod)
            elif i == "*":
                stack.pop()
                p1 = int(stack.pop())
                p2 = int(stack.pop())
                prod = p1 * p2
                stack.append(prod)
            elif i == "/":
                stack.pop()
                p1 = int(stack.pop())
                p2 = int(stack.pop())
                prod = int(p2/p1)
                stack.append(prod)
         
        return int(stack.pop())

        