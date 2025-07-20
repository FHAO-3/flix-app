import requests
import streamlit as st
from login.service import logout


class ActorsRepository():
    def __init__(self):
        self.__base_url = 'https://fhao.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None

    def create_actors(self, actor: dict):
        # aqui é importante lembrar que nos vamos montar um 'dict' no 'service.py' que ja vai retornar o 'actor'
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor
        )
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        elif response.status_code == 400:
            st.error('Dado Invalido!')
