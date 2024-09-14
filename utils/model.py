from sklearn.cluster import KMeans
from numpy import concatenate, array
from utils.processing import inverse_scaling

def clustering(data, days):

    model = KMeans(n_clusters=days)
    model.fit(data)
    labels = model.labels_
    
    return labels