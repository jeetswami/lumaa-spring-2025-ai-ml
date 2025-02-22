#!/usr/bin/env python
# coding: utf-8

# # Importing Library

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# # Ioading Dataset

# In[2]:


df1 = pd.read_csv('movies.csv')    # Calling Dataset


# # Building Vectors

# In[3]:


# Fill NaN values with empty strings in overview, genres, keywords, cast, directors columns

df1['overview'] = df1['overview'].fillna('')
df1['genres'] = df1['genres'].fillna('')
df1['keywords'] = df1['keywords'].fillna('')
df1['cast'] = df1['cast'].fillna('')
df1['director'] = df1['director'].fillna('')

# Create 'combined_features' with all relevant text fields making them all lowercase
df1['combined_features'] = df1['overview'].str.lower() + ' ' + df1['genres'].str.lower() + ' ' + df1['keywords'].str.lower()


# In[4]:


# TF-IDF Vectorizer with optimized settings

tfidf = TfidfVectorizer(stop_words='english', max_features=10_000, ngram_range=(1,2))

tfidf_matrix = tfidf.fit_transform(df1['combined_features'])  # Convert text data into a numerical representation for similarity computations

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Map titles to indices
indices = pd.Series(df1.index, index=df1['title']).drop_duplicates()


# In[5]:


# Function for user-input-based recommendations
def movie_recommendations(user_input, df1):
    user_tfidf = tfidf.transform([user_input])
    
    # Compute similarity
    cosine_sim_user_input = cosine_similarity(user_tfidf, tfidf_matrix)
    similar_scores = list(enumerate(cosine_sim_user_input[0]))
    
    # Sort by similarity
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)

    # Remove first result if it's an exact match
    if similar_scores[0][1] == 1.0:
        similar_scores = similar_scores[1:6]
    else:
        similar_scores = similar_scores[:5]

    # Extracting movie indices
    movie_indices = [i[0] for i in similar_scores]
    similarity_scores = [i[1] for i in similar_scores]

    # Get recommended movies
    recommended_movies = df1.loc[movie_indices, ['title']].copy()

    return recommended_movies


# # Result Sections

# In[6]:


user_input = input("Please enter your input: ")
print(movie_recommendations(user_input, df1))

