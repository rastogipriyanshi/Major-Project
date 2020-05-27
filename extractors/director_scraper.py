import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests
import csv
import json
from googlesearch import search


new_file = open("directors_dataset.csv","w",encoding="utf-8",newline = '')

csv_writer = csv.writer(new_file)
csv_writer.writerow(['Directors', 'Number of movies', 'Number of awards'])

prd = pd.read_csv("directors.csv", encoding = 'ISO-8859-1')
new_director_list = prd['Directors'].tolist()

for director in new_director_list:
	print(director)
	query = director + " imdb"
	links = search(query, tld="co.in", num=1, stop=1, pause=3)
	for link in links:
		number_movies = 0
		number_awards = 0
		if("https://www.imdb.com/name" in link):
			source = requests.get(link).text
			soup = BeautifulSoup(source,'lxml')
			num_of_movies = soup.find("div",{"id" : ["filmo-head-director"]})
			num_of_awards = soup.find("span", class_ = "awards-blurb")
			if(num_of_movies is not None):
				res_mov = [int(i) for i in num_of_movies.text.split( )[3].split("(") if i.isdigit()]
				number_movies = sum(res_mov)
			print(number_movies)	
			if(num_of_awards is not None):
				res = [int(i) for i in num_of_awards.text.split( ) if i.isdigit()]
				number_awards = sum(res)
			print(number_awards)
		csv_writer.writerow([director, number_movies, number_awards])
