import requests
import streamlit as st
from login.service import logout


class MoviesRepository:
    def __init__(self):
        self.__base_url = 'http://fhao.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers
        )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None

    def create_movies(self, movie):
        for i in movie:
            print(f'>>> {i}')
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie
        )
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        elif response.status_code == 400:
            st.error('Dado Invalido!')
