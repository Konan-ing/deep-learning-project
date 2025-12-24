FROM python:3.9

# Créer un dossier de travail
WORKDIR /code

# Copier les dépendances et les installer
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copier le reste du code et le modèle
COPY . .

# Hugging Face utilise le port 7860 par défaut
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]