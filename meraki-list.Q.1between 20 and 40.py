#write a code,that counts the number between 20 and 40 amd then print its count. 


number=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(number):
    a=number[i]
    if a>20 and a<40:
        count=count+1
        print(a)
    i=i+1

