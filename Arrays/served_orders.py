order1=[17,8,24]
order2=[12,19,2]
order3=[17,8,12,19,24,2]
def in_order(lst1, lst2, servedlst):

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
        if x == lst1[pointer1]:
            pointer1+=1
        elif x == lst2[pointer2]:
            pointer2+=1
        else: 
            return False
    return True

in_order(order1,order2,order3)



