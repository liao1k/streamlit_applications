import streamlit as st
from PIL import Image
HEIF_SUPPORTED = False
HEIF_ERROR = None
try:
    import pillow_heif
    if hasattr(pillow_heif, "register_heif_opener"):
        pillow_heif.register_heif_opener()
        HEIF_SUPPORTED = True
    elif hasattr(pillow_heif, "register_heif"):
        pillow_heif.register_heif()
        HEIF_SUPPORTED = True
    else:
        HEIF_ERROR = "pillow_heif missing register function"
except Exception as e:
    HEIF_ERROR = str(e)
st.title('昆明 Streamlit on GitHub via Cursor AI Editor')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["一只猫", "一只狗", "一只猫头鹰", "当前市场", "本地视频"])

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
    st.header("当前市场")
    if HEIF_SUPPORTED:
        try:
            image = Image.open("CurrentMarket.heic")
            st.image(image, width='stretch')
        except Exception as e:
            st.error(f"HEIC 打开失败: {e}")
    else:
        st.error(f"缺少 HEIC 支持。请先安装: pip install pillow-heif。原因: {HEIF_ERROR}")
with tab5:
    st.header('本地视频')
    st.video("IMG_1908.MOV")







