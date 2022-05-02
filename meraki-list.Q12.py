#Write a program that tells in the above list that how many people are there in the above
#  list who are :
# 1 - `Crorepati`
# 2 - `Lakhpati`
# 3 - `Dilwale`


kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
count=0
count1=0
count2=0
# a=[]
# b=[]
# c=[]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>10000000 :
        # a.append(kitna_paisa_hai)
        count+=1
    elif kitna_paisa_hai[i]>100000:
        # b.append(kitna_paisa_hai)
        count1+=1
    else:
        count2+=1
        # c.append(kitna_paisa_hai)
    i=i+1
print(count,'Crorepati')
print(count1,'Lakhpati')
print(count2,'Dilwale')