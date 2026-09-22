class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result

    def backtrack(self, subset, index, target, result, candidates):
        if target == 0:
            result.append(subset.copy())
            return
        if target < 0:
            return 
        if index >= len(candidates):
            return 
            
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
                
            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            subset.pop()


        