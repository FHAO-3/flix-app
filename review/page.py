import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'stars': 4
    },
    {
        'id': 2,
        'stars': 5
    },    
    {
        'id': 3,
        'stars': 3
    },
]  # dados mocados para uso futuro


def show_reviews():
    st.write('Lista de avaliações')
    # a diferença de `st.write` para `st.text` é que o `st.write` aceita qualquer tipo de dado ja o `st.text` aceita so str

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid'
    )
    # tivemos de instalar o `pandas` para transformar essa lista em um `DataFrame` pois a `AgGrid` tem varios recursos de ordenação de tabela baseados em dataframes

    st.divider()

    st.title('Cadastrar novo avaliação')
    name = st.text_input('Nome do avaliação').title()
    if st.button('Confirmar'):
        st.success(f'avaliação "{name}" adicionado com sucesso!')
