# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectively.



# a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# i=0
# c=0
# k=3
# while i<len(a):
#     if a[i]==k:
#         c+=1
#     i+=1
# print(c,k)


# a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a):
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     if count>2:
#         if a[i] not in b:
#             b.append(a[i])
#     i+=1
# print(b)


# a=[[1,2],[12,34],[12,34,5,67],[23],[9,87,654]]
# i=0
# max=len(a[i])
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         b=a[i]
#     i=i+1
# print(max,b)

