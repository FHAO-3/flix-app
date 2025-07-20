import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from review.service import ReviewService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_review()
    if reviews:
        st.write('Lista de avaliações')

        AgGrid(
            data=pd.json_normalize(reviews),
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Não foi encontrado dados cadastrados')
    st.divider()
