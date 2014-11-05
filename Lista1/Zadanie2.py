'''
Created on 05-11-2014

@author: Ola
'''

def Palindrom (palin):
    
    t1=((str(palin).lower()).replace(" ", ""))
    
    if t1==t1[::-1]:
        return True
    else:
        return False
    
print Palindrom("Zakopane na pokaz")
print Palindrom("ha haha")