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
data_load_state.text("Done!")


choose2 = st.multiselect('Which games do you like? Select two', data['name'],format_func= lambda x:'Select an option' if x== '' else x)

if len(choose2) ==1:
    st.success('First game!')
elif len(choose2) == 2:
    st.success('Second game!')
elif len(choose2) >= 3:
    st.warning('Only two games!')

else:
    st.warning('No option is selected')

'You selected: ',choose2[:2]






    





    




