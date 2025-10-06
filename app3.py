import os
from pymongo import MongoClient

uri=""
props = {"ENVIRONMENT": "azure", "TOKEN_RESOURCE":""}
c = MongoClient(
    uri,
    username="",
    authMechanism="MONGODB-OIDC",
    authMechanismProperties=props,
   # tlsAllowInvalidCertificates=True
)
c.test.test.insert_one({})
c.close()