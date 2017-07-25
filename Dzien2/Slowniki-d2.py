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


