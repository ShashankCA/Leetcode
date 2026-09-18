class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
            
        global_max = nums[0]
        curr_max = 1
        curr_min = 1
        
        for num in nums:
            temp_max = curr_max * num

            curr_max = max(temp_max, curr_min * num, num)
            curr_min = min(temp_max, curr_min * num, num)
            

            global_max = max(global_max, curr_max)
            
        return global_max


        