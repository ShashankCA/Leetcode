class Solution(object):
    def generateParenthesis(self, n):
        result = []
        brackets = [""] * (2 * n)
        self.backtrack(0, 0, brackets, result)
        return result

    def backtrack(self, index, total, brackets, result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        
        if total < 0:
            return
            
        brackets[index] = "("
        self.backtrack(index + 1, total + 1, brackets, result)
        
        brackets[index] = ")"
        self.backtrack(index + 1, total - 1, brackets, result)



