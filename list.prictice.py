# a=['a','b','c','d','e','f']
# b=['g','h','i','j','k','l']
# i=0
# n=[]
# while i<len(a):
#     s=''
#     s=a[i]+b[-i-1]
#     n.append(s)
#     i+=1
# print(n)



# a=[['T','A','N'],['U','J','A']]
# i=0
# s=''
# while i<len(a):
#     s1=''
#     j=0
#     while j<len(a[i]):
#         s1+=a[i][j]
#         j+=1
#     s+=s1 
#     i+=1
# print(s)



# a=[[1,2,3,],[4,8,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a[i]):
#         s+=a[i][j]
#         j+=1
#     b.append(s)
#     i+=1
# print(b)

# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# while i<len(a):
#     s=a[i],b[-i-1]
#     i+=1
#     print(s)



# a='megha'
# i=0
# b=[]
# j=5
# while i<len(a):
#     if a[i] not in b:
#         c=a[i]
#         b.append(c)
#         b.append(j)
#         j+=5
#     i+=1
# print(b)


# a=['megha','tanu','artu']
# i=1
# b=[]
# while i<=len(a):
#     s=a[-i]
#     b.append(s)
#     i+=1
# print(b)


# list=[1,0,2,0,3,0,4,0,5,0]
# i=0
# b=[]
# while i<len(list):
#     if list[i]==0:
#         pass
#     else:
#         b.append (list[i])
#     i+=1
# print(b)

# a=[6,1,3,5,6,1,3,5,4]
# b=[]
# i=0
# while i<len(a):
#     if (a[i]) not in b:
#         b.append(a[i])
#     i+=1
# print(b)

# a="dhanashree"
# i=0
# b=[]
# j=5
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         b.append(j)
#         j+=5
#     i+=1
# print(b)

# a=["34 SSS","40 DD","O 6 EE"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=""
#     while j<len(a[i]):
#         if a[i][j]>="0" and a[i][j]<="9":
#             sum+=a[i][j]
#         j=j+1
#     b.append(int(sum))
#     i=i+1
# print(b)


# a=[1,9,2,8,3,7,4,6,5,10]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j+=1
#     i+=1
# print(a)


# a=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     c=[]
#     while j<len(a[i]):
#         s=a[j][i]
#         c.append(s)
#         j+=1
#     b.append(c)  
#     i+=1
# print(b)


# a=[1,2,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     if i==1:
#         b.append(4)
#     elif i==3:
#         b.append(2)
#     i+=1
# print(b)


# a=[[1,2,3],[3,4,5]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j+=1
#     i+=1
# print(b)


# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# i=0
# b=[]
# k=1
# c=2
# while i<len(a):
#     s=[a[i],a[k],a[c]]
#     b.append(s)
#     k+=3
#     c+=3
#     i+=3
# print(b)


# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# i=0
# b=[]
# k=1
# c=2
# while i<len(a):
#     s=[a[i],a[k],a[c]]
#     b.append(s)
#     i+=3
#     k+=3
#     c+=3
# print(b)




# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# i=0
# c=[]
# while i<len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i+=1
# print(c)
# i=0
# while i<len(c):
#     j=0
#     while j<len(c)-1:
#         if c[i]<c[j]:
#             s=c[i]
#             c[i]=c[j]
#             c[j]=s
#         j+=1
#     i+=1
# print(c)

        

# a=[1,[3,5,[5,7,3,1],[9],9,0,[8],[0,3,7]]]
# b=[]
# for i in a:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 for s in j:
#                     b.append(s)
#             else:
#                 b.append(j)
#     else:
#         b.append(i)
# print(b)

# i=1
# l=[]
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         l.append(i)
#     i+=1
# print(l)



# a=[1,2,3,4,5]
# i=0
# b=[]
# while i<len(a):
#     s=[a[i], a[i]+1]
#     b.append(s)
#     i+=1
# print(b)
 




# a=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     s=0
#     while j<len(a[i]):
#         s+=a[i][j]
#         j+=1
#     b.append(s)

#     i=i+1
# print(b)

#reverce number if if else:
  

# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# i=0
# a=[]
# while i<len(string_list):
#     if string_list[i]not in a:
#         a.append(string_list[i])
#     i+=1
# print(a)

# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] in list2:
#         a.append(list1[i])
#     i+=1
# print(a)


# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] in list2:
#         a.append(list1[i])
#     i+=1
# print(a)



# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# i=0
# a=[]
# while i<len(list1):


# a=[1,0,4,8,0,4,9,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         c.append(a[i])
#     else:
#         b.append(a[i])
#     i+=1
# print(c,b)
    



# a=[1,2,3,[3,4,[8,9,]]]
# i=0
# sum=0
# while i<len(a):
#     # a[i]=str(a[i])
#     # s=0
#     j=0
#     while j<len(a[i]):
#         sum+=a[j][i]
#         j+=1
#     # sum+=s
#     i+=1
# print(sum)



# a=[1,2,3,[3,4,]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         sum=sum+a[i]
#     i+=1
# print(sum)


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
# i=0
# sum=0
# while i<len(b):
#     if type(b[i])==list:
#         j=0
#         while j<len(b[i]):
#             sum=sum+b[i][j]
#             j+=1
#     else:
#         sum=sum+b[i]
#     i+=1
# print(sum)