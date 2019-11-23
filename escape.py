import json
import commons
import escape_som_op_tablet as tablet
import escape_open_boekenkast as bk
import escape_vullen_torens as torens
import escape_bellen_specialist as bellen

def escape_totaal ():
    # Bereken de code die op de tablet getoond wordt
    tabletcode = tablet.BerekenCodeopTablet()
    # Open met deze code de boekenkast
    bkcode = bk.openboekenkast(tabletcode)
    # Vul nu de torens op de juiste volgorde in
    torencode = torens.vul_torens(bkcode)
    # Bel nu de juiste specialist
    escapecode = bellen.bel_specialist(torencode)
    # En nu escapen door een delete aan te roepen
    commons.deleteAPIresource("verwijderslot", escapecode)






