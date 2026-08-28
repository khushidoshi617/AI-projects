import streamlit as st

st.set_page_config(
    page_title="Mental Health Assistant",
    page_icon="🧠"
)

st.title("🧠 Mental Health Assistant")

st.write(
    "This application provides general supportive wellness information "
    "based on how the user is feeling."
)

st.subheader("How are you feeling today?")

feeling = st.text_area(
    "Describe your feelings:",
    placeholder="Write how you are feeling..."
)

if st.button("Get Support"):
    if feeling.strip():
        st.success("Thank you for sharing. Remember to take care of yourself.")

        st.write("### General Supportive Suggestions")
        st.write("- Take a short break and relax.")
        st.write("- Talk to someone you trust.")
        st.write("- Get enough rest and sleep.")
        st.write("- Spend some time doing an activity you enjoy.")
        st.write("- If you are struggling, consider talking to a qualified professional.")
    else:
        st.warning("Please enter how you are feeling.")
