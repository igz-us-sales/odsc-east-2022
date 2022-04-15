from mlrun import code_to_function

fn = code_to_function(kind='job',
                      filename='data_iris.py',
                      handler='iris_generator',
                      image='mlrun/mlrun')

params={"format":"parquet"}
fn.run(params=params)