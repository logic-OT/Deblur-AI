from Preprocess import preprocess
from unet import Model


def motion_blur_fix(image,intensity=0):
    path = "saved_weights/motion_blur/"
    motion_weights = ['motion_blur_weights.h5','motionblurweights2.h5']
    #preprocess
    preprocessor = preprocess()
    preprocessed = preprocessor.fit_transform(image)
    #load_weights
    model = Model()
    model.load_weights(path+motion_weights[intensity])
    #prediction
    prediction = model.predict(preprocessed.reshape((1,224,224)))[0]

    return prediction

def sharpen(image,intensity=0):
    path = "saved_weights/average_blur/"
    average_weights = ['averageblurweights.h5','averageblurweights1.h5']
    #preprocess
    preprocessor = preprocess()
    preprocessed = preprocessor.fit_transform(image)
    #load_weights
    model = Model()
    model.load_weights(path+average_weights[intensity])
    #prediction
    prediction = model.predict(preprocessed.reshape((1,224,224)))[0]

    return prediction
