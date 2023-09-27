import cv2
import numpy as np

class preprocess:
    def __init__(self):
        self.detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    def fit_transform(self,image):
        image = np.array(image)
        zoomed = self.__zoom_face(image)
        preprocessed = self.__resize_and_gray(zoomed)
        preprocessed = preprocessed
        
        return preprocessed/255

    def __zoom_face(self,image):
        a = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        face = self.detector.detectMultiScale(a,scaleFactor=1.1,minNeighbors=10)
        if face != ():
            x,y,w,h=face[0]
            padding = 120
            x = max(x - padding, 0)
            y = max(y - padding, 0)
            w = w + 2 * padding
            h = h + 2 * padding
            return image[y:y+h, x:x+w]
        else:
            return image
                
    def __resize_and_gray(self,image):
        print(image)
        transformed = cv2.resize(image,(224,224))
        transformed = cv2.cvtColor(transformed,cv2.COLOR_BGR2GRAY)
        
        return transformed


        