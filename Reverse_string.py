import pytest
from typing import List

def reverseString(s: List[str]) -> List[str]:
    a = ""
    for i in range(len(s)//2):
        a = s[len(s)-1-i]
        s[len(s)-1-i] = s[i]
        s[i] = a
    return(s)

if __name__ == "__main__":
    inp = input("Input string ")
    s = list(inp)
    res = reverseString(s)
    print(res)

def test_reveseString_1():
    res = reverseString(["h","e","l","l","o"])
    assert res == ["o","l","l","e","h"]

def test_reveseString_2():
    res = reverseString(["H","a","n","n","a","h"])
    assert res == ["h","a","n","n","a","H"]

