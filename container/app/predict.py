import os
import numpy as np
import time
import json

from keras.models import model_from_json
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array


class InferenceService(object):
  """
  Loads the model makes an AI inference
  """
  
  model = None  # model kept here (when loaded)
  model_path = '/opt/ml/model'

  @classmethod
  def get_model(cls):
    """Load model object, if not loaded already."""
    if cls.model == None:

      with open(os.path.join(cls.model_path, 'model.json'), 'r') as file:
        cls.model = model_from_json(file.read())
        cls.model.load_weights(os.path.join(cls.model_path, 'weights.hdf5'))

    return cls.model

  @classmethod
  def prepare_image(cls, image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
      image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image
  
  @classmethod
  def predict(cls, image):
    
    try:

      # initialize response
      response = {"success": False}

      # load model
      model = cls.get_model()

      # preprocess the image and prepare it for classification
      image = cls.prepare_image(image, target=(224, 224))

      # classify the input image and then initialize the list
      # of predictions to return to the client
      preds = model.predict(image)
      results = imagenet_utils.decode_predictions(preds)
      response["predictions"] = []

      # loop over the results and add them to the list of
      # returned predictions
      for (imagenetID, label, prob) in results[0]:
        r = {"label": label, "probability": float(prob)}
        response["predictions"].append(r)

      # indicate that the request was a success
      response["success"] = True

      # return the response dictionary as a JSON response
      return (json.dumps(response), 200)

    except Exception as e:
      return (json.dumps(e), 500)
