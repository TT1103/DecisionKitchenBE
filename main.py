import threading
import time
import ParseData
from YelpFetch import YelpFetcher
from Model import Model
from firebase import FBData

def main():
    model = Model(4)
   # model.trainModel("official_train.txt")           
    #print (model.getPrediction("predictdata.txt"))
    model.loadModel()
    fb = FBData("-KqK2DFRvziwDxcMqXnm")
    
    yelp = YelpFetcher(['breakfast_brunch', 'chinese', 'diners', 'hotdogs', 'hotpot', 'italian', 'japanese',   'korean', 'mongolian', 'pizza', 'steak', 'sushi', 'tradamerican', 'vegetarian'])
    
    done=False
    while not done:
        time.sleep(1)
        print ("waiting")
        done=fb.is_done(2)
    

    time.sleep(1)
    print ("running")


    userRestData, userPriceComp, userCatData, userDelivData = fb.start()

    userArr=[]
    #userArr contains [categoriesArr, price]
    #userRestData firebaserestArry contains [categoriesArr, priceArr,rating, rating #] 
    #
    print ("user rest data: ",userRestData)        
    userCatComp=[0.0 for x in range(len(userCatData[0]))]
    cnt=0.0
    for c in userCatData:
        for i in range(len(c)):
            userCatComp[i] += c[i]
        cnt+=1.0

    userCatComp = [x/cnt for x in userCatComp]

    userArr = [userCatComp, userPriceComp]

    yelpRestDict = {} #dict of restaurants to query key: id, value: vector [categoryArr, price, rating, rating #

    yelpRestData = yelp.vectors_nearest(37.5737019, -122.3269701, True)
    for i in range(len(userCatComp)):
        x=userCatComp[i]
        if x != 0 : #query restaurants for this category if not zero

            yelpId = yelpRestData[i][0]["id"]
            yelpRestDict[str(yelpId)] = yelpRestData[i][1]



    #check yelp restaurants
    restKeyList = list(yelpRestDict.keys())

    fileStr=""
    for k in restKeyList:
        tmp = ParseData.combineUserAndYelp(userArr, yelpRestDict[k])

        tmp = [str(x) for x in tmp]
        fileStr +=",".join(tmp) +"\n"

    f= open("official_predict.txt", "w")
    f.write(fileStr)
    f.close()

    predictions = model.getPrediction("official_predict.txt")

    retDict ={}

    for i in range(len(restKeyList)):
        retDict[restKeyList[i]] = predictions[i]


    #check user restaurants:
    fileStr=""
    userRestDict={} # key: id, value: vector
    for d in userRestData:
        userRestDict[d[0]["id"]] = d[1]

    userRestKeyList = list(userRestDict.keys())
    for k in userRestKeyList:
        tmp = ParseData.combineUserAndYelp(userArr, userRestDict[k])

        tmp = [str(x) for x in tmp]
        fileStr +=",".join(tmp) +"\n"

    f= open("official_predict.txt", "w")
    f.write(fileStr)
    f.close()

    predictions = model.getPrediction("official_predict.txt")

    for i in range(len(userRestKeyList)):
        retDict[userRestKeyList[i]] = predictions[i] +0.5

    retList= sorted(retDict.items(), key=lambda value: value[1])
    retList = [list(x) for x in retList]

    for k in retList:
        k[1]=str(k[1])
    print (retList)
    fb.push_update(retList)



if __name__ == "__main__":
    main()