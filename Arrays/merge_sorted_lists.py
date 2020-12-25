"""The DRY approach, haven't it out yet 
def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list"""








kevin=[3, 4, 6, 10, 11, 15]
alice=[1, 5, 8, 12, 14, 19, 22, 24]
kevin=[]
alice=[2]


def merge_lists(lst1, lst2):
    final= []
    pointer1=0
    pointer2=0

    while pointer1 != len(lst1) or pointer2 != len(lst2):

        if pointer1 == len(lst1):
            final.append(lst2[pointer2]) 
            pointer2+=1
        elif pointer2 == len(lst2):
            final.append(lst1[pointer1])
            pointer1+=1
        elif lst1[pointer1] >= lst2[pointer2]:
            final.append (lst2[pointer2])
            pointer2+=1
        else:
            final.append(lst1[pointer1])
            pointer1+=1
    print (final)

merge_lists(kevin, alice)
    
