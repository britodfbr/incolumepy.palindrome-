from copy import copy


def isPalindrome(x):
    """Check Palindrome for natural numbers"""
    rev = 0
    original = copy(x)
    if x < 0:
        return False   # not natural number
    while x > 0:
        rev = rev*10 + x%10
        x = x//10

    if int(rev) == original:
        return True, original, rev,
    return False, original, rev,
