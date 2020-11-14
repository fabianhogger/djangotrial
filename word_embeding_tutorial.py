import io
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets  as tfds

#embedding_layer=layers.Embedding(1000,5)
#result=embedding_layer(tf.constant([1,2,3]))
#print(result.numpy())
#print(result.numpy().shape)
(train_data,test_data), info=tfds.load('imdb_reviews/subwords8k',split=(tfds.Split.TRAIN,tfds.Split.TEST),with_info=True,as_supervised=True)
encoder=info.features['text'].encoder
print(encoder.subwords[:20])
