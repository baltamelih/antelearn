#Kalıpların metin dosyasından veri tabanına aktarılma işlemi
""" hepsini küçük harf, noktalama işaretleri silme YAPILACAK!!!!! """
import DbHelper

db = DbHelper.Database()
wordList=[]
kelime_listesi=[]
def patterns_cre():
    with open("patterns.txt","r",encoding='utf-8') as f:
        for j in f:
            wordList.append(j.split("\t"))
    for i in range (len(wordList)):
        print(i)
        for k in range (3):
            print(k)
            if (k % 3 == 0):
                patterns = wordList[i][k]
                print(patterns)
            elif (k % 3 == 1):
                translation = wordList[i][k]
                print(translation)
            elif (k % 3 == 2):
                definition = wordList[i][k]
                print(definition)
        db.patterns_split(patterns,translation,definition)

"""
BAKILACAK BU KODA

def counter_patterns():
    count = 0
    searched_word = db.patterns_counter(1)
    with open("howimeetyourmothers1e1.txt","r") as f:
        for i in f:
            word = i.split()
            kelime_listesi.append(word)
    for l in range (2):
        for k in range (len(kelime_listesi)):
            for j in range(len(kelime_listesi[k])):
                if(kelime_listesi[k][j]==db.patterns_counter(l)):
                    count=count+1
                print(kelime_listesi[k][j])
        print(db.patterns_counter(l))
        print(count)
        count=0
counter_patterns()"""


