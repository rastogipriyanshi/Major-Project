from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np
import json
import csv
import math
from sklearn.cluster import KMeans

genre="Action"
producer="3 Arts Entertainment"
gen=pd.read_csv("genres.csv")
pro=pd.read_csv("producer_dataset.csv")
pro_list=gen['Producers'].tolist()


df=pd.DataFrame(pro_list)


new_list_budg = []
new_list_rev = []
new_list_pro = []

for p in pro_list:
    gen_budg = 0
    gen_rev = 0
    count=0
    for movies in pro[pro.Producers == p].values.tolist():
        if genre in movies[3]:
            count=count+1
            gen_budg += movies[2]
            gen_rev += movies[5]
    if(gen_budg!=0 and gen_rev!=0):

        new_list_budg.append(gen_budg/count)
        new_list_rev.append(gen_rev/count)
        new_list_pro.append(p)
        
cl=pd.DataFrame()
cl.insert(0, "budg_of_sel_gen", new_list_budg)
cl.insert(1, "rev_of_sel_gen", new_list_rev)

index_value = new_list_pro.index(producer)
#print("The index of input producer is",index_value)

kmeans = KMeans(n_clusters=2,random_state=3425).fit(cl)
centroids = kmeans.cluster_centers_


plt.scatter(cl['budg_of_sel_gen'], cl['rev_of_sel_gen'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("Average Budget")
plt.ylabel("Average Revenue")
cluster_map = pd.DataFrame()
cluster_map['data_index'] = cl.index.values
cluster_map['cluster'] = kmeans.labels_

cluster_map[cluster_map.cluster == 3]
# with pd.option_context('display.max_rows', 1325, 'display.max_columns', None):  # more options can be specified also
#     print(cluster_map)

cluster_num=kmeans.labels_[index_value]
print("cluster number of input producer",cluster_num)

#print("centroids are",centroids[cluster_num])
