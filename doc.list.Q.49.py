# Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15
# Last occurrence of k in the said list:
# 14
# Last occurrence of w in the said list:
# 12


a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
i=0
while i<len(a):
    if a[i]=="f":
        a1=i
    if a[i]=="c":
        a2=i
    if a[i]=="k":
        a3=i
    if a[i]=="w":
        a4=i
    i+=1
print("f :-",a1)
print("c :-",a2)
print("k :-",a3)
print("w :-",a4)