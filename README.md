
# 🚗 Sistema de Gestão de Frota para Autoescolas

Este projeto tem como objetivo oferecer uma solução automatizada para **monitoramento e controle dos prazos de substituição dos veículos** utilizados por autoescolas. Desenvolvido com Python e Streamlit, o sistema ajuda a evitar falhas administrativas causadas por controles manuais, fornecendo alertas automáticos sobre a proximidade dos prazos de troca obrigatória da frota.

---

## 📌 Contexto

As autoescolas desempenham um papel crucial na formação de condutores. Uma das exigências legais para o funcionamento dessas instituições é a **gestão eficiente da frota de veículos**, com a substituição obrigatória dos veículos conforme regulamentação do órgão competente. O não cumprimento pode levar à exclusão dos veículos do sistema e à suspensão das atividades da autoescola.

Muitas instituições ainda realizam esse controle manualmente, o que aumenta os riscos de falhas. Este software foi criado justamente para resolver esse problema.

---

## ⚙️ Funcionalidades

- 📋 Cadastro de veículos (com placa, modelo, ano, categoria, quilometragem e data de compra).
- 🚨 Alertas automáticos para veículos próximos do prazo ou fora do prazo de validade.
- 📊 Listagem e visualização de todos os veículos cadastrados.
- 💡 Cálculo automático do status de validade com base na categoria:
  - Categoria A: 8 anos
  - Categoria B: 12 anos
  - Categoria D: 20 anos
- 💾 Armazenamento dos dados em arquivos CSV.

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu)

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/WilliamJesus-engandlawyer/Univesp-PI.git
   cd Univesp-PI/main
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo Streamlit:
   ```bash
   streamlit run main.py
   ```

---

## 📁 Estrutura do Projeto

```
Univesp-PI/
│
├── main/
│   ├── main.py                # Arquivo principal do app
│   ├── home.py                # Página inicial com alertas
│   ├── veiculos.py            # Página de listagem e cadastro
│   ├── cadastro.py            # Formulário de novos veículos
│   └── dados/
│       └── veiculos.csv       # Base de dados dos veículos
```

---

## 📝 Licença

Este projeto foi desenvolvido como parte de um Projeto Integrador da UNIVESP. Uso educacional e não comercial.

---

## 👨‍💻 Autor

**William Jesus**  
Estudante de Engenharia da Computação – UNIVESP  
Desenvolvedor backend e entusiasta por soluções digitais para problemas reais.
```
