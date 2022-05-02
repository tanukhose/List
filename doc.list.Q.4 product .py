# List product excluding duplicates.
#     List = [6,1,3,5,6,3,1]
#     Output: 60

a= [6,1,3,5,6,3,1]
i=0
prod=1
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        prod=prod*b[i]
    i+=1
print(b,prod)


# a= [6,1,3,5,6,3,1]
# i=0
# prod=1
# while i<len(a):
#     prod*=a[i]%10
#     i+=1
# print(prod)

# for i in range (1,10,2):
#     i=i+2
#     print(i)
0
# while i<=5:
#     j=1
#     while j<=5-i:0
# while i<=5:
#     j=1
#     while j<=5-i:0
# while i<=5:
#     j=1
#     while j<=5-i:0
# while i<=5:
#     j=1
#     while j<=5-i:
#         print()
#         print()
#         print()
#         print()