
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
