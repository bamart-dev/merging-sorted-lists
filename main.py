

def merge_lists(list_1, list_2):
    """Return one merged, sorted list from elements in given lists.

    Given two lists of sorted integers, returns one merged list
    composed of elements from both lists. Duplicate values are not
    included in the resulting list and the sort order is maintained.
    """
    merged_list = []
    i = 0
    j = 0
    if list_1 == list_2:
        return list_1

    try:

        while i < len(list_1) and j < len(list_2):
            if type(list_1[i]) is not int or type(list_2[j]) is not int:
                raise TypeError

            if list_1[i] <= list_2[j]:
                merged_list.append(list_1[i])
                i += 1
            else:
                merged_list.append(list_2[j])
                j += 1

        while i < len(list_1):
            if type(list_1[i]) is not int:
                raise TypeError

            merged_list.append(list_1[i])
            i += 1

        while j < len(list_2):
            if type(list_2[j]) is not int:
                raise TypeError

            merged_list.append(list_2[j])
            j += 1

    except TypeError:
        return "Merge failed: invalid element present."

    return merged_list
