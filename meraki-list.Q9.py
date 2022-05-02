#Write a code that works for any list, and that tells how many odd numbers and how many 
# even numbers are there in a given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
count1=0
a=[]
b=[]
while i<len(elements):
    num=elements[i]
    if  num%2==0:
        a.append(elements[i])
        count+=1
    else:
        b.append(elements[i])
        count1+=1
    i+=1
print(a,count,'even')
print(b,count1,'odd')



# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# count=0
# count1=0
# while i<len(elements):
#     num=elements[i]
#     if  num%2==0:
#         count+=1
#     else:
#         count1+=1
#     i+=1
# print(count,'even')
# print(count1,'odd')











