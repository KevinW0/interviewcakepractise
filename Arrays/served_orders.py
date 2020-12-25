import unittest
order1=[17,8,24]
order2=[12,19,2]
order3=[17,8,12,19,24,2]
def is_first_come_first_served(lst1, lst2, servedlst):
    if  len(lst1)+len(lst2) != len(servedlst):
        return False

    """pointer 1 and pointer 2
    base case: 0th el needs to be at lst1[pointer1] or lst2[pointer2]
    if it is either one, then move pointer down one

    normal case: nest element needs to be - either one of the pointers.
    if it is the pointer, then move the poiner down and repeat.

    Edge cases: will the empties be handled (one, two, three)
    """
    pointer1=0
    pointer2=0
    for x in servedlst:
        print (pointer1)
        print(pointer2)
        pointer1exceed = pointer1 >= len(lst1)
        pointer2exceed = pointer2 >= len(lst2)
        if not (pointer1exceed) and  x == lst1[pointer1]:
            pointer1+=1
        elif not (pointer2exceed) and x == lst2[pointer2]:
            pointer2+=1
        elif pointer2exceed and x == lst1[pointer1]:
            pointer1+=1 
        elif pointer1exceed and x == lst2[pointer2]:
            pointer2+=1
            """Why the last two cases are redudant.
             Without loss of generality,
             If the first pointer exceeds, the second case will either 
             catch (suggesting one list is longer than another) and evaluate
             the number as normal with the second list. If the second case doesn't catch
             This is a contradiction - as this suggests both lists have been exhausted
             but there are still more elements in served list to check. But then that means
             served list is greater than the sum of both lists, which is returned as false
             in lines 6 and 7.

            """
        else: 
            return False
    return True

# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)


unittest.main(verbosity=2)



