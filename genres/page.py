import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comedia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]  # dados mocados para uso futuro


def show_genres():
    st.write('Lista de generos')
    # a diferença de `st.write` para `st.text` é que o `st.write` aceita qualquer tipo de dado ja o `st.text` aceita sp str

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid'
    )
    # tivemos de intalar o `pandas` para transformar essa lista em um `DataFrame` pois a `AgGrid` tem varios recursos de ordenação de tabela baseados em dataframes

    st.divider()

    st.title('Cadastrar novo genero')
    name = st.text_input('Nome do genero').title()
    if st.button('Confirmar'):
        st.success(f'Genero "{name}" Cadastrado com sucesso!')
