import numpy as np
import tensorflow as tf
from keras.utils import img_to_array, load_img

class DiseaseModelFactory:
    def __init__(self):
        self.models = {
            "Brain Tumor": DiseaseModel("./Brain-Tumor.tflite", ['Glioma', 'Meningioma', 'Notumor', 'Pituitary']),
            "Tuberculosis": DiseaseModel("./Kidney.tflite", ['Infected', 'Normal'], target_size=(224, 224), color_mode="rgb"),
            "Kidney Disease": DiseaseModel("./Kidney.tflite", ['Cyst', 'Normal', 'Stone', 'Tumor']),
            "Lungs Disease": DiseaseModel("./Lung.tflite", ['Covid', 'Lung_Opacity', 'Normal', 'Viral_Pneumonia'])
        }

    def get_model(self, disease_name):
        return self.models.get(disease_name)

class DiseaseModel:
    def __init__(self, model_path, diseases_labels, target_size=(512, 512), color_mode="grayscale"):
        self.model_path = model_path
        self.diseases_labels = diseases_labels
        self.target_size = target_size
        self.color_mode = color_mode
        self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
        self.interpreter.allocate_tensors()
        self.input_index = self.interpreter.get_input_details()[0]["index"]
        self.output_index = self.interpreter.get_output_details()[0]["index"]

    def load_and_prepare_image(self, img_path):
        image = load_img(img_path, color_mode=self.color_mode, target_size=self.target_size, interpolation="nearest")
        return np.expand_dims(img_to_array(image), axis=0)

    def predict(self, img_path):
        test_image = self.load_and_prepare_image(img_path)
        self.interpreter.set_tensor(self.input_index, test_image)
        self.interpreter.invoke()
        
        output_data = self.interpreter.get_tensor(self.output_index)
        pred = output_data[0]
        
        dis_name = self.diseases_labels[np.argmax(pred)] if np.max(pred) == 1 else "None"
        
        return dis_name, dis_name