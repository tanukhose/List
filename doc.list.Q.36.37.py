# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']



# a=['1', '2', '3', '4', '5', '6', '7', '8']
# i=0
# b=[]
# while i



# Write a Python program to pair up the consecutive elements of a given list.
# Original lists:
# [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# Original lists:
# [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5]]

a=[1, 2, 3, 4, 5, 6,7]
i=0
b=[]
while i<len(a)-1:
    c=a[i],a[i+1]
    n=list(c)
    b.append(n)
    i+=1
print(b)