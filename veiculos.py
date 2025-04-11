import streamlit as st
import pandas as pd
from datetime import datetime

CAMINHO_VEICULOS = "dados/veiculos.csv"  # caminho fixo ou você pode passar via parâmetro

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

def app(veiculos_data):
    st.title("🚘 Gestão de Veículos")
    
    st.subheader("📋 Lista de Veículos")
    st.dataframe(veiculos_data)

    st.markdown("---")

    with st.expander("➕ Adicionar Novo Veículo"):
        with st.form("form_veiculo"):
            placa = st.text_input("Placa")
            modelo = st.text_input("Modelo")
            ano = st.number_input("Ano", min_value=1900, max_value=datetime.now().year, step=1)
            categoria = st.selectbox("Categoria", ["A", "B", "D"])
            km_atual = st.number_input("KM Atual", min_value=0, step=100)
            data_compra = st.date_input("Data de Compra")

            if st.form_submit_button("Salvar"):
                if not placa or not modelo:
                    st.error("Preencha todos os campos obrigatórios.")
                else:
                    status = calcular_status(int(ano), categoria)

                    novo = {
                        "placa": placa.upper(),
                        "modelo": modelo,
                        "ano": int(ano),
                        "categoria": categoria,
                        "data_compra": data_compra.strftime('%Y-%m-%d'),
                        "status": status,
                        "km_atual": int(km_atual)
                    }

                    try:
                        df = pd.read_csv(CAMINHO_VEICULOS)

                        if novo["placa"] in df["placa"].values:
                            st.warning("🚫 Essa placa já está cadastrada.")
                        else:
                            df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
                            df.to_csv(CAMINHO_VEICULOS, index=False)
                            st.success("✅ Veículo adicionado com sucesso!")
                            st.rerun()  # Recarrega a página para atualizar a lista
                    except FileNotFoundError:
                        df = pd.DataFrame([novo])
                        df.to_csv(CAMINHO_VEICULOS, index=False)
                        st.success("✅ Veículo adicionado com sucesso!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao salvar o veículo: {e}")
