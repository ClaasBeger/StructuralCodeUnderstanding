class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                sub_str = ""
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                stack.pop()

                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(int(multiplier) * sub_str)

        return "".join(stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a2[c]]"))