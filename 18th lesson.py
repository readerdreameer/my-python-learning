# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:04:54 2024

@author: azizb
"""

ismlar = []
print("Do'stlaringizning ro'yxatini tuzamiz!")
n=1
while True:
    savol = f"{n} - do'stingizning ismini kiriting"
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana do'stingizning ismini qo'shasizmi? ha/yo'q")
    if javob != "ha":
        for ism in ismlar:
         print(ism.title())
        break 
    else:
     n+=1
print("Do'stlaringiz ismi va yoshini saqlaymiz")
friends = {}
ishora = True 
while ishora:
    ism = input("Dostingizning ismini kiriting")
    yosh = input("Do'stingizning yoshini kiriting")
    friends[ism] = int(yosh)
    savol = input("Yana do'stingizni qo'shasizmi? ha/yo'q")
    if savol !="ha":
        ishora = False
for ism,yosh in friends.items():
    print(f"{ism.title()} {yosh} yoshda")
cars = ["nexia","cobalt","malibu","malibu"]
while "malibu" in cars:
    cars.remove("malibu")
    print(cars)
talabalar = ["arslon","temur","abror"]
baholangan_talabalar = {}
while talabalar:
 talaba = talabalar.pop()
 baho =input( f"{talaba.title()}ning yakuniy bahosini qo'ying")
 print(f"{talaba.title()} baholandi")
 baholangan_talabalar[talaba] = baho   
for ism,baho in baholangan_talabalar.items():
    print(f"{ism} - {baho}")
savat = []
while True:
    mahsulot = input("Keraklik narsani nomini kiriting\n~")
    savat.append(mahsulot)
    savol = input("Yana narsa qo'shasizmi? ha/yo'q")
    if savol!="ha":
        break
for narsa in savat :
 print(narsa)
print("Haridingizdan mamnunmiz:)")
ebozor = {}
print("Mahsulot va uning narxini saqlab olamiz")
while True:
    mahsulot = input("Mahsulot nomini kiriting")
    narx = input("Mahsulotning narxini kiritng")
    print(f"{mahsulot} saqlandi")
    ebozor[mahsulot] = narx
    stop = input("Barcha mahsulotlarni saqlab bo'lgach stop deb yozing! Davom etish uchun hop deb yozing")
    if stop == "stop":
        break
for nom,qiymat in ebozor.items():
    print(f"{nom} - {qiymat} so'm")
buyurtmalar = ["suv","non","choy"]
mahsulotlar = {
    "non":3000,
    "choy":1000,
    "nok":5000}
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
      narx = mahsulotlar[buyurtma]
      print(f"{buyurtma} - {narx} so'm")




























