from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # convert dict to hash set for fast searching
        wordSet = set(wordDict)

        @lru_cache(None)

        # use dfs for recursive checking
        def dfs(i):
            # recurrence function -> check if cursor reaches the end
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                # check if word slice is in set
                if s[i : j + 1] in wordSet:
                    # if valid, recurse from word till stack returns true
                    if dfs(j + 1):
                        return True
            return False
        
        return dfs(0)