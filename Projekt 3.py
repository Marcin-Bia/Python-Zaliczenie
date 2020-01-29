
import numpy as np
import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
#utworzyć metody
#1. wyswietlanie wspolrzednych
#2. Zwieksz o inny wektor(suma)
#3. zmniejsz o inny wektor(różnica)
#4. Iloczyn przez liczbe
#5. iloczyn przez drugi wektor skalarne
#6. obroc o dany kat
#7. obliczanie modułu
#8. wyznaczanie wektora przeciwnego
        
    def Wyswietlanie(self):
        return self.x,self.y

    def suma(self,a,b):
        self.x = self.x + a
        self.y = self.y + b
        
    def roznica(self,c,d):
        self.x = self.x - c
        self.y = self.y - d
    def iloczyn(self,liczba):
        self.x = self.x*liczba
        self.y = self.y*liczba
    def skalarny(self,x,y):
        return self.x*x + self.y*y
    def obrot(self, kat):
        katstopnie=kat*math.pi/180
        sinus = math.sin(katstopnie)
        cosinus = math.cos(katstopnie)
        x=self.x
        y=self.y
        self.x = x*cosinus - y*sinus
        self.y = x*sinus + y*cosinus
        
    def modul(self):
        return math.sqrt((self.x* self.x) +(self.y*self.y))
    def przeciw(self):
        return -self.x, -self.y