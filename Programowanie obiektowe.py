# -*- coding: utf-8
import random
# importacja dostępu do bliblioteki random


'''
#slownik
literki = {'a' : 'A', 'b' : 'B','c' : 'C'}
print(literki)

#sprawdzanie długości
print(len(literki))

#kopiowanie wartosci ze slownika 2 do pierwszego
print(literki['a'], literki['b'], literki['c'])
literki['c'] = "napis"
print(literki['c'])

print(literki.keys(), literki.values())

literki['d'] = "D"
del literki["c"]
print(literki)
literki[2] = 'abc'
print(literki)
'''
'''literki2 {'k':'K','s':'S'}
print(literki.update(literki2))

to_str = str(literki)
print(to_str[0], to_str[1])'''

#P44
'''
to_dec = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4,'pięć':5, 'piec':5}
key1 = input('Podaj liczbę (1-5) zapisaną słownie: ')
to_rom = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}

print(key1.capitalize()+ " w postaci liczby dziesiętnej to: "+str(to_dec[key1]) + ", a w postaci rzymskiej: " +str(to_rom[to_dec[key1]]))
'''

#P47
'''#s2 = {słownie:rzymska}
to_rom = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}


print(key1.capitalize() +" w postaci liczby dziesiętnej to: "+str(to_dec[key1]) + " , a w postaci rzymskiej: " + str(to_rom[to_dec[key1]]))
'''
'''
#P48

nazwa = input("jaki produkt chcesz zamówić? (chleb, bułki, bagietka)")
ilość = int(input("Podaj ilość wybranego produktu: "))
nazwa_t = {'chleb':'0x1','bułki':'0x2', 'bagietka':'0x3'}
cena_n= {'0x1':1.99, '0x2':3.99, '0x3':5.99}

print("Do zapłaty: "+ str(round(cena_n[nazwa_t[nazwa]]*ilość,2)) + "zł ("+str(round((cena_n[nazwa_t[nazwa]]*ilość)*1.23,2))+"zł brutto.)")
'''
#ZBIORY set - tworzy zbór
'''
kształty = set(['koło','kwadrat','trókąt'])
kształty.add('okrąg')
kształty.discard('koło')
print(kształty)

okrągłe = set(['okrąg'])
print(len('kształty'), len('okrągłe'))
      
print(kształty.issubset(okrągłe))
print(kształty.issuperset(okrągłe))

#operacje na zbiorach

print(kształty | okrągłe)
print(kształty & okrągłe)
print(kształty - okrągłe)
print(kształty ^ okrągłe)

los1 = random.randint(1,49)
print(los1)

#zad wyniki losowania
S = set()
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
print(S)

S = set()
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))

L = list(S)
print(L[:6])
'''

#słowniki    {}
#            S = {k:v}           S[k]                S[k]=vn                          S[kn]=vn
#Zbiory
#            Z = set([])
#            Z = freneset([])    print(Z)           Z.discard(wartość)             Z.add(wartość)
# operacje na zbiorach (|,&, -, ^)


#INSTRUKCJE
#składnia musi kończyć sie dwukropkiem

#infrukcja if
'''
a = int(input('Podaj liczbę: '))
if(a%2 == 0):
    print("Liczba "+str(a)+' jest parzysta')
    print('jestem jeszcze w if')
    
print('jestem już za instrukcją if')
'''
#instrukcaj if else
'''
a = int(input('Podaj liczbę: '))
if(a%2 == 0):
    print("Liczba "+str(a)+' jest parzysta')
    print('jestem jeszcze w if')
else:
    print("Liczba "+str(a)+' jest nieparzysta')
print('jestem już za instrukcją if')
'''

#instrukcaj if-elif if-elif-else (else+if)
'''
a = int(input('Podaj liczbę: '))
if(a%2 == 0):
    print("Liczba "+str(a)+' jest parzysta')
    if(a>= 10):
        print("Liczba "+str(a)+' jest parzysta i większa równa od 10')
    else:
        print("Liczba "+str(a)+' jest parzysta i mniejsza od 10')
else:
    print("Liczba "+str(a)+' jest nieparzysta')
print('jestem już za instrukcją if')
'''
'''

a = int(input('Podaj liczbę: '))

if(a%2 == 0 and a >= 10):
    print("Liczba "+str(a)+' jest parzysta i większa równa od 10')
elif(a%2 == 0 and a < 10):
    print("Liczba "+str(a)+' jest parzysta i mniejsza od 10')
else:
    print("Liczba "+str(a)+' jest nieparzysta')
    
print('jestem już za instrukcją if')
'''

#P53
'''
if(bool(0)):
    print(bool(0))
if(bool(1)):
    print(bool(1)) 
if(bool(2)):
    print(bool(2))
if(bool(3)):
    print(bool(3))
if(bool(4)):
    print(bool(4))
'''

#P54
'''
index = int(input("Podaj który element chcesz wyświetlić: "))

if(index >= 0 and index <=9):
    print("Liczba znajduje sie w wybranym przedziale")
else:
    print('out of range')
'''    
'''
lista = [1,2,3,4,5,6,7,12,9]
index = int(input("Podaj indeks elementu, który chcesz wyświetlić: "))

if(index >= 0 and index <=(len(lista)-1)):
    print("Index is ok")
    print(lista[index])
else:
    print('out of range')
'''

#P55
'''
lista = [1,2,3,4,5,6,7,12,9]
index = int(input("Podaj indeks elementu, który chcesz wyświetlić: "))

if(lista[0]>0 and lista[1]>0):
   print('Oba elementy większe od zera')
elif(lista[0]>0 and lista[1]<0):
   print('Pierwszy element większy od zera, a drugi mniejszy od zera')
elif(lista[0]<0 and lista[1]>0):
   print('Pierwszy element mniejszy od zera, a drugi większy od zera')
else:
   print('Oba elemanty są mniejsze od zera')(lista[0]>0 and lista[1]>0)
  '''
'''
lista = [1,2,3,4,5,6,7,12,9]
index = int(input("Podaj indeks elementu, który chcesz wyświetlić: "))

if(lista[0]>0 and lista[1]>0):
    print('Oba elementy większe od zera')
elif(lista[0]>0 and lista[1]<0):
    print('Pierwszy element większy od zera, a drugi mniejszy od zera')
elif(lista[0]<0 and lista[1]>0):
    print('Pierwszy element mniejszy od zera, a drugi większy od zera')
else:
    print('Oba elemanty są mniejsze od zera')(lista[0]>0 and lista[1]>0)
'''
'''
A = set([1,2,3,4,5])
B = set([2,3,4])

if(A.issuperset(B)):
    print("A jest nadzbiorem B")
else:
    print("B jest nadzbiorem A")
'''  
  
'''     
A = set([1,2,3,4,5])
B = set([1,2,3,4,5])
    
if(A>B):
    print("A jest nadzbiorem B")
elif(A==B):
    print('Zbiory są równe')
else:
    print("B jest nadzbiorem A")
'''


'''
A = set([1,2,3,4,5])
B = set([1,2,3,4,5])

if(A == B):
    print('Zbiory są równe')
elif(A.issuperset(B)):
    print("A jest nadzbiorem B")
else:
    print("B jest nadzbiorem A")
'''

'''
A = set([1,2,3,4,5])
B = set([1,2,3,4,5,8])

if(A == B):
    print('Zbiory są równe')
elif(A.issuperset(B)):
    print("A jest nadzbiorem B")
elif(A.issuperset(A)):
    print("B jest nadzbiorem A")    
else:
    print("Zbiory są różne")
'''

#PĘTLE

'''
lista = [1,2,3,4,5,6,7,8,9]
i = 0
while(i <= (len(lista) -1) ):
    print("Index: "+str(i)+"\t Wartość: "+str(lista[i]))
    i += 1 
    
print('poza pętlą')
'''

#INSTRUKCJE + PĘTLE

"""
#parzyste z listy

lista = [1,2,3,4,5,6,7,8,9]
i = 0
print('Wpisuje parzyste')
while(i <= (len(lista) -1) ):
    if(lista[i]%2==0):
        print("Index: "+str(i)+"\t Wartość: "+str(lista[i]))
    i += 1 
"""

#parzyste z listy w odwrotnej kolejności
'''
lista = [1,2,3,4,5,6,7,8,9]
i = len(lista) -1
print('Wpisuje parzyste')
while(i >= 0):
    if(lista[i]%2==0):
        print("Index: "+str(i)+"\t Wartość: "+str(lista[i]))
    i -= 1 
'''

#while-else

'''
lista = [1,2,3,4,5,6,7,8,9]
i = len(lista) -1
print('Wpisuje parzyste')
while(i >= 0):
    if(lista[i]%2==0):
        print("Index: "+str(i)+"\t Wartość: "+str(lista[i]))
    i -= 1
else:
    print('jeste w elese')
print('jestem poza')
'''

#wyrażenie trójargumentowe
# która z liczb jest większa i o ile wyr trójargumentowe

'''
a = 20
b = 19
print("a jest większe od b o: "+str(a-b)) if (a >= b) else print("a jest mniejsze od b o: "+str(b-a))
'''

#PĘTLA FOR A IN
'''
lista = [1,2,3,4,5,6,7,8,9]
for var in lista:
    print("Wartości: "+ str(var))
 '''

'''
lista = [1,2,3,4,5,6,7,8,9]
for var in lista:
   print("Wartości: "+ str(var))
lista.append(15)
for index, var in enumerate(lista):
   print("Index: "+str(index)+"\tWartości: "+ str(var))
'''

'''
SL = {'a':1, 'b':2, 'c':3}
for k in SL:
    print(k, SL[k])
'''

#zagnierzdzenie for in

'''
SL = {'a':1, 'b':2, 'c':3}
for k in SL:
    if (SL[k] >= 2):
        print(k, SL[k])
        '''

# range 1-100

'''
s1 = range(100)
print(s1)
for i in s1:
    print(i)
'''


'''
s1 = range(100)
print(s1)
for i in s1:
    print(i)
   #wypisuje od 15 do 24 
for j in range(15,25):
    print(j)
 # wypisuje co 3 elemen)   
for k in range(0,50,3):
    print(k)
'''

'''
#kwadraty wszystkich liczb parzystych
s1 = range(100)
print(s1)
for i in s1:
    print(i)
   #wypisuje od 15 do 24 
for j in range(15,25):
    print(j)
 # wypisuje co 3 elemen)   
for k in range(0,20,2):
    print(k, k**2)
'''

#kwadraty wszystkich liczb parzystych
'''
s1 = range(100)
print(s1)
  
for k in range(0,100):
    print(k, k**2, k**3)
'''

#określanie / formatowanie długości (można osadzic, i - intidżery, flouty, s, c,...) 

'''
s1 = range(100)
print(s1)

for k in range(0,100):
    print("Wynik: %4i%6i%8i" % (k, k**2, k**3))
    '''

#osoadznie ułamków dziesiętnych
'''
s1 = range(100)
print(s1)

for k in range(0,100):
    print("Pierwiastek sześcienny z %4i to: %6.5f" % (k, k**0.3))
    '''

#P57  BREAK
'''
zamowienie = input("Wybierz towar: ")
sklep_produkty = {'chleb':'a','masło':'b','mleko':'c'}

for k in sklep_produkty:
    if(zamowienie == k):
        print("Produkt dostępny: " + k)
        break
 '''   
#P58

'''
zamowienie = input("Wybierz towar: ")
zamowienie_ilosc = int(input("Podaj ilość zamawianego produktu: "))
sklep_produkty = {'chleb':'a','masło':'b','mleko':'c'}
produkty_cena = {'a':1.5,'b':4.6,'c':7}
produkty_dostepnosc = {'a':10,'b':80,'c':7}
suma = 0
i = "t"
while(i == "t"):
    zamowienie = input("Wybierz towar: ")
    zamowienie_ilosc = int(input("Podaj ilość zamawianego produktu: "))
    for k in sklep_produkty:
        if(zamowienie == k and produkty_dostepnosc[sklep_produkty[k]] >= zamowienie_ilosc):
            print("Produkt dostępny: " + k)
            print("Zamawiasz: " + str(zamowienie_ilosc) + 'szt')
            suma += zamowienie_ilosc*produkty_cena[sklep_produkty[k]]
            
        elif(zamowienie == k and produkty_dostepnosc[sklep_produkty[k]] < zamowienie_ilosc):
            print("Produkt dostępny: " + k)
            print("Jest dostępne tylko: " + str(produkty_dostepnosc[sklep_produkty[k]] + 'szt'))
    i = input("czy chcesz zamawiac dalej? (t/n)")
print("Do zapłaty: " + str(suma))

'''

# niezrobione
'''
sklep_produkty = {'chleb':'a','masło':'b','mleko':'c'}
produkty_cena = {'a':1.5,'b':4.6,'c':7}
produkty_dostepnosc = {'a':10,'b':80,'c':7}
suma = 0
i = "t"
while(i == "t"):
    zamowienie = input("Wybierz towar: ")
    zamowienie_ilosc = int(input("Podaj ilość zamawianego produktu: "))
    if (zamowienie in sklep_produkty.keys()):
        if(produkty_dostepnosc[sklep_produkty[k]] >= zamowienie_ilosc):
                print("Produkt dostępny: " + k)
                print("Zamawiasz: " + str(zamowienie_ilosc) + 'szt')
                suma += zamowienie_ilosc*produkty_cena[sklep_produkty[zamowienie]]
        elif(produkty_dostepnosc[sklep_produkty[k]] < zamowienie_ilosc):
                print("Produkt dostępny: " + k)
                print("Jest dostępne tylko: " + str(produkty_dostepnosc[sklep_produkty[k]] + 'szt'))
    else:
        print("Brak produktu który chcesz zamówić")  
    i = input("czy chcesz zamawiac dalej? (t/n)")
print("Do zapłaty: " + str(suma))
'''



'''    
    
        break   
'''

#P60
'''
i = "t"
res = []
to_dec = {0:'zero',1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'pięć',6:'sześć',7:'siedem',8:'osiem',9:'dziewięć'}
while(i == "t"):
    dig = input("Wprowadź cyfrę: ")
    if(dig.isdigit()):
        dig = int(dig)
        res.append(to_dec[dig])
    else:
        print("podana wartość nie jest cyfrą")
    i = input("czy chcesz wprowadzac dalej? (t/n)")
for i in res:
    print(i,end="")

'''
#ignorujemy znaki
#konwertujemy cyfry

#P61

#s1 = range(0,11)
#print(s1)
'''
for k in range(1,11):
    print("====================")
    print("Wynik: %4i%4i%4i%4i%4i%4i%4i%4i%4i%4i" % (k,k*2,k*3,k*4,k*5,k*6,k*7,k*8,k*9,k*10))
'''
'''
line = range(1,6)
n = 1
print("%3i%3i%3i%3i%3i" % (1,2,3,4,5))
print("====================")
while(n<=5):
    print(str(n)+" |",end="")
    print("%3i%3i%3i%3i%3i" % (n*line[0], n*line[1],n*line[2],n*line[3],n*line[4])) 
    n +=1
  '''  
#P63
'''
print("Kawadraty liczb nieparzystych!")
np = range(1,10,2)
i = len(np) - 1
while(i>=0):
    print(np[i])
    i -= 1
'''
#po przecinku
'''
print("Kawadraty liczb nieparzystych!")
np = range(1,10,2)
i = len(np) - 1
while(i>=0):
    print(np[i]**2, end=", ")
    i -= 1
   ''' 

   # bez przecinka na końcu
'''
print("Kawadraty liczb nieparzystych!")
np = range(1,10,2)
i = len(np) - 1
while(i>=0):
   if(i==0):
      print(np[i]**2)
   else:
      print(np[i]**2, end=", ")
   i -= 1 
   '''

'''

# dzień 3 koniec pętli

# x do potęgi y w pętli
res = 1
i = 1
#res i<= y

i += 1

x = int(input("x: "))
y = int(input("y: "))

#print("x do potęgi y: ")
while (i <= y):
   res *= x
   i += 1
   print(res)
'''

#suma wartości elementów ciągu 
'''
i = 0 
S = 0

n = int(input("n: "))
a1 = float(input("a1: "))
q = float(input("q: "))
L = []
while(i < n):
   S += a1*(q**i)
   L.append(a1*(q**i))
   i += 1
print()
print(S)
print(L)

print("Suma", S)
print("składowe: ", end="")
for i in L:
   print(i, end=' ')
'''

# tabela
'''
i = 0 
S = 0

n = int(input("n: "))
a1 = float(input("a1: "))
q = float(input("q: "))
L = []
while(i < n):
   S += a1*(q**i)
   L.append(a1*(q**i))
   i += 1
   
print("%10s %-15.2f" % ("Suma: ",S))
print("%10s" % ("Składowe: "), end="")

for i, v in enumerate(L):
   if(i == 0):
      print("%-15.2f" % (v), end=' ')
   else:
      print("%-5.2f" % (v), end=' ')
 '''  
'''
i = 0 
S = 0

n = int(input("n: "))
a1 = float(input("a1: "))
q = float(input("q: "))
L = []
while(i < n):
   S += a1*(q**i)
   L.append(a1*(q**i))
   i += 1
   
print("%10s %-15.2f" % ("Suma: ",S))
print("%10s" % ("Składowe: "), end="")

for v in L:
   
   
   if(i == 0):
      print("%-15.2f" % (v), end=' ')
   else:
      print("%-5.2f" % (v), end=' ')
      
      '''

#P64 

'''
txt = input("wpisz napis: ")
szukaj = input("wpisz literkę: ")
i = 0
licznik = 0

while(i<=len(txt)-1):
   if(txt[i] == szukaj):
      print("Znaleziono", szukaj,"na pozycji",i+1)
      licznik += 1
   i += 1
print("Szukaną frazę znaleziono", licznik, "razy") 
'''


#teraz ciąg znakóW niech wypisuje

'''
txt = input("wpisz napis: ")
szukaj = input("wpisz litery przyległe do siebie należące do napisu: ")


i = 0
licznik = 0

while(i < len(txt) ):
   tab = txt[i:i+len(szukaj)]
   if (tab == szukaj):
      print("Znaleziono", '"'+szukaj+'"',"na pozycji",i+1)
      licznik += 1
   i +=1
print("Szukaną frazę znaleziono", licznik, "razy") 
   
'''
'''
txt = input("wpisz napis: ")
szukaj = input("wpisz litery przyległe do siebie należące do napisu: ")
i = 0
licznik = 0

while(i < len(txt) ):
   tab = txt[i:i+len(szukaj)]
   if (tab == szukaj):
      print("Znaleziono", '"'+szukaj+'"',"na pozycji",i+1)
      licznik += 1
      i = i + len(szukaj)
   else:
      i +=1
print("Szukaną frazę znaleziono", licznik, "razy") 
'''

#P67 stopnie celciusza na farahaity

#Faranhait = (C*1.8)+32

'''
C = range(-20,45,5)
i = len(C)-1
print("%7s | %7s" % ("C","F"))
print("-----------------------------")
while(i >= 0):
   if(C[i] == 0):
      print("-----------------------------")
      print("%7i | %7.1f" % (C[i], (C[i]*1.8)+32))
      print("-----------------------------")
   else:
      print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
   i -=1
'''

#prosimy użytkownika o wpisanie wartości i co ile ma wypisywać

'''
txt = int(input("Proszę podaj min stopnie celcjusza: "))
txt1 = int(input("Proszę podaj max stopnie celcjusza: "))
txt2 = int(input("Podaj co ile jednostek ma wyświetlić się wynik: "))

C = range(txt, txt1 + txt2, txt2)
i = len(C)-1
print("%7s | %7s" % ("C","F"))
print("-----------------------------")
while(i >= 0):
   print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
   i -=1
   
   '''
'''
txt = int(input("Proszę podaj min stopnie celcjusza: "))
txt1 = int(input("Proszę podaj max stopnie celcjusza: "))
txt2 = int(input("Podaj co ile jednostek ma wyświetlić się wynik: "))


while(txt1-txt < txt2):
   print("Przedział za duży, proszę podaj mniejszy")
   txt2 = int(input("Podaj co ile jednostek ma wyświetlić się wynik: "))

C = range(txt, txt1 + txt2, txt2)
i = len(C)-1
print("%7s | %7s" % ("C","F"))
print("-----------------------------")
while(i >= 0):
   print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
   i -=1
'''

# to samo z pomocą if

'''
txt = int(input("Proszę podaj min stopnie celcjusza: "))
txt1 = int(input("Proszę podaj max stopnie celcjusza: "))
txt2 = int(input("Podaj co ile jednostek ma wyświetlić się wynik: "))

if((txt1-txt) % txt2 == 0) :
   C = range(txt, txt1+txt2, txt2)
else:
   C = range(txt, txt1, txt2)
i = len(C)-1
print("%7s | %7s" % ("C","F"))
print("-----------------------------")
while(i >= 0):
   if (C[i] == 0):
      print("-----------------------------")
      print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
      print("-----------------------------")
   else:
      print("%+7i | %+7.1f" % (C[i], (C[i]*1.8)+32))
   i -=1
   
   '''
#P68

'''
D = ['1','2','3','4','5','6']
O = []
i = 'x'
print("Proszę wpisz ocenę: ", end=' ')

while(i != ""): 
   i = input(" ")
   if(i in D):
      O.append(float(i))
   elif(i ==""):
      print("Wprowadzanie ocen zakończone")
   else:
      print("ocena niepoprawna")
sr = 0
if (len(O) != 0):
   for i in O:
      sr += i
   print("Średnia ocen", round(sr/len(O),2))
else:
   print("Brak ocen")
''' 

# FUNKCJE FUNKCJE   FUNKCJE FUNKCJE   FUNKCJE FUNKCJE
#funkcja

'''
def powitanie():
   print("Witaj")
#wywołanie funkcji
powitanie()
'''

 # funkcja moze zwnacac wartosc
'''
def powitanie(imie):
   witaj = "Witaj " + imie 
   return witaj 

print(powitanie("Michał"))
'''
'''
def powitanie(imie):
   witaj = "Witaj " + imie 
   return witaj 

a = powitanie("Michał")
b = powitanie("Ania")
c = powitanie("Staś")

print(a,b,c)
'''
'''
def powitanie(imie):
   witaj = "Witaj " + imie 
   return witaj 

L = []

for i in range(1,4):
   L.append(powitanie(input("Podaj imie do listy: ")))
print(L)
'''

#dodawanie
'''
def dodawanie(a,b):
   wynik = a + b
   print(a,b)
   return wynik

res = dodawanie(14,15)
print(res)
'''

'''
def dodawanie(a,b,imie="Anonim"):
   wynik = a + b
   print(a,b)
   print(imie)
   return wynik

res = dodawanie(a=14,imie="Michał",b=15,)
print(res)
'''
'''
def dodawanie(a,b,imie="Anonim"):
   wynik = a + b
   print(a,b)
   print(imie)
   return wynik

res = dodawanie(a=14,b=15,)
print(res)
'''
'''
def dodawanie(a,b,imie="Anonim",nazwisko="Anonim"):
   wynik = a + b
   print(a,b)
   print(imie,nazwisko)
   return wynik

res = dodawanie(a=14,b=15,)
print(res)
'''

'''

def dodawanie(a,b,imie="Anonim",nazwisko="Anonim"):
   wynik = a + b
   print(a,b)
   print(imie,nazwisko)
   return wynik

res = dodawanie(a=14,b=15,nazwisko="Kru")
print(res)

'''


'''
def dodawanie(a,b,imie="Anonim",nazwisko="Anonim"):
   wynik = a + b
   print(a,b)
   print(imie,nazwisko)
   return wynik

res = dodawanie(a=14,b=15,nazwisko=input('nazwisko: '))
print(res)
'''

# P69

'''
def silnia(n):
   res = 1
   i = 1
   while(i <= n):
      res *= i
   return res


print(silnia(4))
   res *= 1
   i += 1
'''   

'''  
def silnia(n):
   res = 1
   L = []
   i = 1
   while(i <= n):
      res *= i
      L.append(res)
      i += 1
   return L


elem = silnia(4)
for i in elem:
   print(i, end=' ')
'''

'''
def silnia(n):
   res = 1
   L = []
   i = 1
   while(i <= n):
      res *= i
      L.append(res)
      i += 1
   return L
#---------------------

elem = silnia(4)
def wyświetl(lista):
   for i in elem:
      print(i, end=' ')

#--------------------

elem = silnia(4)
wyświetl(elem)
'''

'''
def silnia(n):
   res = 1
   L = []
   i = 1
   while(i <= n):
      res *= i
      L.append(res)
      i += 1
   return L
#---------------------

elem = silnia(4)
def wyświetl(lista):
   for i in lista:
      print(i, end=' ')

#--------------------

wyświetl(silnia(4))
'''
'''
res = 1

def silnia(n):
   res = 1
   L = []
   i = 1
   while(i <= n):
      res *= i
      L.append(res)
      i += 1
   return L
#---------------------

elem = silnia(4)
def wyświetl(lista):
   for i in lista:
      print(i, end=' ')

#--------------------

wyświetl(silnia(4))
print(res) = 

'''

#P70
'''
def fib(n):
   F = [0,1]
   suma = 0
   i = 2
   while(i < n):
      a = (F[i-2] + F[i-1])
      F.append(a)
      i += 1
   for i in F:
      suma = suma + i
   return F[len(F)-1], suma, F

Fib = fib(6)
print("(Element, Suma, Kolejne elemanty)",Fib)
'''


#P71

'''

import random

def zdania(a = 5):
   wyrazy = ["każdy", "następny", "jest", "sumą", "dwóch", "poprzednich"]
   i = 0
   Zdanie = []
   while(i < a):
      Zdanie.append(wyrazy[random.randint(0,len(wyrazy)-1)])
      i += 1
   return Zdanie

def format(zdanie):
   for i, v in enumerate(zdanie):
      if(i == 0):
         print(v.capitalize(), end=" ")
      elif(i == len(zdanie)-1):
         print(v, end=".")
      else:
         print(v, end=" ")
         
format(zdania(7))

'''

#P72



#import math (trzeba potem stosować indeks biblioteki)
#from math import sqrt
from math import * 
#(importuje wszystko)
'''
def dist(x1,y1,x2,y2):
   d = sqrt(((x2-x1)**2) + ((y2-y1)**2))
   return round(d,2)
print(dist(1,1,5,5))
'''


'''
def dist(x1,y1,x2,y2):
   d = sqrt(((x2-x1)**2) + ((y2-y1)**2))
   return round(d,2)

i = 0
x = []
y = []

while(i < 2):
   if (i == 1):
      print("Podaj lokalizację miejsca docelowego: ")
   else:
      print("Podaj swoje położenie: ")  
   u1 = int(input(" "))
   u2 = int(input(" "))
   x.append(u1)
   y.append(u2)
   i = i + 1
   
print("Dystans:" ,dist(x[0],x[0],y[1],x[1]))  
'''   


'''
class PierwszaKlasa:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.dodaj()
    self.odejmowanie()
    def dodaj(self):
  self.wynik_d = self.x + self.ydef odejmowanie(self):
      self.wynik_d = self.x + self.y
    return self.wynik_o
  def __str__(self):
 return 'Wynik dodawania wynisci:  "+ self.wynik_d +"

obiekt1 = PierwszaKlasa(5,6)
print(obiekt1)
'''

# P75

class BMI: 
   def __init__(self, imie, nazwisko, waga, wzrost):
      self.imie = imie
      self.nazwisko = nazwisko
      self.waga = waga
      self.wzrost = wzrost
      self.obliczBMI()
   def obliczBMI(self):
      self.bmi = round(self.waga) / ((self.wzrost/100)**2)
   def __str__(self):
      return "BMI dla "+self.imie+" "+self.nazwisko+" wynosi: "+str(self.bmi)

z1 = BMI("Michał", "Kruczkowski", 75, 182)
print(z1)

      
   

