import requests

baseURL = "http://otagrnap357.duo.ota/"
apiKey = ""

def setapiKey (key):
    apiKey = key

def getAPIresource(resource, params = None, secretcodename = None, secretcodesolution = None):
    # URL
    url = baseURL + resource

    # Headers
    headers = {"api-key": apiKey}
    if secretcodename:
        headers[secretcodename] = secretcodesolution

    # Send request
    response = requests.get(url,
                            params=params,
                            headers=headers)
    return response

def PostAPIresource(resource, body, params = None, secretcodename = None, secretcodesolution = None):
    # URL
    url = baseURL + resource

    # Headers
    headers = {"api-key": apiKey}
    if secretcodename:
        headers[secretcodename] = secretcodesolution

    headers['content-type'] = 'application/json'

    # Send request

    response = requests.post(url,
                             data=body,
                             params=params,
                             headers=headers)
    return response

def deleteAPIresource(resource, escapecode):
    # URL
    url = baseURL + resource + "/" + str(escapecode)

    # Headers
    headers = {"api-key": apiKey}

    # Send request
    response = requests.delete(url, headers=headers)
    return response

