import streamlit as st
from PIL import Image
import numpy as np
import json
import redisai as rai

img_file_buffer = st.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"])

if img_file_buffer:
    image = Image.open(img_file_buffer)
    if image is not None:
        img_array = np.array(image)

        device = 'cpu'
        con = rai.Client(host='redisai', port='6379')

        class_idx = json.load(open("imagenet_classes.json"))
        con.tensorset('image', img_array)
        out4 = con.scriptrun(
            'imagenet_script', 'pre_process_3ch', 'image', 'temp1')
        out5 = con.modelrun('imagenet_model', 'temp1', 'temp2')
        out6 = con.scriptrun('imagenet_script', 'post_process', 'temp2', 'out')
        final = con.tensorget('out')
        ind = final.item()
        st.image(
            image,
            caption="Class: {}".format(class_idx[str(ind)]),
            use_column_width=True,
        )
