import tempfile
import urllib
import tensorflow as tf
import pandas as pd


TRAINING_STEPS = 1000
LABEL_COLUMN = "label"
LEARNING_RATE = 0.1
FEATURE_COLUMNS = []
COLUMNS = []
df_train = None
df_predict = None
featureList = None
def input_fn(df):
    continuous_cols = {i: tf.constant(df[i].values) for i in FEATURE_COLUMNS}
    feature_cols = dict(continuous_cols.items())
    label = tf.constant(df[LABEL_COLUMN].values)
    return feature_cols, label


def train_input_fn():
    return input_fn(df_train)

def predict_input_fn():
    continuous_cols = {i: tf.constant(df_predict[i].values) for i in FEATURE_COLUMNS}
    feature_cols = dict(continuous_cols.items())
    return feature_cols

def trainModel(filename, numFeatures):
    global FEATURE_COLUMNS
    global COLUMNS
    global df_train
    global df_predict
    global featureList
    
    COLUMNS = [str(x) for x in range(numFeatures)]
    FEATURE_COLUMNS = COLUMNS[:-1]
    featureList=[tf.contrib.layers.real_valued_column(i) for i in FEATURE_COLUMNS]
    df_train  = pd.read_csv(filename, names=COLUMNS, skipinitialspace=True)
        
    for c in COLUMNS:
        df_train[c] = df_train[c].astype(float)

    df_train[LABEL_COLUMN] = df_train[COLUMNS[-1]].astype(float)

    e = tf.contrib.learn.LinearRegressor(feature_columns=featureList, optimizer=tf.train.FtrlOptimizer(
        learning_rate=LEARNING_RATE),model_dir="/Users/azzy_/Desktop/angelhack/DecisionKitchenBE/model")
    e.fit(input_fn=train_input_fn, steps=TRAINING_STEPS)
    
    df_predict = pd.read_csv("predictdata.txt", names=FEATURE_COLUMNS, skipinitialspace=True)
    

def getBestRestaurants(filename, numFeatures):
    global df_predict 
    global FEATURE_COLUMNS
    
    FEATURE_COLUMNS = [str(x) for x in range(numFeatures)]
    df_predict = pd.read_csv(filename, names=FEATURE_COLUMNS, skipinitialspace=True)

    featureList = [tf.contrib.layers.real_valued_column(i) for i in FEATURE_COLUMNS]

        
    e = tf.contrib.learn.LinearRegressor(feature_columns=featureList, optimizer=tf.train.FtrlOptimizer(
        learning_rate=LEARNING_RATE),model_dir="/Users/azzy_/Desktop/angelhack/DecisionKitchenBE/model")
    
    print("Predicting Data:")
    results = e.predict_scores(input_fn=predict_input_fn)
    for key in sorted(results):
        print(key)
        
        
trainModel("train.txt", 5)
getBestRestaurants("test.txt", 4)