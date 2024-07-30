# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:13:40 2024

@author: azizb
"""

name = input("Ismingiz nma ?\n~")
question = f"Assalomu aleykum {name.title()}. Yoshingiz nechchida?\n~"
age = input(question)
age = int(age)
height = input("Bo'yingiz necha santimetr?\n~")
height = float(height)
print(f"Foydalanuvchi - {name.title()}\n"
      f"Yoshi - {age}\n"
      f"Bo'yi - {height}")
son = 1
while son<5:
    print(son,end=' ')
    son = son+1
print("Kiritilgan sonni kvadratini qaytaruvchi dastur !")
savol = ("Istalgan sonni kiriting ")
savol +=("Dasturni to'xtatish uchun 'exit' so'zini kiriting !\n~ ")
qiymat = ()
while qiymat!="exit":
    qiymat=(input(savol))
    if qiymat!="exit":
        print(float(qiymat)**2)
else:
    print("Dastur toxtadi!")
print("Kiritilgan dasturni kvadratini qaytaruvchi dastur !")
savol = ("Istalgan sonni kiriting. Yoki agar dasturni to'xtatmoqchi bo'lsangiz ")
savol+=("'EXIT' so'zini kiriting\n~")
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == "exit":
        ishora = False
        print("Dastur to'xtadi")
    else:
        print(float(qiymat)**2)
while True:
  qiymat = input(savol)
  if qiymat == "exit":
   print("Dastur to'xtadi !")
   break
  else:
    print(float(qiymat)**2)
sonlar = list(range(1,11)) 
for son in sonlar:
 if son ==5:
  continue
 print(f"{son} ning kvadrati {son**2} ga teng")
son = 0
while son<10:
    son+=1
    if son%2!=0:
        continue
    print(son)
savol = ("Yaxshi ko'rgan kitoblaringiznin nomini kiriting\n")
savol+=("Barcha kitoblaringizning nomini kiritib bo'lgach STOP so'zini kiriting")
while True:
    kitob = input(savol)
    if kitob == "stop":
        break
print("Raxmat")      
print("Xayvonot olamiga hush kelibsiz ")
print("Kirish uchun yoshingizni kiriting! Agar hohlamasangiz Exit yo Quit deb yozing")
yosh=("Iltimos , yoshingizni kiriting")
while True:
 qiymat = input(yosh)
 if qiymat =="exit"or qiymat=="quit":
      break
 savol = int(qiymat)
 if savol<=7:
     narx = 2000
 elif savol<=18:
     narx = 5000
 elif savol<=65:
     narx = 10000
 else:
     narx = 0
 if narx == 0:
     print("Sizga kirish bepul")
 else:
     print(f"Sizga kirish {narx} so'm")
        
          






































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









