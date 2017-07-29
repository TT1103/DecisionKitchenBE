import tempfile
import urllib
import tensorflow as tf
import pandas as panda


COLUMNS = ["Category", "Price", "Rating", "Rating_Count", "Correctness"]
LABEL_COLUMN = "Label"
#df_train =
#df_test =


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


category =  tf.contrib.layers.sparse_column_with_hash_bucket("Category", hash_bucket_size=200)
price = tf.contrib.layers.real_valued_column("age")
rating = tf.contrib.layers.real_valued_column("age")
rating_count = tf.contrib.layers.real_valued_column("age")
#This will probably break, useful tho
#rating_and_count = tf.contrib.layers.crossed_column([rating, rating_count])



def train_input_fn():
  return input_fn(df_train)

def eval_input_fn():
  return input_fn(df_test)