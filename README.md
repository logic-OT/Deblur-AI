# Deblur-AI
Deblur AI allows you to fix blurriness and sharpen images of faces. It works by using **UNet Architecture** to handle **motion blurred** and **low quality images**.

![delur head](https://github.com/logic-OT/Deblur-AI/assets/61668807/75010852-0f95-4597-8900-1dfc5fe389bf)


This version currently outputs only **black-and-white** results!

## Website
[https://deblur-ai.streamlit.app/](https://deblur-ai.streamlit.app/)

## Notebook
**This is the link to the original notebook:** [https://colab.research.google.com/drive/1w4IIBOqMTlrYgOya_N7YOcjBI98EC19K?usp=sharing](https://colab.research.google.com/drive/1w4IIBOqMTlrYgOya_N7YOcjBI98EC19K?usp=sharing)


# Datatset
I scaped collection of 602 images with from web making sure the images were as representative of different facial inflexions as possible. I then applied diffrent blur kernels of motion blur and average blur to create blur images.

**Find the data here**

# Models 
I trained 4 models. 2 models for the average blurred images and 2 models for the motion blurred images.  The 2 models for each blur type were trained on different blur kernels thus have different adjustment intensities.

![Screenshot (133)](https://github.com/logic-OT/Deblur-AI/assets/61668807/d88930b2-d9c2-4ffc-88f1-0db6fc98e11c)

# Results
![Screenshot (135)](https://github.com/logic-OT/Deblur-AI/assets/61668807/83b6001b-3a50-4923-8dc3-2e2765183a36)


# Example Prediction

![download (62)](https://github.com/logic-OT/Deblur-AI/assets/61668807/99e7b291-fc37-4bd5-af18-fd2ba92b77e0)
![download (63)](https://github.com/logic-OT/Deblur-AI/assets/61668807/c3e17821-d27b-418a-929d-20e4dc14a55e)



