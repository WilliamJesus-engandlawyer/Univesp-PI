import streamlit as st
import pandas as pd
from datetime import datetime

def calcular_status(ano, categoria):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    prazos = {
        "A": 8,
        "B": 12,
        "D": 20
    }

    prazo = prazos.get(categoria)
    if prazo is None:
        return "Categoria inválida"

    if idade >= prazo:
        return "Fora do prazo"
    elif idade == prazo - 1:
        return "Próximo do prazo"
    else:
        return "Dentro do prazo"

def app(caminho_csv):
    st.title("📝 Cadastro de Veículos")

    with st.form("cadastro_form"):
        placa = st.text_input("Placa").upper()
        modelo = st.text_input("Modelo")
        ano = st.number_input("Ano", min_value=1900, max_value=datetime.now().year)
        categoria = st.selectbox("Categoria", ["A", "B", "D"])
        data_compra = st.date_input("Data de Compra")

        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            if not placa or not modelo:
                st.error("⚠️ Preencha todos os campos obrigatórios.")
            else:
                status = calcular_status(int(ano), categoria)

                novo_veiculo = {
                    "placa": placa,
                    "modelo": modelo,
                    "ano": int(ano),
                    "categoria": categoria,
                    "data_compra": data_compra.strftime('%Y-%m-%d'),
                    "status": status,
                    "km_atual": 0
                }

                try:
                    df = pd.read_csv(caminho_csv)

                    if placa in df["placa"].values:
                        st.warning("🚫 Essa placa já está cadastrada.")
                    else:
                        df = pd.concat([df, pd.DataFrame([novo_veiculo])], ignore_index=True)
                        df.to_csv(caminho_csv, index=False)
                        st.success("✅ Veículo cadastrado com sucesso!")
                        st.rerun()

                except FileNotFoundError:
                    df = pd.DataFrame([novo_veiculo])
                    df.to_csv(caminho_csv, index=False)
                    st.success("✅ Veículo cadastrado com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao salvar os dados: {e}")
