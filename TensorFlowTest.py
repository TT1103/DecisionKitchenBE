import tempfile
import urllib
import tensorflow as tf
import pandas as pd


TRAINING_STEPS = 200

featureData = [] # get an array of values from austin that are already parsed

featureList = []
'''
#iterate through the featuresData and create a feature for each data piece
for i in range(len(featureData)):
    temp = tf.contrib.layers.real_valued_column(str(i))
    featureList.append(temp) 

ids = range(len(featureData))
'''
df_train = pd.read_csv(train_file, names=ids, skipinitialspace=True)
print (type(df_train))


'''


e = tf.contrib.learn.LinearClassifier(feature_columns=featureList) 
e.fit(input_fn=input_fn_train, steps=TRAINING_STEPS)

# Evaluate for one step (one pass through the test data).
results = e.evaluate(input_fn=input_fn_test, steps=1)

# Print the stats for the evaluation.
for key in sorted(results):
        print("%s: %s" % (key, results[key]))










#COLUMNS = ["Category", "Price", "Rating", "Rating_Count", "Correctness"]
#LABEL_COLUMN = "Label"
df_train =
df_test =
#df_train[LABEL_COLUMN] = df_train["Correctness"]
#df_test[LABEL_COLUMN] = df_test["Correctness"]


CATEGORICAL_COLUMNS = ["Category"]
CONTINUOUS_COLUMNS = ["Price", "Rating", "Rating_Count"]



def input_fn(df):
  continuous_cols = {i: tf.constant(df[i].values)
                     for i in CONTINUOUS_COLUMNS}
  categorical_cols = {k: tf.SparseTensor(
      indices=[[i, 0] for i in range(df[k].size)],
      values=df[k].values,
      dense_shape=[df[k].size, 1])
                      for k in CATEGORICAL_COLUMNS}
  # Merges the two dictionaries into one.
  feature_cols = dict(continuous_cols.items() + categorical_cols.items())
  # Converts the label column into a constant Tensor.
  label = tf.constant(df[LABEL_COLUMN].values)
  # Returns the feature columns and the label.
  return feature_cols, label





def train_input_fn():
  return input_fn(df_train)

def eval_input_fn():
  return input_fn(df_test)

  '''
