from random import random, randint

f = open("train.txt", "w")
s=""
for i in range(1000):
    s += str(i/1000) +"," +str(i/1000) + "," + str(i/1000)
    s+="\n"


f.write(s)

