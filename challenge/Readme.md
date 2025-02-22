About Dataset

This dataset, downloaded from Kaggle, is intended for building movie recommendation systems. It includes a diverse range of movies across different genres, time periods, and regions, along with details such as cast, crew, director, and an overview. The dataset contains 4,803 rows and 24 attributes.

dataset download link: https://www.kaggle.com/datasets/abdallahwagih/movies


Steps for loading the dataset:
If you are using Jupyter Notebook, follow these steps to download and upload the dataset for successful execution:

1) Ensure that the required libraries are installed.
2) In the next cell, load your movies.csv dataset. Ensure that the movies.csv file is in the same directory as your Jupyter Notebook, or specify the full path to the file.

Python Version:
Python 3.10.9 (Packaged by Anaconda, Inc.)
Anaconda Base Environment (64-bit)

Result Explanation:

When a user inputs a query like "I like Batman movies," the system processes the text and matches it with movies that share similar features, such as genres, keywords, and descriptions. The system will return a list of movies, such as Batman Returns, Batman: The Dark Knight Returns, Part 2, and The Dark Knight which are thematically similar to the Batman franchise based on high cosine similarity scores. Other movies like Grindhouse may also appear due to shared elements like action or thriller genres, even though they are not directly linked to the Batman universe. The recommendations are ranked by their similarity to the user's input, with Batman-related titles appearing at the top.