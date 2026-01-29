# Utiliser une image nginx
FROM nginx:alpine

# Copier les fichiers statiques dans le dossier par défaut de nginx
COPY . /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80

# Lancer nginx
CMD ["nginx", "-g", "daemon off;"]
