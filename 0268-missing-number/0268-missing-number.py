class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

        
obj = Solution()
nums = [9,6,4,2,3,5,7,0,1]
answer = obj.missingNumber(nums) 
print(answer)     