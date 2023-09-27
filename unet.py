import keras

def layer(f,k,s,p):
        conv1 = keras.layers.Conv2D(f,k,s,padding='same',activation='relu')(p)
        conv2 = keras.layers.Conv2D(f,k,s,padding='same',activation='relu')(conv1)

        return conv2

def unet(Input):
    #encoder
    layer1 = layer(32,2,1,Input)
    pool1 = keras.layers.MaxPool2D((2,2))(layer1)

    layer2= layer(64,2,1,pool1)
    pool2 = keras.layers.MaxPool2D((2,2))(layer2)

    layer3 = layer(128,2,1,pool2)
    pool3 = keras.layers.MaxPool2D((2,2))(layer3)

    layer4= layer(256,2,1,pool3)
    pool4 = keras.layers.MaxPool2D((2,2))(layer4)

    layer5= layer(512,2,1,pool4)
    pool5 = keras.layers.MaxPool2D((2,2))(layer5)
    #end of encoder

    #decoder
    upsample0= keras.layers.UpSampling2D((2,2))(pool5)
    skip1 = keras.layers.Concatenate()([upsample0,layer5])
    conv1 = keras.layers.Conv2D(512,2,1,padding='same',activation='relu')(skip1)
    conv2 = keras.layers.Conv2D(512,2,1,padding='same',activation='relu')(conv1)


    upsample1 = keras.layers.UpSampling2D((2,2))(conv2)
    skip2 = keras.layers.Concatenate()([upsample1,layer4])
    conv3= keras.layers.Conv2DTranspose(256,2,1,padding='same',activation='relu')(skip2)
    conv4= keras.layers.Conv2DTranspose(256,2,1,padding='same',activation='relu',dilation_rate=2)(conv3)

    upsample2 = keras.layers.UpSampling2D((2,2))(conv4)
    skip3 = keras.layers.Concatenate()([upsample2,layer3])
    conv5 = keras.layers.Conv2DTranspose(128,2,1,padding='same',activation='relu')(skip3)
    conv6 = keras.layers.Conv2DTranspose(128,2,1,padding='same',activation='relu',dilation_rate=3)(conv5)

    upsample3 = keras.layers.UpSampling2D((2,2))(conv6)
    skip4 = keras.layers.Concatenate()([upsample3,layer2])
    conv7 = keras.layers.Conv2DTranspose(64,2,1,padding='same',activation='relu')(skip4)
    conv8 = keras.layers.Conv2DTranspose(64,2,1,padding='same',activation='relu',dilation_rate=3)(conv7)


    upsample4 = keras.layers.UpSampling2D((2,2))(conv8)
    skip5 = keras.layers.Concatenate()([upsample4,layer1])
    conv9 = keras.layers.Conv2DTranspose(64,2,1,padding='same',activation='relu')(skip5)
    conv10 = keras.layers.Conv2DTranspose(64,2,1,padding='same',activation='relu')(conv9)

    #end of decoder

    return conv10

def Model():
    Input = keras.layers.Input((None,None,1))
    archictecture = unet(Input)
    output =  keras.layers.Conv2D(1,1,activation='sigmoid')(archictecture)
    model = keras.Model(inputs=Input,outputs=output)
    model.compile(loss='mse',optimizer='adam')

    return model
