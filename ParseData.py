def combineUserAndYelp(userData, yelpData):
    '''
    userData: [categories, price]
    yelpData: [categories, price, rating, rating #] 
    
    '''
    #combine and normalize as needed
    
    userCat= userData[0]
    yelpCat= yelpData[0]
    
    tmp=userCat[::]
    for i in range(len(tmp)):
        tmp[i] *=yelpCat[i]
    
    catSum = sum(tmp)
    
    
    userPrice = userData[1]
    yelpPrice = yelpData[1]/4.0
    
    
    rating = yelpData[2]/5.0
    ratingNum = yelpData[3]/100.0
    
    overAllPrice = userPrice - yelpPrice
    overAllPrice/=2.0
    overAllPrice+=0.5
    
    
    return [catSum, overAllPrice, rating, ratingNum ]