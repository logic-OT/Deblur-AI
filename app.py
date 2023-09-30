import streamlit as st
from PIL import Image
from deblur import sharpen,motion_blur_fix

st.title('Welcome to Deblur AI')

lead = Image.open('media/delur head.png')
st.image(lead,width=300)

st.write('**Deblur AI** allows you to fix blurriness and sharpen images of faces. It works by using UNet Architecture to handle motion blurred and low quality images.')
st.write('This version currently outputs only **Black and white** results!')
st.header('Lets Go!')

option = st.selectbox('**Which operation do you want to perform**', options=['Sharpening','Motion Blur fix'])
intensity = st.selectbox('**Intensity**', options=['low','high'])

st.write('#### Upload your image')
file = st.file_uploader('Upload your image')




intensity_dict ={'low':0,'high':1}
if file is not None:
    image = Image.open(file)
    st.image(image,caption='Is this your image?',width=300)
    
    clicked = st.button(':green[TRANSFORM]')

    if clicked:
        if option == 'Sharpening':
            fixed = sharpen(image,intensity=intensity_dict[intensity])
            st.image(fixed,caption='Voila!!!!!!',width=300)

        if option == 'Motion Blur fix':
            fixed = motion_blur_fix(image,intensity=intensity_dict[intensity])
            st.image(fixed,caption='Voila!!!!!!',width=300)






