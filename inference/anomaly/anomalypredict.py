import os
import pickle
import flask
import json
import numpy as np
from six import BytesIO
from tensorflow import keras

prefix = '/opt/ml/'
model_path = os.path.join(prefix, 'model')

def numpy_loads(data):
    """
    Deserializes npy-formatted bytes into a numpy array
    """
    stream = BytesIO(data)
    return np.load(stream)


def numpy_dumps(data):
    """
    Serialized a numpy array into a stream of npy-formatted bytes.
    """
    buffer = BytesIO()
    np.save(buffer, data)
    return buffer.getvalue()

class AnomalyPredictionService(object):
    model = None        

    @classmethod
    def get_model(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model == None:
            cls.model = keras.models.load_model(os.path.join(model_path,"anomalydetection_model"))

        return cls.model

    @classmethod
    def predict(cls, input):
        """For the input, do the predictions and return them.
        Args:
            input (a pandas dataframe): The data on which to do the predictions. There will be
                one prediction per row in the dataframe"""
        clf = cls.get_model()
        return clf(input)

# The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """Determine if the container is working and healthy. In this sample container, we declare
    it healthy if we can load the model successfully."""
    health = AnomalyPredictionService.get_model() is not None  # You can insert a health check here

    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    data = None

    if flask.request.content_type == 'application/json':
        print("Predict request received of json type")
        # Decode data from request here
        data = json.loads(flask.request.data)
        inp = np.asarray(data)
        output =AnomalyPredictionService.predict(inp).numpy().tolist()  
        result = json.dumps(output)
        return flask.Response(response=result, status=200, mimetype='application/json')
    elif flask.request.content_type == 'application/x-npy':
        print("Predict request received of numpy array")
        data = numpy_loads(flask.request.data)
        result =AnomalyPredictionService.predict(data)
        return flask.Response(response=numpy_dumps(result), status=200, mimetype='application/x-npy')
    else:
        return flask.Response(response='This predictor only supports jsnified numpy data', status=415, mimetype='text/plain')

