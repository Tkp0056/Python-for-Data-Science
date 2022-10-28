import streamlit as st
import pickle
import pandas as pd
import requests # to hit on API
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recommmend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.loc[i[0]].movie_id

       
        recommended_movies.append(movies.loc[i[0],'title'])
        recommended_movies_poster.append(fetch_poster(movie_id))       # fetch poster from API
    return recommended_movies,recommended_movies_poster

movie_dict=pickle.load(open('movies_dict.pkl','rb')) # deserialize 
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')       #Display text in title formatting

selected_movie_name=st.selectbox('Which movie do you like ? ', movies['title'].values) #Display a select widget

if st.button('Recommend'):
    names,posters=recommmend(selected_movie_name)
    col1, col2, col3,col4,col5= st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    