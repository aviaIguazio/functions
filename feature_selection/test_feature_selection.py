from pathlib import Path
import os
from mlrun import code_to_function
from feature_selection import feature_selection

ARTIFACTS_PATH ='artifacts'


def _validate_paths(paths: {}):
    base_folder = ARTIFACTS_PATH
    for path in paths:
        full_path = os.path.join(base_folder, path)
        if Path(full_path).is_file():
            print("File exist")
        else:
            raise FileNotFoundError


def test_run_local():
    cwd = os.getcwd()
    fn = code_to_function(name='test_feature_selection',
                          filename="feature_selection.py",
                          handler="feature_selection",
                          kind="job",
                          )
    fn.run(name="task-feature-selection",

                    params={'k': 2,
                           'min_votes': 0.3,
                           'label_column': 'is_error',
                            },
                   inputs={'df_artifact': 'data/metrics.pq'},
            local=True
           )
    _validate_paths({'feature_scores.parquet',
                     'selected_features.parquet'})
    print("fails on '<Buffer>': Invalid: Parquet file size is 0 bytes")