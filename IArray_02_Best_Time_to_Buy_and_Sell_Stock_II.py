import pytest
from typing import List

def maxProfit(prices: List[int]) -> int:
    profit = 0
    if len(prices) > 1:
        increasePrice = False
        minPrice = 0
        maxPrice = 0
        i = 1
        while i < len(prices):
            if prices[i] > prices[i-1]:
                if not increasePrice:
                    increasePrice = True
                    minPrice = prices[i-1]
                maxPrice = prices[i]
            else:
                if increasePrice:
                    increasePrice = False
                    profit = profit + maxPrice - minPrice
                    maxPrice = prices[i-1]
                minPrice = prices[i]
            i += 1
        if increasePrice and prices[-1] > prices[-2]:
            profit = profit + prices[-1] - minPrice
    return profit
    
if __name__ == "__main__":
    profit = maxProfit([7,1,5,3,6,4])
    print(profit)

def test_maxProfit_1():
    res = maxProfit([7,1,5,3,6,4])
    assert res == 7

def test_maxProfit_2():
    res = maxProfit([1,2,3,4,5])
    assert res == 4

def test_maxProfit_3():
    res = maxProfit([7,6,4,3,1])
    assert res == 0
