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

st.subheader('Raw dataframe')
st.write(data)

option1 = st.selectbox(
    'Which game do you like best?',
     data['name'])

'You selected: ', option1

option2= st.selectbox(
    'Do you want to add another game that you like?',
    data['name'])
'You selected: ', option2

players= [1,2,3,4,5,6,7,8,9,10]
option3= st.selectbox(
    'For how many players',
    players)
'You selected: ', option3

#choose = st.multiselect('Which games do you like? Select two', data['name'],format_func= lambda x:'Select an option' if x== '' else x)
#if len(choose)==1:
    #st.success('Goog game!')
#elif len(choose)==2:
    #st.success('Goog game!')
#elif len(choose)>=3:
    #st.warning('Only two games!')
#else:
    #st.warning('No option is selected')

#'You selected: ',choose[:2]


choose2 = st.multiselect('Which games do you like? Select two', data['name'],format_func= lambda x:'Select an option' if x== '' else x)

for elem in choose2:
    
    if len(choose2)==1:
        st.success('Goog game!')
    elif len(choose2)==2:
        st.success('Goog game!')
    elif len(choose2)>=3:
        st.warning('Only two games!')
        break
    else:
        st.warning('No option is selected')

'You selected: ',choose2[:2]





#Imagenes
#pics = {
    #"Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
    #"Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
    #"Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg"
#}
#pic = st.selectbox("Picture choices", list(pics.keys()), 0)
#st.image(pics[pic], use_column_width=True, caption=pics[pic])
    





    




