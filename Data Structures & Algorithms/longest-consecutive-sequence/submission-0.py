class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            # check if num is the start of a sequence
            if (num - 1) not in numSet:
                length = 0

                # check for consecutive nums
                while (num + length) in numSet:
                    length += 1
                
                # update current longest
                longest = max(length, longest)
        
        return longest
        
        