# -*- coding: utf-8
'''
napis = "To jest długi napis"

print(napis[3])
napis = "zawartość"
print(napis.capitalize())
print(napis.count("a"))
print(napis.isdigit())
print(napis.islower())
print(napis.index("a"))
b = (napis.index("a"))
print(napis.replace("zawa","otwa"))
'''
#LISY/TABLICE      
#tworzymy liste, na poczatku pusta liste sie tworzy
'''Tab.append(1)
Tab.append("abc")
Tab.append('A')

print(Tab[0],Tab[1],Tab[2])
print(Tab[2])


print(Tab[0],Tab[1],Tab[2])
#deklaracja i przypisanie wartości
oceny= []
a = input("Podaj ocenę")
oceny.append(a)
oceny.append(input("Podaj ocenę"))
print(oceny[0], oceny[1])
'''
'''print(Tab[0],Tab[1],Tab[2])
oceny2 = [3,4,5]
'''
#lista list
'''ListList = [ [1, 2, 3], ["Nocny", "Dzienny"] ]
print(ListList[1],[1])
'''
'''ListList = [ [1, 2, 3], ["Nocny", "Dzienny", ["r", "n"] ] ]
print(ListList[1],[1],[1])

oceny2 = [3,4,5,6,7,8,9,10]
print(oceny2[2:5])
print(oceny2[3::2])
print(len(oceny2))
'''
#sktórcenie listy
'''
text = 'napis'
lista = list(text)
print(lista)
lista[2] = "w"
print(lista)
 
 #pop
print(lista.pop(2))
print(lista)
print(lista[2])
'''
#P40
'''a = "chleb"
b = "masło"
c = "pomidor"
d = "sok"
e = "wiśnie"

arty = [[a,b,c,d,e],[1.99,3.15,2.0,4.3,8.9]]
print(arty)
print("nazwa\tcena")
print(arty[0][0] +"\t\t"+ str(arty[1][0]))
print(arty[0][1] +"\t\t"+ str(arty[1][1]))
print(arty[0][2] +"\t\t"+ str(arty[1][2]))
print(arty[0][3] +"\t\t"+ str(arty[1][3]))
print(arty[0][4] +"\t\t"+ str(arty[1][4]))
'''

#listy []
#L=[]                       L[index]                      L[index]=wartość          L.append(wartość)
#L=[1,"a",...]              L[index.start:index.stop]     
#deklaracja                 odczyt                         modyfikacja              zais

#Krotki ()
#K = (wartości,wart)        K[index]
#K = ( , ) v K = ..., ...   K[index.start:index.stop]

#Krotki ()
'''krotka2 = "a", "b", "c"
print(krotka)
print(krotka2)
'''
#P43
'''
a = "chleb"
b = "masło"
c = "pomidor"
d = "sok"
e = "wiśnie"
data = (("a","b","c","d","e"),("01-01-2009","01-01-2010","01-01-2011","01-01-2012","01-01-2013"))
print(data)
print(data[0][0] +"\t\t"+ str(data[1][0]))
print(data[0][1] +"\t\t"+ str(data[1][1]))
print(data[0][2] +"\t\t"+ str(data[1][2]))
print(data[0][3] +"\t\t"+ str(data[1][3]))
print(data[0][4] +"\t\t"+ str(data[1][4]))
'''
Tabela = [("Kowal",("Nowak","-Cos")),("1987-02-15","1985-02-14"),["dev","dev"]]
#indeksacja tabeli
Tabela[2][0] = "admin"
Tabela[1][1] = "Mikołaj"
print(Tabela[0][0], Tabela[1][0], Tabela[2][0])
print(Tabela[0][1][0]+Tabela[0][1][1], Tabela[1][1], Tabela[2][1])#

#33

