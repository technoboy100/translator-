import datetime as dt  
import streamlit as st
import requests
from bokeh.models.widgets import Div
import time
import webbrowser
now = dt.datetime.now()
st.write(f"It is {now}")
beluga_name =" Made by - beluga.jr "
st.write(f"{beluga_name}")
if st.button('Instagram'):
    js = "window.open('https://www.instagram.com/insane_havoc0p/')"  # New tab or window
    js = "window.location.href = 'https://www.instagram.com/insane_havoc0p/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
st.write("en -Englidh , de -Greman , zh-cn - chinese , Hi - hindi , ro -Romanian")
slangs = ('de','en', 'ro','hi', 'zh-cn')

tlangs = ('ro','zh-cn','de','hi','en')

sourceLang = st.selectbox('Select source language', slangs)

targetLang = st.selectbox('Select target language', tlangs)

sourceText = st.text_input("Enter text to translate:")

url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + sourceLang + "&tl=" + targetLang + "&dt=t&q=" + sourceText

response = requests.get(url)

if st.button('Translate'):

  result = response.text

  indexx = result.index('","')

  result = result[4:int(indexx)]
  st.success(result)
my_bar=st.progress(0)

for i in range(100):
  time.sleep(0.0)
  my_bar.progress(i+1)
