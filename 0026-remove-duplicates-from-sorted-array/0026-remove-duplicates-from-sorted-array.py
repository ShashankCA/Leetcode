class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0
        j = i + 1
        while j < n:
            if nums[i]!= nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i +1   

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]
obj = Solution()
answer = obj.removeDuplicates(nums)
print(answer)