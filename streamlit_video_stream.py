import streamlit as st
st.title('昆明 Streamlit on GitHub via Cursor AI Editor')
tab1, tab2, tab3, tab4 = st.tabs(["一只猫", "一只狗", "一只猫头鹰", "AWS 财金视频"])

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
    st.header('AWS 财金视频')
    st.video('https://banyanhill.s3.dualstack.us-east-1.amazonaws.com/StrategicFortunes/Webinar/2025/Landing_Pages/090225_IKA_LP.html?vid2=75525ca09396c0ad367ebb455ae64960daf5aab968bdd0b8dfacc5d5bfa87d92f7df0e92a0a2854d1ed2c08675657a64&utm_campaign=090225_IKA_Weekly_-_All&utm_source=Iterable&utm_medium=email&itbl_templateId=19310838&itbl_campaignId=14820195')



