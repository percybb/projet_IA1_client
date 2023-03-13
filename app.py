import pandas as pd
import numpy as np
import streamlit as st
import matplotlib as plt
from sklearn.datasets import load_iris
# from sklearn.neighbors import neighbors_class

import plotly.express as px
from eda import eda_fun
from ml import ml_fucntion


st.set_page_config(page_title="Eda page",
                   layout="centered",
                   initial_sidebar_state="auto"
                   )

st.title("EDA and Predictive Modeling")

option = ["EDA", "Predictive modelling"]

selected_option = st.sidebar.selectbox("Selected Option", option)


# def file_selector(folder_path='.'):
#    filenames = os.listdir(folder_path)
#    selected_filename = st.selectbox('Select a file', filenames)
#    return os.path.join(folder_path, selected_filename)


# filename = file_selector()
# st.write('You selected `%s`' % filename)

if selected_option == "EDA":
    eda_fun()
    
elif selected_option == "Predictive modelling":
    st.subheader("Predictive Modelling")
    st.write("Choose a transform type and model from the option below:")
    ml_fucntion()
