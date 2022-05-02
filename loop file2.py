# a=int(input("enter the num"))
# i=1
# k=1
# while i<=a:
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         j+=2
#         k+=1
#     print()
#     i+=2


# num=int(input("enter  "))
# i=0
# sum=0
# while i<num:
#     num1=int(input("enter  "))
#     sum+=num1
#     i+=1
# print(sum)



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
#     while j<=i:
#         print(a[i],end="")
#         j+=1
#     print("_",end=" ")
#     i+=1







# a="python"
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[i],end="")
#         j+=1
#     print()
#     i+=1


# a=input("enter the string")
# i=0
# while i<len(a):
#     j=0
#     while j<=i:
#         print(a[i],end=" ")
#         j+=1
#     print()
#     i+=1



# a=input("enter the string")
# i=0
# while i<len(a):
#     if a[i]=="a"or a[i]=="e"or  a[i]=="i"or  a[i]=="o"or  a[i]=="u":
#         print("vowel",a[i])
#     else:
#         print("consonant",a[i])
#     i+=1



# year=int(input("enter the year"))
# month=year 
# if year%4==0:
#     print("pichale :-",month-4," next :-",month+4,'\n')
#     if year%100==0:
#         print("pichale :-",month-8," next :-",month+8,'\n')
#         if year%400==0:
#             print("pichale :-",month-12," next :-"month+12,'\n')
#         else:
#             print(month-4,month+4)
#     else:
#         print(month-8,month+8)
# else:
#     print(month-12,month+12)

# a=[]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     i+=1
# print(b)

# a=[1,2,3,4,5,6,7,8]
# i=0
# b=[]
# while i<len(a):
#     s=(a[i])+1
#     b.append(s)
#     i+=1
# print(b)



# a=[1,2,3,4,5,6,7,8]
# i=0
# sum=0
# pro=1
# while i<len(a):
#     if i<=4:
#         sum+=a[i]
#     else:
#         pro*=a[i]
#     i+=1
# print("sum ",sum)
# print("product",pro)


# a=[1100,1050]
# i=0
# b=[]
# while i<len(a):
#     a[i]=str(a[i])
#     j=0
#     s=" "
#     while j<len(a[i]):
#         if a[i][j]!="0":
#             s+=a[i][j]
#         j+=1
#     b.append(int(s))
#     i+=1
# print(b)



