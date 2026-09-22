class Solution(object):
    def runningSum(self, nums):
        n = len(nums)
        result = []
        current_sum = 0
        
        for i in range(n):
            current_sum += nums[i]
            result.append(current_sum)
            
        return result


        

        