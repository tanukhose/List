# write a code that checks whether a list is a palindrome or not.


name=['n','i','t','i','n']
i=0
b=''
a=''
while i<len(name):
    b+=name[i]
    i=i+1
i=1
while i<=len(name):
    a+=name[-i]
    i=i+1
print(a)    
if b==a:
    print(a,"palindrome")
else:
    print("not palindrome")


# name=['t','a','n','u','j','a']
# i=0
# b=''
# a=''
# while i<len(name):
#     b+=name[i]
#     i=i+1
# print(b)
# i=1
# while i<=len(name):
#     a+=name[-i]
#     i=i+1
# print(a)    
# if b==a:
#     print(a,"palindrome")
# else:
#     print("not palindrome")












