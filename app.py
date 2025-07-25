import streamlit as st
from actors.page import show_actors
from genres.page import show_genres
from home.page import show_home
from login.page import show_login
from movies.page import show_movies
from reviews.page import show_reviews


# usando função por questões de boas praticas
def main():
    if 'token' not in st.session_state:
        # if logout
        show_login()
    else:
        # if login
        st.title("Flix App")
        menu_option = st.sidebar.selectbox(
            'selecione uma das opções abaixo',
            ['Inicio', 'Atores/Atrizes', 'Avaliações', 'Generos', 'Filmes']
        )
        match menu_option:
            case 'Inicio':
                show_home()
            case 'Atores/Atrizes':
                show_actors()
            case 'Avaliações':
                show_reviews()
            case 'Generos':
                show_genres()
            case 'Filmes':
                show_movies()


if __name__ == '__main__':
    main()