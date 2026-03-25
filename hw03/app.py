import streamlit as st
import numpy as np
from PIL import Image
from src.face_utils import detect_faces, draw_face_boxes

# 网页标题
st.title("🧑 人脸识别作业")

# 上传图片
uploaded = st.file_uploader("上传一张有人脸的照片", type=["jpg", "png"])

if uploaded is not None:
    # 打开图片
    img = Image.open(uploaded)
    img_array = np.array(img)

    # 检测人脸
    locations = detect_faces(img_array)
    st.success(f"✅ 检测到 {len(locations)} 张人脸！")

    # 画框
    img_result = draw_face_boxes(img_array.copy(), locations)

    # 显示结果
    st.image(img_result, caption="人脸识别结果", use_column_width=True)