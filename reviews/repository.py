from login.service import logout
import requests
import streamlit as st


class ReviewRepository:
    def __init__(self):
        self.__base_url = 'https://fhao.pythonanywhere.com/api/v1/'
        self.__review_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_review(self):
        response = requests.get(
            self.__review_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None

    def create_review(self, review):
        response = requests.post(
            self.__review_url,
            headers=self.__headers,
            data=review,
        )
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 401:
            logout()
            return None
        elif response.status_code == 400:
            st.error('Dado Invalido!')