import json
import commons

# Kijken door de verrekijker levert de opdracht op. De torens moeten in de juiste volgorde gevuld worden

# Inhoud van het boek:
torens = [ {"name": "akerk", "height": 76, "built": 1492 },
            {"name": "martini", "height": 97, "built": 1469 },
            {"name": "nieuwekerk", "height": 47, "built": 1660 },
            {"name": "stJozefkerk", "height": 75, "built": 1887 },
            {"name": "academiegebouw", "height": 66, "built": 1909 },
         ]

def sortlist(opdracht):
    sortedList = []
    opdracht = opdracht.get("torens")
    is_ascending = opdracht.get("typeSortering") == "Oplopend"
    if opdracht.get("alfabetisch"):
        sortedList = sorted(torens, key=lambda i: i['name'],reverse = not is_ascending)
    if opdracht.get("hoogte"):
        sortedList = sorted(torens, key=lambda i: i['height'],reverse = not is_ascending)
    if opdracht.get("bouwjaar"):
        sortedList = sorted(torens, key=lambda i: i['built'],reverse = not is_ascending)
    print (sortedList)
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
    if not response.status_code:
        raise Exception("Torens get error")
    else:
        opdracht = json.loads(response.text)

    # Antwoord is nu zoiets als: {"torens": {"typeSortering": "Oplopend", "alfabetisch": false, "hoogte": false, "bouwjaar": true}}

    antwoord = convert2antwoordstring(sortlist(opdracht))
    response = commons.PostAPIresource(resource='torens',
                                       secretcodename='Oplossing1',
                                       secretcodesolution=oplossingboekenkast,
                                       body=antwoord)
    if not response.status_code:
        raise Exception("torens post error")
    else:
        # De response header bevat de code van Oplossing2
        return response.headers['Oplossing2']

