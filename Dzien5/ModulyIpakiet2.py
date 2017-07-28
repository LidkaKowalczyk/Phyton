# -*- coding: utf-8
'''
import ModulyIpakiety

print(ModulyIpakiety.a)
ModulyIpakiety.info()

a = ModulyIpakiety.Nowa()
a.Witaj()
'''
'''
from ModulyIpakiety import *

print(a)
info()

a = Nowa()
a.Witaj()
'''


'''
from Pakiet.ModulyIpakiety import *
'''

'''
from Pakiet.ModulyIpakiety import *

print(a)
info()

a = Nowa()
a.Witaj()
'''

#Praca na plikach

F = open("moduly.txt", "w")

print(F.closed, F.mode, F.name)

F.write("Poczatek pliku")
F.write("Kolejny napis")
F.writelines(["\n3 linia", "\n4 linia", "\n4 linia"])

#print (F.read())


F.close()
print(F.closed, F.mode, F.name)


G = open("moduly.txt","r")
print (G.read(10))
print(G.tell())
G.seek(0)
print(G.tell())
G.seek(20)
print(G.tell())
G.seek(0,2)
print(G.tell())


print(G.read(5))