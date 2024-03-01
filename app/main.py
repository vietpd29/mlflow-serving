from fastapi import FastAPI
import uvicorn
from fastapi import Depends
from api.serving import predict_route
# from app.core.config import settings
# from app.core.authentication import Oauth2ClientCredentials

# oauth2_scheme = Oauth2ClientCredentials(
#     tokenUrl=f"{settings.KEYCLOAK_BASE_URL}/realms/{settings.REALM_NAME}/protocol/openid-connect/token"
# )

app = FastAPI(
    docs_url="/", version="1.0.0", swagger_ui_parameters={"syntaxHighlight.theme":"obsidian"}, title="Mlflow Serving Model"
)

app.include_router(
    predict_route, 
    prefix="",
    # dependencies=[Depends(oauth2_scheme)]
) 

if __name__=='__main__':
    uvicorn.run(app, host='0.0.0.0', port=8829) 