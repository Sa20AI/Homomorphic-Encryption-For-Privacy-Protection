<<<<<<< HEAD
import pandas as pd
from sklearn import datasets
import numpy as np
import phe as paillier
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import f1_score
from sklearn.metrics import mean_squared_error, r2_score

class LogModel:
	def __init__(self):
		pass

	def getResults(self):
		df=pd.read_csv('diabetes.csv')
		X=df.drop(['SkinThickness','Outcome'],axis=1)
		y=df['Outcome']
		X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
		log=LogisticRegression(max_iter=1000)
		log.fit(X_train,y_train)
		y_pred=log.predict(X_test)
		RMSE=pow(mean_squared_error(y_pred, y_test),0.5)
		R=r2_score(y_pred, y_test)
		print(R)
		f1=f1_score(y_test, y_pred)
		print(f1)
		return log, y_pred, RMSE, f1


	def getCoef(self):
		return self.getResults()[0].coef_


def main():
	cof=LogModel().getCoef()
	print(cof)


if __name__=='__main__':
	main()
=======
import pandas as pd
from sklearn import datasets
import numpy as np
import phe as paillier
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import f1_score
from sklearn.metrics import mean_squared_error, r2_score

class LogModel:
	def __init__(self):
		pass

	def getResults(self):
		df=pd.read_csv('diabetes.csv')
		X=df.drop(['SkinThickness','Outcome'],axis=1)
		y=df['Outcome']
		X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
		log=LogisticRegression(max_iter=1000)
		log.fit(X_train,y_train)
		y_pred=log.predict(X_test)
		RMSE=pow(mean_squared_error(y_pred, y_test),0.5)
		R=r2_score(y_pred, y_test)
		print(R)
		f1=f1_score(y_test, y_pred)
		print(f1)
		return log, y_pred, RMSE, f1


	def getCoef(self):
		return self.getResults()[0].coef_


def main():
	cof=LogModel().getCoef()
	print(cof)


if __name__=='__main__':
	main()
>>>>>>> 6aed3a62115b5736341a4ec04768bec54fb9a143
