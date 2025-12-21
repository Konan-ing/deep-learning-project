import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# données fictives
X = np.random.rand(100, 1)
y = 3 * X + 1

# modèle
model = keras.Sequential([
    layers.Dense(16, activation="relu"),
    layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse")

# entraînement
model.fit(X, y, epochs=20, verbose=0)

# sauvegarde
model.save("model")
