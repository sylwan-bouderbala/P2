import os

with open('lab.txt','r') as lab:
    tab={}
    x=0
    for j in range(15):
      x=0
      for i in lab.readline():
          tab[(j,x)]=i
          x=x+1
print(tab)