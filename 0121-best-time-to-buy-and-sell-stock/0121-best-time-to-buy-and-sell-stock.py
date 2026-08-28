class Solution(object):

  def maxProfit(self, prices):
    n = len(prices)
    min_price = float('inf')
    max_price = 0
    for i in range(0, n):
      min_price = min(min_price, prices[i])
      max_price = max(max_price, prices[i] - min_price)
    return max_price
