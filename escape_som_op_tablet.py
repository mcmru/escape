import json
import commons

# Bereken de som die de tablet getoond wordt

def BerekenCodeopTablet():
    return oplossing1ComputeEntryCode(oplossing1getassignment())

def oplossing1getassignment():
    solution = commons.getAPIresource(resource='rekensom')
    if solution.status_code:
        return json.loads(solution.text)
    else:
        raise Exception("API not accessible")


def oplossing1ComputeEntryCode(opdracht):
    # Welke getallen
    getal1 = opdracht.get("som").get("getal1")
    getal2 = opdracht.get("som").get("getal2")

    def optellen():
        return getal1 + getal2

    def delen():
        return getal1 / getal2

    def vermenigvuldigen():
        return getal1 * getal2

    def aftrekken():
        return getal1 - getal2

    operate = {"optellen": optellen, "delen": delen, "vermenigvuldigen": vermenigvuldigen, "aftrekken": aftrekken}

    # Welke functie moeten we uitvoeren
    for operator, active in opdracht.items():
        if active:
            return (operate.get(operator)())

    return -1  # Geen opdracht gevonden


