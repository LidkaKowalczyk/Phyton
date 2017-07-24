# -*- coding: utf-8 -*-

# komentarz jednowierszowy
'''zmienna1 = 5
zmienna2 = 5.3
'''
'''
poczatek komentarza blkowego
text = "to jest moj teks"
text2 = 'to jest inny tekst'
literki = "A"
literki = 'a'
koniec komentarza blokowego
'''
'''
witaj = "I'm Michal"


zmienna3 = 2 + 5
Zmienna3 = 'liczba'
nowa_zmienna = zmienna3 + 5

print(zmienna1)
print(zmienna1, zmienna2)
print(witaj)
print(Zmienna3, zmienna3)
print(nowa_zmienna)
print("Hi, " + witaj)
print("Hi, " + witaj + " I'm")


print("Przed zmiana", Zmienna3)
Zmienna3 = 3.14
print("po zmianie:", zmienna3)

del(zmienna1)'''
#print(zmienna1)

#P1
'''a = 1
b = 2.4
c = "w1"
print(a)
print(b)
print(c)

#P2
a = 2.1
b = "abc"
c = 0
print(a)
print(b)
print(c)
print(a,b,c)
'''


#P3
'''
Imie = "Marysia"
Nazwisko = "Kąkol"
Rok_urodzenia = "1980"
data_urodzenia = '1980-01-01'
Stanowisko = "Prezes"
Placa = 10000000
print(Imie,Nazwisko,Rok_urodzenia,data_urodzenia,Stanowisko,Placa)
'''

#P4
'''pi = 3.14
promien = int(input("Podaj liczbę"))
pole_powierzchni_kola = pi*promien*promien
'''
# podniesienie do kwadratu
# podstawa ** wykladnik
#print(pole_powierzchni_kola)
#pole_powierzchni_kola2 =pi*promien**2
#print(pole_powierzchni_kola2, pi*(promien**2))
# int() - rzutuje na integer
# input() - czyta wartość z klawiatury - strin!


#wprowadzanie zmiennych z klawiatury
"""
Imie = input("Podaj Imie:")
Nazwisko = input("Podaj Nazwisko:")
Rok_urodzenia = input("Podaj Rok_urodzenia:")
data_urodzenia = input("Podaj data_urodzenia:")
Stanowisko = input("Podaj Stanowisko:")
Placa = input("Podaj Placa:")
print(Imie,Nazwisko,Rok_urodzenia,data_urodzenia,Stanowisko,Placa)
"""
'''
# type() - zwraca typ wartosci zmiennej
#print(type(pole_powierzchni_kola))
print(type(21j))

dluga = 31474836479908079697
print(type(dluga))
#dluga2 = Long32
#print(type(dluga2))
#dzielenie, zaokraglanie
print(3/2, 3//2)
print(round(3.1444), round(1.5), round(3.7))
#int() - rzutuje w dół (zaokragla w dol
print(int(1.3),int(1.5),int(1.9))
'''
##P10
'''kwota_netto = float(input("Podaj kwotę netto: "))
vat = int(input("Podaj stawkę VAT (3%, 7%, 23%): "))
kwota_brutto = kwota_netto + (kwota_netto*(vat/100))
print("Twoja kowta netto przy stawce "+str(vat)+" vat wynosi: "+str(kwota_brutto)+" zł.")
'''

#P11
'''nazwa_p1 = "chleb"
nazwa_p2 = "mleko"
nazwa_p3 = "cukierki"

cena_p1= 1.99
cena_p2 = 4.15
cena_p3 = 15.99

zamowienie_p1 = int(input("Liczba chlebów: "))
zamowienie_p2 = int(input("Litry mleka: "))             
zamowienie_p3 = int(input("Waga cukierków (g): "))
suma = (cena_p1 * zamowienie_p1) + (cena_p2 * zamowienie_p2) + ((cena_p3/1000) * zamowienie_p3)

print("Twoje zamówienie")
print("================")
print("Ilość chlebów:", zamowienie_p1, "szt.")
print("Litry mleka: ", zamowienie_p2, "l")
print("Waga cukierków: ", zamowienie_p3, "g.")
print("================")
print("Do zapłaty")
print("================")
print(round(suma,2), "zł")
'''
'''
print((1+1j)+(12+20j))
print(0o11)
print(0x11)
a = 12 
b = 1+(-1j)
print(a*b)

#typy logiczne
log1 = True
print(type(log1))

b = False
print(bool(""), bool(0), bool("Ala"))
'''
a = """autor:
data:
wersja:
"""
'''
print(a)

#\n - znak przejścia do nowej lini
b = "autor:\ndata:\nwersja:"
print(b)

# kilka razy wyświetla
txt = "napis "
print(txt*3)
'''

"""imie = input("Podaj imie: ")
imie_1 = imie + ", "
imie_2 = imie + ". "
n = int(input("Podaj ile razy mam wpisać Twoje imię: "))

print((imie_1 * (n-1)) + imie_2)
"""
#P22
'''Imie = input("Podaj Imie:")
Nazwisko = input("Podaj Nazwisko:")
Wiek = input("Podaj Wiek:")
Pensja = input("Podaj wynagrodzenie:")
Stanowisko = input("Podaj Stanowisko:")
print(Imie,Nazwisko,Wiek,Pensja,Stanowisko)

print("Pan", Imie, Nazwisko, "(" + Wiek + " " + "lat" + ")" + " " + "Pracuje na stanowisku: " + Stanowisko + " " + "(Zarabia:" + " " + Pensja + " " + "brutto" + ")")
'''

'''
a = 1
print(type(a))
napis = str(a)
# bool(), float(), int(), str()
print(type(napis))

x = 1
a = 5.5
b = 6.5
print(type(a+b+x))
'''
'''
#P25
wynagrodzenie = 5500
stawka_godzinowa = 5500/168
print("Kwota netto / h", round(stawka_godzinowa,2), "zł")
print("Kwota netto /h", round(stawka_godzinowa * 1.23,2), "zł")

#P26
#~(p^q) <=> (~pv~q)
p = True
q = True
dM1 = not (p and q)
dM2 = (not p) and (not q)
print(dM1, dM2)
print(dM1 == dM2)

p = True
q = False
dM1 = not (p and q)
dM2 = (not p) and (not q)
print(dM1, dM2)
print(dM1 == dM2)
'''

'''
a = False
b = False
c = True
p1 = (not a) and (not b) and (not c)
p2 = (not a) and (not b) and c
p3 = (not a) and b and (not c)
p4 = a and (not b) and (not c)

res = p1 or p2 or p3 or p4
print(res)
'''

'''
print("Ala" == 'Alan')
print("Ala" < 'Alan')
'''

#P28
'''
liczba = round(17**(1/2),2)
uroj = 1j
print(liczba * uroj)

liczba = round(17**(1/2),2)
uroj = 1j
res = str(liczba * uroj)
print(0 * res)
print("Liczba zespolona: 0 + " + res)
'''

#P29
'''print(Z*(Z + 3))
print(Z**2 + Z*3)
'''

#P30
'''
print((str(1.2e+3+34.5))+";"))*20
'''

#P30
'''
print((str(1.2e+3+34.5)+";")*20)
'''

#P32
'''
n1 = input("Wpisz nazwę1: ")
n2 = input("Wpisz nazwę2: ")
print("napis 1 jest większy leksygograficznie", n1 > n2)
print("napisy są takie same", n1 == n2)
print("napis 2 jest większy leksykograficznie", n1 < n2)
'''

#znaki specjalne back slesh - \t
'''
print("imie\t"+"nazwisko\t"+"stanowisko")
'''
'''
imie = input("Jak masz na imię?")
print("Witaj", imie, "!")
'''

#P38
#V=SPK(1+P)**N
'''
SPK = int(input("Podaj SPK "))
P = float(input("Podaj oprocentowanie "))
N = int(input("Podaj liczbę lat "))
res = round(SPK*(1 + (P/100))**N,2)
print("Kwota po "+str(N)+" latach wynosi: "+str(res) +" zł.")
'''

#SEKWENCJE
