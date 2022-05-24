#Modules Imported
import pickle
import requests
import streamlit as st
from PIL import Image

im=Image.open('logo.jpg')
st.set_page_config(
        page_title="TK Movie Recommendation System",
        page_icon=im,
        layout="wide",
    )

#Fetch poster function
#display the recommended movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=961f5addacb70ea48b126b4ab888904f&language=en-US".\
        format(movie_id)
    #api key = 961f5addacb70ea48b126b4ab888904f
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + str(poster_path)
    return full_path


#Movie Recommender function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters


#display the overall window
st.title('Movie Recommender System')
name=st.text_input("Enter your Name : ")
age=st.slider("Enter your Age : ",min_value=0,max_value=100)
if (not(age and name)):
    st.warning("Please fill out the above fields")


#loads .pkl files
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


#button
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


#html
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: variable;
left: 0;
bottom: 0;
width: 100%;
background-color: wheat;
color: darkred;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with 💗 by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/tusharkhanna5112/" target="_blank">Tushar Khanna</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)