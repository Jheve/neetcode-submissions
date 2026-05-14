class Solution:
    def rob(self, nums: List[int]) -> int:
        best_res1 = 0   # best result up to prev house
        best_res2 = 0   # best result up to house before prev

        for num in nums:
            # decide whether to rob or skip the house
            temp = max(num + best_res1, best_res2)

            # sliding window -> track the "best so far"
            best_res1 = best_res2
            best_res2 = temp
        
        return best_res2
        