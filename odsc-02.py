import mlrun
from os import path

project_name_base = 'odsc-2022-east'
project_name, artifact_path = mlrun.set_environment(project=project_name_base, artifact_path='./', user_project=True)

fn = mlrun.code_to_function(kind='job',
                      filename='data_iris.py',
                      handler='iris_generator',
                      image='mlrun/mlrun')

params={"format":"parquet"}
fn.run(params=params,
       artifact_path=path.join(artifact_path, 'data'))