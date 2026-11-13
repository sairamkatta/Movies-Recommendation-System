import streamlit as st
import pickle
import nltk
import sklearn
import pandas as pd
import joblib


st.title("Movie Recommend System")

with open("movies.pickle", "rb") as m:
    movies=pickle.load(m)

similarties=joblib.load("similarties.joblib")

movie_names=movies['title'].values

def recommend(name_movie):
    
    movie_index = movies[movies["title"] ==name_movie].index[0]
    
    recommendations = similarties[movie_index]
    
    movies_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies 
        
name_movie=st.selectbox("Enter the Movie Name :",movie_names)

if st.button("Recommend"):
    r=recommend(name_movie)
    
    st.write("The Recommend Movies are :")
    
    for i in r:
        st.write(i)