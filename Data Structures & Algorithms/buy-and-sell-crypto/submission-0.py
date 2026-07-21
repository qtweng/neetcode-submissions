class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen_min = prices[0]
        max_profit = 0
        for i, p in enumerate(prices):
            seen_min = min(seen_min, p)
            current_trade = p - seen_min
            max_profit = max(current_trade, max_profit)
        return max_profit
