import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rake_nltk import Rake
import pandas as pd
import numpy as np
from .models import NGO

#df = pd.read_csv("data.csv")
def generate_recommendations(data, title): 
    df = data
    df = df[['Name', 'Cause', 'City', 'Details']]
    df.fillna("null", inplace=True)

    count = CountVectorizer()

    df['Keywords'] = ""
    df['bag_of_words'] = ""

    for index, row in df.iterrows():
        details = row['Details']
        causes = row['Cause']
        r = Rake()
        r.extract_keywords_from_text(details)
        keywords_dict_scores = r.get_word_degrees()
        keywords = list(keywords_dict_scores.keys())
        keywordString = ""
        for keyword in keywords:
            keywordString = keywordString + " " + keyword
        x = Rake()
        x.extract_keywords_from_text(causes)
        keywords_cause = x.get_word_degrees()
        keys = list(keywords_cause.keys())
        causeString = ""
        for cause in keys:
            causeString = causeString + " " + cause

        keywordString += " "
        keywordString += causeString
        row['Keywords'] = keywordString

        cityString = ""
        
        cities = row['City']
        if cities is not "null":
            cityString = cities.lower()
        
        row['bag_of_words'] = cityString + keywordString


    df.drop(columns = ['Cause', 'City', 'Details', 'Keywords'], inplace = True)
    df.set_index('Name', inplace = True)


    count_matrix = count.fit_transform(df['bag_of_words'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    indices = pd.Series(df.index)

# def recommendations(title, cosine_sim = cosine_sim):
    recommended_ngos = []
    idx = indices[indices == title].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_10_indexes = list(score_series.iloc[1:4].index)
    for i in top_10_indexes:
        recommended_ngos.append(list(df.index)[i])
    return recommended_ngos
print(NGO.objects.all())