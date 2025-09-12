import streamlit as st
st.title('昆明 Streamlit on GitHub via Cursor AI Editor')
tab1, tab2, tab3, tab4 = st.tabs(["一只猫", "一只狗", "一只猫头鹰", "本地视频"])

with tab1:
    st.header("一只猫")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("一只狗")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("一只猫头鹰")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
with tab4:
    st.header('本地视频')
    st.video("IMG_1908.MOV")







