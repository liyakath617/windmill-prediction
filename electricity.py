import pandas as pd
import numpy as np
import pickle
import joblib 


data=pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/electricity.csv")

data["ForecastWindProduction"] = pd.to_numeric(data["ForecastWindProduction"], errors= 'coerce')
data["SystemLoadEA"] = pd.to_numeric(data["SystemLoadEA"], errors= 'coerce')
data["SMPEA"] = pd.to_numeric(data["SMPEA"], errors= 'coerce')
data["ORKTemperature"] = pd.to_numeric(data["ORKTemperature"], errors= 'coerce')
data["ORKWindspeed"] = pd.to_numeric(data["ORKWindspeed"], errors= 'coerce')
data["CO2Intensity"] = pd.to_numeric(data["CO2Intensity"], errors= 'coerce')
data["ActualWindProduction"] = pd.to_numeric(data["ActualWindProduction"], errors= 'coerce')
data["SystemLoadEP2"] = pd.to_numeric(data["SystemLoadEP2"], errors= 'coerce')
data["SMPEP2"] = pd.to_numeric(data["SMPEP2"], errors= 'coerce')

data=data.drop(columns=['Holiday'], axis=1)
data=data.drop(columns=['DateTime'], axis=1)

data['ForecastWindProduction']=data['ForecastWindProduction'].fillna(data['ForecastWindProduction'].mean())
data['SystemLoadEA']=data['SystemLoadEA'].fillna(data['SystemLoadEA'].mean())
data['SMPEA']=data['SMPEA'].fillna(data['SMPEA'].mean())
data['ORKTemperature']=data['ORKTemperature'].fillna(data['ORKTemperature'].mean())
data['ORKWindspeed']=data['ORKWindspeed'].fillna(data['ORKWindspeed'].mean())
data['CO2Intensity']=data['CO2Intensity'].fillna(data['CO2Intensity'].mean())
data['ActualWindProduction']=data['ActualWindProduction'].fillna(data['ActualWindProduction'].mean())
data['SystemLoadEP2']=data['SystemLoadEP2'].fillna(data['SystemLoadEP2'].mean())
data['SMPEP2']=data['SMPEP2'].fillna(data['SMPEP2'].mean())

x = data[["Day", "Month", "ForecastWindProduction", "SystemLoadEA",
          "SMPEA", "ORKTemperature", "ORKWindspeed", "CO2Intensity",
          "ActualWindProduction", "SystemLoadEP2"]]
y = data["SMPEP2"]

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y,test_size=0.2,random_state=42)

model=RandomForestRegressor()

model.fit(xtrain,ytrain)

# Save the r object
pickle.dump(model,open('ele.pkl','wb'))
# Save the trained model
with open('ele.pkl', 'wb') as f:
    pickle.dump(model, f)
