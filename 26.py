
from collections import Counter
import math
def srednia(x):
    return sum(x)/len(x)

def skosnosc(y):
    sr = srednia(x)
    suma = 0
    for i in range(len(x)-1):
        suma = suma + (x[i] - sr)**2
    return suma/len(x)

#USER wpisuje w konsole liste liczb w postaci: "x = [liczba1, liczba2, itd]"
#nastepnie wpisuje w konsoli polecenie "skosnosc(x)"