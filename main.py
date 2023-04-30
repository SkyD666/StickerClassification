import tensorflow as tf
from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

assert tf.__version__.startswith('2')


def train():
    data = DataLoader.from_folder("stickers")
    train_data, rest_data = data.split(0.8)
    validation_data, test_data = rest_data.split(0.5)

    model = image_classifier.create(
        train_data=train_data,
        validation_data=validation_data,
        model_spec=image_classifier.EfficientNetLite4Spec(
            uri='https://hub.tensorflow.google.cn/tensorflow/efficientnet/lite4/feature-vector/2',
        ),
        shuffle=True,
        epochs=60
    )

    model.summary()

    loss, accuracy = model.evaluate(test_data)

    print(f"loss: {loss}, accuracy: {accuracy}")

    model.export(export_dir='.', tflite_filename='sticker_classification.tflite')


if __name__ == '__main__':
    train()
