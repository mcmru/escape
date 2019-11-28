import commons

# Met de eerder verkregen code wordt de boekenkast geopend
# De response header bevat een nieuwe code ' Oplossing1'  voor de volgende puzzel

def openboekenkast(cijfercode):

    response = commons.getAPIresource(resource='cijferslot',params="oplossing=" + cijfercode)

    code = response.headers["Oplossing1"]
    if code:
        return code

    raise Exception("boekenkast code niet gevonden")