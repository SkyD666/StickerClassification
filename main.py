import tensorflow as tf
from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

assert tf.__version__.startswith('2')


def train(model_name: str = "EfficientNet-Lite4"):
    data = DataLoader.from_folder("stickers")
    train_data, rest_data = data.split(0.8)
    validation_data, test_data = rest_data.split(0.5)

    if model_name == "EfficientNet-Lite4":
        model = image_classifier.create(
            train_data=train_data,
            validation_data=validation_data,
            model_spec=image_classifier.EfficientNetLite4Spec(
                uri='https://hub.tensorflow.google.cn/tensorflow/efficientnet/lite4/feature-vector/2',
            ),
            # batch_size=256,
            dropout_rate=0.37143,
            epochs=200,
            momentum=0.9,
            shuffle=True,
        )
    else:
        model = image_classifier.create(
            train_data=train_data,
            validation_data=validation_data,
            model_spec=image_classifier.EfficientNetLite2Spec(
                uri='https://hub.tensorflow.google.cn/tensorflow/efficientnet/lite2/feature-vector/2',
            ),
            # batch_size=256,
            dropout_rate=0.28571,
            epochs=150,
            momentum=0.9,
            shuffle=True,
        )

    model.summary()

    loss, accuracy = model.evaluate(test_data)

    print(f"loss: {loss}, accuracy: {accuracy}")

    model.export(export_dir='.', tflite_filename=f'sticker_classification_{model_name}.tflite')


if __name__ == '__main__':
    train(model_name="EfficientNet-Lite4")
