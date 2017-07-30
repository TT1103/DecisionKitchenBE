from random import random, randint
#[American, Chinese, Indian, Japanese, Mongolian, price, rating, # rating]
s=""
f=open("train.txt","w")


def getAns(arr):
    ratingNum = arr[-1]
    rating = arr[-2]
    price = arr[-3]
    
    numCat = len(arr)-3
    
    
    '''
    rating: 0.3
    price: 0.3
    ratingNum 0.1
    categories: 0.3
    
    '''
    ans=0
    ans+=price * 0.2
    ans+=ratingNum*0.1
    ans+=rating * 0.3
    
    for c in arr[:numCat]:
        ans+= (c/float(numCat)) *0.3
    return ans


for i in range(1,6):#price
    for j in range(1,6):#rating num
        for x in range(1,6):#rating
            for y in range(1,6): #categoriess
                temp = [0]*5
                temp[y-1]=i/5.0
                temp.append(i/5.0)
                temp.append(x/5.0)
                temp.append(j/5.0)
                temp.append(getAns(temp))
                temp=[str(l) for l in temp]
                s+= ",".join(temp)
                s+="\n"
           

f.write(s)
f.close()