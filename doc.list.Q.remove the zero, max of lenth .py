# a=[101,100,1002]
# b=[]
# i=0
# while i<len(a):
#     a[i]=str(a[i])
#     s=''
#     j=0
#     while j<len(a[i]):
#         if a[i][j]!='0':
#             s+=a[i][j]
#         j+=1
#     b.append(int(s))
#     i=i+1
# print(b)

# a=['ab','abc']
# i=0
# max=(a[i])
# b=[]
# while i<len(a):
#     if (a[i])>max:
#         max=(a[i])
#         b.append(max)
#     i=i+1
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



# a=[12,123]
# i=0
# b=[]
# while i<len(a):
#     a[i]=str(a[i])
#     s=0
#     j=0
#     while j<len(a[i]):
#         s+=int(a[i][j])
#         j+=1
#     b.append(s)
    # i+=1
# print(b)




# i=1
# k=1
# while i<=8:
#     j=1
#     while j<=i:
#         print(k,end="")
#         j+=2
#         k+=1
#     print(end=" ")
#     i+=2


# a=[101,100,1002]
# b=[]
# i=0
# while i<len(a):
#     a[i]=str(a[i])
#     s=''
#     j=0
#     while j<len(a[i]):
#         if a[i][j]!='0':
#             s+=a[i][j]
#         j+=1
#     b.append(int(s))
#     i=i+1
# print(b)



a=[[1,2,3],[4,5,6],[7,8,9],[10,12,13]]
i=0
max=len(a[i])
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        if len(a[i][j])>max:
            max=len(a[i][j])
        b=a[i][j]
    i=i+1
print(max,b)
