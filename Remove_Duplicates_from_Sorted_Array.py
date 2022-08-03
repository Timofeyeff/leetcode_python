import pytest
from typing import List

def removeDuplicates(num: List[int]) -> List[int]:
    temp = -1
    res = []
    for i in range(len(num)):
        if num[i] > temp:
            temp = num[i]
            res.append(num[i])
    return res

if __name__ == "__main__":
    nums = [1,1,2]
    print(removeDuplicates(nums))

def test_rmoveDuplicates_1():
    res = removeDuplicates([1,1,2])
    assert len(res) == 2
    assert res == [1, 2]

def test_rmoveDuplicates_2():
    res = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    assert len(res) == 5
    assert res == [0,1,2,3,4]