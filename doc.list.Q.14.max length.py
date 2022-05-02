# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# max=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if (a[i][j])>max:
#             max=a[i][j]
#         j+=1
#     i+=1
# print(max)

a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=len(a[i])
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        b=a[i]
    i=i+1
print(max,b)




# a=[[1,3],[4],[10,11,12],[79]]
# i=0
# max=len(a[i])
# while i<len(a):        
#     if len(a[i])>max:
#         max=len(a[i])
#         b=a[i]
#     i+=1
# print(max,b)




# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# b=[]
# while i<len(a):
#     # a[i]=str(a[i])
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum+=int(a[i][j])
#         j+=1
#     b.append(sum)
    
#     i+=1
# print(b)


# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# s=0
# while i<len(a):
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum+=int(a[i][j])
#         j+=1
#     s+=sum
    
#     i+=1
# print(s)

