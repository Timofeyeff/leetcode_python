from typing import List
import pytest

def fizzBuzz(n: int) -> List[str]:
    res_array = []
    for i in range (1, n+1):
        if i%3 == 0 and i%5 == 0:
            res_array.append("FizzBuzz")
        elif i%3 == 0:
            res_array.append("Fizz")
        elif i%5 == 0:
            res_array.append("Buzz")
        else:
            res_array.append(str(i))
    return res_array

if __name__ == "__main__":
    str_n = input ("Input number")
    n = int(str_n)
    if n > 0:
        res = fizzBuzz(n)
    print(res)

def test_fizzBuzz_1():
    res = fizzBuzz(3)
    assert res == ["1","2","Fizz"]

def test_fizzBuzz_2():
    res = fizzBuzz(5)
    assert res == ["1","2","Fizz","4","Buzz"]

def test_fizzBuzz_3():
    res = fizzBuzz(15)
    assert res == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

