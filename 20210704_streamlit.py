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
    data = pd.read_csv(folder+'/cb_recommendations20000.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(1000)
#st.dataframe(data)
game_list = data['game'].to_list()


#title_list = load_titles(folder+'/r_users_bgs.csv')
#title_list = load_titles(folder+'/cb_recommendations20000.csv')




# Recommender System algorithm selection
sys = st.radio("Select an algorithm",
                       ('Popularity',
                        'Content Based',
                        'Collaborative Based Filtering'))

# User preferences

st.write('### Enter Your TWO Favorites Board Games')
game_1 = st.selectbox('Fisrt Option',game_list[:])
#game_2 = st.selectbox('Second Option',title_list[400000:])
#fav_games = [game_1,game_2]
fav_games=game_1


# Perform top-10 board games recommendation generation
if sys == 'Popularity':
    if st.button("Recommend"):
        try:
            with st.spinner('Crunching the numbers...'):
                top_recommendations = content_model(game_list=fav_movies,
                                                            top_n=10)
                st.title("We think you'll like:")

                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
        except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")
                    
                    

if sys == 'Content Based':
    if st.button("Recommend"):
        with st.spinner('Crunching the numbers...'):
            for e in data['game'].iteritems():
                if e[1] == fav_games:
                    idx=e[0]
                    t_r= data['recomendacion'][idx].replace('[','').replace(']','').replace("'",'')
                    top_rec=t_r.split(',')
                

            st.title("We think you'll like:")
            for i,e in enumerate (top_rec):
                st.subheader(str(i+1)+'. '+e)




if sys == 'Collaborative Based Filtering':
    if st.button("Recommend"):
        try:
            with st.spinner('Crunching the numbers...'):
                top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
        except:
            st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


