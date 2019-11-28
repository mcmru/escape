import uuid
import commons
import requests

def start_escape():

    params = {"gebruikersnaam" : "Triple R",
              "api-key": commons.getapiKey()
              }

    response = commons.PostAPIresource(resource='hervat', body="", params=params)






