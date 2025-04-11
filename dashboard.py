import streamlit as st

def app(veiculos_data):
    st.title("📊 Dashboard de Veículos")
    st.write("Aqui você pode ver estatísticas da frota.")

    st.dataframe(veiculos_data)

    # Exemplo de contagem de veículos por ano
    if 'ano' in veiculos_data.columns:
        st.bar_chart(veiculos_data['ano'].value_counts().sort_index())
