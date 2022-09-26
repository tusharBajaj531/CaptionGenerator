#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import keras
import pickle
from keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input,ResNet50
from keras.models import Model, load_model
from keras.preprocessing.sequence import pad_sequences
from keras.layers.merge import add


# In[4]:


model = load_model("static/model_weights/model_19.h5")    


# In[5]:


model_temp = ResNet50(weights="imagenet",input_shape=(224,224,3))


# In[6]:


model_resnet = Model(model_temp.input,model_temp.layers[-2].output)


# In[7]:


def preprocessing_img(img):
    img = image.load_img(img,target_size=(224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img,axis=0)
    #Normalisation
    img = preprocess_input(img)
    return img


# In[13]:


def encode_image(img):
    img = preprocessing_img(img)
    feature_vector = model_resnet.predict(img)
    feature_vector = feature_vector.reshape(1,2048)
#     print(feature_vector.shape)
    return feature_vector


# In[14]:



# In[15]:



# In[18]:


max_len = 35


# In[25]:


with open("static/saved/word_to_idx.pkl","rb") as f:
    word_to_idx = pickle.load(f)

with open("static/saved/idx_to_word.pkl","rb") as f:
    idx_to_word = pickle.load(f)


# In[26]:


def predict_caption(photo):
    
    in_text = "startseq"
    for i in range(max_len):
        sequence = [word_to_idx[w] for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence],maxlen=max_len,padding='post')
        
        ypred = model.predict([photo,sequence])
        ypred = ypred.argmax() #WOrd with max prob always - Greedy Sampling
        word = idx_to_word[ypred]
        in_text += (' ' + word)
        
        if word == "endseq":
            break
    
    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)
    return final_caption


# In[28]:

def caption_this_image(image):
    
    enc = encode_image(image)
    caption = predict_caption(enc)

    return caption


# In[ ]:




