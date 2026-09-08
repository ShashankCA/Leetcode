class Solution(object):
    def maxSubArray(self, nums):
        total = 0
        maxi = float("-inf")

        for i in range(len(nums)):
            total = total + nums[i]
            maxi = max(total,maxi)
            if total < 0:
                total = 0
        return maxi
       



        