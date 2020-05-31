## EXTRACT GENRE AND BUDGET FOR EACH PRODUCER

import pandas as pd
import numpy as np
import json
import csv
import math
from sklearn.cluster import KMeans

def genre_with_max_profit(producer_name, prd):
	
	#extracts all the unique genres in a list
	list1 = prd['Genres'].tolist()
	str1 = " ".join(list1)
	list2 = str1.split(" ")
	genres = np.unique(list2)

	genres_budget = {}
	genres_revenue = {}
	genres_profit_or_loss = {}

	#initialize budget,revenue and profit with 0
	for genre in genres:
		genres_profit_or_loss[genre] = 0
		genres_budget[genre] = 0
		genres_revenue[genre] = 0


	#calculate total budget and revenue for a particular producer in each genre
	for movies in prd[prd.Producers == producer_name].values.tolist():
		for genre in genres:
			if genre in movies[3]:
				genres_budget[genre] += movies[2]
				genres_revenue[genre] += movies[5]


	#calculate profit for a particular producer in each genre
	for genre in genres_profit_or_loss:
		if(genres_budget[genre]!=0):
			genres_profit_or_loss[genre] = (genres_revenue[genre] - genres_budget[genre]) / genres_budget[genre] * 100


	#convert to list and sort in descending order of profit
	list_genres = list(genres_profit_or_loss.items())
	top_genres = sorted(list_genres, key = lambda k:k[1], reverse=True)

	#Pick the genre with maximum profit
	genre_selected = top_genres[0][0]

	return genre_selected

def budget_revenue(producer_name, prd, genre_selected):

	#Traverse the list of all producers to check which producer has the maximum profit in that genre
	p = prd["Producers"].values.tolist()
	x = np.array(p)
	unique_producers = np.unique(x).tolist()

	new_list_budg = []
	new_list_rev = []
	new_list_prod = []

	for pr in unique_producers:
		gen_budg = 0
		gen_rev = 0
		count = 0
		for movies in prd[prd.Producers == pr].values.tolist():
			if genre_selected in movies[3]:
				count += 1
				gen_budg += movies[2]
				gen_rev += movies[5]
		if(gen_budg != 0 and gen_rev != 0):
			new_list_budg.append(gen_budg/count)
			new_list_rev.append(gen_rev/count)
			new_list_prod.append(pr)

	budget_revenue_dict = {}		
	budget_revenue_dict["producer_list"] = new_list_prod
	budget_revenue_dict["budg_of_sel_gen"] = new_list_budg
	budget_revenue_dict["rev_of_sel_gen"] = new_list_rev

	return budget_revenue_dict











