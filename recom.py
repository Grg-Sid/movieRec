import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

movies = pd.read_csv("movies.csv")

movies = movies[['name', 'genre','director', 'writer', 'star', 'country', 'company']].copy()
movies = movies.dropna()

combined = ''
for i in movies:
    combined = combined+" "+movies[i] 
    
vectorizer=TfidfVectorizer()
feature_vector=vectorizer.fit_transform(combined)
similarity=cosine_similarity(feature_vector)

ind = []
for i in range(7646):
    ind.append(i)
    
movies['index'] = ind

result = []

def recommend(title):
    movie_title = title
    
    res = []
    
    list_movie = movies['name'].tolist()
    find_close_match = difflib.get_close_matches(movie_title,list_movie)
    close_match = find_close_match[0]
    
    name_index = movies[movies.name == close_match]['index'].values[0]    
    
    similarity_score = list(enumerate(similarity[name_index]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
        
    i=1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies[movies.index == index]['name']
        if(i < 10):
            res.append(title_from_index.values[0])
            i+=1
    
    result = res
    # print(result)
    return result

recommend("Avatar")
    
