import pandas as pd

def get_profitable_countries(producer_name, selected_genre):

	df = pd.read_csv("Datasets/countries_genre_dataset.csv")
	row = df[(df.Producers == producer_name) & (df.Genre == selected_genre)][df.columns[2:]]
	countries_list = row.values[0].tolist()
	countries_list.sort(reverse = True)
	countries = []
	for value in countries_list[:5]:
		countries.append((row == value).idxmax(axis=1).values[0])

	return countries
	
