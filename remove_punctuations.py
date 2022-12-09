import os.path
import string
from textblob import TextBlob
from num2words import num2words

import word_insert


class Remove_punctuation():
    dizi = []
    def __init__(self,file_path):
        self.filepath = file_path
        self.remove_punctuations_text(self.filepath)
    def count_for_words(self,filepath): #Burada kelimelerin kaçar adet olduğunu saydıran fonksiyon
        text = open(filepath,"r+")
        d = dict()
        for line in text:
            line = line.replace("  "," ")
            line = line.strip()
            line = line.lower()
            print(line)
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word] = d[word] + 1
                else:
                        d[word] = 1

        for key in list(d.keys()):
            if key!=" ":
                Remove_punctuation.save_a_words(self,key,d[key])
        text.close()


    def save_a_words(self,word,count):
        translation = Remove_punctuation.translate(self,word)
        self.empty_file_add(str(word),str(translation),str(count))

    def empty_file_add(self,word,translation,count):
        empty_filepath = "empty_file.txt"
        empty_file = open(empty_filepath,"a+",encoding='utf-8')
        line = word+" "+count+" "+translation+"\n"
        empty_file.write(line)
        return empty_filepath



    def translate(self,word):
        if word == "i":
            word = word.upper()
        if word.isnumeric():
            word = num2words(word)
        if word != "a":
            translate_word = TextBlob(word).translate(from_lang="en",to="tr")
            translate_word = translate_word.lower()
        else:
            return "bir"
        return translate_word


    def remove_punctuations_text(self,file_path): #Almış olduğu metin belgesindeki kelimeleri noktalama işaretlerinden ayırma ve her kelimeyi küçük harf yapma fonksiyonu
        if(os.path.exists(file_path)):
            print("The file exists")
            clean_text_list = []
            clean_text = "cleantext.txt"
            clean_file =open(clean_text,"w")
            with open (file_path,"r") as f:
                for j in f:
                    clean_text_list.append(j.split())
            for i in range (len(clean_text_list)):
                for k in range (len(clean_text_list[i])):

                    if(clean_text_list[i][k].translate(str.maketrans("","",string.punctuation))!=" "):
                        clean_file.write(clean_text_list[i][k].translate(str.maketrans("","",string.punctuation))+" ")

            clean_file.close()

            print("Created file: ",file_path)

            clean_file.close()
            Remove_punctuation.count_for_words(self,clean_text)
        else:
            print("The specified file does NOT exists")






