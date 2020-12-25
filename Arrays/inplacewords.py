import unittest
def reverse_words(msg):

    def reverseword(start, end):
        while (start != end and start < end):
            temp=msg[start]
            msg[start]= msg[end]
            msg[end]=temp
            start+=1
            end-=1


    reverseword(0,len(msg)-1)


    start=0
    end=0
    for i in range (0, len(msg)):
        if msg[i] ==  ' ':
            end = i-1
            reverseword(start, end)
            start=end+2
        elif i == (len(msg)-1):
            reverseword(start, len(msg)-1)

    return msg
   
        




# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)