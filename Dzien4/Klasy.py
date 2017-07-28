# -*- coding: utf-8


'''
class PierwszaKlasa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dodaj()
        self.odejmowanie()
    def dodaj(self):
        self.wynik_d = self.x + self.y
    def odejmowanie(self):
        self.wynik_o = self.x + self.y
    def __str__(self):
        return "Wynik dodawania wynisci:  "+ str(self.wynik_d)
    

obiekt1 = PierwszaKlasa(5,6)
print(obiekt1)

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

z1 = BMI("Michal", "Kruczkowski", 75, 182)
print(z1)


class Sklep:
    
    
    
    def __init__(self, towar, cena, ilosc):
        self.towar_klasa = towar
        self.cena_klasa = cena
        self.ilosc_klasa = ilosc
    def zaplata(self):
        self.do_zaplaty = self.cena_klasa * self.ilosc_klasa
        
zakup1 = Sklep("chleb", 3.99, 4)

print(zakup1.ilosc_klasa)
print(zakup1.towar_klasa)
print(zakup1.cena_klasa)

zakup1.ilosc_klasa = 5
print(zakup1.ilosc_klasa)
zakup1.zaplata()
print(round(zakup1.do_zaplaty))
'''
#P78
'''
import random

class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))
        
los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
los5 = Lotto()
los6 = Lotto()
'''

#rodzaj1
'''
import random

class Lotto:
    def __init__(self):
        self.L = range(1,50)
        self.Tab = random.sample(self.L,6)
        self.sort()
    def sort(self):
        self.Tab_s = sorted(self.Tab)
        self.__str__()
    def __str__(self):
        self.res = ""
        for i, v in enumerate(self.Tab_s):
            if(i == len(self.Tab_s) - 1):   
                self.res += str(v)
            else:
                self.res += str(v) + ", "
        return "Wynik losowania: " + self.res
        

        
los1 = Lotto()
print(los1)
los2 = Lotto()
print(los2)
los3 = Lotto()
print(los3)
los4 = Lotto()
print(los4)
los5 = Lotto()
print(los5)
los6 = Lotto()
print(los6)

'''




# rodzaj 2 tego co na górze tam przez pętle na dole, na górze przez tekst ??? - niezrobione
'''
import random

class Lotto:
    def __init__(self):
        self.L = range(1,50)
        self.Tab = random.sample(self.L,6)
        self.sort()
    def sort(self):
        self.Tab_s = (sorted(self.Tab))
        self.__str__()
    def __str__():
        return str(self.Tab_s[])
        

        
los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
los5 = Lotto()
los6 = Lotto()

'''

#DZIEDZICZENIE      DZIEDZICZENIE       DZIEDZICZENIE

'''
#P 
class Szkolenia:
    def __init__ (self, nazwa, termin, cena_n, il_osob):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.il_osob = il.osob
    def obliczCalk(self):
        self.Suma_b = (self.cena_n * self.il_osob) * 1.23
           

class Technologie(Szkolenia):
    def __init__(self, nazwa, termin, cena_n, il_osob, technologia, poziom):
        super().__init__(nazwa, termin, cena_n, il_osob)
        self.technologia = technologia
        self.poziom = poziom

class Trenerzy(Technologie):
    def __init__(self, nazwa, termin, cena_n, il_osob, technologia, poziom , imie, nazwisko, pensja):
        super().__init__(nazwa, termin, cena_n, il_osob, technologia, poziom)
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
    def obliczCalk(self):
        return self.obliczCalk() - (self.pensja * 1.23)
        
    
s1 = Technologie ("Kurs Python dla dzieci", '2000-02-20', 2000, 20, "Python3.6", 'zero') 
s2 = Trenerzy ("Kurs Python dla dzieci", '2000-02-20', 2000, 20, "Python3.6", 'zero', "Michal", "Kruczkowski", 1000)
print(s2.obliczCalkTrener())

'''
#P80 
'''
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return" Produkt: "+self.nazwa+" "+ str(self.cena)
class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system
    def __str__(self):
        return auper().__str() + " " + self.jezyk + " " +self.system
class Szkolenie(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):
        return "Produkt: "+self.nazwa +" " + str(self.cena) + " " + self.jezyk+ " " + self.system + " " +self.termin
    
s1 = Szkolenie("Witaj Python", 1000, "Python2", "MacOS", "2012-02-20")
print(s1)
'''
# drugi obiekt
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return" Produkt: "+self.nazwa+" "+ str(self.cena)
class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system
    def __str__(self):
        return auper().__str() + " " + self.jezyk + " " +self.system
class Szkolenie(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):
        return self.nazwa +" " + str(self.cena) + " " + self.jezyk+ " " + self.system + " " +self.termin
    
s1 = Szkolenie("Witaj Python", 1000, "Python2", "MacOS", "2012-02-20")
print(s1)

    





