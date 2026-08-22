class Solution(object):
    def isPalindrome(self, x):
        nums = x
        result = 0
        while nums >0:
            ld = nums % 10
            result = (result * 10) +ld
            nums = nums // 10

        return x == result




obj = Solution()
answer = obj.isPalindrome(-123)
print(answer)

        