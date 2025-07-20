import requests
import streamlit as st
from login.service import logout


class GenreRepository:
    def __init__(self):
        self.__base_url = 'http://fhao.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }
        # Essa autorização funciona como o Bearer Token do Postman.
        # Esse token que está sendo trazido de `session state` é o que salvamos quando fizemos a parte de login.

    def get_genres(self):
        # Busca gêneros
        response = requests.get(
            self.__genres_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            # OBS: Quando vamos pegar um dado, o status code é 200.
            return response.json()
        elif response.status_code == 401:
            logout()
            return None

    def create_genre(self, genre: dict):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre
        )
        # `headers` é o token de autenticação.
        # O valor que é enviado em `data` é um `dict`.
        if response.status_code == 201:
            # OBS: Quando vamos enviar um dado, o status code é 201.
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        elif response.status_code == 400:
            st.error('Dado Invalido!')