import pandas as pd
import numpy as np
import csv

df = pd.read_csv("movie_dataset.csv")
df1 = pd.read_csv("movie_metadata.csv")

new_file = open("directors.csv", "w", encoding = "utf-8", newline='')
csv_writer = csv.writer(new_file)
csv_writer.writerow(['Directors','Genres','Number of FB likes'])


p = df["director"].values.tolist()

x = np.array(p)

prod = np.unique(x).tolist()
genre_list = []
fb_likes = []

for comp in prod:
	genre_list.append(df[df.director == comp]["genres"].values.tolist())

i=0
for comp in prod:
	print(i)
	print(df1[df1.director_name==comp]["director_facebook_likes"].values.tolist())
	i+=1
	if (len(df1[df1.director_name==comp]["director_facebook_likes"].values.tolist()) > 0):
		fb_likes.append(df1[df1.director_name==comp]["director_facebook_likes"].values.tolist()[0])
	else :
		fb_likes.append(0)

genre_list3 = []

i=0
for g in genre_list:
	str1=" ".join(g)
	genre_list2=str1.split(" ")
	un_list = np.unique(genre_list2)
	genre_list3.append(un_list.tolist())

i=0
for comp in prod:
	csv_writer.writerow([comp,genre_list3[i],fb_likes[i]])
	i=i+1
