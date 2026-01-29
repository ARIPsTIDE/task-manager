# Version slim plus légère
FROM python:3.12-slim

# Variables d'environnement Python
# Eviter de créer des fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Désactiver les buffering des logs
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le container
WORKDIR /app

# Dépendances systèmes minimales - compiler certaines libs Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copier uniquement les dépendances pour le cache
COPY backend/requirements.txt .

# Installation des dépendances Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copier le code applicatif
COPY . .

# Création d'un utilisateur non-root - Par défaut Docker tourne en root
RUN adduser --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app

USER appuser

# Port exposé
EXPOSE 8000

# Ajout du healthcheck - vérifie si l'app est vivante
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

#Lancement de l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
