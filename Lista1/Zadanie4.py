'''
Created on 05-11-2014

@author: Ola
'''
def duplikaty(dup):
    ok=[]
   
    for i in dup:
        if i not in ok:
            ok.append(i)
    return ok

dup=['kot','pies','chomik','kot','pies','pies','wydra','lis']

print duplikaty(dup)