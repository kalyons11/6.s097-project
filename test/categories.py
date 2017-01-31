import numpy as np, csv

def parse_location_string(inp):
	inp = inp[1:-1]
	i = inp.index('///')
	x = float(inp[:i])
	y = float(inp[i + 3:])
	return np.array([x, y])

seed = 123

np.random.seed(seed)

filename = '../data/crime_data.csv'

data = np.array(list(csv.reader(open(filename, "rU"), dialect=csv.excel_tab, delimiter=",")))

crime_names = [s.upper() for s in np.unique(data[1 : , 2])]

# Declaring categories...

violent = ["32GUN", "AGGRAVATED ASSAULT", "BALLISTICS", "BIOTHREAT", "BOMB", "BOMB HOAX", "EXPLOS", "EXPLOSIVES", 
"FIRE", "HOMICIDE", "INDECENT ASSAULT", "MANSLAUG", "RAPE AND ATTEMPTED", "SIMPLE ASSAULT"]

damage = ["ARSON", "AUTO THEFT", "AUTO THEFT RECOVERY", "BURGTOOLS", "COMMERCIAL BURGLARY", "CRIMES AGAINST CHILDREN",
"FIRE RELATED REPORTS", "FIREARM DISCOVERY", "FIREARM VIOLATIONS", "HAZARDOUS", "INVPER", "INVPROP", "INVVEH",
"LARCENY FROM MOTOR VEHICLE", "LARCENY", "OTHER BURGLARY", "PROPDAM", "PROPFOUND", "PROPLOST", "PROPERTY FOUND", 
"PROPERTY LOST", "PROPERTY RELATED DAMAGE", "RESIDENTIAL BURGLARY", "ROBBERY", "RECOVERED STOLEN PROPERTY",
"STOLEN PROPERTY CHARGES", "SEARCH WARRANTS", "SEARCHWARR", "VAL", "VANDALISM", "VIOLATION OF LIQUOR LAWS", "VANDALISM"]

# Two more categories: disrupt and other.

for c in crime_names:
	if c not in violent and c not in damage:
		print(c)