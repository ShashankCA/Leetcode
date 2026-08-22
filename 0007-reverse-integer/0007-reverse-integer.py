class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        nums = abs(x)
        result = 0
        
        while nums > 0:
            ld = nums % 10
            
            if result > 214748364 or (result == 214748364 and ld > 7):
                return 0
                
            result = (result * 10) + ld
            nums = nums // 10 
            
        return result * sign

obj = Solution()
answer = obj.reverse(123)
print(answer)

answer = obj.reverse(123)
print(answer)