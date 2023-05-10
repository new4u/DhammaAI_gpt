import streamlit as st
from PIL import Image
import os
from openai.error import OpenAIError
import streamlit.components.v1 as components

from knowledge_gpt.utils import (
    embed_docs,
    get_answer,
    get_sources,
    parse_docx,
    parse_pdf,
    parse_txt,
    search_docs,
    text_to_docs,
    wrap_text_in_html,
)


def clear_submit():
    st.session_state["submit"] = False


st.set_page_config(page_title="DocGPT", page_icon="📖", layout="wide")
st.header("📖DocGPT")



# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)



# Construct the file path dynamically
#image_path = os.path.abspath("docgpt.jpg")

# Load the image
#img = Image.open(image_path)
#img = Image.open("knowledge_gpt/wechatpay.jpg")

# Load the images
image1 = Image.open("knowledge_gpt/wechatqrcode.jpg")
image2 = Image.open("knowledge_gpt/paypalqrcode.png")

# Display the image with text on top
st.write("Each document costs about $1 for OpenAI API call. Please consider pay to keep this service alive! Thank you!")
st.write("每篇文章调用OpenAI API的费用约为¥7人民币，请帮助支付以便我能够一直提供这个AI小程序，谢谢您！")
#st.image(img, caption=None, width=200)

# Divide the app page into two columns
col1, col2 = st.columns(2)

# Display the first image in the first column
with col1:
    st.image(image1, caption="WeChat Pay", width=200)

# Display the second image in the second column
with col2:
    st.image(image2, caption="PayPal", width=200)

components.html(
   """
<div id="customgpt_chat"></div>
<script src="https://cdn.customgpt.ai/js/embed.js" width="100%" height="500px" p_id="1824" p_key="50a7b1a9e4e384f4b1284a5aa074770f" div_id="customgpt_chat"></script>
	"""
)
components.html(
	"""
	<script src="https://cdn.customgpt.ai/js/chat.js"></script>

<script>window.onload = function () { CustomGPT.init({p_id: "1824", p_key: "50a7b1a9e4e384f4b1284a5aa074770f" }); };</script>
	"""
)
