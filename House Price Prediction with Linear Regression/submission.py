import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import r2_score


dataset = pd.read_csv('data/prices.csv')

x = dataset[['lot_area','living_area','num_floors','num_bedrooms',
             'num_bathrooms','waterfront','year_built','year_renovated']] #independent variables
y = dataset['price'] #dependent variables

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0) # %20 teste %80 traine

from sklearn.linear_model import LinearRegression
regressor = LinearRegression() # lin reg
regressor.fit(X_train, Y_train) 

prediction = regressor.predict(X_test) 
act_pred = pd.DataFrame({'Actual': Y_test, 'Predicted': prediction})

print(act_pred)
print('R2:',r2_score(act_pred["Actual"],act_pred["Predicted"]))
print('MSE:', metrics.mean_squared_error(Y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(Y_test, prediction))) 


fig, ax = plt.subplots() #[y.min(), y.max()], [y.min(), y.max()] because of the dimesions ,using the variable ax for single a Axes
ax.scatter(act_pred["Actual"],act_pred["Predicted"])
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k')
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
plt.show()

plt.scatter(act_pred["Actual"], act_pred["Predicted"]);
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.show()

plt.scatter(x["lot_area"],y,color='red')
plt.xlabel('Price') 
plt.ylabel('Lot_Size')
plt.show()

plt.scatter(x["living_area"],y,color='blue')
plt.xlabel('Price') 
plt.ylabel('Living area')
plt.show()

plt.scatter(x["num_floors"],y,color='yellow')
plt.xlabel('Price') 
plt.ylabel('Number of floors')
plt.show()

plt.scatter(x["num_bedrooms"],y,color='black')
plt.xlabel('Price') 
plt.ylabel('Number of bedrooms')
plt.show()

plt.scatter(x["num_bathrooms"],y,color='green')
plt.xlabel('Price') 
plt.ylabel('Number of bathrooms')
plt.show()


plt.scatter(x["waterfront"],y,color='orange')
plt.xlabel('Price') 
plt.ylabel('waterfront')
plt.show()

plt.scatter(x["year_built"],y,color='purple')
plt.xlabel('Price') 
plt.ylabel('year_built')
plt.show()

plt.scatter(x["year_renovated"],y,color='pink')
plt.xlabel('Price') 
plt.ylabel('year_renovated')
plt.show()
