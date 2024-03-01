import os
import mlflow.pyfunc
import pandas as pd
from pydantic import SecretStr
import mlflow
from pyspark.sql import SparkSession
from fastapi import APIRouter
# from app.utils.logs import logger
predict_route = APIRouter()

@predict_route.post('/predict')
def predict(data: dict, tracking_uri: str, model_uri: str, mlflow_tracking_username: str, mlflow_tracking_password: SecretStr):
    try:
        spark = SparkSession.builder.getOrCreate() 
        str_pass = mlflow_tracking_password.get_secret_value()

        # uname and pass to log in mlflow server
        os.environ["MLFLOW_TRACKING_USERNAME"]=mlflow_tracking_username
        os.environ["MLFLOW_TRACKING_PASSWORD"]=str_pass

        tracking_uri_last = "http://" + tracking_uri

        # set uri for taking model
        mlflow.set_tracking_uri(tracking_uri_last)

        #get the info of model in json
        model_info = mlflow.models.get_model_info(model_uri)

        model_module = model_info.flavors['python_function']['loader_module']

        input_df = pd.DataFrame(data)

        if model_module == 'mlflow.spark':

            # load model from mlflow
            spark_model = mlflow.spark.load_model(model_uri)
            
            # create spark df from input
            spark_df = spark.createDataFrame(input_df)

            # get predictions from model and data
            predictions = spark_model.transform(spark_df)
            
            # select 2 column features and predictions
            features_prediction = predictions.select('features', 'prediction')
            
            # turn spark df to pandas df
            predictions_pandas = features_prediction.toPandas()

            # pandas df to dict
            dict_predict = predictions_pandas.to_dict('list')
            
            # turn value features to array list
            dict_predict['features'] = [e.toArray().tolist() for e in dict_predict['features']]

            response = dict_predict
            # logger.info(f"this is spark model prediction!")

        elif model_module == 'mlflow.sklearn':

            # load model from mlflow    
            sklearn_model = mlflow.sklearn.load_model(model_uri)

            # get prediction from model and input
            predictions = sklearn_model.predict(input_df)

            response = {
                "predictions": predictions.tolist()
            }
            # logger.info(f"this is sklearn model prediction!")

        return response
    except Exception as e:
        # logger.info(f"Thông tin lỗi")
        return {
            "error": e
        }

    