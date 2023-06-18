import streamlit

streamlit.title('My parents new Healthy diner')

streamlit.header('Breakfast Favourites')
streamlit.text(' 🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 kale, spinach & Rocket smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Tange Egg')
streamlit.text(' 🥑🍞 Avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)                
