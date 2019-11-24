import uuid
import commons
import requests

def start_escape(teamnaam):
    params = {"gebruikersnaam" : teamnaam,
              "api-key": commons.getapiKey()
              }
    response = commons.PostAPIresource(resource='hervat', body="", params=params)
    if (response.status_code):
        print("The game has begun")
    else:
        print (f"Sorry, the game cannot start. Statuscode: ", response.status_code)





