import tempfile
import urllib
import tensorflow as tf
import pandas as pd


TRAINING_STEPS = 1000
LABEL_COLUMN = "label"
def input_fn(df):
    continuous_cols = {i: tf.constant(df[i].values) for i in FEATURE_COLUMNS}
    print ("Cont cols: ", continuous_cols)
    feature_cols = dict(continuous_cols.items())
    print ("Featurecols: ",feature_cols)
    # Converts the label column into a constant Tensor.
    label = tf.constant(df[LABEL_COLUMN].values)
    print ("Label: " , label)
    # Returns the feature columns and the label.
    return feature_cols, label


def train_input_fn(df_train):
    return input_fn(df_train)

def eval_input_fn():
    return input_fn(df_test)

def predict_input_fn():
    df=df_predict
    continuous_cols = {i: tf.constant(df[i].values) for i in ["a","b"]}
    feature_cols = dict(continuous_cols.items())
    return feature_cols


def trainModel(inputData):
    
    COLUMNS = ["a","b","c"]
    FEATURE_COLUMNS = ["a","b"]

    df_train  = pd.read_csv("traindata.txt", names=COLUMNS, skipinitialspace=True)
    df_test = pd.read_csv("testdata.txt", names=COLUMNS, skipinitialspace=True)
    df_predict = pd.read_csv("predictdata.txt", names=["a","b"], skipinitialspace=True)
    #print (type(df_train))
    #print (df_train)

    featureList=[]
    a = tf.contrib.layers.real_valued_column("a")
    featureList.append(a) 

    b = tf.contrib.layers.real_valued_column("b")
    featureList.append(b) 

    print ("DF: ", df_train["c"])

    df_train["label"] = df_train["c"].astype(float)
    df_test["label"] = df_test["c"].astype(float)

    df_train["a"] = df_train["a"].astype(float)
    df_train["b"] = df_train["b"].astype(float)
    df_train["c"] = df_train["c"].astype(float)

    df_test["a"] = df_test["a"].astype(float)
    df_test["b"] = df_test["b"].astype(float)
    df_test["c"] = df_test["c"].astype(float)

    

    e = tf.contrib.learn.LinearRegressor(feature_columns=featureList, optimizer=tf.train.FtrlOptimizer(
        learning_rate=0.1),model_dir="/Users/TigerZhao/Desktop/angelhack/DecisionKitchenBE/model") 
    e.fit(input_fn=train_input_fn, steps=TRAINING_STEPS)


    print (e)

    print ("Showing test results:")
    results = e.predict_scores(input_fn=predict_input_fn)
    for key in sorted(results):
        print (key)



    '''
    # Evaluate for one step (one pass through the test data).
    results = e.evaluate(input_fn=input_fn_test, steps=1)

    # Print the stats for the evaluation.
    for key in sorted(results):
            print("%s: %s" % (key, results[key]))
    '''

trainModel()
def getBestRestaurants(predictData):
    pass
