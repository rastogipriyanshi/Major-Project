import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests
import csv
import json
from googlesearch import search



new_file = open("actors_dataset.csv","w",encoding="utf-8",newline = '')

csv_writer = csv.writer(new_file)
csv_writer.writerow(['Actors', 'Number of movies', 'Number of awards'])


actor_list = []
prd = pd.read_csv("producer_dataset.csv", encoding = 'ISO-8859-1')
list1 = prd['Cast'].tolist()
for ele in list1:
	list2 = ele.split(" ")
	for i in range(0,len(list2),2):
		if((i+1) < len(list2)):
			str_name = list2[i] + " " + list2[i+1]
			actor_list.append(str_name)
		else:
			str_name = list2[i]
			actor_list.append(str_name)

new_actor_list = []
new_num_movies_list = []

for actor in actor_list:
	if(actor not in new_actor_list):
		new_actor_list.append(actor) 


for actor in new_actor_list:
	query = actor + " imdb"
	links = search(query, tld="co.in", num=1, stop=1, pause=2)
	for link in links:
		number_movies = 0
		number_awards = 0
		if("https://www.imdb.com/name" in link):
			source = requests.get(link).text
			soup = BeautifulSoup(source,'lxml')
			num_of_movies = soup.find("div",{"id" : ["filmo-head-actor", "filmo-head-actress"]})
			num_of_awards = soup.find("span", class_ = "awards-blurb")
			if(num_of_movies is not None):
				res_mov = [int(i) for i in num_of_movies.text.split( )[3].split("(") if i.isdigit()]
				number_movies = sum(res_mov)
			print(number_movies)	
			if(num_of_awards is not None):
				res = [int(i) for i in num_of_awards.text.split( ) if i.isdigit()]
				number_awards = sum(res)
			print(number_awards)
		csv_writer.writerow([actor, number_movies, number_awards])