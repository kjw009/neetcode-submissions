class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brk_map = {
            ']'  :'[',
            '}'  :'{',
            ')'   :'('
        }



        for i in range(len(s)):
                if s[i] in brk_map:
                    if stack and stack[-1] == brk_map[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])

        return len(stack) == 0


            