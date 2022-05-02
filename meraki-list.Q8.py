# # How to find all pairs in an array of integers whose sum is equal to the given number?
# Output:-
# [[11,19], [12,18],[13,17]]


n = [10, 11, 12, 13, 14, 17, 18, 19]
number = 30
list=[]
i=0
while i<len(n):
    j=0
    while j<len(n):
        a=n[i]
        b=n[j]
        if n[i]+n[j]==number:
            list.append([a,b])
        j=j+1
    i=i+1
print(list)

