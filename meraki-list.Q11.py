#Write a code that works for any list, it shows the two averages as the output.
#  One is the average of even numbers and the other is the average of odd numbers
#  from the given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]    
i=0
count=0
count1=0
sum=0
sum1=0
while i<len(elements):
    num=elements[i]
    if  num%2==0:
        count+=1
        sum+=elements[i]
    else:
        count1+=1
        sum1+=elements[i]
    i+=1
print(sum,count,'even','average',sum/count)
print(sum1,count1,'odd','average',sum1/count1)