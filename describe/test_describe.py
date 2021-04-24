import mlrun


def test_describe():
    from describe import summarize

    DATA_URL = "https://s3.wasabisys.com/iguazio/data/iris/iris_dataset.csv"

    task = mlrun.new_task(
        name="tasks-describe",
        handler=summarize,
        inputs={"table": DATA_URL},
        params={"update_dataset": True, "label_column": "label"},
    )
    run = mlrun.run_local(task)