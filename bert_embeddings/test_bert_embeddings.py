import nuclio
from bert_embeddings import handler, init_context
import json
import pickle


def test_bert_embeddings():
    # Mocked Nuclio context
    context = nuclio.Context()
    event = nuclio.Event(body=json.dumps(["John loves Mary"]))

    # Mocked context initialization
    init_context(context)
    outputs = pickle.loads(handler(context, event))
    assert (1, 768) == outputs[1].shape  # check they have the same string
