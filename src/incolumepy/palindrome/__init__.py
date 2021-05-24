from inspect import stack

def isPalindrome(x):
    """Check Palindrome for strings"""
    lst = [i for i in str(x)]
    lst_rev = lst[::-1]
    if lst == lst_rev:
        return True, ''.join(lst), ''.join(lst_rev), stack()[0][3],
    return False, ''.join(lst), ''.join(lst_rev), stack()[0][3],