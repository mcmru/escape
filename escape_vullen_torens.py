import json
import commons

# Kijken door de verrekijker levert de opdracht op. De torens moeten in de juiste volgorde gevuld worden

# Inhoud van het boek:
torens = [ {"name": "aKerk", "height": 76, "built": 1492 },
            {"name": "martini", "height": 97, "built": 1469 },
            {"name": "nieuweKerk", "height": 47, "built": 1660 },
            {"name": "stJozefKerk", "height": 75, "built": 1887 },
            {"name": "academieGebouw", "height": 66, "built": 1909 },
         ]

def sortlist(opdracht):
    sortedList = []
    opdracht = opdracht.get("torens")
    is_ascending = opdracht.get("typeSortering") == "Oplopend"
    if opdracht.get("alfabetisch"):
        sortedList = sorted(torens, key=lambda i: i['name'].lower(),reverse = not is_ascending)
    if opdracht.get("hoogte"):
        sortedList = sorted(torens, key=lambda i: i['height'],reverse = not is_ascending)
    if opdracht.get("bouwjaar"):
        sortedList = sorted(torens, key=lambda i: i['built'],reverse = not is_ascending)
    return sortedList

def convert2antwoordstring(sortedList):
    # Maak een dictionary met namen als keys en index als value
    return (
        {
            sortedList[i].get("name"): i for i in range(0,len(sortedList))
        }
    )


def vul_torens(oplossingboekenkast):
    response = commons.getAPIresource(resource='torens')
    opdracht = json.loads(response.text)

    # Antwoord is nu zoiets als: {"torens": {"typeSortering": "Oplopend", "alfabetisch": false, "hoogte": false, "bouwjaar": true}}

    antwoord = convert2antwoordstring(sortlist(opdracht))

    response = commons.PostAPIresource(resource='torens',
                                       secretcodename='Oplossing1',
                                       secretcodesolution=oplossingboekenkast,
                                       body=json.dumps(antwoord))
    return response.headers['Oplossing2'], json.loads(response.text)


