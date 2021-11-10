from bitcoin import *
from string import *
import numpy as np
import os
import multiprocessing
from multiprocessing import Pool
import binascii, hashlib, base58, ecdsa
import firebase_admin
import datetime as dt
from firebase_admin import credentials
from firebase_admin import db
cores=4
cred = credentials.Certificate('crypto-wall.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://crypto-wall-92f82-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')
def addToDB(addr='', pub='', priv='', str1='', str2='', cnt=''):
    ref = db.reference('bitgen-Wallets-Heroku')
    ref.push({
        'Address': addr,
        'Public': pub,
        'Private': priv,
        'Value1': str1,
        'Value2': str2,
        'TransCnt': cnt
    })

start =  4200000
finish = 10000000000000000000000000000000
addr, pub, priv = '','',''
#for num in range(start, finish):
   # val = ''
def seek(r, greet):
    global num_threads
    LOG_EVERY_N = 1000
    start_time = dt.datetime.today().timestamp()
    i = 0
    print("Core " + str(r) +":  Searching Private Key..")
    while(True):
        i=i+1
        priv_key = os.urandom(32)
        fullkey = '80' + binascii.hexlify(priv_key).decode()
        #priv = sha256(val)
        pub = privtopub(fullkey)
        addr = pubtoaddr(pub)
        h = history(addr)z
        cnt = count(h)
        if(cnt>0):
            addToDB(addr, pub, priv, str(num), str(num), cnt )
        print(addr+' --####-- '+fullkey+'---####----'+str(cnt)+'--Core--'+str(r)+'-Count-'+str(i))
    print("Ending of num  lower case ................................................................")

if __name__ == '__main__':
	jobs = []
	#df_handler = pd.read_csv(open('bit.txt', 'r'))
	for r in range(cores):
		p = multiprocessing.Process(target=seek, args=(r, "Hello"))
		jobs.append(p)
		p.start()
