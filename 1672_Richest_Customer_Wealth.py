from typing import List
import pytest

def maximumWealth(accounts: List[List[int]]) -> int:
    return max([sum(account) for account in accounts])

if __name__ == "__main__":
    res = maximumWealth([[1,2,3],[3,2,1]])
    print ("input [1,2,3],[3,2,1] output ", res)

def test_maximumWealth_1():
    res = maximumWealth([[1,2,3],[3,2,1]])
    assert res == 6

def test_maximumWealth_2():
    res = maximumWealth([[1,5],[7,3],[3,5]])
    assert res == 10

def test_maximumWealth_3():
    res = maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
    assert res == 17

