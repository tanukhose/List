# Write a Python program to remove all the values except integer values from a given
#  array of mixed values. 
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed
#  values: [12, 0]


a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
b=[]
while i<len(a):
    if (type(a[i]))==int:
        b.append(a[i])
    i+=1
print(b)