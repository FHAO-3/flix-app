import streamlit as st
from reviews.repository import ReviewRepository


class ReviewService:
    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repository.get_review()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie, stars, comment):
        review = dict(
            stars=stars,
            comment=comment,
            movie=movie,
        )
        new_reviews = self.review_repository.create_review(review)
        st.session_state.reviews.append(new_reviews)
        return new_reviews
