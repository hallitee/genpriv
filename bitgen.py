from bitcoin import *
import os
from string import *
def gens(n):
    i = 1
    num = count(str(n))
    end=0
    res = ""
    if num==1:
        end=65
    if num==2:
        end=33
    if num==3:
        end=22
    if num==4:
        end=17
    while i<end:
        res = res+str(n)
        i+=1
    return res


arr  = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

for num in arr:
    for sec in arr:
        for thr in arr:
            for fur in arr:
                strg = str(num)+str(sec)+str(thr)+str(fur)
                mod = 64%count(strg)
                priv = gens(strg)
                if mod!=0:
                    priv = gens(strg)
                    g = "".join(arr[0:mod])
                    priv=priv+g
                    #print(strg," ------- ", count(strg))
                print(priv," --- " , count(priv))
                pub = privtopub(priv)
                addr  = pubtoaddr(pub)
                h = history(addr)
                ct = count(h)
                if ct>0:
                    file = open('founds.txt', 'a')
                    cons = str(priv)+","+str(addr)+","+strg+","+str(ct)+"\n"
                    file.write(cons)
                    file.close()
                print(addr, " -- ", ct)






