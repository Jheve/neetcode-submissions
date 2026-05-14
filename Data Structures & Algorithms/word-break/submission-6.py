class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)   # set up dp array 
        dp[len(s)] = True             # base case -> empty suffix  

        # iterate from right to left
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # check if word slice is within bounds and matches target word
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                # early break -> if one word meets dp requirement, no need to check anymore
                if dp[i]:
                    break

        return dp[0]