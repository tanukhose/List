# Write a Python program to scramble the letters of string in a given list. 
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']



a=['Python' 'list' 'exercises' 'practice' 'solution']
i=0
while i<len(a):
    j=1
    while j<len(a[i])+1:
        print(a[i][-j],end=" ")
        j=j+1
    i=i+1



# /a=['Python', 'list', 'exercises', 'practice', 'solution']
# i=1
# b=[]
# while i<len(a)+1:
#     s=a[-i]
#     b.append(s)
#     i+=1
# print(b)

