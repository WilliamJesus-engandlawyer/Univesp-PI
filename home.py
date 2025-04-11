import streamlit as st

def app(alertas):
    st.title("🏠 Início")
    st.subheader("⚠️ Alertas de Troca de Veículos")

    if alertas:
        for alerta in alertas:
            st.error(f"🚨 {alerta['Placa']} ({alerta['Modelo']}) - {alerta['Status']} (idade: {alerta['Idade']}, prazo: {alerta['Prazo']})")
    else:
        st.success("✅ Nenhum veículo perto do prazo de troca.")

