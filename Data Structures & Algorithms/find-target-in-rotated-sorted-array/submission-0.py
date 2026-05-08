class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        pivot = low

        def binary_search(low: int, high: int) -> int:
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1   

            return -1
        
        result = binary_search(0, pivot - 1)

        if result != -1:
            return result
        
        return binary_search(pivot, len(nums) - 1)
             