FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3-pip

ENV AWS_ACCESS_KEY_ID AKIAQY7WH4KII4JFJIO5

ENV AWS_SECRET_ACCESS_KEY 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

WORKDIR /mlflow

COPY basic_auth.ini /mlflow/basic_auth.ini

COPY requirements.txt /mlflow/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /mlflow/requirements.txt

RUN cp /mlflow/basic_auth.ini /usr/local/lib/python3.10/dist-packages/mlflow/server/auth/basic_auth.ini

CMD mlflow server \
  --backend-store-uri postgresql://mlflow:mlflow@postgres1:5432/mlflowdb \
  --artifacts-destination s3://v-mlflow-store-artifact \
  --host 0.0.0.0 \
  --port 8668 \
  --app-name basic-auth

