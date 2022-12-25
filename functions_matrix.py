# import required module
import os

import pandas
import yaml
from yaml.loader import SafeLoader

# assign directory
directory = '.'

function_matrix = {"function_name": [], "test_file": [], "example": [], "hidden": []}


# Open the file and load the file
def is_hidden(yaml_path):
    with open(yaml_path) as f:
        data = yaml.load(f, Loader=SafeLoader)
        print(data['hidden'])
        function_matrix['hidden'].append(data['hidden'])
        return
    function_matrix['hidden'].append(None)


def is_function_dir(sub_root_dir):
    for file_name in os.listdir(sub_root_dir):
        f = os.path.join(sub_root_dir, file_name)
        if f.endswith("item.yaml"):
            function_matrix['function_name'].append(sub_root_dir)
            print("{} is function".format(sub_root_dir))
            is_hidden(f)
            return True


def contains_test_file(sub_root_dir):
    for file_name in os.listdir(sub_root_dir):
        if file_name.startswith("test_"):
            print("{} test file".format(file_name))
            function_matrix['test_file'].append(file_name)
            return
    function_matrix['test_file'].append(None)


def contains_notebook(sub_root_dir):
    for file_name in os.listdir(sub_root_dir):
        if file_name.endswith(".ipynb"):
            print("{} notebook ".format(file_name))
            function_matrix['example'].append(file_name)
            return
    function_matrix['example'].append(None)


# iterate over files in
# that directory
def main():
    for dir in sorted(os.listdir(directory)):
        # f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isdir(dir):
            if is_function_dir(dir):
                contains_test_file(dir)
                contains_notebook(dir)
    print(function_matrix)
    print(len(function_matrix["function_name"]),
          len(function_matrix["test_file"]),
          len(function_matrix["example"]),
          len(function_matrix["hidden"]),
          )
    df_function_matrix = pandas.DataFrame(function_matrix)
    df_function_matrix.to_csv("function_matrix.csv")


if __name__ == "__main__":
    main()
