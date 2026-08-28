import streamlit as st

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱"
)

st.title("🌱 Plant Disease Detection")

st.write(
    "Upload a plant leaf image to get a simple demonstration "
    "of plant disease identification."
)

uploaded_file = st.file_uploader(
    "Upload a plant leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Plant Leaf",
        use_container_width=True
    )

    st.subheader("Detection Result")

    st.info(
        "This is a demonstration version. "
        "A trained machine-learning model would be used "
        "for real disease classification."
    )

    st.write("Possible result: **Healthy / Disease Detected**")

else:
    st.write("Please upload a leaf image to begin.")
