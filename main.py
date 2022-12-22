import streamlit as st
import pandas as pd

st.title("Data Explorer")
st.write("Data explorer app let's you see muliple csv files in interative mode and let you see their statistics and visualizaton")

uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True, type ="csv")
for uploaded_file in uploaded_files:
    with st.container():
      st.write("Data Description of file : ",uploaded_file.name)
      dataframe = pd.read_csv(uploaded_file)
      dataframe = dataframe.dropna()
      st.write("Dataframe overall view")
      st.dataframe(dataframe)
      st.write("Data types present in dataframe")
      st.table(dataframe.dtypes)
      st.write("Statistical Operations on dataframe")
      st.table(dataframe.describe())
      numerical = dataframe.select_dtypes(include=["number","float64"])
      cateogircal = dataframe.select_dtypes(include=["object_","object"])
      st.write("Seeing the correlation between numerical dataframe columns")
      st.table(numerical.corr())
      option_numerical = st.multiselect('Select which numerical columns to keep',list(numerical.columns))
      st.write('You selected:', option_numerical)
      option_categorical = st.multiselect('Select which categorical columns to keep',list(cateogircal.columns))
      st.write('You selected:', option_categorical)
      st.write("Bar chart of selected categorical columns")
      st.bar_chart(cateogircal[option_categorical])
      st.write("Line chart of selected numerical columns")
      st.line_chart(numerical[option_numerical])


    