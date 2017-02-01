from arrays import disrupt_labels, med_labels
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
import random

# Config.

the_labels = med_labels
n_clusters = 10
filename = '../data/med.csv'

# Work.

data = np.array(list(csv.reader(open(filename, "rU"), dialect=csv.excel_tab, delimiter=",")))

loc_data = np.array(data[1: , [0 , 1]]).astype('float64')

cluster_array = range(n_clusters)

#now import picture

img = mpimg.imread('../code/capture2.png')
imgplot = plt.imshow(img)

#now calculate x and y values of picture
#picture is 621 pixels high and 588 pixels wide

y_margin = (42.40-42.23)/621.0
x_margin = (-70.96+71.18)/588.0

area = 5

for i in range(len(cluster_array)):
	x_list = []
	y_list = []
	c = cluster_array[i]
	for j in range(the_labels.shape[0]):
		d = the_labels[j]
		if d == c:
			# We are in the correct cluster.
			r = loc_data[j]
			x = 588 -(-1*r[1] - 70.96)/x_margin
			x_list.append(x)
			y = (42.40 - r[0])/y_margin
			y_list.append(y)
	colors = np.random.rand(3,)
	plt.scatter(x_list, y_list, s = area, c = colors, marker='o', lw=0)

plt.show()

print("Process complete.")