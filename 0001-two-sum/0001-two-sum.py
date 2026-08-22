class Solution(object): 
    def twoSum(self, nums, target):
        hashmap = {}
        remaining = 0
        n = len(nums)
        for i in range(0, n):
            remaining = target - nums[i]
            if remaining in hashmap:
                return [hashmap[remaining], i]
            hashmap[nums[i]] = i

obj = Solution()
nums = [2, 7, 11, 15]
target = 9
answer = obj.twoSum(nums, target)
print(answer)
