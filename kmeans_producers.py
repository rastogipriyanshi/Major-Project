import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.collections

def get_similar_producers(budget_revenue_dict, producer_name):

	producers_list = budget_revenue_dict["producer_list"];

	producer_index_value = producers_list.index(producer_name)
	# Creates a data frame consisting of revenue and budget of all the producers for k-means clustering
	cluster_data_frame = pd.DataFrame()		
	cluster_data_frame.insert(0, "budg_of_sel_gen", budget_revenue_dict["budg_of_sel_gen"])
	cluster_data_frame.insert(1, "rev_of_sel_gen", budget_revenue_dict["rev_of_sel_gen"])
	
	#creates a k-means cluster	
	kmeans = KMeans(n_clusters=2).fit(cluster_data_frame)
	centroids = kmeans.cluster_centers_


	plt.scatter(cluster_data_frame['budg_of_sel_gen'], cluster_data_frame['rev_of_sel_gen'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
	plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

	cluster_map = pd.DataFrame()
	cluster_map['data_index'] = cluster_data_frame.index.values
	# Findes the cluster of all the producers
	cluster_map['cluster'] = kmeans.labels_

	# Gets the cluster of input producers
	cluster_num=cluster_map['cluster'][producer_index_value]

	X=[]
	for i in range(0,len(producers_list)):
	    Z = []
	    Z.append(budget_revenue_dict["budg_of_sel_gen"][i])
	    Z.append(budget_revenue_dict["rev_of_sel_gen"][i])
	    X.append(Z)

	# Gets all the points in the cluster given   
	d = kmeans.transform(X)[:,cluster_num]
	# Sorts the points by nearest to the cluster
	producer_indexes = np.argsort(d)[::][:10]

	return producer_indexes

