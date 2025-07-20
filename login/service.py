import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    # chamando autenticação de login
    response = auth_service.get_token(
        username,
        password
    )
    # realizando a autenticação de login
    if response.get('error'):
        st.error(f'Falha ao realizar login: {response.get("error")}')
    else:
        st.session_state.token = response.get('access')
        # obiservação o nome dessa `variavel session state` pode ser qualquer um mas tem que ser mais descritivi possivel
        st.rerun()
        # funciona como se fosse um reload na tela
        # obiservacão o `st.rerun()` é usado quando queremos dar reload somente na tela atual
    # varificando se o login deu certo, se login correto salva o token e recarrega a tela


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()