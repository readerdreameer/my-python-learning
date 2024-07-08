# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 22:35:24 2024

@author: azizb
"""

car = {"model" : "Cobalt" , "raqam" : "102"}
print(car["raqam"])
talaba = {"ism":"abdulaziz","yosh":"20","universtitet":"Chonnam national university"}
print(f"Talabaning ismi {talaba['ism'].title()}\
 #va u {talaba['yosh']} yoshda\
 #qahramonimiznig ta'lim olayotga universtiteti {talaba['universtitet']}")
print({"Talabamizning ismi" " " + talaba['ism'].title()})
#talaba["t_yil"] = 2004
#talaba['millati'] = "o'zbek" 
#talaba_1 = {}
#talaba_1['ism'] = 'abdulloh'
#talaba_1['familiya'] = 'raximberdiyev'
#talaba_1['millati'] = 'o\'zbek'
#print(f"Talabamizning millati - {talaba_1['millati'].upper()}\
 #, ismi - {talaba_1['ism'].title()}\
 #familyasi - {talaba_1['familiya'].title()}")
#talaba['yosh'] = 21
#del talaba['universtitet']
#telefonlar = {
   # 'ali' : 'samsung',
  #  'abror' : 'iphone',
 #   'abdulaziz' : 'iphone 14 +'
#    }
#kitoblar = {
   #'1-yil' : 'Steve Jobs',
  #  '2-yil' : 'Tavsiri Xilol',
 #   '3-yil' : 'Baxtiyor oila'
 #   }
#kitob = kitoblar.get('4 - yil', "bu yil hali kelmagan !")
#ota = {"t_yil":"1975","ism":"sardorbek","kasb":"tadbirkor"}
#print(f"Mening otamning ismi {ota['ism'].title()},\
 #{ota ['t_yil']} yil da tavallud topganlar,\
 #va kasblari {ota['kasb']}.")
#oilam = {
 #   "otam":"manti",
  #  "onam":"mastava",
   # "ukam":"osh",
    #"buvijonim":"sho'rva",
    #"akam":"manti",
 }
print(f" Otamning sevimli ovqatlari {oilam['otam']}\n \
Onamning sevimli ovqatlari {oilam['onam']}\n \
Buvijonimning sevimli ovqatlari {oilam['buvijonim']}\n \
Akamning sevimli ovqatlari {oilam['akam']}\n \
Ukamning sevimli ovqati {oilam['ukam']}")
python = {
    "integer":'butun son',
    'float':'o\'nlik son',
    'tuple':'o\'zgarmas matn',
    'max':'umumiy yig\'indini topish',
    'min':'eng kamini topish',
    "type":'saqlangan malumotni turini tekshirish',
    'for':'uchun',
    'else':'agarda',
    'keywords':'kalit so\'zlar'
    }
#print({python["min"]})
#print({python['else']})
kalit = input("Kalit so'zni kiritng - ").lower()
#print(python.get(kalit , "Bunday so'z bizda mavjud emas !"))
tarjima = python.get(kalit)
if tarjima == None:
    print(kalit,"degan so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")













 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
