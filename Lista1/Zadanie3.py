'''
Created on 04-11-2014

@author: Ola
'''

from math import sqrt

def fkwadratowa(a,b,c,x):
    return a*x**2 + b*x + c

def miejsca_zerowe(a,b,c):
    
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        return [x1, x2]
    elif delta == 0:   
        return [-b/(2*a)]
    else:
        return None

a = 1
b = 2
c = 1

print "Miejsca zerowe funkcji to: "+str(miejsca_zerowe(1,-1,-1))
for i in xrange(-10, 11,1):
    print "Wartosc funkcji dla argumentu %s wynosi %s." % (i, str(fkwadratowa(1,-1,-1,i)))