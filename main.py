

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
            num_1 = validate_num(list_1[i])
            num_2 = validate_num(list_2[j])

            if num_1 <= num_2:
                merged_list.append(num_1)
                i += 1
            else:
                merged_list.append(num_2)
                j += 1

        while i < len(list_1):
            num = validate_num(list_1[i])

            merged_list.append(num)
            i += 1

        while j < len(list_2):
            num = validate_num(list_2[j])

            merged_list.append(num)
            j += 1

    except TypeError:
        return "Merge failed: invalid element present."

    return merged_list


def validate_num(element):
    if type(element) is not int:
        raise TypeError

    return element
