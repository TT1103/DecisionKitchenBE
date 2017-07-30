from random import random, randint

f = open("train.txt", "w")
s=""
for i in range(1000):
    vals = [random() + randint(0,2), randint(1,4)/2, randint(1,5), randint(1,1000)]
    for i in range(4):
        s+=str(vals[i]) + ","
    s+=str(sum(vals[:3]) + vals[-1]/100) + "\n"


f.write(s)

