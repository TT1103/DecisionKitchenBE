import tempfile
import urllib
import tensorflow as tf
import pandas as pd


TRAINING_STEPS = 200
LABEL_COLUMN = "label"
COLUMNS = ["a","b","c"]

df_train  = pd.read_csv("traindata.txt", names=COLUMNS, skipinitialspace=True)
#print (type(df_train))
#print (df_train)

featureList=[]
a = tf.contrib.layers.real_valued_column("a")
featureList.append(a) 

b = tf.contrib.layers.real_valued_column("b")
featureList.append(b) 



df_train[LABEL_COLUMN] = df_train["c"].astype(float)

def input_fn(df):
  continuous_cols = {i: tf.constant(df[i].values)
                     for i in COLUMNS}
  
  # Merges the two dictionaries into one.
  feature_cols = dict(continuous_cols.items())
  # Converts the label column into a constant Tensor.
  label = tf.constant(df[LABEL_COLUMN].values)
  # Returns the feature columns and the label.
  return feature_cols, label





def train_input_fn():
  return input_fn(df_train)

def eval_input_fn():
  return input_fn(df_test)


e = tf.contrib.learn.LinearClassifier(feature_columns=featureList) 
e.fit(input_fn=train_input_fn, steps=1)


print (e)

results = e.evaluate(input_fn=train_input_fn, steps=1)
for key in sorted(results):
    print ("%s: %s" % (key, results[key]))

'''
# Evaluate for one step (one pass through the test data).
results = e.evaluate(input_fn=input_fn_test, steps=1)

# Print the stats for the evaluation.
for key in sorted(results):
        print("%s: %s" % (key, results[key]))
'''

