import threading
import time
import ParseData
#import YelpFetch
from Model import Model
#import firebase

def main():
    model = Model(4)
    Model.deleteModels()
    model.trainModel("train.txt")           
    print (model.getPrediction("predictdata.txt"))

    while True:
        
        time.sleep(1)
        print ("test")
        

if __name__ == "__main__":
    main()