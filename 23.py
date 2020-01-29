
from collections import Counter
import math
list = [1.2,1.2,3,5,7,8,9]
def srednia(x):
    return sum(x)/len(x)

def dominanta(z):
    c = Counter(list)
    return c.most_common(1)[0][0]
