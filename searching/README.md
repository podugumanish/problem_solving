Explain linear search and its time complexity.
seach each element untill end of list with conditional statement. 

Time complexitiy: 
best case O(1), 
worst case O(n) if no where the condition satsfied, 

space complexity:
o(1) space Note: No extra memory used

When would you prefer linear search over binary search?
As per small size or unsorted
cost of list sort is higher than scan
finding all occurances of the value
You have linked lists or streaming data where random access is expensive or not possible.

What is binary search, and why does it require a sorted list?
Its divide and conquor rule based search 
repeatedly splits to find the element
compare target with middle
if equal found
else target is smaller search with the left elements
else target is larger search with the right elements


Explain the time complexity of binary search (worst, best, average case).
Timecomplexity:
best when middle element is target
worst keep half untill one element remains
avg expectig halving the process

space complexity: 
itervative version o(1)
recursive version o(log n)


How would you perform a search in an unsorted list in Python?
using linear search with the conditional statement as per target compare with each element.
else index() works the same

What is exponential search? When is it useful?
unknown /infinite search with sorted or strcutred patterned values.

Explain interpolation search. How is it different from binary search?
improves on binary search by guessing position based on value distribution
pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
instrad always checknig from middle it estimates where the values would be.
as per uniformity it searches the value

it works when the data is uniformly distributed making it faster.
worst case for skewed distribution


How do in and list.index() work under the hood in Python?
both does the linear scan
in returns true or false
index() returns first position of the element raise value error if present

What are the trade-offs between searching in a list, set, and dictionary in Python?

List: orders, supports indexes, slicing, slow for larger data
Set: fast membership tests, no duplicates, no ordering
Dict: Fast key lookup, key-value storage




Why is searching in a Python dictionary O(1) on average but not always?
o(1) avg case hash distrubte function
o(n) hash collition function multiple keys hash to same bucket

🧑‍💻 Coding Questions

Implement linear search without using built-in functions.
usecase: finding an element inside a list
approach:
    takes the target input and list of elements
    validate element wise
    if found return the index of the value in list provided



Implement binary search iteratively and recursively.
usecase: iterative binary search
approach:
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

usecase: recursively binary search
    approach:
    take input of list,target, lowest index as 0, highest index as len(lis)-1
    find the mid with low + high //2
    validate with target
    if validated send back mid index
    else if check with target is greater than the mid of list
    call the func sending target, list, low as mid+1,high as high
    else call the func sending target, list, low as low,high as mid-1

    example:[1,2,3,4,5,6]

Find the first and last occurrence of a number in a sorted list.
usecase:
target = 10
[1,2,3,4,1,4,1,1,3,1,4,3,2,5]
approach:

Find the index of the smallest element greater than or equal to a target (lower bound search).

Find the index of the largest element less than or equal to a target (upper bound search).

Search in a rotated sorted array (e.g., [4,5,6,7,0,1,2]).

Search in a 2D matrix (matrix is row-wise and column-wise sorted).

Search in a nearly sorted array (where elements are at most one position away).

Implement jump search in Python.

Implement ternary search on a sorted array.

⚡ Optimization & Advanced

Explain how to optimize repeated search queries on large datasets (hint: use hashing or pre-processing).

When would you choose a Trie for searching? Implement a basic prefix search using a Trie.

How would you search efficiently in a large text file (GBs in size) without loading the whole file into memory?

Write a program to find duplicates in a list efficiently (O(n) time, O(n) space).

Implement binary search using Python’s bisect module.

How would you handle case-insensitive searching in Python?

How to search for a substring in a string efficiently? (Explain KMP, Rabin-Karp).

Find all occurrences of a substring in a string without using .find() or regex.

How do you search for a pattern in a streaming data input?

Design a search API (input: list of products, output: matched product suggestions in O(log n) time).