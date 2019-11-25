import json
import commons


# Specialisten telefoonnummers. Geen idee welke je moet hebben dus allemaal proberen.

specialisten = ("587426", "527786", "527786", "7346337","627836")

def bel_specialist(oplossingtorensCode):
    for telnr in specialisten:
        response = commons.getAPIresource(resource="toolondersteuning/belspecialist/" + telnr,
                                      secretcodename="Oplossing2",
                                      secretcodesolution=oplossingtorensCode
                                      )
        if response.status_code == 200:
            antwoord = json.loads(response.text)
            escapecode = antwoord["escapecode"]
            print(f"Bellen specialist gelukt op telnr: ", telnr, ". Escapecode = ", escapecode)
            return escapecode

# Nieuwe poging: bel de specialist die NIET voorkomt op het antwoord bij de torens

taSpecialist = {"Protractor":"527786",
                "SoapUI": "32843",
                "Selenium": "587426",
                "Postman": "627836",
                "Cucumber":"7346337"
                }

def bel_specialistV2(oplossingtorensCode, toollijstTorens):
    # Bepaal welke tool niet voorkomt in de lijst
    specialistSet = set(taSpecialist.keys())
    toollijstSet = set(toollijstTorens.get("tools"))
    specialistToCall = specialistSet - toollijstSet
    telnr = taSpecialist.get(specialistToCall.pop())

    response = commons.getAPIresource(resource="toolondersteuning/belspecialist/" + telnr,
                                      secretcodename="Oplossing2",
                                      secretcodesolution=oplossingtorensCode
                                      )
    if response.status_code == 200:
        antwoord = json.loads(response.text)
        escapecode = antwoord["escapecode"]
        print("Bellen specialist gelukt")
        return escapecode
    else:
        print("Er is iets mis gegaan met het bellen: ", response.status_code)