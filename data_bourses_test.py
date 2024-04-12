import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pandas.tseries.offsets import BDay
from datetime import datetime, timedelta
from API_bourses.connection import collection
from API_crypto.connection_crypto import collection_name_crypto

# Définition du titre et de la mise en page globale
st.set_page_config(page_title="Dashboard Analyse de Données", page_icon=":bar_chart:", layout="wide")

# Titre principal
st.title("Analyse de Données Financières")


# Fonction pour afficher les miettes de pain
def show_breadcrumbs(categories):
    breadcrumbs = ""
    for index, category in enumerate(categories):
        if index > 0:
            breadcrumbs += " > "
        breadcrumbs += f"[{category.capitalize()}](#{category.replace(' ', '-')})"
    st.write(breadcrumbs)


# Récupération des données depuis MongoDB
def fetch_data(collection):
    cursor = collection.find({})
    data = list(cursor)
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    # Sélection de la catégorie
    category = st.sidebar.radio("Catégorie", ["Données Historiques", "Prédictions"])

    # Affichage des miettes de pain
    show_breadcrumbs(["Accueil", category])

    if category == "Données Historiques":
        # Affichage des données historiques
        st.header("Données Historiques")

        # Sélection de l'onglet
        tab = st.sidebar.radio("Sélectionner une Source", ["Bourses", "Cryptomonnaies"])

        # Affichage des miettes de pain
        show_breadcrumbs(["Accueil", "Données Historiques", tab])

        # Récupération des données en fonction de l'onglet sélectionné
        if tab == "Bourses":
            df = fetch_data(collection)
            title = "Bourses"
        else:
            df = fetch_data(collection_name_crypto)
            title = "Cryptomonnaies"

        # Sélection du symbole
        selected_symbol = st.selectbox("Sélectionner un Symbole", df['Symbole'].unique())

        # Sélection de la période
        period_options = ['Open', 'Low', 'High', 'Close']
        selected_period = st.selectbox("Sélectionner une Période", period_options)

        # Filtrage des données
        filtered_data = df[df['Symbole'] == selected_symbol]
        filtered_data.set_index('Date', inplace=True)

        # Affichage du graphique
        st.line_chart(filtered_data[selected_period])

    elif category == "Prédictions":
        # Affichage des prédictions
        st.header("Prédictions")

        # Affichage des miettes de pain
        show_breadcrumbs(["Accueil", "Prédictions"])

        # Fonction pour calculer les prédictions
        def make_predictions(collection):
            predictions = []
            for symbol in collection.distinct('Symbole'):
                df_symbol = collection.find({'Symbole': symbol})
                df_symbol = pd.DataFrame(list(df_symbol))
                df_symbol['Date'] = pd.to_datetime(df_symbol['Date'])
                start_date = pd.to_datetime('2024-02-05')
                df_symbol = df_symbol[df_symbol['Date'] >= start_date]
                df_symbol['Days'] = (df_symbol['Date'] - df_symbol['Date'].min()) / np.timedelta64(1, 'D')
                X = df_symbol['Days'].values.reshape(-1, 1)
                y = df_symbol['Close'].values.reshape(-1, 1)
                regressor = LinearRegression()
                regressor.fit(X, y)
                start_forecast_date = pd.to_datetime('2024-03-21')
                days_in_future = 31
                future_business_days = pd.date_range(start_forecast_date, periods=days_in_future, freq=BDay())
                future_forecast_days = [(day - start_date).days for day in future_business_days]
                future_forecast = np.array(future_forecast_days).reshape(-1, 1)
                y_pred = regressor.predict(future_forecast)
                ath_date = df_symbol.loc[df_symbol['Close'].idxmax(), 'Date']
                today = datetime.today()
                if today - ath_date <= timedelta(days=90):
                    ath_period = 'Récent (-3 mois)'
                elif timedelta(days=90) < today - ath_date <= timedelta(days=365):
                    ath_period = 'Moins d\'un an'
                else:
                    ath_period = 'Plus d\'un an'
                last_real_data = df_symbol['Close'].iloc[-1]
                last_predicted_data = y_pred[-1]
                trend = 'Haussière' if last_real_data < last_predicted_data else 'Baissière'
                # Calculer l'évolution attendue en pourcentage
                evolution_pct = ((y_pred[30] - last_real_data) / last_real_data) * 100
                predictions.append({
                    'Symbole': symbol,
                    'Dernière Close': last_real_data,
                    'Date ATH': ath_date,
                    'ATH': df_symbol['Close'].max(),
                    'Période ATH': ath_period,
                    'Tendance': trend,
                    'Prediction J+30': y_pred[30],
                    'Evolution attendue (%)': evolution_pct
                })
            return predictions

        # Prédiction des données
        predictions = make_predictions(collection)
        st.write(predictions)
