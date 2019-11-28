import json
import commons

taSpecialist = {"Protractor":"527786",
                "SoapUI": "32843",
                "Selenium": "587426",
                "Postman": "627836",
                "Cucumber":"7346337"
                }

def bel_specialist(oplossingtorensCode, toollijstTorens):

    # Bepaal welke tool niet voorkomt in de lijst
    specialistSet = set(taSpecialist.keys())
    toollijstSet = set(toollijstTorens.get("tools"))
    specialistToCall = specialistSet - toollijstSet

    telnr = taSpecialist.get(specialistToCall.pop())

    response = commons.getAPIresource(resource="toolondersteuning/belspecialist/" + telnr,
                                      secretcodename="Oplossing2",
                                      secretcodesolution=oplossingtorensCode
                                      )
    antwoord = json.loads(response.text)
    escapecode = antwoord["escapecode"]

    return escapecode
