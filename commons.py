import requests
import logging
import http.client as http_client
import os

baseURL = "http://otagrnap357.duo.ota/"
apiKey = "ddc3f655-79a4-4f7e-b5cf-031914db0eea"

http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Geen proxy !
os.environ['NO_PROXY']= baseURL

def getapiKey ():
    return apiKey

def initSession():
    session = requests.session()

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
    #print("Get API op: ", resource, "met status: ", response.status_code, "en response body: ", response.text)
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
    #print("Post API op: ", resource, "met status: ", response.status_code, "en response body: ", response.text)
    return response

def deleteAPIresource(resource, escapecode):
    # URL
    url = baseURL + resource + "/" + str(escapecode)
    print("Delete op URL:", url)

    # Headers
    headers = {"api-key": apiKey}
    print("delete me headers:", headers)
    # Send request
    response = requests.delete(url, headers=headers)
    print("Delete API op: ", resource, "met status: ", response.status_code, "En headers: ", response.headers, "met inhoud: ", response.text)
    return response
