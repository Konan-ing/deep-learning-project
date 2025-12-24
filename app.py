import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

app = FastAPI()

# Configuration du CORS pour autoriser votre portfolio GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://konan-ing.github.io"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chargement du modèle sauvegardé
model = tf.keras.models.load_model("model.h5")

class DataInput(BaseModel):
    data: float

@app.post("/predict")
async def predict(item: DataInput):
    # Préparation de la donnée pour le modèle
    input_val = np.array([[item.data]])
    prediction = model.predict(input_val)
    
    return {"resultat": float(prediction[0][0])}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)