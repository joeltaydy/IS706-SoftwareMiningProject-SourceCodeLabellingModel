# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:55:16 2020

@author: Rico
"""
from sklearn.externals import joblib
from keras import models
from keras.metrics import top_k_categorical_accuracy 
import functools
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np
import tensorflow as tf
import keras

def test(input_code):
    
    top1_acc = functools.partial(tf.keras.metrics.top_k_categorical_accuracy, k=1)
    top5_acc = functools.partial(tf.keras.metrics.top_k_categorical_accuracy, k = 5)
    top1_acc.__name__ = 'top1_acc'
    top5_acc.__name__ = 'top5_acc'
    
    def auc(y_true, y_pred):
        auc = tf.metrics.auc(y_true, y_pred)[1]
        keras.backend.get_session().run(tf.local_variables_initializer())
        return auc 
    
    tokenizer = joblib.load("tokenizer.pickle")
    multilabel_binarizer = joblib.load("binarizer.pickle")
    classifier = models.load_model("model/basic_model_word_embedding.h5", 
                                   custom_objects={'top1_acc':top1_acc, 'top5_acc':top5_acc, 'auc':auc})
    
    text_labels = multilabel_binarizer.classes_
    

    sequences = tokenizer.texts_to_sequences([input_code])
    x = pad_sequences(sequences, maxlen=200, padding='post')
    
    predictions = classifier.predict(x)

    predicted = predictions[0]

    prediction_list = []
    for i, prob in enumerate(predicted):
        if prob > 0.4:
            print(text_labels[i])
            prediction_list.append(text_labels[i])
    print(prediction_list)
    return prediction_list
    

if __name__ == '__main__':
    input_code = """
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

    """
    test(input_code)