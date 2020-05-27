# An Intelligent Decision Support System for Movie Production Company

* The proposed model is an intelligent decision support system for the movie production company to make decisions at the earliest stage of production and thus prevent huge investment losses.
* The system recommends the right combination of actors, directors and the countries to release the movie prior the investment is made which will help in maximizing the profit of the production company. 
* The proposed system uses hybrid algorithm to recommend based on the detailed analysis of the Internet Movie Database(IMDb), Box Office Mojo and The Movies Dataset that uses both content-based and collaborative filtering techniques for better recommendation.
* In this system, using __data analysis__ the data is arranged in descending order of profit earned by each genre and the genre with maximum profit is selected.
* The system uses user-based __collaborative filtering__ technique and finds out similar producers using __k- means clustering__ taking average budget and average revenue as the features for a particular genre in which the input producer has maximum profit . The __Silhouette algorithm__ will find out the optimal number of clusters.
* Using __content-based filtering__, similarity between the cast of input producer and the cast working with the producers similar to input producer is calculated using __cosine-similarity__ and the most similar cast is recommended.


