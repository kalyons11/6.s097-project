import numpy as np, csv, pandas
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

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

paired_output_data = data[1: , [2, 3]]

col = np.unique(data[1: , 2])

print(col.shape)

encoder = LabelEncoder()

Y_train_num = np.transpose(encoder.fit_transform(data[1: , 2]))

print(Y_train_num[0])

Y_train_str = encoder.inverse_transform(Y_train_num)

Y_train_num = np_utils.to_categorical(Y_train_num)

print(Y_train_num.shape)

print(Y_train_str.shape)

raw_location_data = data[1 : , -1]

X_train = np.array([parse_location_string(s) for s in raw_location_data]).astype('float64')

print(X_train.shape)

print(X_train[0])

model = Sequential()

# Adding layers.

model.add(Dense(2, input_dim = 2))
model.add(Dense(127, init='normal', activation='sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Model compiled!")

# 9. Fit model on training data
model.fit(X_train, Y_train_num, batch_size=32, nb_epoch=5, verbose=1)

print("Model trained!")

# 10. Evaluate model on test data
score = model.evaluate(X_train, Y_train_num, verbose=1)

print()

print("Model tested!")

print("Score on test data = {}.".format(score))

print("Process complete.")