import json
import commons
import escape_som_op_tablet as tablet
import escape_open_boekenkast as bk
import escape_vullen_torens as torens
import escape_bellen_specialist as bellen
import escape_start as start

teamnaam = "Team Triple R"

def escape_totaal ():
    # Init het spel
    start.start_escape(teamnaam)
    # Bereken de code die op de tablet getoond wordt
    tabletcode = tablet.BerekenCodeopTablet()
    # Open met deze code de boekenkast
    bkcode = bk.openboekenkast(tabletcode)
    # Vul nu de torens op de juiste volgorde in
    torencode, toollijstTorens = torens.vul_torens(bkcode)
    # Bel nu de juiste specialist
    # Oude versie:
    # escapecode = bellen.bel_specialist(torencode)
    #Nieuwe versie heeft ook de response van de torens nodig
    bellen.bel_specialistV2(bkcode, toollijstTorens)
    # En nu escapen door een delete aan te roepen
    resp = commons.deleteAPIresource("verwijderslot", escapecode)
    print(f'Delete heeft geleid tot: ', resp.status_code, resp.text)



if __name__ == '__main__':
    escape_totaal()



