import unittest
"""Rough Idea:
Determine the length of the string
Push everything into a key:freq pair table

if even, then all in the set should be 2 occurances
if odd, up to one in the set should be 1 occurance 

"""



"""
Corrections:
The middle letter might not exclusively show up once. you should check that it's odd
letters might not only show up twice. change the val 2 check to be even occurances.
"""

#retusns a bool
def check_permutation(hashset, even):
    flag = True
    for key in hashset:
        val = hashset.get(key, -1)
        if val % 2 != 0: #is odd
            if flag == True and even == False:
                flag = False
            else:
                return False
    return True

                
def has_palindrome_permutation(the_string):
    even = (len(the_string) % 2 == 0)
    hashtable = {}
    for i in the_string:
        val = hashtable.get(i, -1)
        if val == -1:
            hashtable[i] = 1
        else:
            hashtable[i] = val + 1
    
    return check_permutation(hashtable, even)

    


    

    # Check if any permutation of the input is a palindrome
    

    return False


















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)