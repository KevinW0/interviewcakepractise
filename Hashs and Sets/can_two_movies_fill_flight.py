import unittest

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