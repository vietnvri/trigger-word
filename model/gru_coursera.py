from keras.layers import Input, BatchNormalization, Conv1D, Dropout, GRU, TimeDistributed, Dense, Activation
from keras.models import Model, load_model
import keras.backend as K


def model(input_shape):
    """
    Function creating the model's graph in Keras.

    Argument:
    input_shape -- shape of the model's input data (using Keras conventions)

    Returns:
    model -- Keras model instance
    """

    X_input = Input(shape=input_shape)

    # Step 1: CONV layer
    X = Conv1D(256, kernel_size=15, strides=4)(X_input)  # CONV1D
    X = BatchNormalization()(X)  # Batch normalization
    X = Activation('relu')(X)  # ReLu activation
    X = Dropout(0.8)(X)  # dropout (use 0.8)
    print(X.shape)

    # Step 2: First GRU Layer
    X = GRU(units=128, return_sequences=True)(X)  # GRU (use 128 units and return the sequences)
    X = Dropout(0.8)(X)  # dropout (use 0.8)
    X = BatchNormalization()(X)  # Batch normalization

    # Step 3: Second GRU Layer
    X = GRU(units=128, return_sequences=True)(X)  # GRU (use 128 units and return the sequences)
    X = Dropout(0.8)(X)  # dropout (use 0.8)
    X = BatchNormalization()(X)  # Batch normalization
    X = Dropout(0.8)(X)  # dropout (use 0.8)

    # Step 4: Time-distributed dense layer
    X = TimeDistributed(Dense(1, activation="sigmoid"))(X)  # time distributed  (sigmoid)
    model = Model(inputs=X_input, outputs=X)
    return model


# import numpy as np
#
#
# def loss(y_true, y_pred):
#     weight = np.zeros_like(y_true)
#     weight = weight * 9
#     return K.mean(
#         K.mean(- weight * y_true * K.log(y_pred + 0.000001) - (1 - y_true + 0.000001) * K.log(1 - y_pred), axis=1))
#
#
# # return loss
#
#
# m = model((5511, 101))
# m.summary()
# import keras.loss
# m.compile(optimizer='adam', loss=loss, metrics=['acc'])
#
# # m1 = load_model('../pretrain/tr_model.h5')
# # m1.summary()


m = model((5511, 101))
m.summary()