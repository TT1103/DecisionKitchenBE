import tempfile
import urllib
import tensorflow as tf
import pandas as pd


TRAINING_STEPS = 200
COLUMNS = ["Category_rank", "Price", "Rating", "Rating_Count", "Correctness"]
LABEL_COLUMN = "Label"
df_train = pd.read_csv("train.txt", names=COLUMNS, skipinitialspace=True)
df_test = pd.read_csv("test.txt", names=COLUMNS, skipinitialspace=True)

featureList=[tf.contrib.layers.real_valued_column(i) for i in COLUMNS]



df_train[LABEL_COLUMN] = df_train["Correctness"]
df_test[LABEL_COLUMN] = df_test["Correctness"]

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

model_dir = tempfile.mkdtemp()
e = tf.contrib.learn.LinearRegressor(feature_columns=featureList, model_dir=model_dir)
e.fit(input_fn=train_input_fn, steps=TRAINING_STEPS)


print(e)
''
results = e.predict_scores(input_fn=eval_input_fn)
for key in sorted(results):
    print(key)
'''
# Evaluate for one step (one pass through the test data).
results = e.evaluate(input_fn=input_fn_test, steps=1)

# Print the stats for the evaluation.
for key in sorted(results):
        print("%s: %s" % (key, results[key]))
'''

