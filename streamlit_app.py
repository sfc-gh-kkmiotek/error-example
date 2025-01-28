import streamlit as st

st.title("🎈 My new app 2025")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

error = st.button('trigger error')
if error:
    1 / 0
