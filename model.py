from tensorflow import keras
from tensorflow.keras import layers, Model

import tensorflow as tf
from tensorflow.keras.models import Model

discriminator=keras.models.load_model('discriminator_model.h5')

def build_discriminator(input_shape):
    model = tf.keras.Sequential([
        layers.Conv2D(64, (4, 4), strides=(2, 2), padding='same', input_shape=input_shape),
        layers.LeakyReLU(alpha=0.2),
        layers.Dropout(0.3),

        layers.Conv2D(128, (4, 4), strides=(2, 2), padding='same'),
        layers.LeakyReLU(alpha=0.2),
        layers.Dropout(0.3),

        layers.Flatten(),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

def extract_facial_features(image_path):
    # Load and preprocess the image
    example_image = tf.io.read_file(image_path)
    example_image = tf.image.decode_jpeg(example_image, channels=1)  # Decode as grayscale
    example_image = tf.image.resize(example_image, (64, 64))
    example_image = tf.expand_dims(example_image, axis=0)  # Add batch dimension

    # Create an instance of the discriminator model for grayscale images
    input_shape = (64, 64, 1)  # Change according to your grayscale image shape
    discriminator = build_discriminator(input_shape)

    # Define a new model to extract features using intermediate layers
    intermediate_layer_model = Model(inputs=discriminator.input,
                                     outputs=discriminator.layers[-3].output)

    # Get intermediate layer activations for the example image
    extracted_features = intermediate_layer_model.predict(example_image)

    return extracted_features # Return extracted features and processed image



features =  extract_facial_features('./tanmay.jpeg')
print(features)
