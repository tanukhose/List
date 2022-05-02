# a=[1,"f",2,"b",3,4,5,"h","j",6,9,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     elif type(a[i])==int:
#         c.append(a[i])
#     i=i+1
# print(b)
# print(c)

# a=[1,2,2,3,4,4,5,1]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=1:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[[1,2],[3,2],[5,6],[4],[89],[80]]
# sum=0
# i=0
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a[i]):
#         s+=a[i][j]
#         j+=1
#     sum+=s
#     i=i+1
# print(sum)

# a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# max=len(a[i])
# min=len(a[i])
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         b=a[i]
#     else:
#         min=len(a[i])
#         c=a[i]
#     i+=1
# print(max,b)
# print(min,c)



#  a=[22.4,4.0,16.22,9.1,11.0,12.22,14.2,5.2,17.5]
# i=0
# max=a[0]
# min=a[0]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     elif a[i]<min:
#         min=a[i]
#     i=i+1
# print(int(max))
# print(int(min))

# a=["red","orange","green","blue","white"],["black","yellow","green","blue"]
# i=0
# b=[]
# while i<len(a):



# t=int(input("number"))
# for i in range(t):
#     n=int(input(""))
#     l=list(str(int(input())))
#     if '0' in l or '5'in l:
#         print("yes")
#     else:
#         print("no")    


# a=[[1,2,3],[2,4,5],[1,1,1]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j+=1
#     i+=1
# print(a)



# a=int(input("enter the number :"))
# a=[0,9,5]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if i!=j and j!=k and k!=i:
#                 print(a[i],a[j],a[k])
#             k+=1
#         j+=1
#     i+=1
 

# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# while i<len(a):
#     j=1
#     while j<len(b)+1:
#         print(a[i],b[-j])
#         j=j+1
#         i=i+1
 
# a=[1,"f",2,"b",3,4,"h","j",6,9,0,"k"]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#         i=i+1
# print(b)
# print(b)


# a=int(input("enter the number : "))
# i=0
# while i<=1:
#     if a%5==0:
#         print("yes")
#     else:
#         i=a%10
#         a//=10
#         if a%5==0:
#             print("yes")
#         else:
#             print("no")
#     i=i+1




# num=int(input("enter the number"))
# a=num%10
# num//=10
# b=num%10
# num//=10
# c=num%10 
# num//=10
# d=num%10
# num//=10
# if d%10:
#     print(a,b,c,d,num)
# else:
#     print("error")


# l=[1,2,3,4,2,4,6,2,1]
# l=(set(l))
# print(list(l))


# a=["n","a","v","g","u","r","u","k","u","l"]
# i=0
# sum=''
# while i<len(a):
#     sum+=a[i]
#     i+=1
# print(sum)


# a="Navgurukul"
# i=0
# s=[]
# while i<len(a):
#     s.append(a[i])
#     i+=1
# print(s)1