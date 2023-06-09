import streamlit as st
from PIL import Image
import os
# from knowledge_gpt.components.sidebar import sidebar
import streamlit.components.v1 as components
# from openai.error import OpenAIError

st.set_page_config(page_title="new4uAI", page_icon="📖", layout="wide")
# st.header("扫描码或者联系小助手1259388进群")

# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """

# button = """
# <script src="https://cdn.customgpt.ai/js/chat.js"></script>

# 	<script>window.onload = function () { CustomGPT.init({p_id: "1824", p_key: "50a7b1a9e4e384f4b1284a5aa074770f" }); };</script>"""

# components.html(button, 
# 	height=700,)

# st.markdown(
#     """
#     <style>
#         iframe[width=100%] {
#             position: fixed;
#             bottom: 30px;
#             right: 50px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# sidebar()
# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)

components.html(
   """
   
<div id="customgpt_chat"></div>
<script src="https://cdn.customgpt.ai/js/embed.js" width="100%" height="500px" p_id="4650" p_key="a870e3adb5c26e1ef3a70e4588b6035a" div_id="customgpt_chat"></script>
""",height=500,
)

components.html(
"""
<button onclick="document.getElementById('feedback-form').style.display='block'">任何问题都可以联系我 </button>

<div id="feedback-form" style="display:none;">
<h2>反馈</h2>
<form action="mailto:zhangpei.adam@gmail.com" method="post" enctype="text/plain">
<label for="feedback">请提供反馈：</label>


<textarea id="feedback" name="feedback" rows="5" cols="50"></textarea>


<input type="submit" value="提交">
<input type="reset" value="重置">
</form>
</div>
""",
	height=200,
)

# # Display the image with text on top
st.write("Each document costs about $1 for OpenAI API call. Please consider pay to keep this service alive! Thank you!")

# # Construct the file path dynamically
# #image_path = os.path.abspath("docgpt.jpg")



# Load the images
image1 = Image.open("knowledge_gpt/wechatqrcode.jpg")
image2 = Image.open("knowledge_gpt/paypalqrcode.png")


# Divide the app page into two columns
col1, col2= st.columns(2)

# Display the first image in the first column
with col1:
     st.image(image1, caption="WeChat Pay", width=200)

# Display the second image in the second column
with col2:
     st.image(image2, caption="PayPal", width=200)
