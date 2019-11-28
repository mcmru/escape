import json
import commons

# Bereken de som die de tablet getoond wordt

def BerekenCodeopTablet():
    return oplossing1ComputeEntryCode(oplossing1getassignment())

def oplossing1getassignment():

    solution = commons.getAPIresource(resource='rekensom')
    return json.loads(solution.text)


def oplossing1ComputeEntryCode(opdracht):
    # Welke getallen
    getal1 = opdracht.get("som").get("getal1")
    getal2 = opdracht.get("som").get("getal2")

    def optellen():
        return str(getal1 + getal2)

    def delen():
        return str(round(getal1 / getal2))

    def vermenigvuldigen():
        return str(getal1 * getal2)

    def aftrekken():
        return str(getal1 - getal2)

    operate = {"optellen": optellen, "delen": delen, "vermenigvuldigen": vermenigvuldigen, "aftrekken": aftrekken}

    # Welke functie moeten we uitvoeren
    for operator, active in opdracht.items():
        if active:
            return (operate.get(operator)())

    raise ("Geen rekenopdracht gevonden")


