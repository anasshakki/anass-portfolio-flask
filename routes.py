# routes.py
from app import app
from flask import render_template

# Données statiques pour le portfolio avec tous les détails
PROJETS = [
    {
        'id': 1, 
        'nom': 'Amélioration des performances de tir (ML)', 
        'description': 'Projet de recherche combinant physique, électronique embarquée et Machine Learning (SVM) pour analyser et améliorer la précision des tirs au basketball.', 
        'tech': 'Python (SVM, Scikit-learn, Pandas), Arduino/MPU-6050, Mécanique', 
        'annee': 2025,
        'github_url': 'https://github.com/anasshakki', 
        'details': [
            {'titre': 'Problématique', 'texte': 'Comment les données collectées par un capteur MPU-6050 et la classification par Machine à Vecteurs de Support (SVM) peuvent-elles être utilisées pour analyser et améliorer la précision des tirs ?'},
            {'titre': 'Collecte des Données', 'texte': 'Utilisation du capteur MPU-6050 (accéléromètre et gyroscope triaxial) lié à une carte Arduino pour capturer les mouvements du bras pendant les tirs (tirs corrects vs. tirs incorrects).'},
            {'titre': 'Analyse Physique et Préparation', 'texte': 'Étude de la chute parabolique et de ses équations. Nettoyage, extraction des caractéristiques (variance, moyenne) et normalisation des données pour l\'apprentissage automatique.'},
            {'titre': 'Modélisation SVM', 'texte': 'Comparaison des performances des modèles SVM avec noyau Linéaire et noyau Polynomial. Le noyau Linéaire a montré une précision supérieure (85.76%) dans la classification des tirs.'}
        ],
        'images': ['projet1_photo1.png', 'projet1_photo2.png', 'projet1_photo3.png'] 
    },
    {
        'id': 2, 
        'nom': 'Site E-commerce Parfums (Flask)', 
        'description': 'Développement d\'une application web full-stack minimaliste pour la vente de parfums, incluant la gestion du catalogue et la simulation d\'un processus d\'achat.', 
        'tech': 'Flask, Jinja2, HTML/CSS', 
        'annee': 2025,
        'github_url': 'https://github.com/anasshakki', 
        'details': [
            {'titre': 'Conception de l\'Architecture', 'texte': 'Mise en place d\'un micro-service Flask modulaire, séparant la logique des routes, des données statiques et des vues HTML.'},
            {'titre': 'Gestion du Panier', 'texte': 'Implémentation d\'une logique de session (variable globale) pour suivre les articles ajoutés par l\'utilisateur et calculer le prix total.'},
            {'titre': 'Design et Expérience Utilisateur', 'texte': 'Création d\'un thème sombre et professionnel avec des cartes produits responsives, ajout d\'un système de navigation et d\'une simulation de page de paiement.'}
        ],
        'images': ['projet2_photo1.png', 'projet2_photo2.png', 'projet2_photo3.png'] 
    },
    {
        'id': 3, 
        'nom': 'Mini Application de Gestion de Tâches (Flask)', 
        'description': 'Application web de type To-do List développée pour la gestion simple des tâches : ajout, modification, suppression et suivi du statut (terminé/en attente).', 
        'tech': 'Flask, SQLite, HTML/CSS, JavaScript', 
        'annee': 2024,
        'github_url': 'https://github.com/anasshakki', 'details': [
            {'titre': 'Architecture et Persistence', 'texte': 'Développement en Flask avec une base de données SQLite pour un stockage léger et intégré des informations des tâches.'},
            {'titre': 'Fonctionnalités CRUD', 'texte': 'Implémentation complète des opérations (Ajouter, Afficher, Modifier, Supprimer) et gestion du statut des tâches.'},
            {'titre': 'Interface Utilisateur', 'texte': 'Style simple en HTML/CSS, avec utilisation de JavaScript pour des effets visuels (comme l\'effet de suppression).'}
        ],
        'images': ['projet3_photo1.png', 'projet3_photo2.png', 'projet3_photo3.png'] 
    },
    {
        'id': 4, 
        'nom': 'Mini Blog – Application Web Node.js', 
        'description': 'Application web full-stack simple mais complète pour gérer et publier des articles de blog, avec authentification sécurisée et gestion des sessions.', 
        'tech': 'Node.js, Express, SQLite, EJS, bcryptjs', 
        'annee': 2024,
        'github_url': 'https://github.com/anasshakki',
        'details': [
            {'titre': 'Architecture Serveur', 'texte': 'Utilisation de Node.js et du framework Express pour la création du serveur et la gestion des routes côté Backend.'},
            {'titre': 'Authentification Sécurisée', 'texte': 'Implémentation complète de l\'inscription, la connexion et la déconnexion, avec hachage des mots de passe (bcryptjs) et gestion des sessions utilisateur.'},
            {'titre': 'Gestion des Articles (CRUD)', 'texte': 'Fonctionnalités permettant de créer, éditer et supprimer des articles de blog, avec protection des routes réservées aux membres connectés.'}
        ],
        'images': ['projet4_photo1.webp', 'projet4_photo2.jpg', 'projet4_photo3.jpg'] 
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projets')
def liste_projets():
    return render_template('projets.html', projets=PROJETS)

@app.route('/projet/<int:id>')
def details_projet(id):
    """Affiche les détails d'un projet spécifique."""
    projet = next((p for p in PROJETS if p['id'] == id), None)
    if projet is None:
        return render_template('404.html'), 404 
    return render_template('projet_details.html', projet=projet)

@app.route('/contact')
def contact():
    return render_template('contact.html')