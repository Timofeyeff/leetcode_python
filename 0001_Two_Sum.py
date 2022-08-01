from typing import List
import pytest

def twoSum (nums: List[int], target: int) -> List[int]:
    if len(nums) > 1:
        for i in range(len(nums)):
            if i+1 <= len(nums):
                for j in range (i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
    return [0,0]


if __name__ == "__main__":
    res = twoSum([2,7,11,15],9)
    print("input [2,7,11,15],9 output ", res)

def test_two_sum_1():
    res = twoSum([2,7,11,15],9)
    assert res == [0,1]

def test_two_sum_2():
    res = twoSum([3,2,4],6)
    assert res == [1,2]

def test_two_sum_3():
    res = twoSum([3,3],6)
    assert res == [0,1]

def test_two_sum_4():
    res = twoSum([3,4],6)
    assert res == [0,0]
