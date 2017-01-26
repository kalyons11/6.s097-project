import numpy, csv

filename = '../data/crime_data.csv'

result = numpy.array(list(csv.reader(open(filename, "rt"), delimiter=",")))

shape = result.shape

print('Shape = {}.'.format(shape))

print("Process complete!");