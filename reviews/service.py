from reviews.repository import ReviewRepository


class ReviewService:
    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        return self.review_repository.get_review()

    def create_review(self, movie, stars, comment):
        review = dict(
            stars=stars,
            comment=comment,
            movie=movie,
        )
        return self.review_repository.create_review(review)
