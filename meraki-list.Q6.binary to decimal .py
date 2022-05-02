#In this program, if we are given any number in binary form, then we will learn to convert 
# that number in decimal form.



bin= [1,1,1]
l=len(bin)
sum=0
a=0
i=0
while i<l:
    sum+=bin[i]*(2**a)
    i=i+1
    a=a+1
print(sum)


# a=(1)*2**7+(0)*2**6+(0)*2**5+(1)*2**4+(1)*2**3+(0)*2**2+(1)*2**1+(1)*2**0     
# print(a)                  

# a=int(input("enter the number"))
# l=len(str(a))
# l=int(l)
# s=0
# i=0
# while i<l:
#     s+=a*i
#     s*=i
#     print(s)
#     i=i+1
