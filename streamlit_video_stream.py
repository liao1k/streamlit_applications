import streamlit as st
st.title('My First Streamlit Tabs Application')
tab_titles = ['Topic A', 'Topic B', 'Topic C', 'Using Stream']
tab1, tab2, tab3, tab4 = st.tabs(tab_titles)
with tab1:
    st.header('Topic A')
    st.write('Topic A content')

with tab2:
    st.header('Topic B')
    st.write('Topic B content')

with tab3:
    st.header('Topic C')
    st.write('Topic C content')

with tab4:
    st.header('YouTube Video 放鬆音樂 Streaming')
    st.video('https://www.youtube.com/watch?v=yjiJ5CBrJg0')

