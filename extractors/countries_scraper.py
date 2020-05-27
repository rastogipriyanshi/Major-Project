import pandas as pd
import csv
from bs4 import BeautifulSoup
import requests
import csv
import json
from googlesearch import search
import re

prd = pd.read_csv("movie_dataset.csv", encoding = 'ISO-8859-1')
list2 = prd['original_title'].tolist()

movies_dict = {}
for movie in list2:
	countries_dict = {}
	print(movie)
	query = movie + " box office mojo"
	links = search(query, tld="com", num=10, stop=10, pause=3)
	for link in links:
		tables = []
		if("https://www.boxofficemojo.com/release" in link):
			print(link)
			source1 = requests.get(link).text
			soup1 = BeautifulSoup(source1,'lxml')
			movie_link = soup1.find("select", {"name": "release-picker-navSelector"}).find("option")['value']
			print(movie_link)
			source = requests.get("https://www.boxofficemojo.com/"+movie_link).text
			soup = BeautifulSoup(source,'lxml')
			tables = soup.findAll("table")
			for table in tables:
				rows = table.findAll("tr")
				for row in rows:
					data = row.findAll("td")
					if(data):
						countries_dict[data[0].text] = data[3].text	
			movies_dict[movie] = countries_dict
			break

list_of_countries = []
for movie in list2:
	if movie in movies_dict.keys():
		cont_dic = movies_dict[movie]
		for key in cont_dic.keys():
			if key not in list_of_countries:
				list_of_countries.append(key)
final_list = []
print(len(list_of_countries))

for movie in list2:
	list_of_gross = []
	if movie in movies_dict.keys():
		cont_dic = movies_dict[movie]
		for c in list_of_countries:
			if c in cont_dic.keys():
				list_of_gross.append(cont_dic[c])
			else:
				list_of_gross.append(0)
	print(movie)
	list_of_gross.insert(0,movie)			
	print(list_of_gross)
	final_list.append(list_of_gross)

list_of_countries.insert(0, 'Movie Title')
df = pd.DataFrame(final_list, columns = list_of_countries)
print(df)

df.to_csv('countries_data.csv')
