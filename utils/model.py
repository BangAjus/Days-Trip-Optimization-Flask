from sklearn.cluster import KMeans
from numpy import concatenate, array
from utils.processing import inverse_scaling

def clustering(data, days):

    colors = {'#e82020':0,
              '#221380':1,
              '#088012':2,
              '#d5d909':3,
              '#9009d9':4,
              '#f241d8':5,
              '#41f2c6':6,
              '#e87c23':7,
              '#7ef037':8,
              '#10bee6':9}
    
    colors = {i:j for i, j in zip(colors.values(),
                                  colors.keys())}
    
    model = KMeans(n_clusters=days)
    model.fit(data)
    labels = model.labels_
    coloring = array([colors[i] for i in labels])
    
    return labels, coloring