from collections import Counter
import math
list = [1,1,3,5,7,8,9]
def srednia(x):
    return sum(x)/len(x)
            
def od_sta_sre(list):
    value = 0 
    for x in list:
        value = (x- srednia(list))**2
    return math.sqrt(value / len(list))