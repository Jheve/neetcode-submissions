class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            # keep track of sum
            current_sum = numbers[left] + numbers[right]

            # if sum more than target, go smaller
            if current_sum > target:
                right -= 1
            # if sum less than target, go bigger
            elif current_sum < target:
                left += 1
            # if sum matches target, return indices
            else:
                return [left + 1, right + 1]
        
        return []
            
        