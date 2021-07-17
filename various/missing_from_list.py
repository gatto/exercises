from rich import print


def what_missing(my_coll: list) -> int:
    """Takes a list of sequential integers, returns the (only) missing number. Must be an inside number, so not in the first or last position. Doesn't care if starting from 1 or from any number"""
    my_coll = sorted(my_coll)
    my_min = my_coll[0]
    for i, el in enumerate(my_coll):
        if i + my_min != el:
            return i + my_min


def which_missing(my_coll: list[int]) -> list[int]:
    """As before, but can find all the missing numbers."""
    my_coll = sorted(my_coll)
    results = []
    expected_value = my_coll[0]
    current_ind = 0
    while current_ind < len(my_coll):
        if expected_value != my_coll[current_ind]:
            results.append(expected_value)
        else:
            current_ind += 1
        expected_value += 1
    return results


# throws exception if not integers
a = [int(item) for item in input("Enter the integers separated by spaces : ").split()]

missing = what_missing(a)
print(f"From {a} the first integer missing is {missing}.")

missing = which_missing(a)
print(f"From {a} the integers {missing} are missing.")
