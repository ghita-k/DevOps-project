# Utilise une image Python officielle comme base
FROM python:3.9-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers de l'application dans le répertoire de travail
COPY . /app

# Installe les dépendances nécessaires
RUN pip install --no-cache-dir -r requirements.txt

# Définit la variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose le port sur lequel Flask fonctionne
EXPOSE 5000

# Commande par défaut pour exécuter l'application
CMD ["flask", "run", "--host=0.0.0.0"]





