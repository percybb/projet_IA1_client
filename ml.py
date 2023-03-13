import streamlit as st

import pandas as pd
import numpy as np
import json
import requests
# Predictive Modelling
url = "https://projet-ia1-app.herokuapp.com/predictive"


def ml_fucntion():

    transform_options = ["Normal",
                         "Rescale",
                         "Standardization",
                         "Normalization"]
    transform = st.selectbox("Select data transform",
                             transform_options)

    classifier_list = ["Logistic Regression",
                       "Decision Tree Classifier",
                       "Random Forest",
                       "K-Nearest Neighbors",
                       "Support Vector Classifier"]
    classifier = st.selectbox("Select classifier", classifier_list)
    # Add option to select classifiers
    # Add LogisticRegression
    sepalL = st.slider("Select the value of Sepal Length (cm):",
                       min_value=1.0, max_value=10.0, step=0.1)

    sepalW = st.slider("Select the value of Sepal Width (cm):",
                       min_value=1.0, max_value=10.0, step=0.1)

    petalL = st.slider("Select the value of Petal Length (cm):",
                       min_value=1.0, max_value=10.0, step=0.1)

    petalW = st.slider("Select the value of Petal Width (cm):",
                       min_value=1.0, max_value=5.0, step=0.1)

    requests_data = json.dumps(
        {'transform': transform, 'classifier': classifier, 'sepalL': sepalL, 'sepalW': sepalW, 'petalL': petalL, 'petalW': petalW})

    requespost = requests.post(url, requests_data)
    res = requespost.json()

    # Display dresults
    st.write('Prediction:', res['prediction'])
    st.write('Type:', res['type'])

    st.write('probability:', round(res['probability'], 4))
    st.dataframe(res['prob_total'])
#    st.dataframe(val2)
