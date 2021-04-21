from mlrun import code_to_function
import yaml


def upload_items():
    with open("item.yaml") as item_file:
        item_attributes = yaml.load(item_file, Loader=yaml.FullLoader)
    return item_attributes


def build(item_attributes):
    # create job function object from notebook code
    fn = mlrun.code_to_function(
        item_attributes["name"],
        kind=item_attributes["spec"]["kind"],
        handler=item_attributes["spec"]["handler"],
        filename=item_attributes["spec"]["filename"],
        image=item_attributes["spec"]["image"],
        description=item_attributes["description"],
        categories=item_attributes["categories"],
        labels=item_attributes["labels"],
        requirements=item_attributes["spec"]["requirements"],
    )

    fn.export("sentiment_analysis_serving.yaml")


if __name__ == "__main__":
    items = upload_items()
    build(items)
