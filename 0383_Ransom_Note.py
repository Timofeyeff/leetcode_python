import pytest

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for key, value in enumerate(ransomNote):
        if value in magazine:
            magazine = magazine.replace(value,"",1)
        else:
            return False
    return True

if __name__ == "__main__":
    ransomNote = input("Input Ransom Note ")
    magazine = input("Input Magazine ")
    res = canConstruct(ransomNote, magazine)
    if res:
        print("Ransom note may be construct from Magazine")
    else:
        print("Sorry, Ransom note NOT may be construct from magazine")

def test_canConstruct_1():
    res = canConstruct("a", "b")
    assert res == False

def test_canConstruct_2():
    res = canConstruct("aa", "ab")
    assert res == False

def test_canConstruct_3():
    res = canConstruct("aa", "aab")
    assert res == True