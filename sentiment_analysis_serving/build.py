from mlrun import code_to_function
import yaml


def upload_items():
    with open("item.yaml") as item_file:
        item_attributes = yaml.load(item_file, Loader=yaml.FullLoader)
    return item_attributes


def build(item_attributes):
    # create job function object from notebook code
    fn = code_to_function(
        name=item_attributes["name"],
        filename=item_attributes["spec"]["filename"],
        handler=item_attributes["spec"]["handler"],
        kind=item_attributes["spec"]["kind"],
        image=item_attributes["spec"]["image"],
        description=item_attributes["description"],
        requirements=item_attributes["spec"]["requirements"],
        categories=item_attributes["categories"],
        labels=item_attributes["labels"],
        with_doc=False
    )

    fn.export("sentiment_analysis_serving.yaml")


def handler():
    items = upload_items()
    build(items)

