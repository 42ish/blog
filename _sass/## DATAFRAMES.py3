## DATAFRAMES

def del_na(X, y = None):
	if type(X) == 'pandas.core.frame.DataFrame':
		mask = X.isnull().sum(axis = 1) > 0
		new_X = X[mask]
		if y:
			new_y = y[mask]
	elif type(X) in ['numpy.ndarray', 'numpy.matrixlib.defmatrix.matrix']:
		return "FINISH THIS"

	if y:
		return new_X, new_y
	else:
		return new_X
X.isnull().sum(axis = 1) > 0