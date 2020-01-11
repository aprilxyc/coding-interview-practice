"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39474/Why-the-greedy-algorithm-works-(pairwise-differences-only)

# approach one with a single pass where you just keep adding each consecuive transaction
def maxProfit(prices): 
    max_profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            max_profit += (prices[i+1] - prices[i])
    return max_profit

# approach 2 where we consider the sum of all the (peaks - valleys)
# wrap your head around the fact that when you calculate total profit, you are essentially calculating the profit at all the stages
# i.e. 
# the profit so far = (prices[i+1] - prices[i]) + (prices[i+2] - prices[i+1]) 
#  = prices[i+2] - prices[i]
def maxProfit(prices):
    i = 0
    valley = prices[0]
    peak = prices[0]
    max_profit = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        max_profit += (peak - valley)
    return max_profit
