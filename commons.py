import requests

baseURL = "http://otagrnap357.duo.ota/"
apiKey = "ddc3f655-79a4-4f7e-b5cf-031914db0eea"

def getapiKey ():
    return apiKey

def getAPIresource(resource, params = None, secretcodename = None, secretcodesolution = None):
    # URL
    url = baseURL + resource

    # Headers
    headers = {"api-key": apiKey}
    # no-caching voorkomt een 406 bij de escape
    headers["Cache-Control"] = "no-cache"
    headers["Pragma"] = "no-cache"

    if secretcodename:
        headers[secretcodename] = secretcodesolution

    # Send request
    response = requests.get(url,
                            params=params,
                            headers=headers)
    if response.status_code != 200:
        raise ("getAPI resource ging fout:", url, response.status_code)

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

    if response.status_code != 200:
        raise ("postAPI resource ging fout:", url, response.status_code)

    return response

def deleteAPIresource(resource, escapecode):
    # URL
    url = baseURL + resource + "/" + str(escapecode)

    # Headers
    headers = {"api-key": apiKey}

    # Send request
    response = requests.delete(url, headers=headers)
    if response.status_code != 200:
        raise ("deleteAPI resource ging fout:", url, response.status_code)

    return response
