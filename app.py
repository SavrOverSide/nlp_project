import streamlit as st

user_review = st.text_input(label='Оставьте свой отзыв здесь')

if user_review:
    st.write(user_review)