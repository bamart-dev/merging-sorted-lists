

def merge_lists(list_1, list_2):
    """Return one merged, sorted list from elements in given lists.

    Given two lists of sorted integers, returns one merged list
    composed of elements from both lists. Duplicate values are not
    included in the resulting list and the sort order is maintained.
    """
    if list_1 != list_2:
        exists = set(list_1)

        for i_2 in range(len(list_2)):
            if list_2[i_2] in exists:
                continue
            is_biggest = True

            for i in range(len(list_1)):
                if list_2[i_2] < list_1[i]:
                    list_1.insert(i, list_2[i_2])
                    is_biggest = False
                    break

            if is_biggest:
                list_1.append(list_2[i_2])

    return list_1
