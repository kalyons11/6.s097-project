import numpy as np, csv, time, random
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import sqrt

# Config.

filename = '../data/med.csv'
do_plot = True
n_clusters = 10

# End config.

start = time.time()

seed = 123

np.random.seed(seed)

data = np.array(list(csv.reader(open(filename, "rU"), dialect=csv.excel_tab, delimiter=",")))

location_matrix = data[1 : , [0 , 1]]

cluster = KMeans(n_clusters = n_clusters, tol = 1e-8)

cluster.fit_predict(location_matrix)

labels = cluster.labels_

centers = list(cluster.cluster_centers_)

i = cluster.inertia_

# print("Shape of our labels object = {}.".format(labels.shape))

np.set_printoptions(threshold = np.inf)

# Allows me to print full array...

data = np.array(list(csv.reader(open(filename, "rU"), dialect=csv.excel_tab, delimiter=",")))

loc_data = np.array(data[1: , [0 , 1]]).astype('float64')

# now import picture

if do_plot:
	img = mpimg.imread('../code/capture2.png')
	imgplot = plt.imshow(img)

# now calculate x and y values of picture
# picture is 621 pixels high and 588 pixels wide

	y_margin = (42.40-42.23)/621.0
	x_margin = (-70.96+71.18)/588.0

	area = 5

clusters = {} # Dict mapping labels to lists of tuples of locations AND max distance...

def dist(x1, y1, x2, y2):
	return sqrt((x2 - x1)**2 + (y2-y1)**2)

for i in range(n_clusters):
	# i represents cluster ID
	current = []
	for j in range(labels.shape[0]):
		d = labels[j]
		if d == i:
			r = loc_data[j]
			current.append([r[0], r[1]])
	# Now, find max_dist
	c_x, c_y = centers[i][0], centers[i][1]
	max_dist = 0
	for p in current:
		x, y = p[0], p[1]
		d = dist(c_x, c_y, x, y)
		if d > max_dist:
			max_dist = d
	clusters[i] = {'dist' : max_dist, 'points' : current}

# Now, we want to shave to clusters within a certain range...
# Get clusters with highest crime frequency, ignore others.

threshold = 80

while min([len(clusters[e]['points']) for e in clusters]) < threshold:
	# Remove one with the max...
	m = float('inf')
	i = -1
	for c in clusters:
		if len(clusters[c]['points']) < m:
			m = len(clusters[c]['points'])
			i = c
	print(m)
	clusters.pop(i, None)
	try:
		centers.pop(i)
	except Exception as e:
		centers.pop()

color_list = []

for i in clusters:
	if do_plot:
		x_list = []
		y_list = []
	for j in range(labels.shape[0]):
		d = labels[j]
		if d == i:
			# We are in the correct cluster.
			r = loc_data[j]
			if do_plot:
				x = 588 -(-1*r[1] - 70.96)/x_margin
				x_list.append(x)
				y = (42.40 - r[0])/y_margin
				y_list.append(y)
	if do_plot:
		colors = np.random.rand(3,)
		color_list.append(colors)
		plt.scatter(x_list, y_list, s = area, c = colors, marker='o', lw=0)

# Also plot cluster centers.

'''
if do_plot:

	real_centers = []

	for point in centers:
		x = 588 -(-1*point[1] - 70.96)/x_margin
		y = (42.40 - point[0])/y_margin
		real_centers.append([x, y])

	real_centers = np.array(real_centers)

	for i in range(len(real_centers)):
		c = real_centers[i]
		plt.scatter(c[0], c[1], s = area, marker = 'o', c = color_list[i], lw=50)

'''

if do_plot:
	plt.show()

# Now, clusters has correct setup...

print("Process complete.")