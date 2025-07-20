from actors.repository import ActorsRepository


class ActorsService():
    def __init__(self):
        self.actor_repository = ActorsRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()

    def create_actors(self, name, birthday, nationality):
        actor = {
            'name': name,
            'birthday': birthday,
            'nationality': nationality
        }
        return self.actor_repository.create_actors(
            actor=actor
        )
