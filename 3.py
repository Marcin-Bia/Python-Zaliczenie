def KMnaMILE(k):
    print("Wartosc w Milach")
    return(k*0.62137)
def MILEnaKM(m):
    print("Wartosc w Kilometrach")
    return(m/0.62137)
print("Program do zamiany kilometrów na mile i na odwrót")
print("Jeżeli chcesz zamienic kilometry na mile wcisnij 1 lub Jeżeli chcesz zamienic mile na kilometry wcisnij 2 ")
x = float(input())
if x == 1:
    print("wpisz ilosc kilometrów")
    KMnaMILE(float(input()))
if x == 2:
    print("wpisz ilosc mili")
    MILEnaKM(float(input()))

