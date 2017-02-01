#will read in csv file as 2d array
#boundaries are 42.23, -71.18 and 42.40, -70.96
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def readFile(filename):
    import_data = []
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ",")
        for row in spamreader:
            import_data.append(row)
    return import_data


#will take in tuple string and extract list
def stringToList(string_name):
    return_list = []
    current_num = ""
    for char in string_name:
        if char.isdigit() or char == "." or char == "-":
            current_num += char
        elif char == ",":
            return_list.append(float(current_num))
            current_num = ""
    return_list.append(float(current_num))
    return return_list

#code to find all list names
import_data = readFile("C:\\Users\\Mark\\Desktop\\crime_data.csv")
coordinate_list = []
for i in range(1,268057):
    coordinate_list.append(stringToList(import_data[i][19]))

#now find min/max longitude and min/max latitude
min_latitude = coordinate_list[0][0]
max_latitude = coordinate_list[0][0]
min_longitude = coordinate_list[0][1]
max_longitude = coordinate_list[0][1]

for element in coordinate_list:
    element0 = element[0]
    element1 = element[1]
    if element0 != 0:
        min_latitude = min(min_latitude, element0)
        max_latitude = max(max_latitude, element0)
    if element1 != 0:
        min_longitude = min(min_longitude, element1)
        max_longitude = max(max_longitude, element1)


#now import picture
img = mpimg.imread("C:\\Users\\Mark\\Desktop\\capture2.PNG")
imgplot = plt.imshow(img)

#now calculate x and y values of picture
#picture is 621 pixels high and 588 pixels wide

y_margin = (42.40-42.23)/621.0
x_margin = (-70.96+71.18)/588.0

x_list = []
y_list = []
for coordinate in coordinate_list:
    if coordinate[1] != 0:
        x_coordinate = 588 -(-1*coordinate[1] - 70.96)/x_margin
        x_list.append(x_coordinate)
    if coordinate[0] != 0:
        y_coordinate = (42.40 - coordinate[0])/y_margin
        y_list.append(y_coordinate)

area = 5
plt.scatter(x_list,y_list,s=area)
plt.show()