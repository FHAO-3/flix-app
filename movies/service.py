from movies.repository import MoviesRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MoviesRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()

    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        return self.movie_repository.create_movies(movie=movie)
