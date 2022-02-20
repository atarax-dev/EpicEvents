# EpicEvents

#  Projet OC n°12


Introduction: Il s'agit d'une application permettant de gérer des clients et les contrats et évènements qui leur sont liés.

La documentation Postman (https://www.postman.com/downloads/) incluse dans ce dossier permet de comprendre les différents points de 
terminaisons et leur utilisation.

Importez le fichier EpicEvents.postman_collection.json afin d'avoir accès à la documentation

Précisions concernant les choix disponibles dans certains champs de certains modèles:

-status de Account: Active ou Not Active

-status de Contract: Signed ou Not Signed

-status de Event: Coming ou Ended

-role de user : Admin, Sales ou Support

Lancez un terminal

Récupérez l'ensemble du projet :

`git clone https://github.com/atarax-dev/EpicEvents`

Placez-vous dans le répertoire qui contient le fichier manage.py

Pour pouvoir lancer le programme, créez un environnement virtuel:

`python -m venv venv`

Activez l'environnement :

`source venv/Scripts/activate` (sous windows)

`source venv/bin/activate` (sous Mac ou linux)

Installez les packages requis à l'aide de la commande suivante:

`pip install -r requirements.txt` 

Configurez un serveur PostgreSQL et modifiez les informations d'accès dans le fichier settings.py dans DATABASES = {'NAME','USER','PASSWORD'}

Pour plus d'informations, consultez https://www.postgresql.org/

# Utilisation 

Toujours depuis le répertoire qui contient manage.py dans le terminal, exécutez le programme:

`python manage.py migrate` puis `python manage.py createsuperuser` pour créer un premier compte administrateur 

puis `python manage.py runserver` pour lancer le serveur 

Ouvrez votre navigateur et allez sur la page suivante : http://127.0.0.1:8000/admin pour accéder au site d'administration 
afin d'ajouter de nouveaux utilisateurs et leur assigner des rôles; vous pouvez également 
voir et modifier toutes les données de la base administrée

Assignez-vous le rôle "Admin" afin d'avoir les permissions adéquates sur l'API

Ouvrez votre navigateur et allez sur la page suivante : http://127.0.0.1:8000/api-auth/login/ 
pour vous authentifier et accéder à l'API

