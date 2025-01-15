import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Suivi de Projet", layout="wide")



# Sections avec titres et contenus
sections = [
    {"title": "Risque(s)",
     "content": [
         "Problèmes techniques (bugs et pannes)",
         "Problèmes de sécurité des données",
         "Manque d'adoption par le public cible",
         "Problèmes d'intégration avec les systèmes existants",
         "Erreurs de gestion des réservations (double réservations, erreurs de synchronisation)",
         "Réactions négatives des clients",
         "Dépendance aux fournisseurs de services tiers",
         "Mauvaise gestion des données utilisateur",
         "Problèmes de scalabilité",
         "Concurrence et différenciation",
         "Problèmes liés à l'expérience utilisateur (UX)"
     ]},
    {"title": "Impact(s)",
     "content": [
         "Amélioration de l'efficacité du restaurant",
         "Augmentation de la satisfaction client",
         "Gain de temps pour les restaurateurs",
         "Réduction du taux de non-présentation",
         "Augmentation de la fréquentation du restaurant",
         "Amélioration de la prise de décision",
         "Optimisation de l'occupation des tables",
         "Renforcement de la compétitivité",
         "Réduction des coûts opérationnels",
         "Impact positif sur la réputation du restaurant"
     ]},
    {"title": "Plan(s) d'atténuation",
     "content": [
         "Mettre en place des tests automatisés et manuels",
         "Effectuer des mises à jour régulières du code",
         "Utiliser un hébergement fiable avec sauvegardes et récupération rapide",
         "Implémenter le chiffrement des données sensibles",
         "Utiliser une authentification à plusieurs facteurs",
         "Respecter les normes de confidentialité comme le GDPR",
         "Mener des études de marché pour ajuster les fonctionnalités",
         "Promouvoir l'application via des canaux de marketing ciblés",
         "Collaborer avec les responsables du restaurant pour comprendre les systèmes existants",
         "Garantir des API ou interfaces compatibles",
         "Mettre en place une vérification automatique en temps réel des réservations",
         "Synchroniser les réservations en ligne avec la disponibilité des tables",
         "Collecter des retours réguliers pour améliorer l'interface",
         "Simplifier les processus de réservation et d'annulation",
         "Choisir des partenaires fiables",
         "Avoir un plan de secours pour la gestion des réservations en cas de défaillance",
         "Assurer une gestion transparente des données",
         "Mettre en place un contrôle strict sur l'accès aux données sensibles",
         "Concevoir une architecture scalable",
         "Tester régulièrement la charge du système et utiliser des serveurs et bases de données adaptés",
         "Offrir des fonctionnalités uniques (par exemple, cartographie interactive des tables)",
         "Assurer une amélioration continue de l’application",
         "Engager des designers UX pour tester et améliorer l'interface",
         "Assurer une réactivité rapide aux retours utilisateurs"
     ]},
    {"title": "Méthodologie de suivi",
     "content": [
         "Réunions hebdomadaires",
         "Rapports d’étape",
         "Tableaux de bord de performance",
         "Revues de sprint",
         "Feedback utilisateur",
         "Suivi des indicateurs de performance clés (KPI)",
         "Réunions de revue de code",
         "Surveillance des performances du système",
         "Mises à jour sur les risques",
         "Documentation continue"
     ]}
]

# Affichage des sections
for section in sections:
    with st.expander(f"{section['title']}"):
        for item in section['content']:
            st.markdown(f"-**{item}**</span>", unsafe_allow_html=True)


# Barre de navigation en bas
st.markdown("""
    <style>
    .navigation-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8f9fa;
        padding: -1px 700px;
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
    </div>
    
""", unsafe_allow_html=True)

st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)
