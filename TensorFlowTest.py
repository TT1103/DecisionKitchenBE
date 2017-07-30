import tempfile
import urllib
import tensorflow as tf
import pandas as panda
import TestGenerator


COLUMNS = []
CATEGORIES = ["American", "Indian", "Chinese", "Sushi", "Mongolian"]
COLUMNS.extend(CATEGORIES)
COLUMNS.extend(["Price", "Rating", "Rating_Count", "Correctness"])
LABEL_COLUMN = "Label"
df_train = TestGenerator.make_test_vectors(3, 5, COLUMNS)
df_test = TestGenerator.make_test_vectors(200, 5, COLUMNS)


df_train[LABEL_COLUMN] = df_train["Correctness"]
df_test[LABEL_COLUMN] = df_test["Correctness"]



def input_fn(df):
  feature_cols = {i: tf.constant(df[i].values)
                     for i in COLUMNS}
  # Converts the label column into a constant Tensor.
  label = tf.constant(df[LABEL_COLUMN].values)
  # Returns the feature columns and the label.
  return feature_cols, label
model_dir = tempfile.mkdtemp()
feature_columns = [tf.contrib.layers.real_valued_column(i) for i in COLUMNS]

m = tf.contrib.learn.LinearClassifier(feature_columns=feature_columns, model_dir=model_dir)


def train_input_fn():
  return input_fn(df_train)

def eval_input_fn():
  return input_fn(df_test)

m.fit(input_fn=train_input_fn, steps=200)
results = m.evaluate(input_fn=eval_input_fn, steps=1)
for key in sorted(results):
    print("%s: %s" % (key, results[key]))
