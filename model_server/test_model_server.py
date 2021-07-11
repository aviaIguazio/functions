from mlrun import code_to_function, import_function
from sklearn.datasets import load_iris
from model_server import *


def test_local_model_server():
    model = 'https://s3.wasabisys.com/iguazio/models/iris/model.pkl'

    iris = load_iris()

    x = iris['data'].tolist()
    y = iris['target']

    my_server = ClassifierModel('classifier', model_dir=model)
    my_server.load()

    a = my_server.predict({"instances": x})
    assert len(a) == 150


