class Solution(object):
    def finalValueAfterOperations(self, operations):
        total = 0
        for num in operations:
            if "+" in num:
                total += 1
            else:
                total -= 1
        return total
