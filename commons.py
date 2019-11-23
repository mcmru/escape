import requests

baseURL = "http://otagrnap357.duo.ota/"
apikey = "4080cdbd-3888-41bc-8dc8-d450153d10f3"

def getAPIresource(resource, params, secretcodename, secretcodesolution):
    # URL
    url = baseURL + resource

    # Headers
    headers = {"apikey": apikey}
    headers[secretcodename] = secretcodesolution

    # Send request
    response = requests.get(url,
                            params=params,
                            headers=headers)
    return response

def PostAPIresource(resource, params, secretcodename, secretcodesolution, body):
    # URL
    url = baseURL + resource

    # Headers
    headers = {"apikey": apikey}
    headers[secretcodename] = secretcodesolution

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
    headers = {"apikey": apikey}

    # Send request
    response = requests.delete(url, headers=headers)
    return response

