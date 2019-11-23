package escape;

import nl.duo.testautomatisering.tmf.domain.rest.RestCallType;
import nl.duo.testautomatisering.tmf.domain.rest.RestMessageCall;
import org.junit.Test;

import static nl.duo.testautomatisering.utils.messageutils.JsonUtils.getJsonValue;

public class TheGreatEscape {
    @Test


    public void automatedEscape() {
        String o1 = oplossingPuzzle1(createcode());
        String volgorde = "{\"academieGebouw\":0,\"aKerk\":1,\"martini\":2,\"nieuweKerk\":3,\"stJozefKerk\":4}";
        String o2 = oplossingPuzzle2(o1, volgorde);
        if (o2.contains("out")) {
            volgorde = "{\"nieuweKerk\":0,\"academieGebouw\":1,\"stJozefKerk\":2,\"aKerk\":3,\"martini\":4}";
            o2 = oplossingPuzzle2(o1, volgorde);
        }
        if (o2.contains("out")){
            volgorde = "{\"martini\":0,\"aKerk\":1,\"nieuweKerk\":2,\"stJozefKerk\":3,\"academieGebouw\":4}";
            o2 = oplossingPuzzle2(o1, volgorde);
        }
        System.out.println ("oplossing " + o2);
        int result = 0;
        result = oplossingPuzzle3(o2, "32843");
        result = oplossingPuzzle3(o2, "587426");
        result = oplossingPuzzle3(o2, "527786");
        result = oplossingPuzzle3(o2, "7346337");
        result = oplossingPuzzle3(o2, "627836");

    }

    private int createcode () {
        // initialiseer een messageCall object
        RestMessageCall messageCall1 = new RestMessageCall();
        // Zo geeft je een type mee aan de messageCall
        messageCall1.setRestCallType(RestCallType.GET);
        // zo stel je een endpoint in
        messageCall1.setEndpoint("http://otagrnap357.duo.ota/rekensom");
        // een body meegeven aan je bericht wanneer je dit nodig hebt
        //messageCall1.setBody("{\"escape\" : \"body\"}");
        // het instellen van path parameters indien gewenst:
        messageCall1.addHeader("Content-Type", "application/json");
        messageCall1.addHeader("api-key", "4080cdbd-3888-41bc-8dc8-d450153d10f3");
        // Het versturen van je call
        messageCall1.sendMessage();
        // Het ophalen van het antwoord
        String delen = getJsonValue(messageCall1.getResponse(), "delen");
        String optellen = getJsonValue(messageCall1.getResponse(), "optellen");
        String aftrekken = getJsonValue(messageCall1.getResponse(), "aftrekken");
        String vermenigvuldigen = getJsonValue(messageCall1.getResponse(), "vermenigvuldigen");

        String getal1 = getJsonValue(messageCall1.getResponse(), "getal1");
        String getal2 = getJsonValue(messageCall1.getResponse(), "getal2");

        int g1 = Integer.parseInt((getal1));
        int g2 = Integer.parseInt((getal2));

        System.out.println(optellen + aftrekken + vermenigvuldigen + delen + getal1 + getal2);
        if (delen.contains("ue")) {
            return g1 / g2;
        }
        if (optellen.contains("ue")){
            return g1 + g2;
            }
        if (vermenigvuldigen.contains("ue")) {
            return g1 * g2;
        }
        if (aftrekken.contains("ue")){
            return g1 - g2;
        }
        return 1;

    }

    private String oplossingPuzzle1(int code){
        // initialiseer een messageCall object
        RestMessageCall messageCall1 = new RestMessageCall();
        // Zo geeft je een type mee aan de messageCall
        messageCall1.setRestCallType(RestCallType.GET);
        // zo stel je een endpoint in
        messageCall1.setEndpoint("http://otagrnap357.duo.ota/cijferslot");
        // een body meegeven aan je bericht wanneer je dit nodig hebt
        //messageCall1.setBody("{\"escape\" : \"body\"}");
        // het instellen van path parameters indien gewenst:
        messageCall1.addQueryParam("oplossing", code);
        // Headers geeft je zo mee
        messageCall1.addHeader("Content-Type", "application/json");
        messageCall1.addHeader("api-key", "4080cdbd-3888-41bc-8dc8-d450153d10f3");
        // Het versturen van je call
        messageCall1.sendMessage();
        // Het ophalen van het antwoord
        String antwoord = messageCall1.getResponse().header("oplossing1");;
        // kijken of er iets in het antwoord zit
        if (antwoord.contains("oplossing1")){
            System.out.println("bevat de tekst oplossing");
        }
        // De waarde van een specifiek Json Element in het respons ophalen

        return (antwoord);
    }

    private String oplossingPuzzle2(String oplossing1, String volgorde){
        // initialiseer een messageCall object
        RestMessageCall messageCall1 = new RestMessageCall();
        messageCall1.setRestCallType(RestCallType.POST);
        messageCall1.setEndpoint ("http://otagrnap357.duo.ota/torens");
        messageCall1.setBody(volgorde);
        // Hier straks e rekensom als api-header
        messageCall1.addHeader("Content-Type", "application/json");
        messageCall1.addHeader("api-key", "4080cdbd-3888-41bc-8dc8-d450153d10f3");
        messageCall1.addHeader("oplossing1", oplossing1);
        // Het versturen van je call
        messageCall1.sendMessage();
        // Het ophalen van het antwoord
        String antwoord = messageCall1.getResponseAsString();
        String oplossing2header = messageCall1.getResponse().getHeader("oplossing2");

        // kijken of er iets in het antwoord zit

            System.out.println("Antwoord: "+ antwoord);
            System.out.println("Header: "+ oplossing2header);

        // De waarde van een specifiek Json Element in het respons ophalen
        //String waarde = getJsonValue(messageCall1.getResponse(), "escaoe");
        if (antwoord.contains("out")) {
            return antwoord;
        }
        return (oplossing2header);


    }



    private int oplossingPuzzle3(String oplossing2, String telnr) {
        // initialiseer een messageCall object
        RestMessageCall messageCall1 = new RestMessageCall();
        // Zo geeft je een type mee aan de messageCall
        messageCall1.setRestCallType(RestCallType.GET);
        // zo stel je een endpoint in
        messageCall1.setEndpoint("http://otagrnap357.duo.ota/toolondersteuning/belspecialist/" + telnr);
        // een body meegeven aan je bericht wanneer je dit nodig hebt
        //messageCall1.setBody("{\"escape\" : \"body\"}");
        // het instellen van path parameters indien gewenst:

        // Headers geeft je zo mee
        messageCall1.addHeader("Content-Type", "application/json");
        messageCall1.addHeader("api-key", "4080cdbd-3888-41bc-8dc8-d450153d10f3");
        messageCall1.addHeader("oplossing2", oplossing2);
        // Het versturen van je call
        messageCall1.sendMessage();
        // Het ophalen van het antwoord
        if (messageCall1.getResponse().statusCode() == 200) {
            String slotcode = getJsonValue(messageCall1.getResponse(), "escapecode");
            oplossingPuzzle4(slotcode);
        }
        return messageCall1.getResponse().statusCode();
    }


    private void oplossingPuzzle4(String slotcode){
        RestMessageCall messageCall1 = new RestMessageCall();
        messageCall1.setRestCallType(RestCallType.DELETE);
        messageCall1.setEndpoint ("http://otagrnap357.duo.ota/verwijderslot/" + slotcode);

        // Hier straks e rekensom als api-header
        messageCall1.addHeader("Content-Type", "application/json");
        messageCall1.addHeader("api-key", "4080cdbd-3888-41bc-8dc8-d450153d10f3");
        // Het versturen van je call
        messageCall1.sendMessage();

    }

    private void voorbeeldRestMessageCall(){
        // initialiseer een messageCall object
        RestMessageCall messageCall1 = new RestMessageCall();
        // Zo geeft je een type mee aan de messageCall
        messageCall1.setRestCallType(RestCallType.GET);
        // zo stel je een endpoint in
        messageCall1.setEndpoint("http://localhost:8080/voorbeeld");
        // een body meegeven aan je bericht wanneer je dit nodig hebt
        messageCall1.setBody("{\"escape\" : \"body\"}");
        // het instellen van path parameters indien gewenst:
        messageCall1.addPathParam("code", "12345");
        // Headers geeft je zo mee
        messageCall1.addHeader("Content-Type", "application/json");
        // Het versturen van je call
        messageCall1.sendMessage();
        // Het ophalen van het antwoord
        String antwoord = messageCall1.getResponseAsString();
        // kijken of er iets in het antwoord zit
        if (antwoord.contains("antwoord")){
            System.out.println("bevat de tekst antwoord");
        }
        // De waarde van een specifiek Json Element in het respons ophalen
        String waarde = getJsonValue(messageCall1.getResponse(), "escaoe");
    }

}
