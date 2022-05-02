# Report Card 
# Sum of the nested list given above -1142 
# Please see this list :

marks=[
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
    ]
i=0
b=[]
sum=0
while i<len(marks):
    j=0
    s=0
    while j<len(marks[i]):
        s+=marks[i][j]
        j=j+1
    sum+=s
    i+=1
    # b.append(sum)
print(sum)
    


# Sum of the nested list given above - 965.


marks=[[78, 76, 94, 86, 88],
      [91, 71, 98, 65],
      [95, 45, 78]
      ]
i=0
sum=0
while i<len(marks):
    j=0
    s=0
    while j<len(marks[i]):
        s+=marks[i][j]
        j=j+1
    sum+=s
    i=i+1
print(sum)



# Sum of the nested list given above - 1324

a=[
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
    ]
i=0
sum=0
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        s=s+a[i][j]
        j+=1
    sum+=s
    i+=1
print(sum)
























# a=[12,123]
# i=0
# b=[]
# while i<len(a):
#     a[i]=str(a[i])
#     j=0
#     s=0
#     while j<len(a[i]):
#         s+=int(a[i][j])
#         j+=1
#     b.append(s)
#     i+=1
# print(b)