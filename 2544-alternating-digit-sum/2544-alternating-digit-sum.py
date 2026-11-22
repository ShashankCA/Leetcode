class Solution(object):
    def alternateDigitSum(self, n):
        total = 0

        for i, digit in enumerate(str(n)):
            if i % 2 == 0:
                total += int(digit)
            else:
                total -= int(digit)

        return total