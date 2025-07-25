import streamlit as st
from actors.repository import ActorsRepository


class ActorsService():
    def __init__(self):
        self.actor_repository = ActorsRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actors(self, name, birthday, nationality):
        actor = {
            'name': name,
            'birthday': birthday,
            'nationality': nationality
        }
        new_actor = self.actor_repository.create_actors(actor=actor)
        st.session_state.actors.append(new_actor)
        return new_actor
