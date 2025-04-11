import streamlit as st
from streamlit_option_menu import option_menu
import home, veiculos, cadastro
from datetime import datetime
import pandas as pd
import os

CAMINHO_VEICULOS = "dados/veiculos.csv"

st.set_page_config(page_title="Gestão de Frota - Autoescola", page_icon="🚗", layout="wide")

# === CSS escuro moderno ===
st.markdown("""
    <style>
        .stApp {
            background-color: #121212;
            color: #E0E0E0;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #00c6ff;
        }
        input, select, textarea {
            background-color: #1E1E1E !important;
            color: #ffffff !important;
            border: 1px solid #00c6ff !important;
            border-radius: 8px;
        }
        button[kind="primary"] {
            background-color: #00c6ff !important;
            color: white !important;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Função para status
def calcular_status(ano, categoria):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    prazos = {"A": 8, "B": 12, "D": 20}
    prazo = prazos.get(categoria, 0)

    if idade >= prazo:
        return "Fora do prazo"
    elif idade == prazo - 1:
        return "Próximo do prazo"
    else:
        return "Dentro do prazo"

# Verificar alertas
def verificar_alertas():
    if not os.path.exists(CAMINHO_VEICULOS):
        return []

    try:
        df = pd.read_csv(CAMINHO_VEICULOS)
        alertas = []

        for _, row in df.iterrows():
            status = calcular_status(int(row["ano"]), row["categoria"])
            idade = datetime.now().year - int(row["ano"])
            prazo = {"A": 8, "B": 12, "D": 20}.get(row["categoria"], 0)

            if status in ["Fora do prazo", "Próximo do prazo"]:
                alertas.append({
                    "Placa": row["placa"],
                    "Modelo": row["modelo"],
                    "Status": status,
                    "Idade": idade,
                    "Prazo": prazo
                })
        return alertas
    except:
        return []

# Carregar veículos
def carregar_veiculos():
    try:
        return pd.read_csv(CAMINHO_VEICULOS)
    except:
        return pd.DataFrame()

# Menu lateral
menu = option_menu(
    menu_title="Menu Principal",
    options=["Início", "Veículos", "Cadastro"],
    icons=["house", "car-front", "clipboard-check"],
    default_index=0,
    orientation="horizontal"
)

# Roteamento entre as páginas
if menu == "Início":
    alertas = verificar_alertas()
    home.app(alertas)

elif menu == "Veículos":
    veiculos_data = carregar_veiculos()
    veiculos.app(veiculos_data)

elif menu == "Cadastro":
    cadastro.app(CAMINHO_VEICULOS)
