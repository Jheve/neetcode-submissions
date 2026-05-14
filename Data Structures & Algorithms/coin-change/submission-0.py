class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # keep track of computed amounts
        amounts = {}

        # use depth first search for recursive computation
        def dfs(amount):
            # base case -> no coins for no amount
            if amount == 0:
                return 0
            
            # return if amount has already been computed
            if amount in amounts:
                return amounts[amount]
            
            result = 1000000000000

            for coin in coins:
                if amount - coin >= 0:
                    # track the minimum amount of coins
                    result = min(result, 1 + dfs(amount - coin))
            
            # store result
            amounts[amount] = result

            return result
        
        min_coins = dfs(amount)

        # check if amount is impossible
        if min_coins >= 1000000000000:
            return -1
        else:
            return min_coins