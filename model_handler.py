"""Handle model operations including loading and predictions"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import requests
from config import MODEL_URL, MODEL_PATH, PRODUCT_NAMES

class ModelHandler:
    def __init__(self):
        self.model = None
        self._ensure_model_exists()
        self._load_model()

    def _ensure_model_exists(self):
        """Download model if it doesn't exist"""
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        if not os.path.exists(MODEL_PATH):
            try:
                response = requests.get(MODEL_URL, stream=True)
                response.raise_for_status()
                with open(MODEL_PATH, 'wb') as f:
                    for chunk in response.iter_content(8192):
                        f.write(chunk)
            except Exception as e:
                raise Exception(f"Model download failed: {e}")

    def _load_model(self):
        """Load the model into memory"""
        try:
            self.model = load_model(MODEL_PATH)
        except Exception as e:
            raise Exception(f"Model loading failed: {e}")

    def predict(self, image_path, confidence_threshold=0.5):
        """Make predictions on the image"""
        try:
            image = tf.keras.utils.load_img(image_path, target_size=(224, 224))
        except Exception:
            raise Exception("Failed to load image. Please ensure it's a valid image file.")

        image_array = tf.keras.utils.img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)

        predictions = self.model.predict(image_array)
        confidence_scores = tf.nn.softmax(predictions[0])
        class_index = np.argmax(confidence_scores)
        confidence = confidence_scores[class_index]

        if confidence < confidence_threshold:
            return None, confidence

        if class_index >= len(PRODUCT_NAMES):
            return None, confidence

        return PRODUCT_NAMES[class_index], confidence