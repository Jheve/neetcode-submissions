class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a min heap because it is more efficient in searching than sorting
        # keeps track of the largest numbers within the k range
        # returns the smallest of the largest -> always the kth largest
        return heapq.nlargest(k, nums)[-1]
        