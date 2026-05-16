class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # sort nums to prune early (stop as soon as number exceeds target)
        nums.sort()

        # i is start index, cur is current combination, total is running sum of cur
        def dfs(i, cur, total):
            # base case -> valid combo found
            if total == target:
                result.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                # prune -> all later nums will be worse
                if total + nums[j] > target:
                    return
                
                cur.append(nums[j])             # choose
                dfs(j, cur, total + nums[j])    # explore j, allow nums to be reused
                cur.pop()                       # backtrack
        
        dfs(0, [], 0)
        return result
        