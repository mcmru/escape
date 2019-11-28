import json
import commons
import escape_som_op_tablet as tablet
import escape_open_boekenkast as bk
import escape_vullen_torens as torens
import escape_bellen_specialist as bellen
import escape_start as start

def escape_totaal ():
    # Init het spel
    start.start_escape()

    # Bereken de code die op de tablet getoond wordt
    tabletcode = tablet.BerekenCodeopTablet()

    # Open met deze code de boekenkast
    bkcode = bk.openboekenkast(tabletcode)

    # Vul nu de torens op de juiste volgorde in
    torencode, toollijstTorens = torens.vul_torens(bkcode)

    # Bel nu de juiste specialist
    escapecode = bellen.bel_specialist(torencode, toollijstTorens)

    # En nu escapen door een delete aan te roepen
    response = commons.deleteAPIresource("verwijderslot", escapecode)
    print(response.text)

if __name__ == '__main__':
    # 10 keer achter alkaar proberen te escapen
    for x in range(10):
        escaped = escape_totaal()




