from urllib import response

import commons

# Met de eerder verkregen code wordt de boekenkast geopend
# De response header bevat een nieuwe code ' Oplossing1'  voor de volgende puzzel

def openboekenkast(cijfercode):
    response = commons.getAPIresource(resource='cijferslot',params="oplossing=" + cijfercode)
    if response.status_code:
        code = response.headers["Oplossing1"]
        if code:
            print("De boekenkast is geopend!")
            return code

    raise Exception("API not accessible")