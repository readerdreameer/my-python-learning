# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:35:11 2024

@author: azizb
"""
def toliq_ism_yasa(ism,familiya,otasiningismi=''):
    """To'liq ism yasaydigan dastur"""
    if otasiningismi:
        toliq_ism=(f"{ism} {otasiningismi} {familiya}")
    else:
     toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba1 =  toliq_ism_yasa("Olim","Hakimov",)
talaba2 = toliq_ism_yasa("Abdulaziz","Sodikov","Sardorbek ug'li")
print(f"Yaxshi insonlar {talaba1} {talaba2}")
def make_car_info(kompaniya,model,rangi,karobka,yili,narxi=' '):
    avto = {'kompaniya':kompaniya,
            "model":model,
            "rangi":rangi,
            "karobka":karobka,
            "yili":yili,
            "narxi":narxi}
    return avto
avto1 = make_car_info("GM","Malibu","Oq","Avtomat","2024","20.000$")
avto2 = make_car_info("Mercedes","CLS","Qora","Avtomat","2024","50.000$")
avtolar = [avto1,avto2]
for avto in avtolar:
    if avto['narxi']:
        narxi=avto['narxi']
    else:
        narxi = "Noma'lum"
    print(f"Kompaniya - {avto['kompaniya']} \nModeli - {avto['model']}\nKarobka - {avto['karobka']}\nNarxi - {avto['narxi']}")
def oraliq(min,max):
 sonlar = []
 while min<max:
     sonlar.append(min)
     min+=1
 return sonlar
print(oraliq(0,11))  
print(oraliq(10,100))  
print("Saytimizdagi mashinalarning ro'yxati") 
avtolar = []
while True:
    print("\nQuyidagi malumotlarni kiriting",end=' ')
    kompaniya = input("Ishlab chiqaruvchi : ")
    model = input("Model : ")
    rangi = input("Rangi : ")
    karobka = input("Karobka : ")
    yili = input("Ishlab chiqarilgan yil : ")
    narxi = input("Narxi : ")
    avtolar.append(make_car_info(kompaniya,model,rangi,karobka,yili,narxi))
    savol = input("Yana mashina qoshasizmi? Ha/yo'q : ")
    if savol == "Yo'q":
        break
def info_maker(ism ,familiya ,t_yil ,tel_raqam=None):
    """Foydalanuvchining malumotlarini yig'uvchi dastur"""
    
    foydalanuvchi = {
        "ism":ism,
        "familiya":familiya,
        "t_yil":t_yil,
        "yoshi":2024 - t_yil,
        "tel_raqam":tel_raqam
    }
    return foydalanuvchi
print("Foydalanuvchi haqida malumotni kiriting : ")
foydalanuvchilar = []
while True:
    ism = input("Ismini kiriting : ")
    familiya = input("Familiyasini kiriting :")
    t_yil = input("Tug'ilgan yilini kiritng :")
    tel_raqam = input("Telefon raqamini kiriting :")
    foydalanuvchilar.append(info_maker(ism,familiya,t_yil,tel_raqam))
    savol = input("Yana foydalanuvchi qo'shasizmi ? ha/yo'q")
    if savol !="ha":
     break
    print("Foydalanuvchilar:")
    for foydalanuvchi in foydalanuvchilar:
       print(f"{foydalanuvchi['ism']} {foydalanuvchi[familiya]} {foydalanuvchi['tel_raqam']}")
















        
    
    
    
    
    









