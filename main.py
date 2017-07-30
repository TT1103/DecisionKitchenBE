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
    fb = FBData("2120b04c-bd1e-42c8-abf1-08fd8fde8133")
    
    yelp = YelpFetcher(['breakfast_brunch', 'chinese', 'diners', 'hotdogs', 'hotpot', 'italian', 'japanese',   'korean', 'mongolian', 'pizza', 'steak', 'sushi', 'tradamerican', 'vegetarian'])
    
    
      
    time.sleep(1)
    print ("running")
    
    if True:
        userRestData, userPriceComp, userCatData, userDelivData = fb.start()

        userArr=[]
        #userArr contains [categoriesArr, price]
        #firebaserestArry contains [categoriesArr, priceArr] 
        #
        print (userRestData)        
        
        userCatComp=[0.0 for x in range(len(userCatData[0]))]
        cnt=0.0
        for c in userCatData:
            for i in range(len(c)):
                userCatComp[i] += c[i]
            cnt+=1.0

        userCatComp = [x/cnt for x in userCatComp]

        userArr = [userCatComp, userPriceComp]

        print (userCatData)
        yelpRestDict = {} #dict of restaurants to query key: id, value: vector [categoryArr, price, rating, rating #

        yelpRestData = yelp.vectors_nearest(37.5737019, -122.3269701, True)
        for i in range(len(userCatComp)):
            x=userCatComp[i]
            if x != 0 : #query restaurants for this category if not zero

                yelpId = yelpRestData[i][0]["id"]
                yelpRestDict[str(yelpId)] = yelpRestData[i][1]



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
        
        print (retDict)
       # fb.saveResponse(retDict)






if __name__ == "__main__":
    main()