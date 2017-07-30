from random import random, randint
import itertools
#[cat, price, rating, # rating]
s=""
f=open("train.txt","w")


def getAns(arr):
    ratingNum = arr[-1]
    rating = arr[-2]
    price = arr[-3]
    cat = arr[0]
    
    
    
    '''
    rating: 0.3
    price: 0.3
    ratingNum 0.1
    categories: 0.3
    
    '''
    ans=0
    ans+=price * 0.3
    ans+=ratingNum*0.1
    ans+=rating * 0.3
    ans+=cat*0.3
    return ans


testFactor=8
for i in range(1,testFactor+1):#price
    for j in range(1,testFactor+1):#rating num
        for x in range(1,testFactor+1):#rating
            for y in range(1,testFactor+1): #categories
                temp=[]
                temp.append(y/float(testFactor))
                temp.append(i/float(testFactor))
                temp.append(x/float(testFactor))
                temp.append(j/float(testFactor))
                temp.append(getAns(temp))
                temp=[str(l) for l in temp]
                s+= ",".join(temp)
                s+="\n"
           

f.write(s)
f.close()