class Solution(object):
    def maxSubArray(self, nums):
        total = 0
        maxi = float("-infinity")
        
        for num in nums:
            total += num
            maxi = max(total, maxi)
            
            if total < 0:
                total = 0
                
        return maxi



        