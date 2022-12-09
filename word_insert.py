import DbHelper
import remove_punctuations
import re
from textblob import TextBlob
db = DbHelper.Database()

class WordInsert():
    def __init__(self,filepath):
        self.filepath = filepath
        self.word_insert(self.filepath)


    def word_insert(self,filepath):
        id_dizi = []
        id_dizi.append(db.filepath_control(filepath))
        series_id = id_dizi[0][0]
        season_id = id_dizi[0][1]
        episode_id = id_dizi[0][2]
        remove_punctuations.Remove_punctuation(filepath)

        with open("empty_file.txt","r+",encoding='utf-8') as file:
            for i in file:
                word = i.split(maxsplit=2)
                db.save_a_word_db(series_id,season_id,episode_id,word[0],word[1],word[2])
            file.truncate(0)








