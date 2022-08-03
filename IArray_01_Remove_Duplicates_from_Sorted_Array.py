import pytest
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    temp = -101
    count = 0
    i = 1
    if len(nums) > 1:
        while i < len(nums) and count < len(nums)-1:
            if nums[count] == nums[count + 1]:
                nums.pop(count + 1)
                nums.append(-101)
            else:
                count += 1
            i += 1
        count += 1
    else:
        count = 1
    return count


if __name__ == "__main__":
    nums = [1,1,2]
    print(removeDuplicates(nums))

def test_rmoveDuplicates_1():
    res = removeDuplicates([1,1,2])
    assert res == 2

def test_rmoveDuplicates_2():
    res = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    assert res == 5