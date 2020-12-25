import unittest

"""
Establishes an upper bound and lower bound

If new upper bound (1) is greater and new lower is...

within upper and lower
> Condense - expand upper bound

less than lower (2)
> Condense - expand lower and upper 

..............................................
If new lower bound is lower than old lower (2), 

and (old) upper not lower than lower (old)
> Condense - expand lower  bound

"""

"""O(n^2) implementation, o(n logn) can be achieved by sorting
the meeting array and merging adjacent elements. 

O(n) for one pass adjacent array, o(n logn) for sort"""

def merge_ranges2(lst):
    condensed=[(lst[0][0],lst[0][1])]
    for tup in lst:
        lower=tup[0]
        upper=tup[1]
        flag=False
        for index in range (0, (len (condensed))+1 ):
            if index == ((len(condensed))):
                if flag == False:
                    condensed.append((lower, upper))
                else:
                    print ("bro something has gone very wrong")
            
            lower2=condensed[index][0] 
            upper2=condensed[index][1]
            
            if upper >= upper2:
                if lower <= upper2 and lower >= lower2:
                    condensed[index]=(lower2, upper)
                    flag=True
                    break
                elif lower < lower2:
                    condensed[index]=(lower, upper)
                    flag=True
                    break
            elif upper < upper2 and lower > lower2:
                flag=True
                break
            elif lower < lower2:
                condensed[index]=(lower, upper2)
                flag=True
                break
    return condensed



#One Pass solution

def merge_ranges(lst):
    lst.sort(key=lambda x: x[0])
    condensed=[]
    for i in range(0, len(lst)):
        lower=lst[i][0]
        upper=lst[i][1]
        if i == (len(lst)-1):
            condensed.append((lower, upper))
            break
        lower2=lst[i+1][0]
        upper2=lst[i+1][1]
        if lower2 <= upper or upper >= upper2:
            lst[i+1]= ((lower, (max (upper, upper2))))
        else:
            condensed.append(lst[i])
    return condensed
            





# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)


