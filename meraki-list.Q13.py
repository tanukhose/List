#Occurences - is made from the word occur which means that how many times a certain
# character or word appears.
# Output of the Sample List
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]



# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a","p"]
# count=0
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# a=[]
# b=[]
# c=[]
# d=[]
# e=[]
# f=[]
# i=0
# while i<len(char_list):
#     if char_list[i]=='a':
#         count+=1
#         a.append (char_list[i])
#     elif char_list[i]=='n':
#         count1+=1
#         b.append (char_list[i])
#     elif char_list[i]=='t':
#         count2+=1
#         c.append (char_list[i])
#     elif char_list[i]=='x':
#         count3+=1
#         d.append (char_list[i])
#     elif char_list[i]=='u':
#         count4+=1
#         e.append (char_list[i])
#     elif char_list[i]=='g':
#         count5+=1
#         f.append (char_list[i])

#     i=i+1
# print(["a",count])
# print(["n",count1])
# print(["t",count2])
# print(["x",count3])
# print(["u",count4])
# print(["g",count5])



list=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a","p"]
l=[]
for i in list:
    c=0
    for j in list:
        if i==j:
            c=c+1
    if i not in l:
        l.append(i)
        print([i,c])

