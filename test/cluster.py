import numpy as np, csv, time
from sklearn.cluster import AgglomerativeClustering

start = time.time()

seed = 123

np.random.seed(seed)

filename = '../data/med.csv'

data = np.array(list(csv.reader(open(filename, "rU"), dialect=csv.excel_tab, delimiter=",")))

print("Shape of our data object = {}.".format(data.shape))

location_matrix = data[1 : , [0 , 1]]

n = 10

ward = AgglomerativeClustering(n_clusters = n, linkage = 'ward')

labels = ward.fit_predict(location_matrix)

print("Shape of our labels object = {}.".format(labels.shape))

np.set_printoptions(threshold = np.inf)

# Allows me to print full array...

print(labels)

print("Took {} seconds.".format(time.time() - start))

print("Process complete.")