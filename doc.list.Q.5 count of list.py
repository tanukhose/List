# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 
#because [1,2,5,8,4] are unique values.


input_list = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
a=[]
count=0
while i<len(input_list):
    if input_list[i] not in a:
        a.append(input_list[i])
        count+=1
    i=i+1
print(a)   
print("count =",count)