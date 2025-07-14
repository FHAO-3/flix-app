import streamlit as st

st.title('Hello world!')
# Esse geito acima é como fazemos para passar um titulo
st.divider()
# esse comando acima é usado para colocar uma linh dividindo
code = '''def hello():
    print("Hello, World with Streamlit")'''
st.code(code, language='python')
# acima esta como colocar os trechos de codigo amostra na tela do site
st.text('Output: "Hello, World with Streamlit"')
# acima temos como escrever textos normais na tela

st.divider()

st.text_input('Digite seu email', placeholder='email@server.com')
# essa maneira é como faz para um campo onde o usuario pode passar um texto
st.text_input('Digite sua senha', placeholder='Senha123')
st.divider()
