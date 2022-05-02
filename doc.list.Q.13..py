# Write a Python program to create a list reflecting the modified run-length encoding from 
# a given list of integers or a given list of characters. 
# Original list
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]



a= ['a','a','b','c','d','d','d','a','d','n','s','s']
b=[]
for i in a:
    count=0
    for j in a:
        if i==j:
            count+=1
    if i not in b:
        b.append(i)
        print([i,count])
    


# list=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a","p"]
# l=[]
# for i in list:
#     c=0
#     for j in list:
#         if i==j:
#             c=c+1
#     if i not in l:
#         l.append(i)
#         print([i,c])
