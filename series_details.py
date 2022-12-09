import DbHelper
db = DbHelper.Database()

def series_save(): # admin dizi ekleme işlemi yapıyor eğer varsa eklemiyor yoksa ekliyor
    series_name = input("Dizi/Film adını giriniz: ")
    if(db.series_control_db(series_name) != False):
        print("Database'e daha önce kayıt edilmiş dizi veya film: ",series_name)
    else:
        db.save_a_series_db(series_name)

def episode_save():# admin girişi için episode database'ine kayıt işlemleri gerçekleşiyor (içeride if else ile dizi daha önce kayıt edilmiş mi kontrol ediyor)
    series_name = input("Dizi adı: ")
    result= db.series_control_db(series_name)
    if result==False:
        db.save_a_series_db(series_name)
        print("Dizi daha önce bulunamadığı için tekrar kayıt yapıldı.")
    season_no = input("Sezon numarası: ")
    season_no_result = db.season_control_db(series_name,season_no)
    if season_no_result == False:
        db.save_a_season_db(series_name,season_no)
        print("Girdiğiniz sezon daha önce kayıt edilmediği için sezon eklemesi yapıldı")
    series_id = int(''.join(map(str,db.series_to_episode(series_name))))
    episode_name = input("Bölüm adı: ")
    episode_no = input("Bölüm numarası:  ")
    episode_filepath = series_name + "s" + season_no + "e" + episode_no + ".txt"
    db.save_a_episode_db(series_id,season_no,episode_name,episode_no,episode_filepath)




