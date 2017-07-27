
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

#P78
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


