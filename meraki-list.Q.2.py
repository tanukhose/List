#write a code that prints the maximum in this list.


number=[50,40,23,70,56,12,5,10,7]
a=0
i=0
while i<len(number):
    if number[i]>a :
        a=number[i]
    i=i+1
print(a)
# number=[50,40,23,70,56,12,5,10,7]
min=number[0]
i=0
while i<len(number):
    if number[i]<min:
        min=number[i]
    i=i+1
print(min)


# while i<len(b):
#     if b[i]>max:
#         max=b[i]
#     if b[i]<min:
#         min=b[i]
#     i+=1
# print("max",max)
# print("min",min)

# a="234567"
# i=0
# sum=0
# while i<len(a):
#     sum+=int(a[i])
#     i+=1
# print(sum)

# a=str(input("enter the string"))
# i=0
# while i<len(a):
#     j=0
#     while j:
#         print(i)
#         j+=1
