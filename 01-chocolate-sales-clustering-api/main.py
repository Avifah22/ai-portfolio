import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Setup FastAPI App
# Pastikan nama file pkl-mu sesuai (di sini tertulis "kmeans_chocolate.pkl")
model = joblib.load("kmeans_chocolate.pkl")
app = FastAPI(title="Chocolate Sales Clustering API")


class SalesData(BaseModel):
    amount: float
    boxes_shipped: int


@app.post("/predict")
def predict_cluster(data: SalesData):
    features = [[data.amount, data.boxes_shipped]]
    cluster = model.predict(features)
    return {
        "amount": data.amount,
        "boxes_shipped": data.boxes_shipped,
        "assigned_cluster": int(cluster[0]),
    }


@app.get("/")
def home():
    return {"message": "Chocolate Sales Clustering API is running successfully!"}
