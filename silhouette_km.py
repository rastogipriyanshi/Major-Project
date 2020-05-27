from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.collections
import numpy as np
import json
import csv
import math
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,davies_bouldin_score,v_measure_score

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

    
km_silhouette = []
# db_score=[]

for i in range(2,7):
    km = KMeans(n_clusters=i, random_state=0).fit(cl)
    preds = km.predict(cl)
    
    
    silhouette = silhouette_score(cl,preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i,silhouette))

    print("-"*100)
plt.figure(figsize=(7,4))
plt.title("The silhouette coefficient method \nfor determining number of clusters\n",fontsize=16)
plt.scatter(x=[i for i in range(2,7)],y=km_silhouette,s=150,edgecolor='k')
plt.grid(True)
plt.xlabel("Number of clusters",fontsize=14)
plt.ylabel("Silhouette score",fontsize=15)
plt.xticks([i for i in range(2,7)],fontsize=14)
plt.yticks(fontsize=15)
plt.show()

