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

disrupt = ['ARGUE', 'ARREST', 'ASSEMBLY OR GATHERING VIOLATIONS', 'BENOPROP', 'BALLIST',
'CONFIDENCE GAMES', 'COUNTERFEITING', 'CRIMINAL HARASSMENT', 'DEATH INVESTIGATION', 'DISORDERLY', 'DRUG CHARGES',
'DISORDERLY CONDUCT', 'DRUG VIOLATION', 'EMBEZELLMENT', 'EVADING FARE', 'FORGERY', 'FRAUD',
'GAMBLING OFFENSE', 'GATHER', 'HARASS', 'HARBOR', 'HARBOR RELATED INCIDENTS', 'HATECRIM', 'INVESTIGATE PERSON',
'INVESTIGATE PROPERTY', 'LANDLORD', 'LANDLORD/TENANT DISPUTES', 'MISSING PERSON LOCATED',
'MISSING PERSON REPORTED', 'OFFENSES AGAINST CHILD/FAMILY', 'OPERATING UNDER THE INFLUENCE', 'PRISON',
'PROSTITUTION CHARGES', 'PERSLOC', 'PRISONER RELATED INCIDENTS', 'PROSTITUTION', 'PUBDRINK',
'RESTRAIN', 'RESTRAINING ORDER VIOLATIONS', 'RUNAWAY', 'SEX OFFENDER REGISTRATION', 'SEXREG', 
'TRESPASS', 'VERBAL DISPUTES', 'WEAPONS CHARGE', 'WARRANT ARRESTS']

other = ['07RV', 'AIRCRAFT', 'LICVIOL', 'LABOR', 'LICENSE PLATE RELATED INCIDENTS',
'LICENSE VIOLATION', 'LIQUOR VIOLATION', 'MVACC', 'OTHER', 'OTHER LARCENY', 'PERSMISS', 'PHONECALLS', 'PLATES',
'POLICE SERVICE INCIDENTS', 'SERVICE', 'SKIPFARE', 'TOWED', 'VIOLATIONS', 'EMBEZZLEMENT']

med = ['MEDASSIST', 'MEDICAL ASSISTANCE', 'MOTOR VEHICLE ACCIDENT RESPONSE', 'OPERATING UNDER INFLUENCE']

for c in crime_names:
	if c not in violent and c not in damage and c not in disrupt and c not in other and c not in med:
		print(c)

print("Process complete.")