import pandas as pd
import numpy as np
import math
import csv

df = pd.read_csv("../Datasets/producer_dataset.csv", encoding = 'ISO-8859-1')
coun = pd.read_csv("../Datasets/countries_dataset.csv", encoding = 'ISO-8859-1')
cnt = pd.read_csv("../Datasets/unique_countries.csv")

new_file = open("../Datasets/countries_genre_dataset.csv","w",encoding="utf-8",newline = '')
csv_writer = csv.writer(new_file)

list1 = df['Genres'].tolist()
str1 = " ".join(list1)
list2 = str1.split(" ")
genres = np.unique(list2)

countries = cnt['Countries']

producer_list = df['Producers'].tolist()
unique_producers = np.unique(producer_list)

producer_genre = {}

j = 0
for prd in unique_producers:
	print(str(j) + " " + prd)
	genre_country = {}
	for genre in genres:
		country_amount = [0] * len(countries)
		print(genre)
		movie_names = df[(df.Producers == prd) & (df.Genres.str.contains(pat = genre))]["Movie Title"].values
		print(movie_names)
		for movie in movie_names:
			print(movie)
			for i in range(0,len(countries)):
				if (len(coun[(coun.MovieTitle == movie)][countries[i]].values) > 0 and not math.isnan(coun[(coun.MovieTitle == movie)][countries[i]].values)):
					country_amount[i] = round((country_amount[i] + int(coun[(coun.MovieTitle == movie)][countries[i]].values)/len(movie_names)),2)
		if len(movie_names)>0:
			country_amount.insert(0,genre)
			country_amount.insert(0,prd)
			genre_country[genre] = country_amount
			print(genre_country[genre])
			csv_writer.writerow(genre_country[genre])
	j = j+1		



