
def linear_search(target,lis=[]):
    """
    takes the target input and list of elements
    validate element wise
    if found return the index of the value in list provided
    """
    for i,val in enumerate(lis):
        if val==target:
            return i
# print(linear_search(1,[9,8,7,6,5,4,4,33,2,1]))

def iterative_binary_search(target,lis):
    """
    approach1:
        With iteration, we use a while loop and manually move the low and high pointers, 
        instead of letting recursion handle the subproblems.
        Explaination:
            declare high and low and assign 0 for low and len(lis)-1 for high
            iterate till high is greater than or equals to low
            find the mid floor div value by 2 with adding high and low 
            if mid is target return its index
            elif target is higher increase low +1
            else target is lower decrease high -1
    example:[1,2,3,4,5,6]
    """
    low, high = 0, len(lis)-1

    while low <= high:
        mid = ( low + high ) //2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return -1

# print(iterative_binary_search(3,[1,2,3,4,5,6]))

def recursive_binary_search(target,lis,low,high):
    """
    approach:
    take input of list,target, lowest index as 0, highest index as len(lis)-1
    find the mid with low + high //2
    validate with target
    if validated send back mid index
    else if check with target is greater than the mid of list
    call the func sending target, list, low as mid+1,high as high
    else call the func sending target, list, low as low,high as mid-1

    example:[1,2,3,4,5,6]
    """
    mid = ( low + high ) //2
    print('checking iterative',low,high,lis,mid)

    if lis[mid] == target:
        return mid
    elif lis[mid] < target:
        recursive_binary_search(target,lis,mid+1,high)
    else:
        recursive_binary_search(target,lis,low,mid-1)
    return -1
lis  = [1,2,3,4,5,6]
print(recursive_binary_search(4,lis,0,len(lis)))

def number_first_last_occurance(target,lis):
    """
    approach1:
    declare variables and assign default values as indexes f=0, l = list length - 1 
    loop the list for first index and assign the index of its first finding of target and break
    loop the list for last index and assign the index of its first finding of target and break
    return f and l indexes back
    
    """

    # approach1:

    # # i/p
    # l,f = len(lis)-1,0
    
    # # process
    # # step1: finding first index
    # i=0
    # while i<len(lis)-1:
    #     if lis[i] == target:
    #         f = i
    #         break
    #     i+=1
    # print('checking first',i)
    # # step2: finding last index 
    # j = len(lis)-1
    # while j>0:
    #     if lis[j] == target:
    #         l = j
    #         break
    #     j-=1
    # print('checking first',j)

    # print('checking first and last',f,l)
    # return f,l

    """approach2"""
    first = -1
    last = -1

    for i, val in enumerate(lis):
        if val == target:
            if first == -1:
                first = i
            last = i
            print('checking first and last',first,last)

    return first, last


        
    

# unittesting
# case1: where number starts from first and  anywhere inbetween
# [1,2,3,4,1,4,1,1,3,1,4,3,2,5], 1
target = 4
lis = [1,2,3,4,1,4,1,1,3,1,4,3,2,5]
# print(number_first_last_occurance(target,lis))
# case2: only one number
target = 1
lis = [1,2,5]
# print(number_first_last_occurance(target,lis))

def first_last_occurrence_sorted(target, lis):
    """
    Find the first and last occurrence of a number in a sorted list using binary search.

    This works in O(log n) time because we use binary search twice:
      - Once to find the first occurrence.
      - Once to find the last occurrence.

    Args:
        target (int): The number to search for.
        lis (list): A sorted list of numbers.

    Returns:
        tuple: (first_index, last_index) or (-1, -1) if not found.

    Example:
    --------
    >>> first_last_occurrence_sorted(3, [1, 3, 3, 3, 5, 7])
    (1, 3)
    """

    def find_first():
        """Binary search to find the first occurrence of target."""
        left, right = 0, len(lis) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] == target:
                first = mid
                right = mid - 1  # keep searching on left side
            elif lis[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def find_last():
        """Binary search to find the last occurrence of target."""
        left, right = 0, len(lis) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] == target:
                last = mid
                left = mid + 1  # keep searching on right side
            elif lis[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    return find_first(), find_last()


# Example usage
print(first_last_occurrence_sorted(3, [1, 3, 3, 3, 5, 7]))  # Output: (1, 3)
print(first_last_occurrence_sorted(5, [1, 3, 3, 3, 5, 7]))  # Output: (4, 4)
print(first_last_occurrence_sorted(2, [1, 3, 3, 3, 5, 7]))  # Output: (-1, -1)

# Find the index of the smallest element greater than or equal to a target (lower bound search).
# def smallest_element_index(target, lis):
#     """
#     This approach targets index ainst the target instead of value on the list vs target
#     """
#     index=-1 # defaulted to -1
#     print('checking target',target)
#     smallest_element_index_greater_than_target = -1
#     for i,val in enumerate(lis):
#         """
#         Smallest element index greater than equals to target
#         smallest element
#         whose index greater than equals to target
        
#         """           
#         if val<target and i>=target:
#             smallest_element_index_greater_than_target = i   
#             break   
#         print('the way of checking',target,val,smallest_element_index_greater_than_target)
#     return smallest_element_index_greater_than_target
# print(smallest_element_index(4,[1,1,2,2,3,3,4,4,5,5,6,6,7,8]))

def smallest_element_index(target, lis):
    """
    Find the index of the smallest element greater than or equal to target (lower bound).

    This uses binary search in O(log n) time.
    If all elements are smaller than the target, returns -1.

    Args:
        target (int): The value to search for.
        lis (list): A sorted list of numbers.

    Returns:
        int: The index of the smallest element >= target, or -1 if none exists.

    Example:
        >>> smallest_element_index(4, [1, 3, 5, 7])
        2   # because lis[2] = 5, which is the smallest >= 4
        >>> smallest_element_index(8, [1, 3, 5, 7])
        -1  # no element >= 8
    """
    left, right = 0, len(lis) - 1
    result = -1  # default to -1 if no element >= target

    while left <= right:
        mid = (left + right) // 2
        if lis[mid] >= target:
            result = mid  # candidate index
            right = mid - 1  # look for a smaller index on the left
        else:
            left = mid + 1

    return result


# Example usage:
print(smallest_element_index(4, [1, 3, 5, 7]))  # 2
print(smallest_element_index(2, [1, 3, 5, 7]))  # 1
print(smallest_element_index(8, [1, 3, 5, 7]))  # -1

def largest_element_index(target, lis):
    """
    Find the index of the largest element less than or equal to a target (upper bound search).

    This uses binary search in O(log n) time.
    If all elements are smaller than the target, returns -1.

    Args:
        target (int): The value to search for.
        lis (list): A sorted list of numbers.

    Returns:
        int: The index of the largest element <= target, or -1 if none exists.

    Example:
        >>> largest_element_index(4, [1, 3, 5, 7])
        1   # because lis[1] = 3, which is the largest <= 4
        >>> largest_element_index(8, [1, 3, 5, 7])
        3  # one element <= 8
    """
    left, right = 0, len(lis) - 1
    result = -1  # default to -1 if no element >= target

    while left <= right:
        mid = (left + right) // 2
        if lis[mid] <= target:
            result = mid  # candidate index
            left = mid + 1
            # look for a largest index on the left
        else:
            right = mid - 1
            

    return result

# Example usage:
print(largest_element_index(4, [1, 3, 5, 7]))  # 1
print(largest_element_index(2, [1, 3, 5, 7]))  # 0
print(largest_element_index(8, [1, 3, 5, 7]))  # 3



# checking and applying in same while loop the both upper and lower bound
def binary_search_bounds(target, lis):
    """
    Perform a single binary search pass to find:
      - Lower Bound (smallest element >= target)
      - Upper Bound (largest element <= target)
      - Exact Match (if exists)
    
    :param target: Value to search for
    :param lis: Sorted list of elements
    :return: dict with keys:
             'lower_index', 'lower_value',
             'upper_index', 'upper_value',
             'exact_index', 'exact_value'
    """
    left, right = 0, len(lis) - 1
    lower_idx = -1
    upper_idx = -1
    exact_idx = -1

    while left <= right:
        mid = (left + right) // 2

        if lis[mid] == target:
            exact_idx = mid
            lower_idx = mid
            upper_idx = mid
            break  # exact match found, no need to continue

        elif lis[mid] > target:
            # Candidate for lower bound
            lower_idx = mid
            right = mid - 1
        else:
            # Candidate for upper bound
            upper_idx = mid
            left = mid + 1

    return {
        "lower_index": lower_idx,
        "lower_value": lis[lower_idx] if lower_idx != -1 else None,
        "upper_index": upper_idx,
        "upper_value": lis[upper_idx] if upper_idx != -1 else None,
        "exact_index": exact_idx,
        "exact_value": lis[exact_idx] if exact_idx != -1 else None
    }

print(binary_search_bounds(8, [1, 3, 5, 7]))  # 3
