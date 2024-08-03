# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:21:52 2024

@author: azizb
"""
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu aleykum")
def salom_ber(ism):
    """Foydalanuvchidan ismini so'rab unga salom beruvchi funksiya"""
    print(f"Assalomu aleykum hurmatli {ism.title()}")
def malumot_ol(ism,familiya):
    """Foydalanuvchidan malumot qabul qiladigan funksiya"""
    print(f"Foydalanuvchining ismi : {ism.title()}\n"
          f"Foydalanuvchining familiyasi : {familiya.title()}")
def yoshini_hissobla(ism,t_yil):
 """Yoshni hissoblaydigan dastur"""
 print(f"Foydalanuvchining ismi : {ism.title()}\n"
       f"Foydalanuvchining yoshi : {2024-t_yil}")    
def hissobla(t_yil ,joriy_yil=2024):
    """Foydalanuvchining yoshini hissloblovchi dastur"""
    print(f"Foydalanuvchi {joriy_yil-t_yil} yoshda")
def hissobla(ism,yosh):
    """Foydalanuvchining yoshini hissoblaydigan dastur"""
    print(f"Foydalanuvchining ismi {ism.title()}\n"
          f"Foydalanuvchining yoshi : {2024-yosh}")
age = int (input("Yoshingizni kiritng : "))
hissobla("abdulaziz,",age)
def toq_juft(son):
    """Sonning toq yoki juftligini hissoblovchi dastur"""
    if son%2:
        print(F"{son} toq son")
    else:
        print(f"{son} juft son")
def aniqla(son1,son2):
    """Sonlarning katta yoki kichikligini aniqlovchi dastur"""
    if son1>son2:
        print(f"{son1}>{son2}")
    elif son1<son2:
        print(f"{son1}<{son2}")
    else:
        print(f"{son1}={son2}")
def daraja(x,y=2):
    """Darajani aniqlovchi dastur"""
    print(f"{x} ning {y}-darajasi {x**2} ga teng")
def bol(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")




























