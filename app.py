import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('Toxic Comment Classification')

tweet = st.text_input("Type your tweet", max_chars=100)

if st.button('Classify Tweet'):
    result = pipe.predict([tweet])
    toxic = result[0][0]
    severe_toxic = result[0][1]   
    obscene = result[0][2]        
    threat = result[0][3]       
    insult = result[0][4]       
    identity_hate = result[0][5]

    if(toxic == 1):
        st.write('Toxic')
    if(severe_toxic == 1):
        st.write('Severe Toxic')
    if(obscene == 1):
        st.write('Obscene')
    if(threat == 1):
        st.write('Threat')
    if(insult == 1):
        st.write('Insult')
    if(identity_hate == 1):
        st.write('Identity Hate')