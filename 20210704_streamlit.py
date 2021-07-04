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

df = pd.read_csv('DATA/r_users_bgs.csv')



















### ------ Recommender Visualization - FRONT-END----




st.markdown("<h1 style='text-align: center; color: black;'>Board Game Recommender</h1>", unsafe_allow_html=True)
st.image('DATA/Catan.png',use_column_width=True)

folder= './DATA'


def load_titles(path_to_games):
    df = pd.read_csv(path_to_games)
    df = df.drop_duplicates()
    game_list = df['Game'].to_list()
    return game_list

title_list = load_titles(folder+'/r_users_bgs.csv')




# Recommender System algorithm selection
sys = st.radio("Select an algorithm",
                       ('Popularity',
                        'Content Based',
                        'Collaborative Based Filtering'))

# User preferences

st.write('### Enter Your TWO Favorites Board Games')
game_1 = st.selectbox('Fisrt Option',title_list[:400000])
game_2 = st.selectbox('Second Option',title_list[400000:])
fav_games = [game_1,game_2]


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
                    
                    
if sys == 'Content Based Filtering':
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










    





    




