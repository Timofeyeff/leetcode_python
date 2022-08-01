from typing import List
import pytest

def runningSum(nums: List[int]) -> List[int]:
    res_array = []
    cur_value = 0
    for i in range(len(nums)):
        cur_value = cur_value + nums[i]
        res_array.append(cur_value)
    return res_array

if __name__ == "__main__":
    res = runningSum([1,2,3,4])
    print('input [1,2,3,4] output', res)

def test_runningSum():
    res = runningSum([1,2,3,4])
    assert res == [1,3,6,10]