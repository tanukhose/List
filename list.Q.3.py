#write a code that finds second maximum element from the list and print its.
#   output= 70 56 50:

# number=[50,40,23,70,56,12,5,10,7]
# max=0
# max2=0
# max3=0
# i=0
# while i<len(number):
#     if number[i]>max :
#         max=number[i]
#     i=i+1
# i=0
# while i<len(number):
#     if number[i]>max2 and number[i]!=max :
#         max2=number[i]
#     i=i+1 
# i=0
# while i<len(number):
#     if number[i]>max3 and number[i]!=max and number[i]!=max2:
#         max3=number[i]
#     i=i+1
# print(max,max2,max3)

     
     
     
     
     
     
     
        # nexted list to simple list 
# a=[1,2,3,[3,4,[8,9,]]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])
#     i+=1
# print(b)


# a=[[2,3,[4,5],[],8,[]]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]!=[]:
#             b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)


# a=["abcd1234"]
# i=0
# b=[]
# while i<len(a):
#     j=1
#     while j<len(a[i])+1:
#         s=a[i][-j]
#         b.append(s)
#         j+=1
#     i+=1
# print(b)

# a=[23,45,36]
# i=0
# b=[]
# while i<len(a):
#     a[i]=str(a[i])
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum+=int(a[i][j])
#         j+=1
#     b.append(sum)
#     i+=1
# print(b)
            
# c=["DD30","SS40","AA60"]
# i=0
# b=[]
# while i<len(c):
#     j=0
#     sum=""
#     while j<len(c[i]):
#         if c[i][j]>="0" and c[i][j]<="9":
#             sum+=c[i][j]
#         j+=1
#     b.append(int(sum))
#     i+=1
# print(b)






a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
b=[]
while i<len(a):
    j=0
    s=0
    count=0
    c=[]
    while j<len(a[i]):
        s+=a[j][i]
        count+=1
        j+=1
    c.append(s)
    b.append(c)  
    i+=1
print(b)