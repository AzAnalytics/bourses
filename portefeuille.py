import pandas as pd
import streamlit as st

# Chargement des données
df_historique = pd.read_csv('data/historical_data.csv', sep=";")

# Convertir la colonne 'Date' en datetime
df_historique['Date'] = pd.to_datetime(df_historique['Date'])

# Définir les options de l'année et du mois
annee_debut = 2002
annee_fin = pd.to_datetime("now").year
mois_options = list(range(1, 13))  # De 1 (Janvier) à 12 (Décembre)

# Création des listes déroulantes pour l'année et le mois dans des colonnes séparées
st.title('Analyse du Portefeuille d’Investissement depuis Janvier 2002')

col1, col2, col3 = st.columns(3)

with col1:
    # Liste déroulante pour choisir une année
    selected_annee = st.selectbox('Choisir une année:', list(range(annee_debut, annee_fin + 1)))

with col2:
    # Liste déroulante pour choisir un mois
    selected_mois = st.selectbox('Choisir un mois:', mois_options, format_func=lambda x: pd.to_datetime(x, format='%m').strftime('%B'))

# Filtrer le DataFrame pour les données à partir du mois et de l'année sélectionnés
df_historique_filtre = df_historique[(df_historique['Date'].dt.year == selected_annee) &
                                     (df_historique['Date'].dt.month >= selected_mois) |
                                     (df_historique['Date'].dt.year > selected_annee)]

# Réorganisation des données
df_pivot_filtre = df_historique_filtre.pivot(index='Date', columns='Symbole', values='Close')

with col3:
    # Liste déroulante pour choisir un symbole
    if not df_pivot_filtre.empty:
        selected_symbole = st.selectbox('Choisir un symbole:', df_pivot_filtre.columns)
    else:
        st.write("Aucune donnée disponible pour la période sélectionnée.")

if not df_pivot_filtre.empty and selected_symbole in df_pivot_filtre.columns:
    # Calcul de la valeur finale pour le symbole sélectionné
    investissement_par_action = 1000
    rendement = df_pivot_filtre[selected_symbole].iloc[-1] / df_pivot_filtre[selected_symbole].iloc[0] - 1
    valeur_finale = investissement_par_action * (1 + rendement)

    # Affichage des résultats
    st.write(f"Rendement pour {selected_symbole} depuis {selected_mois:02d}-{selected_annee}: {rendement:.2%}")
    st.write(f"Valeur finale de l'investissement de 1000€ dans {selected_symbole} depuis {selected_mois:02d}-{selected_annee}: {valeur_finale:.2f}€")
else:
    st.error("Les données pour la sélection actuelle ne sont pas disponibles.")
