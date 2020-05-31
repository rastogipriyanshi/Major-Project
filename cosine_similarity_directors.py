import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(df, index):
	return df[df.Index == index]["Directors"].values[0]

def get_index_from_title(df, director):
	return df[df.Directors == director]["Index"].values[0]

def combine_features(row):
	return str(row['Number of movies']) +" "+str(row['Number of awards'])+" "+str(row['Number of Facebook Likes'])+" "+row["Genres"]	


def get_similar_directors(director_name):

	df = pd.read_csv("Datasets/directors_dataset.csv")

	features = ['Number of movies','Number of awards','Number of Facebook Likes','Genres']

	for feature in features:
		df[feature] = df[feature].fillna('')	

	df["combined_features"] = df.apply(combine_features,axis=1)

	cv = CountVectorizer()

	count_matrix = cv.fit_transform(df["combined_features"])

	cosine_sim = cosine_similarity(count_matrix) 

	director_index = get_index_from_title(df, director_name)

	similar_directors =  list(enumerate(cosine_sim[director_index]))

	sorted_similar_directors = sorted(similar_directors,key=lambda x:x[1],reverse=True)

	director_list = []
	i=0
	for element in sorted_similar_directors:
			director_list.append(get_title_from_index(df, element[0]))
			i=i+1
			if i>5:
				break

	return director_list			
