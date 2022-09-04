import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Sitraka FORLER, Data Expert')

st.info('Economist and Data Scientist! Combine economic thinking systems and new technologies (from data pipelines to advanced and improved predictive models).')

icon_size = 20


st_button('medium', 'https://medium.com/@sitrakaforler', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/ForlerSitraka', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/sitraka-matthieu-forler/', 'Follow me on LinkedIn', icon_size)
st_button('youtube', 'https://www.youtube.com/channel/UC9SHkerBF56p-skyKbm7NpQ', 'Personnal YouTube channel', icon_size)
st_button('youtube', 'https://www.linkedin.com/in/sitraka-matthieu-forler/', 'Sitraka Data YouTube channel', icon_size)
st_button('medium', 'https://www.sitraka.fr/', 'Personnal Web Site', icon_size)
#st_button('Blog', 'https://sites.google.com/view/sitrakamatthieuforler/home', 'My personnal Web Site', icon_size)
# https://sitraka17-linktree-streamlit-app-3xiqa5.streamlitapp.com/
