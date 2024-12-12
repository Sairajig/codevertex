import streamlit as st
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📚 Book Recommendation System")
st.write("Find books similar to your favorites!")
df = pd.read_csv("data.csv")

if st.checkbox("Show Dataset"):
    st.write(df.head())
    st.write(df.info())

selected_features = ["title", "authors", "categories", "published_year", "thumbnail", "description"]
for feature in selected_features:
    df[feature] = df[feature].fillna("")

combined_features = (
    df["title"].astype(str)
    + " "
    + df["categories"].astype(str)
    + " "
    + df["authors"].astype(str)
    + " "
    + df["published_year"].astype(str)
    + " "
    + df["thumbnail"].astype(str)
    + " "
    + df["description"].astype(str)
)

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors, feature_vectors)

st.header("📖 Enter Your Favorite Book")
book_name = st.text_input("Type a book title:", "")

if book_name:
    list_of_all_titles = df["title"].tolist()
    find_close_match = difflib.get_close_matches(book_name, list_of_all_titles)

    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_book = df[df.title == close_match].index[0]

        similarity_score = list(enumerate(similarity[index_of_the_book]))
        sorted_similar_books = sorted(
            similarity_score, key=lambda x: x[1], reverse=True
        )

        st.subheader(f"📚 Recommendations for: {close_match}")
        top_sim = sorted_similar_books[:10]

        for i, book in enumerate(top_sim):
            index = book[0]
            title_from_index = df.iloc[index]["title"]
            description_from_index = df.iloc[index]["description"]

            st.write(f"### {i+1}. {title_from_index}")
            st.write(f"**Description:** {description_from_index}")
    else:
        st.error("No close match found. Please try another title!")
