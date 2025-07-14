import streamlit as st
from genres.page import show_genres


# usando função por questões de boas praticas
def main():
    st.title("Flix App")
    menu_option = st.sidebar.selectbox(
        'selecione uma das opções abaixo',
        ['Inicio', 'Atores/Atrizes', 'Avaliações', 'Generos', 'Filmes']
    )

    match menu_option:
        case 'Inicio':
            st.write('Inicio')
        case 'Atores/Atrizes':
            st.write('Lista de Atores/Atrizes')
        case 'Avaliações':
            st.write('Feedbacks')
        case 'Generos':
            show_genres()
        case 'Filmes':
            st.write('Lista de filmes')


if __name__ == '__main__':
    main()
