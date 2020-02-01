import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rake_nltk import Rake
import pandas as pd
import numpy as np

def rec_events(data, title):
    df = data
    df = df[['Name', 'Purpose']]
    count = CountVectorizer()
    df['bag_of_words'] = ""

    for index, row in df.iterrows():
        purpose = row["Purpose"]
        r = Rake()
        r.extract_keywords_from_text(purpose)
        keywords_dict_scores = r.get_word_degrees()
        keywords = list(keywords_dict_scores.keys())
        keywordString = ""
        for keyword in keywords:
            keywordString = keywordString + " " + keyword
        row['bag_of_words'] = keywordString

    count_matrix = count.fit_transform(df['bag_of_words'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    df.drop(columns=["Purpose"], inplace=True)
    df.set_index("Name", inplace=True)
    indices = pd.Series(df.index)

    recommended_events = []
    idx = indices[indices == title].index[0]
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
    top_3_indexes = list(score_series.iloc[1:4].index)
    for i in top_3_indexes:
        recommended_events.append(list(df.index)[i])
    return recommended_events