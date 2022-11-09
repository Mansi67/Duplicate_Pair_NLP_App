import streamlit as st
import helper
import pickle
import bz2file as bz2

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

rf_final = decompress_pickle('model_compressed.pbz2')
#rf_final = pickle.load(open('C:/Users/mansi/OneDrive/Desktop/Study/Data_Science_Projects/Quora_Question_Pairs/pythonProject1/rf_final.pkl','rb'))


st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = rf_final.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
