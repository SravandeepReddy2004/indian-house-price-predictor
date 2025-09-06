import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

data = pd.read_csv("indian_house_prices.csv")

X = data[[
    "City", "Furnishing", "Facing", "PropertyType", "BuildingType",
    "BHK", "Bathrooms", "Balconies", "CarpetArea_sqft", "Floor", "AgeYears"
]]
y = data["Price_INR"]

# Define categorical and numeric columns
categorical_cols = ["City", "Furnishing", "Facing", "PropertyType", "BuildingType"]
numeric_cols = ["BHK", "Bathrooms", "Balconies", "CarpetArea_sqft", "Floor", "AgeYears"]

# Preprocessing: OneHot encode categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Build pipeline: preprocessing + RandomForest model
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42, n_estimators=200))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
print("✅ Model trained and saved")
