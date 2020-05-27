## CONVERT MOVIE DATA SET TO PRODUCER DATA SET WITH MULTIPLE ROWS OF SINGLE PRODUCER


import pandas as pd
import json
import csv


df = pd.read_csv("movie_dataset.csv", dtype = 'unicode')

new_file = open("producer_dataset.csv","w",encoding="utf-8",newline = '')

csv_writer = csv.writer(new_file)
csv_writer.writerow(['Id' , 'Producers', 'Budget', 'Genres', 'Movie Title', 'Revenue','Cast', 'Director', 'Overview', 'Keywords'])

p = df["production_companies"].values.tolist() 

b = df["budget"].values
g = df["genres"].values
t = df["original_title"].values
r = df["revenue"].values
ca = df["cast"].values
d = df["director"].values
o = df["overview"].values
k = df["keywords"].values


i = 0;
for companies in p:
	json_comp = json.loads(companies)
	for value in json_comp:
		csv_writer.writerow([value["id"],value['name'],b[i],g[i],t[i],r[i],ca[i],d[i],o[i],k[i]])
	i=i+1
	