
from flask import Flask, request,jsonify
# from flask_restful import Resource, Api
# # from sqlalchemy import create_engine
# from json import dumps
# from flask.ext.jsonpify import jsonify

import numpy as np
import pandas as pd
import sys
import os
import json
import scipy
from sklearn.datasets import load_iris
from sklearn.svm import SVC

# sys.path.append(os.path.abspath("./model"))
# from load import * 
#initalize our flask app
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def predict():
          irisData = request.get_json()
          # print(irisData)

          X_test = pd.DataFrame.from_dict(irisData,orient='index')  
           
          values = (X_test.values).reshape(1,4)
          
          X_new = pd.DataFrame(values,columns=X_test.index)
          # from sklearn.datasets import load_iris
          iris = load_iris()
          df = pd.DataFrame(iris['data'],columns=iris['feature_names'])
          df['target'] = iris['target']  
          X = df.drop('target',axis=1)
          y = df['target'] 
          # from sklearn.svm import SVC
          model = SVC()
          model.fit(X,y)
          prediction = model.predict(X_new)      
          # prediction = 555
       


          return jsonify(np.asscalar(prediction[0]))






if __name__ == "__main__":
     #decide what port to run the app in
     # port = int(os.environ.get('PORT', 5000))
     #run the app locally on the givn port
     app.run(port=5000)