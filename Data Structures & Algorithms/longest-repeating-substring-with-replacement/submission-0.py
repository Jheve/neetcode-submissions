class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}      # initialize hash map to track char frequencies
        result = 0

        left = 0
        maxFrequency = 0    # keep track of max char frequencies w/o recomputing
        
        for right in range(len(s)):
            # increment frequency of each char
            charCount[s[right]] = 1 + charCount.get(s[right], 0)

            # update max char frequency if needed
            maxFrequency = max(maxFrequency, charCount[s[right]])

            # check if window is valid, else shrink window from left and adjust counts
            while (right - left + 1) - maxFrequency > k:
                charCount[s[left]] -= 1
                left += 1

            # update result with cur window size
            result = max(result, right - left + 1)
        
        return result
        