import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sb
import requests
import plotly.express as px

import seaborn as sns
import json

url = "http://127.0.0.1:8008/df"


def eda_fun():
    st.subheader("Exploratory data analisys")
    st.write("EDA")
    transform_options = ["Normal",
                         "Rescale",
                         "Standardization",
                         "Normalization"]

    transform = st.selectbox("Select data transform",
                             transform_options)

    if st.checkbox("show raw Data"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/df", requests_data)
        res = requespost.json()
        st.dataframe(res)

    if st.checkbox("Show missng values"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/missing", requests_data)
        res = requespost.json()
        st.dataframe(res)

    if st.checkbox("Show data types"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/df", requests_data)
        res = pd.DataFrame(requespost.json())
        st.dataframe(res.dtypes)

    if st.checkbox("show Descriptive statistics"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/descriptive", requests_data)
        res = requespost.json()
        st.dataframe(res)

    if st.checkbox("Show Correlation Matrix"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/corr", requests_data)
        res = requespost.json()
        corr = pd.DataFrame(res)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        mask = np.triu(np.ones_like(corr, dtype=bool))
        sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm")
        st.pyplot()

    if st.checkbox("Show Histogram for each attributes"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/df", requests_data)
        res = pd.DataFrame(requespost.json())
        for col in res.columns:
            fig, ax = plt.subplots()
            ax.hist(res[col], bins=20, density=True, alpha=0.5)
            ax.set_title(col)
            st.pyplot(fig)

    if st.checkbox("Show Density for each attributes"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/df", requests_data)
        res = pd.DataFrame(requespost.json())
        for col in res.columns:
            fig, ax = plt.subplots()
            sns.kdeplot(res[col], fill=True)
            ax.set_title(col)
            st.pyplot(fig)

    if st.checkbox("Show Scatter plot"):
        requests_data = json.dumps(
            {'transform': transform})
        requespost = requests.post(
            "https://projet-ia1-app.herokuapp.com/df", requests_data)
        res = pd.DataFrame(requespost.json())
        # st.write(res.columns)
        fig = px.scatter(res, x=res.columns[0], y=res.columns[1])
        st.plotly_chart(fig)
