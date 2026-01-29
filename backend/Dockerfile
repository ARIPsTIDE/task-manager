# Version slim plus légère
FROM python:3.12-slim

LABEL maintainer="ton.nom@exemple.com"

# Variables d'environnement Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le container
WORKDIR /app

# Dépendances systèmes minimales pour compiler certaines libs Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl \
    && rm -rf /var/lib/apt/lists/*

# Copier uniquement les dépendances pour optimiser le cache
COPY backend/requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copier uniquement le code backend
COPY backend/ .

# Créer un utilisateur non-root
RUN adduser --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app

USER appuser

# Port exposé
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
