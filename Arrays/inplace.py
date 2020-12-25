"""pretty standard. instead of importing floor to calculate each one
use a double pointer method and exit when left points exceeds the right"""
""" o(1) space. o(n/2)=o(n) time"""


import math

#listof Char -> listof Char
def in_place(lst):
    for i in range (0, math.floor((len(lst)/2))):
        char1 = lst[i]
        lst[i]=lst[-i-1]
        lst[-i-1]=char1

    print (lst)

in_place(['a','b', 'w','c','d'])