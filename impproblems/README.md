The following questions are best practices for an interview
1. fundamentals.py.
Metrics to be noted as per approaches:

# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
# # reverse string
# string = "abcdef"
# # print(string[::-1])
# rev_string= ''
# len_s = len(string)
# print('checking',len_s)
# for i in range(len_s):
#     rev_string += string[(len_s-1)-i]
# print(rev_string)

# list of few indexes
# lis = ['eat','ate','ten','net','bet']
# # divide the list as per anagram
# lis2 = []
# dic = {}
# for i in lis:
#     # key check
    
#     for j in dic:
#         for elem in i:
#             for
        
        # if len(i)==len(j):
            
# multiple duplicate value indexes    # 
# lis = [1,1,2,3,1,5,6,6,7]
# lis2 = tuple(lis)
# dic = {}
# for index,val in enumerate(lis):
#     if val in lis2:
#         if val not in dic:
#             dic[val] =[index]
#         else:
#             dic[val].append(index)
# print(dic)


lis = ['eat', 'ate', 'ten', 'net', 'bet']

# Dictionary to group anagrams
anagram_dict = {}

for word in lis:
    # Sort the word to create the key
    key = ''.join(sorted(word))
    anagram_dict.setdefault(key, []).append(word)

# Get the grouped anagrams as a list of lists
lis2 = list(anagram_dict.values())

print(lis2)

    
            
         
    
    
    