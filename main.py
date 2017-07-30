import threading
import time
import ParseData
#import YelpFetch
import Model
#import firebase

def main():
    Model.deleteModels()
    model = Model(4)
    model.trainModel("train.txt")
    print (model.getPrediction("predictdata.txt"))

    while True:
        
        time.sleep(1)
        print ("test")
        

if __name__ == "__main__":
    main()