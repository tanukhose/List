
# Given a list of numbers, write a Python program to count positive and negative numbers 
# in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

list=[2, -7, 5, -64, -14]
i=0
c=0
c1=0
while i<len(list):

    if list[i]>0:
        c+=1
    else:
        c1+=1
    i+=1
print("pos:-",c,"neg:-",c1)



list=[-12, 14, 95, 3]
i=0
count=0
count1=0
while i<len(list):
    if list[i]>0:
        count+=1
    else:
        count1+=1
    i+=1
print("pos:-",count,"neg:-",count1)

