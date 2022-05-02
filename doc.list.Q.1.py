#terate over both the values in a list and their indices
#grocery_list = ['flour','cheese','carrots']
#Output: 
#=> 0: flour
#=> 1: cheese
#=> 2: carrots

gro_list='flour','cheese','carrots'
i=0
while i<len(gro_list):
    print(i,':',gro_list[i])
    i=i+1
