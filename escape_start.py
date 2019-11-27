import uuid
import commons
import requests

def start_escape():
    commons.initSession()

    params = {"gebruikersnaam" : "Triple R",
              "api-key": commons.getapiKey()
              }
    response = commons.PostAPIresource(resource='hervat', body="", params=params)
    if (response.status_code == 200):
        print("The game has begun")
    else:
        raise (f"Sorry, the game cannot start. Statuscode: ", response.status_code)





