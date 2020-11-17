import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tfds.disable_progress_bar()
def plot_graphs(history, metric):
    plt.plot(history.history[metric])
    plt.plot(history.history['val_'+metric],'')
    plt.xlabel=("Epochs")
    plt.ylabel=(metric)
    plt.legend([metric, 'val_'+metric])


dataset,info=tfds.load('imdb_reviews',with_info=True,as_supervised=True)
train_data,test_data=dataset['train'],dataset['test']
for example, label in train_data.take(1):
  print('text: ', example.numpy())
  print('label: ', label.numpy())
"""

encoder=info.features['text'].encoder
BUFFER_SIZE=10000
BATCH_SIZE=64
padded_shapes=([None],())
train_data=train_data.shuffle(BUFFER_SIZE).padded_batch(BATCH_SIZE,padded_shapes=padded_shapes)
test_data=test_data.shuffle(BUFFER_SIZE).padded_batch(BATCH_SIZE,padded_shapes=padded_shapes)
model=tf.keras.Sequential([tf.keras.layers.Embedding(encoder.vocab_size,64),tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),tf.keras.layers.Dense(64,activation='relu'),tf.keras.layers.Dense(1,activation='sigmoid')])
model.compile(loss='binary_crossentropy',optimizer=tf.keras.optimizers.Adam(1e-4),metrics=['accuracy'])
history=model.fit(train_data,epochs=5,validation_data=test_data,validation_steps=30)


def pad_to_size(size,vec):
    zeros=[0]*(size-len(vec))
    vec.extend(zeros)
    return vec

def sample_predict(sentence,pad):
    encoded_sample_pred_text=encoder.encode(sentence)
    if pad:
        encoded_sample_pred_text=pad(encoded_sample_pred_text,64)
        encoded_sample_pred_text=tf.cast(encoded_sample_pred_text,tf.float32)
        predictions=model.predict(tf.expand_dims(encoded_sample_pred_text,0))
sample_text='this movie was awsome.The acting was incredible.Highly recommend it'
predictions=sample_predict(sample_text,pad=True)*100
print("probability this is a positive review: %.2f" % predictions)
sample_text='this movie was so so.The acting was mediocre.kind of recommend it'

predictions=sample_predict(sample_text,pad=True)*100
print("probability this is a me  review: %.2f" % predictions)
"""
