# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:50:03 2024

@author: azizb
"""
malibus = []
for n in range(1,11):
    new_cars = {
        "model":"malibu",
        "rang":None,
        "yil":2020,
        "narx":None,
        "km":0,
        "karobka":"avto"
        }
    malibus.append(new_cars)
for malibu in malibus[:3]:
    malibu['rang']="qizil"
for malibu in malibus[3:6]:
    malibu['rang']="qora"
for malibu in malibus[6:11]:
    malibu["karobka"]="mexanika"
    malibu['rang']="qora"

for malibu in malibus:
    if malibu["karobka"]=="avto":
        malibu["narx"]=40000
    else:
        malibu["narx"]=30000
dasturchilar = {
    "abdulaziz":['python'],
    "muhammad diyor":['python',' c++'],
    "diyorbek":["python"," c#"],}
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} shu tillarda ishlay oladi " , end = '')
    for til in tillar:
        print(til.upper(),end = '')
hamkasblar = {
    "ali":{"familia":"nuriddinov",
           "tyil":2000,
           "malumot":"oliy",
           "tillar":["python","c++"]
           },
    "abdulaziz":{"familia":"sodikov",
                 "tyil":2004,
                 "malumot":"oliy",      
                 "tillar":["python"]
                 },
    "bekzod":{"familia":"shukrulloyev",
              "tyil":1998,
              "malumot":"oliy",
              "tillar":["python","c++","html"]}
    }
for ism,info in hamkasblar.items():
    print(f"{ism.title()} {info['familia'].title()} , {info['tyil']} yilda tug'ilgan. "
          f"Malumoti {info['malumot']}."
          "Qiyudagi tillarni biladi:")
    for til in info['tillar']:
        print(til.upper())

celebrity = {
    "ism":"Muhammad ibn Musa al-Xorazmiy",
    "kasb":["matematik","geograf","astranom"],
    "tyil":780,
    "asoschisi":"algoritm",
    "asar":"Aljabir"}    
builder = {
    "ism":"Murod Nazarov",
    "kasb":"quruvchi",
    "tyil":1980,
    "asoschisi":"Murad buildings",
    "asar":"Xayot"}
shayx = {
    "ism":"Muhammad Yusuf",
    "kasb":"olim",
    "tyil":1952,
    "asoschisi":"Tavsiri Xilol",
    "asar":"Iymon"}
motivator = {
    "ism":"Andrew Tate",
    "kasb":["kickboxer","influencer"],
    "tyil":1986,
    "asoschisi":"The real world",
    "asar":"Tate's life"}
insonlar = [celebrity,builder,shayx,motivator]
for inson in insonlar:
    ism = inson['ism']
    kasb = inson['kasb']
    tyil = inson['tyil']
    asoschisi = inson["asoschisi"]
    asar = inson["asar"]
    print(f"Ism - {ism}\n"
          f"Kasb - {kasb}\n"
          f"Tavallud topgan sanalari - {tyil} yil\n"
          f"Asoschisi - {asoschisi}\n"
          f"Asari - {asar}")
kinolar = {
    "onam":["kelinlar qo'zg'oloni"],
    "otam":["gugurt izlab"],
    "abdulaziz":["troya"]}
for ism,kinolar in kinolar.items():
    if ism.title()=="Abdulaziz":
        print(f"{kinolar}ni {ism.title()} sevib tomosha qiladi")
    else:
        print(f"{kinolar}ni {ism.title()} sevib tomosha qiladilar")
davlatlar = {
    "o'zbekiston":{ "mustaqil_bolgan_kun":1991,
        "qita":"osiyo",
        "aholi_soni":"40 mln"},
    "uae":{"mustaqil_bolgan_kun":1971,
        "qita":"asia",
        "aholi_soni":"10 mln"},
    "saudi arabia":{"mustaqil_bolgan_kun":1932,
        "qita":"osiyo",
        "aholi_soni":"34 mln"}
    }
davlat= input("Davlat nomini kiriting - ").lower()
if davlat in davlatlar:
  info = davlatlar[davlat]
  print(f"{davlat.upper()} mustaqil bo'lgan yil : {info['mustaqil_bolgan_kun']}\n"
        f"Qit'a : {info['qita']}\n"
        f"Aholi soni {info['aholi_soni']}") 
else:
    print(f"{davlat.upper()} haqida malumot topilmadi")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

























