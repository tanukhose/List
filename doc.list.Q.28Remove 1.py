# The task is to perform the operation of removing all the occurrences of a given 
# item/element present in a list.

# Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :




a=[1,1,2,3,4,5,1,2]
i=0
b=[]
while i<len(a):
    if a[i]!=1:
        b.append(a[i])
    i=i+1
print(b)
