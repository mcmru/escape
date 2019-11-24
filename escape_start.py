import json
import commons
import requests

def start_esacape(teamnaam):
    params={"gebruikersnaam":"Team triple R"}
    response = commons.PostAPIresource(resource='start', body="", params=params)
    dict = json.loads(response.text)
    apikey = dict["apiKey"]
    commons.setapiKey(apikey)



