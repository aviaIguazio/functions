import os
import wget
from build import handler
from mlrun import import_function, code_to_function
import os.path
from os import path
import mlrun


MODEL_PATH = os.path.join(os.path.abspath('./'), 'models')
MODEL = MODEL_PATH + "model.pt"


def download_pretrained_model(path):
    # Run this to download the pre-trained model to your `models` directory
    import os
    model_location = 'https://iguazio-sample-data.s3.amazonaws.com/models/model.pt'
    saved_models_directory = path
    # Create paths
    os.makedirs(saved_models_directory, exist_ok=1)
    model_filepath = os.path.join(saved_models_directory, os.path.basename(model_location))
    wget.download(model_location, model_filepath)


def test_build():
    handler()


def test_local_sentiment_analysis_serving():
    model_path = os.path.join(os.path.abspath('./'), 'models')
    model = model_path+'/model.pt'
    if not path.exists(model):
        download_pretrained_model(model_path)
    #fn = import_function('hub://sentiment_analysis_serving')
    fn = code_to_function(name='test_sentiment',
                          filename="sentiment_analysis_serving.py",
                          handler="handler",
                          kind="serving",
                          image="mlrun/ml-models-gpu")
    fn.add_model('mymodel', model_path=model)
    # create an emulator (mock server) from the function configuration)
    server = fn.to_mock_server()

    instances = ['I had a pleasure to work with such dedicated team. Looking forward to \
                 cooperate with each and every one of them again.']
    result = server.test("/v2/models/mymodel/infer", {"instances": instances})
    assert result[0] == 2

    #result.keys()