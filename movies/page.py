import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Fast and furious'
    },
    {
        'id': 3,
        'name': 'It a coisa'
    },
]  # dados mocados para uso futuro


def show_movies():
    st.write('Lista de filmes')
    # a diferença de `st.write` para `st.text` é que o `st.write` aceita qualquer tipo de dado ja o `st.text` aceita so str

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid'
    )
    # tivemos de instalar o `pandas` para transformar essa lista em um `DataFrame` pois a `AgGrid` tem varios recursos de ordenação de tabela baseados em dataframes
