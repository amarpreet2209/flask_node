# coding: utf-8

# In[1]:
from flask import Flask, request
from flask_restful import Resource, Api
# from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# get_ipython().magic('matplotlib inline')

app = Flask(__name__)

@app.route('/', methods=['POST'])
  def Ex():
    
  # In[2]:

          from sklearn.datasets import load_iris


          # In[7]:

          iris = load_iris()


          # In[13]:

          # iris.keys()


          # In[14]:

          df = pd.DataFrame(iris['data'],columns=iris['feature_names'])


          # In[26]:

          # df.head()


          # # In[29]:

          # iris['target_names']


          # # In[30]:

          # iris['target']


          # In[31]:

          df['target'] = iris['target']


          # In[35]:

          # df.head()


          # In[34]:

          from sklearn.model_selection import train_test_split


          # In[39]:

          X = df.drop('target',axis=1)


          # In[42]:

          y = df['target']


          # In[44]:

          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


          # In[45]:

          from sklearn.svm import SVC


          # In[47]:

          model = SVC()


          # In[48]:

          model.fit(X_train,y_train)


          # In[49]:

          predictions = model.predict(X_test)


          # In[50]:

          from sklearn.metrics import classification_report,confusion_matrix


          # In[51]:

          print(confusion_matrix(y_test,predictions))
          print('\n')
          print(classification_report(y_test,predictions))


          # In[ ]:



