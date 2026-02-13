import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv(r"C:\Data Science\Practice\FastAPI\Campusx_paid\5 ML\housing.csv").iloc[:,:-1].dropna()
print("Read the dataset")



X = df.drop(columns="median_house_value")
y = df["median_house_value"]
print("Splited the dataset")


model = LinearRegression()
model.fit(X,y)
print("Trained the Model")

joblib.dump(model,"model.joblib")
print("Saved the Model")

