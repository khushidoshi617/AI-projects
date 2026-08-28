import streamlit as st

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰"
)

st.title("📰 Fake News Detector")

st.write(
    "Enter a news statement or article below to analyze "
    "whether it contains potentially suspicious language."
)

news_text = st.text_area(
    "Enter news text:",
    placeholder="Paste or type a news article or statement here..."
)

if st.button("Check News"):
    if not news_text.strip():
        st.warning("Please enter some news text.")
    else:
        text = news_text.lower()

        suspicious_words = [
            "shocking",
            "breaking",
            "secret",
            "miracle",
            "100% true",
            "you won't believe"
        ]

        found_words = []

        for word in suspicious_words:
            if word in text:
                found_words.append(word)

        if found_words:
            st.warning("⚠️ Potentially Suspicious Content")
            st.write("Suspicious words/phrases detected:")
            st.write(", ".join(found_words))

            st.info(
                "This does not prove that the news is fake. "
                "Check reliable sources before believing or sharing it."
            )
        else:
            st.success("ℹ️ No obvious suspicious keywords detected.")

            st.info(
                "This simple application cannot verify whether "
                "the news is actually true or false."
            )

st.divider()

st.write(
    "⚠️ This is a demonstration project. A real fake-news "
    "detector would require a trained NLP/ML model and a "
    "reliable dataset."
)
