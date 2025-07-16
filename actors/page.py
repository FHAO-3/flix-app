import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Vin Diesel',
        'birthday': '1967-07-18',
        'nationality': 'USA'
    },
    {
        'id': 2,
        'name': 'Paul Walker',
        'birthday': '1973-09-12',
        'nationality': 'USA'
    },
    {
        'id': 3,
        'name': 'Michele Rodriguez',
        'birthday': '1078-07-12',
        'nationality': 'USA'
    },
    {
        'id': 4,
        'name': 'Jordana Brewster',
        'birthday': '1980-08-26',
        'nationality': 'USA'
    },
]  # dados mocados para uso futuro


def show_actors():
    st.write('Lista de Ator/Atriz')
    # a diferença de `st.write` para `st.text` é que o `st.write` aceita qualquer tipo de dado ja o `st.text` aceita so str

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid'
    )
    # tivemos de instalar o `pandas` para transformar essa lista em um `DataFrame` pois a `AgGrid` tem varios recursos de ordenação de tabela baseados em dataframes

    st.divider()

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do (da) Ator/Atriz').title()
    if st.button('Confirmar'):
        st.success(f'Ator/Atriz "{name}" Cadastrado com sucesso!')
