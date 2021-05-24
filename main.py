from incolumepy.palindrome import brute_force
from incolumepy.palindrome import whitlists
from incolumepy.palindrome import isPalindrome

def show(func, entrance:list):
    for i in entrance:
        print(func(i))


if __name__ == "__main__":
    lista = [11, 121, 1221, 91777719, 19780620, 240942]
    lista2 = lista + ['ana', 'ada', 'calilac', 'abraão', 3.1415, 'oxffff', 'affa']
    show(brute_force.isPalindrome, lista)
    show(whitlists.isPalindrome, lista)
    show(isPalindrome, lista2)
