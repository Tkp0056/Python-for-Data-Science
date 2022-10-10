import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
data=pd.read_csv('cars_sampled.csv')
cars=data.copy()
#pd.set_option('display.float_format')
col=['name','dateCrawled','dateCreated','postalCode','lastSeen']
cars=cars.drop(columns=col,axis=1)
# we will work between 1950 to 2022 because between this range concentrated
#and well distributed data is observed
# and price 100 to 150000
# and PowerPS( horse power) - 10 to 500
# we have done these because its graph was not looking spreaded

cars= cars[(cars.yearOfRegistration<=2018) & 
           (cars.yearOfRegistration>=1950) &
           (cars.price>=100) &
           (cars.price<=150000) &
           (cars.powerPS>=10) &
           (cars.powerPS<=500) ]
        
# further to simplyfy we are combining year of registration with month of registration

cars['Age']=(2018-cars['yearOfRegistration']+cars['monthOfRegistration'])
cars['Age']=round(cars['Age'],2)
sns.distplot(cars['Age'])
sns.distplot(cars['price'])
sns.distplot(cars['powerPS'])
sns.regplot(x='Age',y='price',data=cars)
sns.regplot(x='powerPS',y='price',data=cars)

# all the  seller are private so this categorical variable is of no use 
# same goes with offertype all are offer
# abtest is usefuel as it is divided in to two category

sns.boxplot(x=cars['kilometer'],y=cars['price'])
sns.regplot(x='kilometer',y='price',data=cars)
sns.set(rc={'figure.figsize':(11.7,8.27)})
cars=cars.drop(columns=['seller','offerType','abtest'],axis=1)
cars_omit=cars.dropna(axis=0)
cars=cars.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)
cars_omit=cars_omit.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)
cars_omit=pd.get_dummies(cars_omit,drop_first=True)

#separate input output features

x1=cars_omit.drop(['price'],axis='columns',inplace=False)
y1=cars_omit['price']

# we have changed the price to log because of two reason first one is its graph
#second is its range (which is very huge)

prices=pd.DataFrame({'Before':y1,'After':np.log(y1)})
prices.hist()
y1=np.log(y1)
x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.3)
l=LinearRegression(fit_intercept=True)
model_lin=l.fit(x_train,y_train)
cars_pred_lin=l.predict(x_test)
lin_mse=mean_squared_error(y_test, cars_pred_lin)
lin_rmse=np.sqrt(lin_mse)
residual=y_test-cars_pred_lin
sns.regplot(x=y_test,y=residual)

# calculating r squared value

r2_lin_test=model_lin.score(x_test,y_test)
r2_lin_train=model_lin.score(x_train,y_train)




























