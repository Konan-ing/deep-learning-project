from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app) # Indispensable pour que ton site puisse parler à l'API

# Charger le modèle (le dossier nommé "model")
model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    valeur = float(data['valeur'])
    
    # Prédiction
    entree = np.array([[valeur]])
    prediction = model.predict(entree)
    
    return jsonify({'resultat': float(prediction[0][0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)