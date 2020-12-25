import unittest


"""One pass solution. 
  def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False

"""

"""
The one pass solution works because..... 
There is no loss of generality from which movie you hit first. 
In other words, if you were to iterate across all movie lengths,
you'd hit a 2 compliments. 

So, this approach leverages that you might be hitting a compliment but
not returning true yet because the corresponding movie pair hasnt been seen 
yet.

So yes, this means you might be increasing average runtime in iterating
o(n). My solution will do O(2n) but will have a much larger space
complexity (as you hash all other movies). But it also means it will return 
true on the very first movie pair seen.


"""


def can_two_movies_fill_flight(movie_lengths, flight_length):
    sets={}
    for i in movie_lengths:
        if i not in sets:
            sets[i]=1
        else:
            sets[i]=sets.get(i)+1

    def check_length(fullset, flightlength, discard):
        if fullset[discard] == 1:
            del fullset[discard]
        else:
            fullset[discard]=fullset.get(discard)-1

        compliment = flightlength - discard
        if compliment in fullset:
            return True
        else:
            return False


    for o in movie_lengths:
        if check_length(sets, flight_length, o) == True:
            return True
        

    return False




























# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_multiple_movies_shorter_than_flight(self):
        result = can_two_movies_fill_flight([5, 6, 7, 8], 9)
        self.assertFalse(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)