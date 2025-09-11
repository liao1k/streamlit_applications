import streamlit as st
st.title('My First Streamlit Tabs Application')
tab1, tab2, tab3, tab4 = st.tabs(["Cat", "Dog", "Owl", "MusicVideo Streaming"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


with tab4:
    st.header('YT Video 放鬆音樂 Streaming')
    st.video('https://www.youtube.com/watch?v=yjiJ5CBrJg0')



