def isPalindrome(x: int):
    """Check Palindrome for natural numbers"""
    if not isinstance(x, int):
        return False

    if x < 0:
        return False

    lst = [int(i) for i in str(x)]
    lst_rev = lst[::-1]
    if lst == lst_rev:
        return True
    return False