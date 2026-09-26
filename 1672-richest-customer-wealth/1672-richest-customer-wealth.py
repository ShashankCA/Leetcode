class Solution(object):
    def maximumWealth(self, accounts):
        wealthiest = 0
        for dudes in accounts:
            wealth = sum(dudes)
            wealthiest = max(wealthiest,wealth)

        return wealthiest

        