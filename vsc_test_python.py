#coding=utf-8
#!/usr/bin/env python

import sys
import pickle
f="E:\\work\\ads\\dien\\data\\local_train_splitByUser"
print >> sys.stderr,f
if __name__=="__main__1":
    print("hello,python")
    inf=pickle.load(open("E:\\work\\ads\\dien\\data\\mid_voc.pkl","rb"))
    print(type(inf))
    for i,(k,v) in enumerate(inf.items()):
        if i<10:
            print(k,v)
    print(len(inf))

if __name__=="__main__":
    with open(f,"r") as fr:
        line=fr.readline().strip()
        print(line.split("\t")[5].split("\02"))

        