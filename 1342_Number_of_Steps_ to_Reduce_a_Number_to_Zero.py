import pytest

def numberOfSteps(num: int) -> int:
    count = 0
    while num > 0:
        count += 1
        if num%2 == 0:
            print (num, "is even;")
            num = int(num/2)
            print ("divide by 2 and obtain", num)
        else:
            print (num, "is odd;")
            num -= 1
            print ("substract 1 and obtain", num)
    return count

if __name__ == "__main__":
    num = int(input("Input number"))
    count = 0
    if num > 0:
        count = numberOfSteps(num)
    print ("Output", count)

def test_numberOfSteps_1():
    count = numberOfSteps(14)
    assert count == 6

def test_numberOfSteps_2():
    count = numberOfSteps(8)
    assert count == 4

def test_numberOfSteps_3():
    count = numberOfSteps(123)
    assert count == 12
