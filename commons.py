import requests

baseURL = "http://otagrnap357.duo.ota/"
apikey = "4080cdbd-3888-41bc-8dc8-d450153d10f3"

def getAPIresource(resource, params = None, secretcodename = None, secretcodesolution = None):
    # URL
    url = baseURL + resource

    # Headers
    headers = {"api-key": apikey}
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
    headers = {"api-key": apikey}
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
    url = baseURL + resource + "/" + escapecode

    # Headers
    headers = {"api-key": apikey}

    # Send request
    response = requests.delete(url, headers=headers)
    return response

