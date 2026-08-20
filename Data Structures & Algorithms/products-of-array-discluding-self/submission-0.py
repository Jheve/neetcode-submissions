class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))      # initialize result array using placeholders
        prefix = 1                      # track running product of left nums

        # first pass (left to right)
        # store the product of every num before nums[i]
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        # second pass (right to left)
        # multiply existing left product by each right num  
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
        