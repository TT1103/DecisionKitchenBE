import tensorflow as tf
import pandas as pd
import shutil

TRAINING_STEPS = 1000
LABEL_COLUMN = "label"
LEARNING_RATE = 0.1
MODEL_DIR="./model"

class Model():
    def __init__(self, numFeatures):

        global TRAINING_STEPS
        global LABEL_COLUMN
        global LEARNING_RATE
        global MODEL_DIR
        
        self.FEATURE_COLUMNS = []
        self.COLUMNS = []
        self.df_train = None
        self.df_predict = None
        self.featureList = None
        self.curModel = None
        self.numFeatures = numFeatures
    
    @staticmethod
    def deleteModels():
        shutil.rmtree(MODEL_DIR)
        
        
    def input_fn(self, df):
        continuous_cols = {i: tf.constant(df[i].values) for i in self.FEATURE_COLUMNS}
        feature_cols = dict(continuous_cols.items())
        label = tf.constant(df[LABEL_COLUMN].values)
        return feature_cols, label

    
    def train_input_fn(self):
        return self.input_fn(self.df_train)

    
    def predict_input_fn(self):
        continuous_cols = {i: tf.constant(self.df_predict[i].values) for i in self.FEATURE_COLUMNS}
        feature_cols = dict(continuous_cols.items())
        return feature_cols

    
    def trainModel(self, filename):
        self.COLUMNS = [str(x) for x in range(self.numFeatures)]
        self.FEATURE_COLUMNS = self.COLUMNS[:-1]
        fList = [tf.contrib.layers.real_valued_column(i) for i in self.FEATURE_COLUMNS]
        self.df_train  = pd.read_csv(filename, names=self.COLUMNS, skipinitialspace=True)

        for c in self.COLUMNS:
            self.df_train[c] = self.df_train[c].astype(float)

        self.df_train[LABEL_COLUMN] = self.df_train[self.COLUMNS[-1]].astype(float)

        e = tf.contrib.learn.LinearRegressor(feature_columns = fList, optimizer = tf.train.FtrlOptimizer(
            learning_rate = LEARNING_RATE), model_dir = MODEL_DIR)
        
        e.fit(input_fn = self.train_input_fn, steps = TRAINING_STEPS)

        self.curModel = e
        self.featureList = fList
    
    
    def loadModel(self):
        self.FEATURE_COLUMNS = [str(x) for x in range(self.numFeatures-1)]

        self.featureList = [tf.contrib.layers.real_valued_column(i) for i in self.FEATURE_COLUMNS]

        self.curModel = tf.contrib.learn.LinearRegressor(feature_columns = self.featureList, optimizer = tf.train.FtrlOptimizer(learning_rate = LEARNING_RATE), model_dir = MODEL_DIR)
       
        
    def getPrediction(self, filename):
        if (not self.curModel):
            self.loadModel()

        print("Predicting Data:")
        self.df_predict = pd.read_csv(filename, names = self.FEATURE_COLUMNS, skipinitialspace = True)

        results = self.curModel.predict_scores(input_fn = self.predict_input_fn)
        ret = []
        for r in sorted(results):
            ret.append(r)
        return ret
            
        
Model.deleteModels()
model = Model(4)
model.trainModel("train.txt")
print (model.getPrediction("predictdata.txt"))
