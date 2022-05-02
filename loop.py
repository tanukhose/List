#n=int(input("enter the number :"))
# i=1
# c=0
# while i<=n:
#     if n%i==0 :
#         c=c+1
#     i=i+1
# if c==2:
#     print("prime no")
# else:
#     print("not")






# n=int(input("enter the number :"))
# i=1
# c=0
# while i<=n:
#     if n%i==0 :
#         c=c+1
#     i=i+1
# if c==2:
#     print("prime no")
# else:
#     print("not")

# # n=int(input("enter the number =" ))
# i=0
# while n>i:
#     if n%1==0 and n%2!=0 and n%3!=0 :
#         print(n,"prime no")
#     else:
#         print(n,"not")
#     i=i+1

# n=int(input("enter the number"))
# i=n
# sum=0
# while  n>0:
#     sum=sum+(n%10)*(n%10)*(n%10)
#     n=n//10
# if i==sum:
#     print(i,"a")
# else:
#     print(i,"a no")


# n=int(input("enter the number"))
# i=0
# while n>=0:
#     b=n%100
#     c=b//10
#     if c==2:
#         print("yes")
#     else:
#         print("not")
    
# a="325659"
# s=0
# i=0
# while i<len(a):
#     s=s+int(a[i])
#     i+=1
# print(s)





# a=int(input("enter the number = "))
# i=1
# sum=0
# n=a 
# while i<a:
#     if a%i==0:
#         sum=sum+i
#     i=i+1
# if n==sum:
#     print(sum,"prefect")
# else:
#     print(sum,"not perfect number")

# i=1
# while i<=5:
#     j=5
#     while j>=i:
#         print("*",end = "")
#         j=j-1
#     print()
#     i=i+1


# i=1
# while i<=7:
#     n=1
#     while n<=i:
#         print("#",end=" ")
#         n=n+1
#     print()
#     i=i+1

# i=1
# while i<=7:
#     n="#"
#     print(n*i)
#     i=i+1




# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print( )
#     i=i+1
# i=1
# while i<=4:
#     b=1
#     while i<=5-i:
#         print("",end=" ")
#         b+=1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1
# #     # s=5
#     # while s>=1:
    #     r=1
    #     while r<s-5


# a=[1,[2,3],4,5]
# i=1
# s=0
# b=[]
# while i<len(a):
#         j=1
#         while j<len(a[i]):
#             s=a[i][j]+s
#             j+=1
#         b.append(s)
#         i=i=1
# print(b)

# a="325659"
# s=0
# i=0
# while i<len(a):
#     s=s+int(a[i])
#     i+=1
# print(s)



# i=0
# while i<10:
#     i=i+1
#     if i==5:
#      break
#     print(i)

# i=0
# j=11
# while i<10 and j>0:
#     i+=1
#     j-=1
#     print(i,j)


# i=65
# while i<=69:
#     j=65
#     while j<=i:
#         print(chr(j),end=" ")
#         j=j+1
#     print()
#     i=i+1    

# num=12345
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

# a=int(input("enter the number : "))
# b=a%10
# if b%10:
#     print(b,"last digit")
# else:
    # ("nothing")

# a=int(input("enter the number"))
# b=a%10
# if b%3==0:
#     print(b,"last digit is divisible by 3")
# else:
#     print("error")
 
# a=int(input("enter the number : "))
# if a>18:
#     print(a-18,"greater")
# else:
#     print(18-a,"smaller")



# a="33245"
# sum=0
# i=0
# while i<len(a):
#     sum+=int(a[i])
#     i=i+1
# print(sum)


# date=int(input("enter the date : "))
# month=int(input("enter the month : "))
# year=int(input("enter the year : "))
# if month>=1 or month<=12:
#     print("month")
#     if date>=1 or date<=31:
#         print("date")
#         if year==month or date:
#             print(date+1,"/",month,"/",year)
#         else:
#             ("wrong")
#     else:
#         print("wrong date")
# else:
#     print("wrong month")


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


# i=1
# while i<=10:
#     j=1
#     while j<=100:
#         # print(j)
#         j=j+1
#     print(i,end="")
#     i=i+1

# i=1
# a=11
# b=21
# c=31
# d=41
# while i<=10 and a<=20 and b<=30 and c<=40 and d<=50:
#     print(i,a,b,c,d)
#     i+=1
#     a+=1 
#     b+=1
#     c+=1
#     d+=1





# i=1
# while i<=11:
#     we=int(input("enter the weghit"))
#     if we%5==0:
#         print("divisabile")
#     else:
#         print("wrong")
#     i+=1


# i=1
# while i<=4:
#     a=int(input("enter the number "))
#     if a==5:
#         print("right guess")
#     elif a>5:
#         print("grater")
#     elif a<5:
#         print("less")
#     else:
#         print("wrong")
#     i+=1

# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# while i<len(a):
#     a[i]=str(a[i])
#     b[i]=str(b[i])
#     n=a[i]+"-"+b[i]
#     i+=1
#     print(n)


# a=int(input("enrtr the number "))
# b=int(input("enter the number "))
# print(a//(1/b))



# b=int(input("enter the number"))
# i=1
# while i<=b:
#     j=1
#     while j<i:
#         print(j,end="")
#         j+=1
#     a=i
#     while a>0:
#         print(a,end="")
#         a-=1
#     print()
#     i+=1


# i=1
# while i<=10:
#     if i%2!=0:
#         j=1
#         while j<=i:
#             print(i,end="")
#             j+=1
#     print()
#     i+=1
    
# n=int(input("enter the number"))
# m=int(input("enter the number"))   
# i=1
# sum=0
# while i<=m:
#     sum=sum+n
#     i=i=1
# print(sum)


   
# a=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end="")
#         b+=1
#     j=1
#     while j<=a:
#         print("*",end="")
#         j+=1
#     a+=2
#     print()
#     i+=1


# a=int(input("enter the num :-"))
# i=0
# while i<a:
#     n=a%10
#     a//=10 
#     i+=1
#     print(n)
#     break



# a=int(input("enter the number "))
# if a>999 and a<9999:
#     print("yes")
# else:
#     print("no")

a=int(input("enter the number "))