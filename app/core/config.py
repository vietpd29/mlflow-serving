# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     KEYCLOAK_BASE_URL: str = "http://10.1.42.150:8000/auth"
#     REALM_NAME: str = "ms-core"
#     # nếu chỉ truyền stream thì không bắn kafka
#     LOG_TYPE: str = "stream_and_kafka"
#     LOG_LEVEL: str = "INFO"
#     LOG_DIR: str = "logs"
#     APP_LOG_NAME: str = "app_log_name"
#     WWW_LOG_NAME: str = "access_log"
#     KAFKA_BOOTSTRAP_SERVERS: list = [
#         "10.1.42.152:9092",
#         "10.1.42.156:9092",
#         "10.1.42.157:9092"
#     ]
#     KAFKA_TOPIC_LOG: str = "topic_name"
#     KAFKA_SECURITY_PROTOCOL: str = "PLAINTEXT"
#     KAFKA_SSL_CAFILE: str = ""
#     KAFKA_ARGS_API_VERSION_AUTO_TIMEOUT_MS: int = 1000000
#     KAFKA_ARGS_REQUEST_TIMEOUT_MS: int = 1000000
#     LOG_HOST_NAME: str = "log_host_name"
#
# settings = Settings()