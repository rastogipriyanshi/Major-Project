import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(df, index):
	return df[df.Index == index]["Actors"].values[0]

def get_index_from_title(df, actor):
	return df[df.Actors == actor]["Index"].values[0]

def combine_features(row):
	return str(row['Number of movies']) +" "+str(row['Number of awards'])+" "+row["Genres"]	


def get_similar_actors(actor_name):

	df = pd.read_csv("Datasets/actors_dataset.csv")

	features = ['Number of movies','Number of awards','Genres']

	for feature in features:
		df[feature] = df[feature].fillna('')

	df["combined_features"] = df.apply(combine_features,axis=1)

	cv = CountVectorizer()

	count_matrix = cv.fit_transform(df["combined_features"])

	cosine_sim = cosine_similarity(count_matrix) 

	actor_index = get_index_from_title(df, actor_name)

	similar_actors =  list(enumerate(cosine_sim[actor_index]))

	sorted_similar_actors = sorted(similar_actors,key=lambda x:x[1],reverse=True)

	actors_list = []
	i=0
	for element in sorted_similar_actors:
			actors_list.append(get_title_from_index(df, element[0]))
			i=i+1
			if i>5:
				break

	return actors_list
