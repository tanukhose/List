# import imp
# import requests
# import json
# from bs4 import BeautifulSoup

# url='https://www.imdb.com/title/tt9263550/'
# page=requests.get(url)
# # print(page)
# soup=BeautifulSoup(page.content,'html.parser')
# print(soup)

# a=[1,3,7,8,3,2,5,1]
# b=[]
# i=0
# c=0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i==j:
#             c+=1
    

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


