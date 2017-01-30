import numpy as np, csv, pandas
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

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

col = data[1: , 2]

encoder = LabelEncoder()

Y_train_num = encoder.fit_transform(col)

Y_train_str = encoder.inverse_transform(Y_train_num)

Y_train_num = np_utils.to_categorical(Y_train_num)

print(Y_train_num)

raw_location_data = data[1 : , -1]

X_train = np.array([parse_location_string(s) for s in raw_location_data]).astype('float64')

# X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

# So, two input layers, 1 output layer of the crime type they would expect at that location?

# Let's create our model!

model = Sequential()

model.add(Dense(2, input_shape=X_train.shape, init='normal', activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, init='normal', activation='sigmoid'))

print("Model created!")
 
# 8. Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print("Model compiled!")
 
# 9. Fit model on training data
model.fit(X_train, Y_train_num, batch_size=32, nb_epoch=1, verbose=1)

print("Model trained!")

# 10. Evaluate model on test data
score = model.evaluate(X_train, Y_train_num, verbose=1)

print("Model tested!")

print("Score on test data = {}.".format(score))

print("Process complete!");