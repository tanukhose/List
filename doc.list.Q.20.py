# Write a function that takes one argument “n” and delete that many elements from the list.

# delete_nth ([1,1,1,1],2) # return [1,1]
#             delete_nth ([20,37,20,21],1) # return [20,37,21]



a=[20,37,20,21]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)