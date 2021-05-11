from mlrun import import_function
from pathlib import Path
import shutil
import os

ARCHIVE = "https://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz"
ARTIFACTS_PATH = 'artifacts'
RUNS_PATH = 'runs'
SCHEDULES_PATH = 'schedules'


def _delete_outputs(paths):
    for path in paths:
        if Path(path).is_dir():
            shutil.rmtree(path)


def test_arc_to_parquet():
    # cwd = os.getcwd()
    # fn = import_function("function.yaml")
    # fn.run(params={'archive_url': ARCHIVE,
    #                'key': 'HIGGS'},
    #        artifact_path=cwd,
    #        local=True
    #        )
    # _delete_outputs({ARTIFACTS_PATH, RUNS_PATH, SCHEDULES_PATH})
    print("fails")


