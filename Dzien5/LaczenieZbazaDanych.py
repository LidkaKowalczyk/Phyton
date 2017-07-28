# -*- coding: utf-8

'''

import pymysql  

conn = pymysql.connect("localhost", "root", "koleskoles0420", "skoczkowie")

c = conn.cursor()
c.execute("select id_skoczka, imie, nazwisko, kraj from zawodnicy;")

res = c.fetchall()



for v in res:
    id_skoczka = v[0]
    imie = v[1]
    nazwisko = v[2]
    kraj = v[3]
    print("%-3i %-15s %-30s %-3s" % (id_skoczka, imie, nazwisko, kraj))
    
'''

'''

import pymysql  

class MySQLConnector:
    def __init__(self,passwd):
        self.passwd = passwd
        self.conn = pymysql.connect("localhost", "root", self.passwd, "skoczkowie")
        self.c = self.conn.cursor()
        self.c.execute("SELECT id_skoczka, imie, nazwisko, kraj FROM zawodnicy order by id_skoczka;")        
        res = self.c.fetchall()
        print("Połączenie ustanowione")
        for v in res:
            id_skoczka = v[0]
            imie = v[1]
            nazwisko = v[2]
            kraj = v[3]
            print("%-3s %-15s %-30s %-3s" % (id_skoczka, imie, nazwisko, kraj))
    def insert(self):
        self.c.execute('INSERT INTO zawodnicy VALUES (25, "xxx", "xxx", "GER", "1981-02-24", 187, 68);')
        self.conn.commit()
        print("dane wprowadzono")
    
c1 = MySQLConnector("koleskoles0420")
c1.insert()


'''

'''

import pymysql

class MySQLConnector:
    def __init__(self, passwd):
       self.passwd = passwd
       self.conn = pymysql.connect("localhost", "root", self.passwd, "skoczkowie1")
       self.c = self.conn.cursor()
       print("Połączenie ustanowione")
       nav = ''
       while(nav != "Q"):
           nav = input("Co chcesz zrobić? (S)-select, (I)-insert, (U)-update, (Q)- wyjście")
           if(nav == "S"):
               self.select()
           elif(nav == "I"):
               self.insert()
           elif(nav == "U"):
               self.update()               
       print("Połączenie zakończone")
       self.conn.close()    
    def select(self):
       self.c.execute("SELECT id_skoczka, imie, nazwisko, kraj FROM zawodnicy1 order by id_skoczka;")
       res = self.c.fetchall()       
       for v in res:
           id_s = v[0]
           imie = v[1]
           nazwisko = v[2]
           kraj = v[3]
           print("%-3s %-15s %-30s %-3s" % (id_s, imie, nazwisko, kraj))
    def insert(self):
       self.c.execute("INSERT INTO zawodnicy1 VALUES (25, 'xxx', 'xxx', 'GER', '1981-02-24', 187, 68);")
       self.conn.commit()
       print("dane wprowadzono")
    def update(self):
       self.c.execute("UPDATE zawodnicy1 SET imie='yyy' where id_skoczka = 25;")
       self.conn.commit()
       print("dane zaktualizowane")       
c1 = MySQLConnector("miki123")

'''


#MODUŁY I PAKIETY

