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
def get_batch_data():
    (train_data,test_data), info=tfds.load('imdb_reviews/subwords8k',split=(tfds.Split.TRAIN,tfds.Split.TEST),with_info=True,as_supervised=True)
    encoder=info.features['text'].encoder
    #print(encoder.subwords[:20])
    padded_shapes=([None],())#PADDING OUR DATA SO THAT THEY HAVE THE SAME SHAPE
    train_batches=train_data.shuffle(1000).padded_batch(10,padded_shapes=padded_shapes)
    test_batches=test_data.shuffle(1000).padded_batch(10,padded_shapes=padded_shapes)
    return train_batches,test_batches,encoder
def get_model():
    embedding_dim=16
    model=keras.Sequential([layers.Embedding(encoder.vocab_size,embedding_dim),layers.GlobalAveragePooling1D(),layers.Dense(1,activation='sigmoid')])
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    return model
def plot_data(history):
     history_dict=history.history
     acc=history_dict['accuracy']
     val_acc=history_dict['val_accuracy']
     epochs=range(1,len(acc)+1)
     plt.figure(figsize=(12,9))
     plt.plot(epochs,acc,'bo',label='Training acc')
     plt.plot(epochs,acc,'b',label='validation acc')
     plt.xlabel('Epochs')
     plt.ylabel('Accuracy')
     plt.legend(loc='lower right')
     plt.ylim((0.5,1))
     plt.show()

def retrieve_embeddings(model,encoder):



train_batches,test_batches,encoder=get_batch_data()
model=get_model(encoder)
history=model.fit(train_batches,epochs=10,validation_data=test_batches,validation_steps=20)
plot_data(history)
