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

image1 = "https://cf.geekdo-images.com/itemrep/img/YkRbhRKwFAkS917yqf50cvtNAog=/fit-in/246x300/pic5073276.jpg"
image2 = "https://cf.geekdo-images.com/itemrep/img/YkRbhRKwFAkS917yqf50cvtNAog=/fit-in/246x300/pic5073276.jpg"
image3 = "https://cf.geekdo-images.com/itemrep/img/IBtRtMGWMXEXCVHroWqbbPT8I1g=/fit-in/246x300/pic2439223.jpg"
image4 = "https://cf.geekdo-images.com/itemrep/img/0_gpX_v9CeKcm60nSkDzi47PVOA=/fit-in/246x300/pic361592.jpg"
image5= "https://cf.geekdo-images.com/itemrep/img/xAtnSiJMCFYKpOy9mujcchgZ4jo=/fit-in/246x300/pic1638795.jpg"

indice = ['Nemesis', 'Nemesis','Otro','Otro mas', 'No sé cual es']
st.image([image1,image2, image3, image4, image5], width=150, caption= indice)






    





    




