import json
import commons


# Specialisten telefoonnummers. Geen idee welke je moet hebben dus allemaal proberen.

specialisten = ("587426", "527786", "527786", "7346337","627836")

def bel_specialist(oplossingtorens):
    for telnr in specialisten:
        response = commons.getAPIresource(resource="toolondersteuning/belspecialist/" + telnr,
                                      secretcodename="Oplossing2",
                                      secretcodesolution=oplossingtorens
                                      )
        if response.status_code == 200:
            antwoord = json.loads(response.text)
            escapecode = antwoord["escapecode"]
            print("Bellen specialist gelukt")
            return escapecode


