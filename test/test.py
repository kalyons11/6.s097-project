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

encoder = LabelEncoder()

Y_train_num = encoder.fit_transform(col)

Y_train_str = encoder.inverse_transform(Y_train_num)

Y_train_num = np_utils.to_categorical(Y_train_num)

# print(Y_train_num.shape)

raw_location_data = data[1 : , -1]

X_train = np.array([parse_location_string(s) for s in raw_location_data]).astype('float64')

from keras.wrappers.scikit_learn import BaseWrapper
import copy

def custom_get_params(self, **params):
    res = copy.deepcopy(self.sk_params)
    res.update({'build_fn': self.build_fn})
    return res

BaseWrapper.get_params = custom_get_params

def baseline_model():
	# Create model
	model = Sequential()
	model.add(Dense(128, input_dim=2, input_shape=X_train.shape, init='normal', activation='relu'))
	model.add(Dense(col.shape[0], init='normal', activation='sigmoid'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=3, batch_size=5, verbose=1)
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X_train, Y_train_num, cv=kfold)

print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

print("Process complete!");