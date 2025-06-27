def maxProfit(prices):
    n = len(prices)
    profit = 0
    for i in range(1,n):
        if (prices[i] > prices[i-1]):
             profit += prices[i] - prices[i-1]
    return profit

arr = [100, 180, 260, 310, 40, 535, 695]
maxProfit(arr)