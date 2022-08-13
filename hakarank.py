

a=[['harry',37.21],['berry',37.21],['tina',37],['akriti',41],['harsh',39]]
i=0
b=0
l=[]
while i<len(a):
    if a[i][1] not in l:
        l.append(a[i][1])
    else:
        b=a[i][1]
    i+=1
for i in a:
    if b in i:
        print(i[0])


