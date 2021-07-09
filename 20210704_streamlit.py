# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Script dependencies
import os
import pandas as pd
import numpy as np
#from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.feature_extraction.text import CountVectorizer


### ------ Recommender engine - BACK-END -----


#df = pd.read_csv('DATA/cb_recommendations20000.csv')





### ------ Recommender Visualization - FRONT-END----




st.markdown("<h1 style='text-align: center; color: black;'>Board Game Recommender</h1>", unsafe_allow_html=True)
st.image('DATA/Catan.png',use_column_width=True)

folder= './DATA'

@st.cache
def load_data(nrows):
    data = pd.read_csv(folder+'/cb_recommendations.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(1000)
pop=pd.read_csv(folder+'/popular.csv')
cf = pd.read_csv(folder+'/cf_similars.csv')
#st.dataframe(pop)
game_list = data['game'].to_list()




# Recommender System algorithm selection
sys = st.radio("Select an algorithm",
                       ('Popularity',
                        'Content Based',
                        'Collaborative Filtering'))

# User preferences

st.write('### Enter Your Favorite Board Games')
game_1 = st.selectbox('Choose',game_list[:])
fav_games=game_1


# Perform top-10 board games recommendation generation
if sys == 'Popularity':
    if st.button("Recommend"):
        try:
            with st.spinner('Crunching the numbers...'):
                top_rec=pop['title']
                st.title("We think you'll like:")

                for i,j in enumerate(top_rec):
                    st.subheader(str(i+1)+'. '+j)
        except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                    
                    

if sys == 'Content Based':
    if st.button("Recommend"):
        try:
            with st.spinner('Crunching the numbers...'):
                for e in data['game'].iteritems():
                    if e[1] == fav_games:
                        idx=e[0]
                        t_r= data['recomendacion'][idx].replace('[','').replace(']','').replace("'",'')
                        top_rec=t_r.split(',')
                

            st.title("We think you'll like:")
            for i,e in enumerate (top_rec):
                st.subheader(str(i+1)+'. '+e)
        except:
            st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")




if sys == 'Collaborative Filtering':
    if st.button("Recommend"):
        try:
            with st.spinner('Crunching the numbers...'):
                for e in data['game'].iteritems():
                    if e[1] == fav_games:
                        idx=e[0]
                        t_r= cf['recommendation'][idx].replace('[','').replace(']','').replace("'",'')
                        top_rec=t_r.split(',')
        
            st.title("We think you'll like:")
            for i,e in enumerate (top_rec):
                st.subheader(str(i+1)+'. '+e)
        except:
            st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")

                   
                    

 



