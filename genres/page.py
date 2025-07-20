import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()  # ja recebe um json

    if genres:
        st.write('Lista de gêneros')
        # a diferença de `st.write` para `st.text` é que o `st.write` aceita qualquer tipo de dado ja o `st.text` aceita sp str
        AgGrid(
            data=pd.json_normalize(genres),  # transforma o json em dataframe
            reload_data=True,
            key='genres_grid'
        )
        # tivemos de instalar o `pandas` para transformar essa lista em um `DataFrame` pois a `AgGrid` tem varios recursos de ordenação de tabela baseados em dataframes
    else:
        st.warning('Nenhum gênero encontrado')

    st.divider()

    st.title('Cadastrar novo genero')
    name = st.text_input('Nome do genero').title()
    if st.button('Confirmar'):
        new_genre = genre_service.create_genre(
            name=name
        )
        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o gênero. Verifique o campos')
