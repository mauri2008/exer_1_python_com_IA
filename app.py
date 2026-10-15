import streamlit as st

# Configuração da página (Título na aba do navegador e layout)
st.set_page_config(
    page_title="Calculadora Simples",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write("Selecione a operação, insira os números e clique em **Calcular**.")

st.divider()

# 2. Entradas numéricas
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro número:", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Segundo número:", value=0.0, format="%.2f")

# 3. Seleção da operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"]
)

st.write("")  # Espaçamento simples

# 4 e 5. Botão de ação e lógica do cálculo
if st.button("Calcular", type="primary", use_container_width=True):
    resultado = None
    erro = False

    if operacao == "Soma (+)":
        resultado = num1 + num2
        simbolo = "+"
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
        simbolo = "-"
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
        simbolo = "×"
    elif operacao == "Divisão (/)":
        if num2 == 0:
            st.error("⚠️ Erro: Divisão por zero não é permitida!")
            erro = True
        else:
            resultado = num1 / num2
            simbolo = "÷"

    # Exibição do resultado se não houver erro
    if not erro and resultado is not None:
        st.success("Cálculo realizado com sucesso!")
        st.metric(
            label=f"Resultado ({num1} {simbolo} {num2}):",
            value=f"{resultado:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        )
