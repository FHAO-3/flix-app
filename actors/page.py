import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorsService


def show_actors():
    actor_service = ActorsService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Ator/Atriz')
        # a diferença de `st.write` para `st.text` é que o `st.write` aceita qualquer tipo de dado ja o `st.text` aceita so str
        # converte a lista de atores/atrizes em um DataFrame do pandas
        AgGrid(
            data=pd.json_normalize(actors),
            key='actors_grid'
        )
        # tivemos de instalar o `pandas` para transformar essa lista em um `DataFrame` pois a `AgGrid` tem varios recursos de ordenação de tabela baseados em dataframes
    else:
        st.warning('Nenhum ator/atriz encontrado')

    st.divider()

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do (da) Ator/Atriz').title()

    st.title('Data de nascimento')
    birthday = st.date_input(
        label='Data de nascimanto do (da) Ator/Atriz',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),  # valor minimo para data
        max_value=datetime.today(),  # valor maximo para data
        format='DD/MM/YYYY'  # modelo de data
    )
    st.title('Nacionalidade do ator/atriz')
    nationality_dropdown = ['Nacionalidade', 'BRAZIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )
    if st.button('Confirmar'):
        new_actor = actor_service.create_actors(
            name=name,
            birthday=birthday,
            nationality=nationality
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o ator/atriz. Verifique os campos')
