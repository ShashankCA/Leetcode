class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        min_price = float("infinity")
        max_profit = 0
        for i in range(0,n):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,prices[i]-min_price)
        return max_profit
        
obj = Solution()
prices = [7,1,5,3,6,4]
answer = obj.maxProfit(prices) 
print(answer)      