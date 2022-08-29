"""
1-Kullanıcı Girişi

2-Randevu alınmak istenen poliklik seçimi

3-Seçilen pole göre doktor seçimi

4-Randevu oluşturuldu yazısı ve sıra numarası paylaşımı

"""

ad = {'Ulaş':'Yurt','Begüm':'Çalıkoğlu Yurt'}
def kayit(gelen_ad,gelen_soyad):
	ad[gelen_ad] = gelen_soyad
	print((""""Adınız {} Soyadınız {} olarak kayıt oldunuz.

		""").format(gelen_ad,gelen_soyad))

	sor = input("Giriş yapmak istermisiniz? y/n >>>")
	if sor=='y':
		giris_kontrol(gelen_ad,gelen_soyad)
	else:
		exit()
def giris_kontrol(gelenad,gelensoyad):
	s_d = False
	for i in ad:
		ad_g = i
		soyad_g = ad[i]
		if gelensoyad==soyad_g and gelenad==ad_g:
			print(("""
				Giriş başarılı oturum açıldı
				Hoşgeldiniz {} {} 
                Lütfen Randevu Almak İstediğiniz Polikliniği Seçiniz
				""").format(ad_g,soyad_g))
			s_d= True		
	if s_d==False:
		print("""Hesap bulunamadı,Kayıt olmak istermisiniz?
			y/n
			""")
		sor = input(">>>")
		if sor == 'y':
			ad_Sor = input("""
				İsim:
			 """)
			soyad_Sor = input("""
				Soyad:
			 """)
			kayit(ad_Sor,soyad_Sor)
		else:
			print("Çıkılıyor")
			exit()

	
def kullanici():
	ad = input('Adınız >>>')
	soyad = input('Soyadınız >>>')
	giris_kontrol(ad,soyad)

kullanici()

import random

dis_hekimleri = ["Cemal SÜREYYA","Ahmet Hamdi TANPINAR"]
göz_hekimleri = ["Şinasi","Cahit Sıtkı TARANCI"]
dahiliye_hekimleri = ["Elif ŞAFAK", "Edip CANSEVER"]
kalp_hekimleri = ["Nazım HİKMET", "Turgut UYAR"]
kbb_hekimleri = ["Nilgün MARMARA", "Orhan Veli KANIK"]
nöroloji_hekimleri = ["Ahmed ARİF", "Özdemir ASAF"]
randevu_saati = ["09.00","09.30","10.00","10.30","11.00","11.30","13.00","13.30","14.00","14.30","15.00","15.30"]
sıra_no = random.randint(1,1001)

from random import choice

degerler = ["Diş","Göz","Dahiliye","Kalp","KBB","Nöroloji"]

while True:
    
    print("Diş, Göz, Dahiliye, Kalp, KBB, Nöroloji")
    
    kullanıcı = str(input("Poliklin İsmini Yazınız => "))
    break

if kullanıcı == "Diş":
    print(dis_hekimleri)
    kullanıcı_hekim= (input("Hekim İsmini Tam Yazınız =>"))
    
    if kullanıcı == "Cemal SÜREYYA":
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız"))
        
    
    else:
        kullanıcı_hekim == "Ahmet Hamdi TANPINAR"
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız =>"))

elif kullanıcı == "Göz":
    print(göz_hekimleri)
    kullanıcı_hekim= (input("Hekim İsmini Tam Yazınız =>"))
    
    if kullanıcı == "Şinasi":
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız"))
        
    
    else:
        kullanıcı_hekim == "Cahit Sıtkı TARANCI"
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız =>"))


elif kullanıcı == "Dahiliye":
    print(dahiliye_hekimleri)
    kullanıcı_hekim= (input("Hekim İsmini Tam Yazınız =>"))
    
    if kullanıcı == "Elif ŞAFAK":
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız"))
        
    
    else:
        kullanıcı_hekim == "Edip CANSEVER"
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız =>"))

elif kullanıcı == "Kalp":
    print(kalp_hekimleri)
    kullanıcı_hekim= (input("Hekim İsmini Tam Yazınız =>"))
    
    if kullanıcı == "Nazım HİKMET":
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız"))
        
    
    else:
        kullanıcı_hekim == "Turgut UYAR"
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız =>"))

elif kullanıcı == "KBB":
    print(kbb_hekimleri)
    kullanıcı_hekim= (input("Hekim İsmini Tam Yazınız =>"))
    
    if kullanıcı == "Nilgün MARMARA":
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız"))
        
    
    else:
        kullanıcı_hekim == "Orhan Veli KANIK"
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız =>"))


elif kullanıcı == "Nöroloji":
    print(nöroloji_hekimleri)
    kullanıcı_hekim= (input("Hekim İsmini Tam Yazınız =>"))
    
    if kullanıcı == "Ahmed Arif":
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız"))
        
    
    else:
        kullanıcı_hekim == "Özdemir ASAF"
        print(randevu_saati)
        kullanıcı_randevu=(input("Randevu Saatini Tam Yazınız =>"))





print("\nRandevunuz Oluşturulmuştur")
print("Hekiminiz : ", kullanıcı_hekim)
print("Randevu Saatiniz : ", kullanıcı_randevu) 
print("Sıra Numaranız : " , sıra_no )
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      