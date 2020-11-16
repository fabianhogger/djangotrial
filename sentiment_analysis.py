import tensorflow_datasets as tfds
import tensorflow as tf

dataset,info=tfds.load('imdb_reviews/subwords8k',with_info=True,as_supervised=True)
train_data,test_data=dataset['train'],dataset['test']
encoder=info.features['text'].encoder
BUFFER_SIZE=10000
BATCH_SIZE=64
padded_shapes=([None],())
train_data=train_data.shuffle(BUFFER_SIZE).padded_batch(BATCH_SIZE,padded_shapes=padded_shapess)
test_data=test_data.shuffle(BUFFER_SIZE).padded_batch(BATCH_SIZE,padded_shapes=padded_shapess)
