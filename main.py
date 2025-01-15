import streamlit as st


# Titre principal de l'application
st.title("Projet : Application de Réservation de Tables en Ligne ")

# Liste des sections avec titres et contenus
data = [
    {
        "title": "🌟 Problème ou besoin identifié",
        "content": "Le projet répond au **besoin croissant** des restaurants de moderniser et d'optimiser leur gestion des réservations tout en améliorant l'expérience utilisateur.\n\nLes clients rencontrent souvent des **difficultés à réserver une table à distance** de manière efficace et intuitive, notamment en visualisant les disponibilités dans l’espace du restaurant.\n\nCe projet vise à simplifier ce processus en offrant une plateforme **interactive** qui permet aux clients de sélectionner directement leur table préférée sur un plan visuel, à une date et une heure précises."
    },
    {
        "title": "🎯 Objectif principal du projet",
        "content": "L'objectif principal du projet d'innovation est de créer une solution numérique interactive qui **facilite et optimise** le processus de réservation dans les restaurants.\n\nCette application vise à offrir aux clients une expérience utilisateur **intuitive et visuelle** grâce à une cartographie en temps réel des tables disponibles, tout en permettant aux restaurants de mieux gérer leur capacité et d’améliorer leur efficacité opérationnelle."
    },
    {
        "title": "🔍 Objectif spécifique 1",
        "content": "Développer une interface utilisateur interactive permettant aux clients de **visualiser le plan de la salle** du restaurant et de **sélectionner directement une table disponible** en fonction de la date, de l'heure et du nombre de personnes."
    },
    {
        "title": "🛠️ Objectif spécifique 2",
        "content": "Mettre en place un système de gestion centralisé pour le restaurant, permettant d'**actualiser en temps réel la disponibilité des tables** et de **gérer efficacement** les réservations, les annulations et les modifications."
    },
    {
        "title": "📩 Objectif spécifique 3",
        "content": "Intégrer des **notifications automatisées** (par email ou SMS) pour confirmer les réservations, rappeler les dates et heures aux clients, et informer en cas de modifications ou d'indisponibilités."
    },
    {
        "title": "🚀 Description du projet, éléments innovants et valeur ajoutée",
        "content": "### Description du projet\nLe projet est une application web interactive permettant aux clients de réserver des tables dans un restaurant en ligne, à une date et une heure spécifiques.\n\nL'élément central du système est une **carte interactive** représentant le plan de la salle du restaurant. Cette carte permet aux utilisateurs de choisir visuellement leur table préférée en fonction de sa disponibilité en temps réel.\n\n### Éléments innovants\n1. **Cartographie interactive des tables** : Contrairement aux systèmes de réservation classiques basés sur des listes, ce projet propose une visualisation graphique de la salle, rendant le processus de réservation plus intuitif.\n2. **Mise à jour en temps réel** : Les disponibilités des tables sont actualisées dynamiquement pour éviter les conflits de réservation.\n3. **Expérience utilisateur améliorée** : Une navigation simplifiée et des fonctionnalités telles que des filtres (taille de table, emplacement préféré) et des notifications personnalisées.\n4. **Automatisation des communications** : Envoi de confirmations, rappels et mises à jour automatiques via email ou SMS.\n\n### Valeur ajoutée\n- Pour les **clients** : Une expérience utilisateur fluide et immersive qui simplifie la réservation et offre une meilleure visibilité sur les options disponibles.\n- Pour les **restaurants** : Une gestion optimisée des ressources (tables et personnel), une réduction des erreurs liées aux réservations manuelles, et une satisfaction accrue des clients grâce à un service plus professionnel.\n- Pour le **secteur** : Une approche moderne et innovante qui se démarque des systèmes traditionnels et améliore l'image de marque des restaurants utilisant cette technologie."
    },
    {
        "title": "🏢 Secteur ou domaine visé",
        "content": "Le projet vise le secteur de l'**hôtellerie et de la restauration**, en particulier les restaurants.\n\nIl s'inscrit dans le domaine de la **technologie appliquée** à la gestion des réservations et à l'amélioration de l'expérience client dans le secteur de la restauration.\n\nL'objectif est de moderniser la manière dont les clients interagissent avec les restaurants et d'**optimiser les opérations internes** grâce à des solutions numériques interactives et en temps réel."
    },
    {
        "title": "👥 Utilisateurs finaux ou bénéficiaires",
        "content": "1. **Les clients des restaurants :** Les utilisateurs qui souhaitent réserver une table dans un restaurant de manière simple, interactive et personnalisée.\n\n2. **Les restaurateurs et le personnel de gestion des réservations :** Les restaurants qui utilisent l'application pour gérer efficacement leurs réservations, optimiser la gestion des tables, et réduire les erreurs liées aux réservations manuelles.\n\n3. **Les gestionnaires d'événements dans les restaurants :** Dans le cas des restaurants qui organisent des événements (mariages, repas d'entreprise, etc.), l'application peut être utilisée pour gérer les réservations spécifiques à ces événements, offrant ainsi une solution efficace pour planifier les événements avec une vue d'ensemble sur la salle."
    },
    {
        "title": "📋 Étapes principales",
        "content": "| **Étape**                | **Description**                                                                 | **Durée estimée** | **Responsable**           |\n|------------------------|-----------------------------------------------------------------------------|------------------|--------------------------|\n| Recherche & Analyse    | Étudier le marché, analyser les besoins des utilisateurs et des restaurants. | 2 semaines       | Chef de projet, Analyste  |\n| Conception             | Élaboration de l'interface utilisateur et définition de l'architecture.     | 3 semaines       | Designer, Développeur     |\n| Développement          | Développement de l'application, intégration des fonctionnalités.             | 4-6 semaines     | Développeur full-stack    |\n| Test & Validation      | Réalisation de tests fonctionnels, validation des performances.              | 2 semaines       | Testeur QA, Développeur   |\n| Lancement/Présentation | Déploiement, marketing et formation des utilisateurs.                        | 1-2 semaines     | Responsable marketing     |"
    },
    {
        "title": "📆 Calendrier prévisionnel",
        "content": "| **Semaine** | **Étape**                     | **Tâches principales**                                                               |\n|-------------|-------------------------------|--------------------------------------------------------------------------------------|\n| Semaine 1-2 | Recherche & Analyse           | Étude de marché, analyse des besoins, définition des fonctionnalités.               |\n| Semaine 3-5 | Conception                    | Création de maquettes, élaboration du plan de la salle, préparation de l'architecture. |\n| Semaine 6-11 | Développement                 | Développement du front-end et back-end, intégration du système de réservation.        |\n| Semaine 12-13 | Test & Validation             | Tests fonctionnels et utilisateurs, validation des performances et corrections des bugs. |\n| Semaine 14-15 | Lancement/Présentation        | Déploiement, marketing, formation des utilisateurs.                                  |"
    }
]

# Affichage des sections avec des titres déroulants
for item in data:
    with st.expander(item["title"]):
        st.markdown(item["content"], unsafe_allow_html=True)

# Barre de navigation en bas
st.markdown("""
    <style>
    .navigation-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8f9fa;
        padding: 10px 400px;
        display: flex;
        justify-content: space-around;
        box-shadow: 0px -1px 5px rgba(0, 0, 0, 0.2);
    }
    .navigation-bar a {
        text-decoration: none;
        font-size: 16px;
        color: #007bff;
        font-weight: bold;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .navigation-bar a i {
        font-size: 30px;
    }
    </style>
            
    <div class="navigation-bar">
        <a href="https://presen-5rhrkuhggbivew6z4sbfzf.streamlit.app/"><i class="fas fa-home"></i></a>
        <a href="https://re-f2yf8jvap3cpwdh6afpvkt.streamlit.app/"><i class="fas fa-info-circle"></i></a>
    </div>
    
""", unsafe_allow_html=True)

st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)




