import os

from flask_restx import Api,Resource, fields
from marshmallow import ValidationError


########################################################################################################################
# Config
########################################################################################################################

VERSION = os.getenv("VER")
api = Api(
    title="flask-api-microservice-example",
    version=VERSION,
    prefix=f"/api/{VERSION}",
    doc="/" if os.getenv("FLASK_ENV") == "development" else False,
)


@api.errorhandler(ValidationError)
def handle_validation_error(error: ValidationError):
    del error.data
    return {"message": error.messages}, 400


########################################################################################################################
# Namespaces
########################################################################################################################
