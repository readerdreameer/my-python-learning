# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:43:04 2024

@author: azizb
"""

student = {
    'name':'abdulaziz',
    'surname':'sodikov',
    'university':'chonnam national university',
    'major':'global business'
    }
print(student.items())
for key,value in student.items():
    print(f"Key is {key}")
    print(f"value is {value}")
gadgets = {
    'mom':'A 50',
    'dad':'Z flip 2',
    'friend':'Iphone 14 +'} 
for key,value in gadgets.items():
    print(f"My {key}'s phone is {value}")
print(gadgets.values())
print('Gatget users:')
mahsulotlar = {
    "olma":10000,
    "banan":11000,
    "uzum":5000}   
bozorlik = ["olma",'banan','nok']
for mahsulot in mahsulotlar :
 for narsa in bozorlik:
    if narsa not in mahsulotlar:
        print(f"Iltimos do'koningizga {narsa} ham olib keling )")
    
if mahsulot in bozorlik:
 print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm ekan")
for key in gadgets.keys(): 
    print(key.title())
mahsulotlar ={
    'olma' : 10000,
    'nok' : 15000,
    'banan':20000}
print("Do'kinimizdagi mahsulotlar : ")
for mahsulot in sorted (mahsulotlar) :
    print(mahsulot.upper())
telefonlar = {
    'abdulaziz':'Iphone 14 +',
    'abror':'Iphone 13 pro',
    'yaxyo oka':'Iphone 15 pro',
    'javlon oka':'Iphone 15 pro',
    'mustafo':'Iphone 13 pro'}
print(telefonlar.values())
print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi !")
for tel in telefonlar.values():
 print(tel)    
print("Foydalanuvchilar quyidagi telefonlarni ishlatishar ekan !")
for tel in set(telefonlar.values()):
    print(tel)
python_words = {
    'for':'uchun',
    'else':'agar',
    'in':'ichida',
    'append':'qo\'shmoq',
    'remove':'olib tashlamoq',
    'del':'o\'chirib tashlamoq',
    'tuple':'o\'zgarmas ro\'yxat',
    'integer':'butun son',
    'float':"o'nlik son",
    'list':"ro'yxat"}
for key,value in sorted(python_words.items()):
    print(f"{key} - {value}")
print(python_words.items())
my_phones = {
    '1-telefonim':"6300",
    "2-telefonim":"galaxy 2",
    "3-telefonim":"iphone 5 s",
    "4-telefonim":"iphone 6 s",
    "hozirgi telefonim":"iphone 14 +"}
for tel,telefonlar in my_phones.items():
    print(f"Mening {tel} {telefonlar}")
countries = {
    'Uzbekistan':"Tashket",
    "Saudi Arabia":"Mecca",
    "United Arab Emirates":"Abu dhabi",
    'United States':"Washington",
    "Australia":"Canberra"}
print(sorted(countries.keys()))
print(sorted(countries.values()))
for key,value in countries.items():
    print(f"{key} - {value}")
davlat = input("Davlat nomini kiriting !\n - ")
capital = countries.get(davlat)
if capital==None:
    print("Bu davlat haqida malumot topilmadi")
else:
    print(f"{davlat}ning poytaxti {capital}")
menu = {
        'osh':10000,
        'manti':9000,
        'somsa':3000,
        "non kabob":8000,
        "sho'rva":10000,
        'achchiq go\'sht':13000,
        'xonim':9000,
        "ko'za sho'rva":8000,
        'shashlik':5000,
        "lag'mon":11000}  
print("3 hil taom tanglang !")
buyurtmalar=[]
for n in range(1,4):
 buyurtmalar.append(input(f"{n} - taomni kiriting"))
for buyurtma in buyurtmalar:
    if buyurtma in menu :
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Bizda {buyurtma} mavjud emas (")















  
    
    
    
    
    
    
    
    
    



































               
    
               