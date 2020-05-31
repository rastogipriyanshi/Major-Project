from budget_revenue_extractor import budget_revenue,genre_with_max_profit
from kmeans_producers import get_similar_producers
from cosine_similarity_actor import get_similar_actors
from cosine_similarity_directors import get_similar_directors
from profitable_countries import get_profitable_countries
import pandas as pd


producer_dataset = pd.read_csv("Datasets/producer_dataset.csv", encoding = 'ISO-8859-1')

# For example 1492 Pictures
producer_name = input("Enter the name of the producer : ")
print("Selected producer is : " + producer_name)

# Gets the genre with maximum profit
selected_genre = genre_with_max_profit(producer_name, producer_dataset)
print("Genre with highest profit for " + producer_name + " is : " + selected_genre)

# Gets list of budget and revenue of all the producers for the selected genre
budget_revenue_dict = budget_revenue(producer_name, producer_dataset, selected_genre)

# Gets the list of similar producers
similar_producer_index = get_similar_producers(budget_revenue_dict, producer_name)
producers_list = budget_revenue_dict["producer_list"];

print("Producers similar to ", producer_name, " are : ")

actors_list = []
directors_list = []
# Prints the name of similar producers
for i in similar_producer_index:
    print(producers_list[i])
    # Gets the list of cast for the given producer and selected genre
    cast_list = producer_dataset[(producer_dataset.Producers == producers_list[i]) & (producer_dataset.Genres.str.contains(pat = selected_genre))]["Cast"].values[0]
    cast_split = cast_list.split(" ")
    actors = [cast_split[i] + " " + cast_split[i+1] for i in range(0,len(cast_split),2)]
    actors_list.extend(actors)
    # Gets the list of director for the given producer and selected genre
    director_names = producer_dataset[(producer_dataset.Producers == producers_list[i]) & (producer_dataset.Genres.str.contains(pat = selected_genre))]["Director"].values
    directors_list.extend(director_names)

print("==========================================")

unique_actors_set = set(actors_list)
unique_actors_list = list(unique_actors_set)

# Prints similar actors to the one's which have brought high profits to the producer
for actor in unique_actors_list:
	print("Actors similar to ", actor, " are : ")
	similar_actors = get_similar_actors(actor)
	for similar_actor in similar_actors:
		if actor != similar_actor:
			print(similar_actor)

print("==========================================")	

unique_directors_set = set(directors_list)
unique_directors_list = list(unique_directors_set)	

# Prints similar directors to the one's which have brought high profits to the producer
for director in unique_directors_list:
	print("Directors similar to ", director, " are : ")
	similar_directors = get_similar_directors(director)
	for similar_director in similar_directors:
		if director != similar_director:
			print(similar_director)	

print("==========================================")

print("Top profitable countries for", producer_name, " are : ")
# Gets top 5 countries to release
profitable_countries = get_profitable_countries(producer_name, selected_genre)
for country in profitable_countries:
	print(country)
   
