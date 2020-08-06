import streamlit as st
import pandas as pd
import numpy as np

st.title('Game Recommended')

folder= './Data'

@st.cache
def load_data(nrows):
    data = pd.read_csv(folder+'/Top100game.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(100)
data_load_state.text("Done! (using st.cache)")

st.subheader('Dataframe')
st.write(data)

option = st.selectbox(
    'Which game do you like best?',
     data['name'])

'You selected: ', option
