""" Bu dosyada en çok kullanılan 1000 kelimenin database'e kaydedilme işlemi yapılmaktadır.
Gereksiz yere çalıştırmayınız!!!!!! """
import DbHelper
import mysql.connector
db = DbHelper.Database()
myList= []
myList2=[]
list =[]
with open("word.txt","r", encoding='utf-8') as f:
    myList.append(f.readline().split())
    for k in range (1):
        for kk in range (1000):
            list.append(myList[k][kk])
    print(list[1])

with open("translations.txt","r", encoding='utf-8') as ff:
    for ii in ff:
        myList2.append(ii)
for i in range (len(list)):
    db.most_used_words(list[i],myList2[i])