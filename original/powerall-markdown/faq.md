# Powerall - FAQ

## Hoe, wat m.b.t. de Firewall

#### Firewall poorten:

De volgende poorten moeten openstaan bij het gebruik van het betreffend programma:

| Poort | Type | Richting | Omschrijving |
| --- | --- | --- | --- |
| 5632 | TCP | Inkomend | Benodigd voor Thin Client (acurcl.exe). |
| 9000 | TCP | Inkomend | Benodigd voor planbord en barcodescanner. |
| 9000 | TCP | Inkomend | Nodig i.c.m. CNH eParts |
| 1433 | TCP | Uitgaand | SQL-verkeer, benodigd voor datasynchronisatie naar Overall Cloud, met IP-subnets:104.40.169.32 - 104.40.169.3913.69.112.168 - 13.69.112.17552.236.184.32 - 52.236.184.3920.61.99.192 - 20.61.99.223Zie ../azure-sql/../gateway-ip-addresses (West Europa). |

- Poort 9000 moet alleen nog openstaan vanaf extern, als er gebruik wordt gemaakt van de barcodescanner in bijv. een servicebus waarbij in de scanner het WAN IP adres wordt ingevuld en de gebruiker inlogt op een terminalserver.
- Tijdens de installatie van Powerall Connect worden deze firewall uitsluitingen automatisch toegevoegd aan de Windows Firewall (bij geavanceerde instellingen).
- Als er een andere firewall actief is, dienen deze regels handmatig toegevoegd te worden.
- Hierbij een overzicht van het Netwerkverkeer i.c.m. Powerall Connect.

Voor vragen kunt u contact opnemen met onze helpdesk.

- Welke instellingen zijn van belang bij het installeren van Powerall Connect?

---
## Hoe kan ik een link van de &lt;site&gt; openen?

# Hoe kan ik een link van de  openen?

In de webbrowser Chrome en Firefox is het (soms) niet mogelijk om de  van een website te openen, bijv. Belastingdienst.nl: Factuureisen. Onderstaande meldingen kunnen dan verschijnen.

#### Meldingen

Chrome

- ERR_EMPTY_RESPONSE of
- Deze site is niet bereikbaar.

Firefox

- Toegang geblokkeerd

#### Oplossing

#### Chrome

- U kunt een nieuw incognitovenster openen door te klikken op Menu > Nieuw incognitovenster, of door te drukken op Ctrl+Shift+N.

Firefox

- U kunt een nieuw privévenster openen door te klikken op Menu > Nieuw privévenster, of door te drukken op Ctrl+Shift+P.

---
## Hoe voeg ik een nieuwe administratie toe?

Belangrijk: • Bij het instellen van een nieuwe administratie in Powerall Connect moet veel ingericht worden. Voor de juiste werking van Powerall Connect moet dit correct gebeuren. • Neem daarom contact op met de helpdesk of planning.

---
## Welke instellingen zijn van belang bij het installeren van Powerall Connect?

Bij de installatie van het softwarepakket Powerall Connect is het volgende van belang:

#### Samenvatting:

- PW share toegankelijk voor gebruikers (bijv. C:\Beversoftware\PW (PW moet dan gedeeld worden en voor iedereen toegankelijk zijn).
- Thinclient op werkstations / terminal server (cliënt niet via wifi).
- Runtime service op applicatie server op poort 5632.
- Barcode:barcode service op poort 9000 (is alleen voor intern verkeer).
- barcode scanners via het wifi netwerk (kan ook bedraad).
- barcode printers via netwerk.

Netwerkprinters worden in Powerall Connect gedefinieerd (dus vaste namen i.v.m. printvoorkeuren).
E-factuur uitgaand: via smtp / imap / exchange (relay) / office 365, zie Instellingen documentbeheer.
E-factuur inkomend: lokale scanner of Powerall Connect Outlook Inbox
EDI koppeling: via een gedeelde map.
Betaalbestanden (sepa) inlezen via gedeelde map.

#### Virus uitsluitingen

- Voor virus uitsluitingen zie Wat zijn de virusscanner uitsluitingen of exceptions?

Firewall

- Voor firewall info zie Hoe, wat m.b.t. de Firewall

#### FAQ

Wat is een mogelijk probleem, bij het installeren van barcode service?

Het is mogelijk dat poort 9000 bezet, door een andere applicatie. Om dit te controleren, doorloopt u de volgende stappen:

1. Type  in, (bij windows zoeken).Het Opdrachtpromt scherm verschijnt.
2. Type het volgende commando in; .
3. In onderstaand voorbeeld is poort 9000, gekoppeld aan PID 4.
4. Ga naar Taakbeheer -> tabblad Details
5. In de kolom naam/beschrijving is te zien, welke applicatie, gebruikt maakt van deze poort 9000.

Oplossing

Powerall Connect werkt alleen met poort 9000, oplossing:

- Verwijder de 'vreemde' applicatie.Of
- Wijzig de poort van de applicatie.

- Wat zijn de virusscanner uitsluitingen of exceptions?
- Hoe, wat m.b.t. de Firewall

---
## Wat zijn de virusscanner uitsluitingen of exceptions?

Op bijna alle systemen waarop Powerall Connect gebruikt wordt, is ook een antivirus programma of scanner actief. Het gevolg hiervan is:

- Bij het scannen van bestanden worden deze in gebruik gehouden, waardoor Powerall Connect de bestanden niet altijd exclusief kan openen.
- Powerall Connect kan langzamer reageren, omdat elk bestand dat geopend wordt, ook (eerst) gescand wordt.

Om bovenstaand te voorkomen, sluit het volgende uit in de virusscanner:

#### Mappen:

- C:\Program Files (x86)\Beversoftware\*
- C:\\PW\*
- \\\PW\*
- Installatiemap van PowerallAdministratiemappen, als deze niet onder de installatiemap vallen (wat normaliter wel zo is).

#### Bestandsextensies:

- *.acu
- *.ppr

Programma's /processen:

- Acurcl.exe
- Acuthin.exe
- Wrun32.exe
- PowerAll.DataProvider.exe
- PowerAll.ServiceHost.exe

Voor vragen kunt u contact opnemen met onze helpdesk.

- Welke instellingen zijn van belang bij het installeren van Powerall Connect?

---
## FAQ Beheer

In dit hoofdstuk staan de meest gestelde vragen m.b.t. het beheer van Powerall Connect.

- Powerall Connect API
- Powerall Connect beheer services
- Powerall Connect Outlook Inbox
- Powerall Schaduwkopie

- Actieve taken / gebruikers
- FAQ gedeelde (administratie) gegevens
- Hoe pas ik de achtergrond PDF's aan van de facturen etc.?
- Hoe stel ik WiFi op de Datalogic Memor X3 scanner in?
- Hoe installeer ik een Powerall Connect update?
- Hoe voeg ik een nieuwe administratie toe?
- Hoe, wat m.b.t. de Firewall
- Wat betekent de ... status?
- Wat doe ik als NACK melding bij het uitlezen op de Opticon 1700/2700 scanner verschijnt?
- Wat zijn de virusscanner uitsluitingen of exceptions?

*Hoe start ik Remote support of TeamViewer? Met remote support is het mogelijk om mee te kijken op een computer, desktops e.d. Om Remote support te starten, doorloopt u de volgende stappen: 1. Ga naar het Powerall Connect informatie symbool (i-tje) in de bovenste menubalk. 2. Kies voor de knop Remote Support. De installatie van Teamviewer wordt gestart. 3. Bevestig de Windows gebruikersaccount melding. 4. Geef het ID en wachtwoord door. Er is nu een verbinding met Powerall Connect Support, rechtsonder verschijnt het teamviewer support symbool. Kan ik een programma of menu beveiligen met een wachtwoord? Ja, dit is mogelijk. Om dit te doen, doorloopt u de volgende stappen: 1. Ga naar Onderhoud menu's (BAM). 2. Selecteer het menu of programma. 3. Kies voor de knop Wijzig. 4. Geef het wachtwoord in. 5. Kies voor de knop Opslaan. De optie is beveiligd met een wachtwoord. Tip: Log in onder betreffende gebruiker en controleer of het werkt. Is het mogelijk om de dossier mappen* flexibel in te stellen bij een administratie?

Ja, het is mogelijk om de Dossier mappen flexibel in te stellen.

- Neem contact op met de planner om dit te regelen.
- Voor meer informatie over dossier mappen zie ook Dossier.

Hoe test ik de mailserver?

Het is mogelijk om de mailserver te testen. Dit geldt voor de ingestelde mailserver Powerall Connect of de eigen mailserver Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Instellingen documentbeheer (BIE)
2. Vul bij Testmail verzenden aan het  in.
3. Kies voor de knop Verzenden.

Controleer of de email binnengekomen is.

Opmerking: Indien gewenst kan de knop Verwijderen geautoriseerd worden, zodat niet iedereen een order kan verwijderen. Neem contact op met de planner om dit in te stellen.

- FAQ Powerall Connect installatie, updates e.d.

---
## Wat is de historie van de online documentatie?

### Algemeen

Regelmatig worden er een nieuwe hoofdstukken of FAQ's toegevoegd aan deze documentatie.

Wanneer gebeurt dit?

- Één (standaard) of twee keer per maand.
- Bij belangrijke nieuwe functies of wijzigingen in Powerall Connect.

Daarnaast worden veelgestelde vragen van klanten regelmatig toegevoegd en geactualiseerd.

Opmerking: Voor alle wijzigingen zie Release notes of Wat is nieuw in Powerall Connect?.

Wanneer is de documentatie voor het laatst bijgewerkt?

- De documentatie is voor het laatst geüpload op donderdag 11 juni 2026.

### Historie

#### 2026 Versie v2606 juni

- | Nieuwe Powerall logo: | | | --- | --- |
- Klik hier, voor meer informatie over dit onderwerp. De uitstraling van Powerall is krachtiger / stoerder geworden. Nieuwe slogan > Powerall: Grip that never slips
- Nieuw kleur > iets feller turqoise

#### 2026 Versie v2605 mei

- Release notes 3.30 - Beta / Release notes 3.30 beta versie, eind mei
- Machine portaal bij Instellingen is het mogelijk om externe links toe te voegen in het Dashboard of Navigatiemenu, vanaf mei 2026.
- Bij Peppol kunnen vier extra velden, zoals orderreferentie, ingegeven worden, vanaf versie 3.30.
- Bij Instellingen machines kunnen Duitse machine (factuur)teksten ingegeven worden voor Duits talige klanten, vanaf versie 3.30.
- Automatische accepteren van kratten i.c.m. picken, zie Hoe werkt picken / gereserveerd bij werkorders? vanaf versie 3.30.
- Machine kaart verzenden nieuw een aanbiedingsprijs kan ingegeven en e-mail bericht template, in eigen stijl, kan gebruik worden vanaf versie 3.30.
- Bij een Offerte is het mogelijk om de relatie te wijzigen: Hoe wijzig ik de relatie van een offerte of werkorder? vanaf versie 3.30 instelling.
- Op de Werkbon app is het mogelijk om Artikel informatie op te vragen, vanaf versie 3.30.
- Op de Werkbon app is bij de interne Notities de tekst uitgebreid.
- Bij Werkorders wordt in de voet het geregistreerde - en gefactureerde aantal uren / bedrag getoond. Hierdoor is een verschil gemakkelijker te zien, vanaf versie 3.30.

#### 2026 Versie v2604 april / v2605 mei

- Release notes 3.29/ Release notes 3.29 stabiele versie, vanaf einde mei
- Factuur afdrukken / verzenden nieuw, vanaf versie 3.29.
- Bij Machine levering / ontvangst is extra info toegevoegd, namelijk de leverancier en bij levering ook de eigenaar, vanaf versie 3.29.
- Vrijgeven offerte naar een bestaande Werkorder, vanaf versie 3.29.
- Werkbon app optie direct verzenden bij interne Notities, vanaf versie 3.29.

#### 2026 Versie v2602 februari / v2603 maart

- Release notes 3.28 / Release notes 3.28
- De nieuwe scanner op de Werkbon app, via de camera, vanaf versie 3.28, heeft de volgende voordelen: Sneller en nauwkeuriger, in en uitzoomen - en zaklamp functie bij weinig licht.
- Klik hier, voor meer informatie over dit onderwerp. De scan software, via de camera, is vernieuwd: 1. Pop-up informatie scherm wordt getoond. Als Niet meer tonen aangevinkt wordt, verschijnt deze pop-up niet meer. 2. Scan functie wordt getoond. Pinch: Je beweegt je duim en wijsvinger uit elkaar op het scherm. 3. Zoom: Je beweegt je duim en wijsvinger naar elkaar toe. 4. Tik op het witte kruis(je) om te focussen. 5. Scannen bij weinige licht, zaklamp kan gebruikt worden, druk op . 6. Scannen m.b.v. de zaklamp. Zie afbeelding #4 waarbij de zaklamp aan, let op mogelijke overbelichting.

Op de Werkbon app kan de Pauzetabel ook toegepast worden, vanaf versie 3.28.

Klik hier, voor meer informatie over dit onderwerp.

- Hiervoor is de instelling gebruik pauzetabel toegevoegd bij Instellingen werkorders, tabblad Werkbon app.
- De betreffende monteur moet gekoppeld zijn aan een Pauzetabel.
- De pauze begint en stopt automatische op de ingestelde pauzetabel tijd.
- Het is mogelijk om de pauze te stoppen, om verder te gaan met het werk.
- Als een gebruiker zelf al eerder de pauze gestart heeft, dan loopt de pauze zolang als deze in de pauzetabel staat.
- Minder dan 1 minuut wordt niet geregistreerd.
- Als de pauze meer dan 1 uur duurt, wordt bijv. 1u:4m getoond, zonder seconden.

Op de werkbon app verschijnt dan onderstaande melding:

Pauze duurt nog: x minuten : Y seconden

Bij STOP PAUZE:

- De pop-up verdwijnt, pauze stopt en wordt 'later' geregistreerd.

Bij ANNULEREN:

- De pop-up verdwijnt en komt weer terug. Pauze (tijd) wordt 'later' geregistreerd (bij elke annulering).

Bij afsluiten Werkbon App komt pop-up weer terug.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

'Later' is bij Einde werkdag.

Als er geen pauze (tabel) is ingesteld, wordt de gebruiker geacht zelf zijn pauze te registreren.

In Powerall is de Duitse vertaling beschikbaar, zie FAQ Taal.

Bij Peppol een link toegevoegd voor controleer Peppol-nummer: Peppolnummer controle.

Intake machine (snelle ingave servicemelding).

Boeken inkooporder machines nieuwe kostensoorten zijn toegevoegd bij grootboekrekening met een kostendrager.

Selecteren servicemeldingen nieuw: het adres is toegevoegd in kolom Postcode / adres.

Standaard journaalposten importeren / boeken er kan ook een kostendrager geïmporteerd worden nieuw.

#### 2026 Versie v2601 januari

- Release notes 3.27 - hotfix verbeterde versie van 3.27.
- Verhuur planbord 2.0 offerte en dubbele contracten zijn zichtbaar en de beschikbaarheid en opmaak is verbeterd, vanaf versie 3.27.

#### 2025 v2510 oktober / v2511 november / v2512 december

- Release notes 3.27
- Al de apps zijn bijgewerkt en zitten op Android versie 15+.
- Barcode scanner bijgewerkt / de barcodescanner software is geüpdatet. Beschikbaar in de Google Playstore, zie Powerall Barcode. Klik hier, voor meer informatie over dit onderwerp. Update Barcode app. De barcodescanner-software is geüpdatet. Bij eerdere versies was het niet mogelijk om op de scanner te controleren of een artikel bestond, en het terugkijken van gescande onderdelen was omslachtig. De nieuwe Barcode App biedt aanzienlijk meer functionaliteit en intelligentie. Artikelen kunnen eenvoudig worden gescand, inclusief EAN-codes en equivalentnummers. Dankzij de realtime verbinding met de Powerall-database wordt direct het juiste artikel opgezocht. Indien een artikel niet wordt herkend, verschijnt er een foutmelding. De controle via een pop-up bij het uitlezen is komen te vervallen. Deze controle vindt direct plaats tijdens het scannen. Het uitlezen gebeurt voortaan via een directe verbinding met de server of hoofdcomputer, in plaats van via een werkstation. Voor het achteraf bekijken van gescande gegevens blijft het Overzicht barcode scanningen beschikbaar, waarin alle gescande informatie wordt weergegeven. Belangrijkste verbeteringen: Onze doelstelling is om een intelligente scanner te ontwikkelen met steeds meer functionaliteiten. Daarom is de 'pop-up met gescande artikelen' niet langer nodig of beschikbaar. Bij Overzicht barcode scanningen zijn nog steeds alle gescande gegevens te zien. Belangrijkste verbeteringen:
- Bij het scannen van een artikel wordt direct de artikelcode weergegeven. Artikelen kunnen worden gescand op zowel EAN-code als equivalentcode.

Verzenden

- De artikelen worden vóór verzending gecontroleerd op geldigheid.
- Bij het verzenden worden de gegevens direct en automatisch verwerkt, zonder dat verwerken Uitlezen barcode scanner open hoeft te staan. 1. Uitzonderingen zijn Balie i.c.m. bonnen en Bestellen i.c.m. goedkeuren.

Bij werkorders kunnen ter info ook de klantnaam en referentie worden getoond.

In de CRM app wordt bij Machine transacties de status van de werkorder weergegeven.

Klik hier, voor meer informatie over dit onderwerp.

Een werkorder heeft de volgende status:

- Open - bij geen artikelen en uren nieuw.
- In Uitvoering - bij artikelen of uren incl. bedragen nieuw.
- Gereed - de werkorder is vrijgegeven.

Hierdoor zijn de open - en lopende werkorders met de prijzen beter inzichtelijk.

Artikelen

- Deze bevat Materiaalverbruik, Eerder geregistreerd en Bestellen in één scherm, vanaf versie 3.27.

Besteladvies op basis historie

Hoe, wat m.b.t. kleine machines (vernieuwd)

- Serienummers & Barcode scanner

Onderhoud machine merken toegevoegd fabrikant

Bij Opvragen artikelen, Opvragen relaties F6 en Opvragen machines (MO) is het mogelijk om in diverse tabbladen de regels te sorteren.

Verhuur borg 2.0.

Verhuur planbord 2.0 verbeterd, maandweergave toegevoegd.

Peppol integratie mogelijk voor een relatie met alleen een GLN-nummer nieuw.

Vrijgeven verkooporder is mogelijk via de Taakplanner nieuw, vanaf versie 3.27.

Werkbon app Ritten verbetering van de weergave van het volledig (bezoek) adres.

Powerall Schaduwkopie nieuw incl. logs.

Webshop en Vooruitbetaling

Bij Zoek artikelen worden bij Granit en TVH alternatieve artikelen getoond.

Powerall Connect versie 3.26 vervalt, de betreffende updates zitten in 3.27.

#### 2025 Versie v2507 juli / v2508 augustus / 2509 september

- Release notes 3.25
- Welke leveranciers integraties zijn er? Toegevoegd: Oosterberg parts inquiry en digitale order.

Machine portaal verbetering van de zoekfunctie o.a. bij servicemeldingen en de uitgebreide teksten van een werkorder zijn te zien.

Op de Barcode scanner kan er op een Werkorder een dynamische samenstelling aangemaakt worden.

- Bij het scannen van een artikelstructuur met een dynamische samenstelling is het mogelijk om, d.m.v. een pop-up, meerdere artikelen te scannen, die in totaliteit de samenstelling vormen.
- Neem contact op met de planning om dit in te richten.

Via Invoeren kassabonnen kan ook een Kleine machine of Machine verkocht worden.

Hoe, wat m.b.t. Peppol nieuw geldt ook voor inkomende facturen

Verhuur / Contracten 2.0

Werkbon app Openstaand werk icm scannen werkorder nieuw.

#### 2025 Versie v2505 mei / v2506 juni

- Release notes 3.24
- Hoe werkt ondertekenen offerte i.c.m. Stiply? Nieuw standaard of eigen e- mailtekst.
- Integraties nieuw CNH
- Overzicht matching controlelijst FAQ's toegevoegd
- Vaste activa rapportage de rapportage keuze jaaroverzicht is verbeterd, zodat e.a. beter gecontroleerd kan worden.

#### 2025 Versie v2503 maart / v2504 april

- Release notes 3.23
- Machine inkooporder nieuwe optie voor alleen Machine inkooporders (IM)
- Vooruitbetaling op een werkorder nieuw.
- Hoe werkt ondertekenen offerte i.c.m. Stiply?

#### 2025 Versie v2501 januari / v2502 februari

- Release notes 3.22
- Bij Onderhoud artikelstructuren is het vinkje Dynamisch toegevoegd. Bij het scherm Artikel samenstelling (dynamisch) kunnen dan artikelen toegevoegd worden.

Bij Onderhoud kassa's kan een Kostenplaats gekoppeld worden.

De kolom Gepickt is ook zichtbaar bij Invoeren / wijzigen werkorders bij picken orders.

Machine portaal

Hoe werkt partnershop order doorfacturering (Kramp / Granit)? geldt ook voor Granit.

Powerall barcode scanner - instellingen

2024

#### 2024 Versie v2411 november / v2412 december

- Release notes 3.21
- Jaarafsluiting verbeterd: Jaarafsluiting - 3.0 menu
- Jaarafsluiting - klassiek menu

Bij e-Factuur kan een betaallink i.c.m. MultiSafepay in de e-mail toegevoegd worden.

Kopiëren uit catalogus of online informatie nieuw vinkje Aanvullen na aanmaken toegevoegd.

MultiSafepay mutaties kunnen geïmporteerd worden bij Inlezen/verwerken bankafschriften.

Bij selecteren van een Kleine machine kan er een Servicemelding aangemaakt worden Instelling.

Hoe, wat m.b.t. scan en herken? Mogelijkheid om feedback te geven op een ingescande pdf bon of factuur.

Hoe werkt de feedback functie?

Het is mogelijk om een reactie of feedback te geven op het ingescande document, bijv. als een factuurbedrag niet klopt, vanaf versie 3.21.

Om dit te doen, doorloopt u de volgende stappen:

1. Druk op de regel Klik hier om feedback te geven. Rechts verschijnen de Herkende waardes.
2. Corrigeer de Juiste waarde, indien nodig.
3. Markeer de betreffende waarde, d.m.v. een rode rechthoek, op het PDF.
4. Kies voor de knop Versturen.
5. De pop-up De feedback is verzonden verschijnt. Kies voor de knop OK.
6. De tekst Feedback verstuurd verschijnt.

Powerall Connect informatie er is een link toegevoegd naar Linkedin/Powerall en Facebook.

#### 2024 Versie v2409 september / v2410 oktober

- Release notes 3.20
- Hoe meld ik mij aan voor de bankkoppeling? nieuw
- Kassa pin terminal nieuw.
- Selecteren machines tabblad Alle, nieuw vinkjes voor status en configuratie met selectie element 1 t/m 4.
- Machine (magazijn) locaties Het volgende is van toepassing bij machine locaties: Bij Onderhoud machines (MBB) is het mogelijk gebruik te maken van de magazijnlocaties. Er kan gebruik gemaakt worden van vrij invulbare locaties of standaard locaties.
- Als er bij het betreffend magazijn locaties aanwezig zijn, kunnen deze d.m.v. het loepje of F4 geselecteerd worden.

Bij Instellingen machines kan bij het veld magazijnlocatie ingesteld worden of deze al of niet verplicht is.

Bij Onderhoud magazijnlocaties (ABZ) kunnen de (machine) locaties, per magazijn, ingegeven worden.

Hoe werkt WhatsApp? nieuw

#### 2024 Versie v2408 augustus

- Release notes 3.19
- Het volgende is in te stellen bij Werkorder(s): Selecteren werkorders De werkorder datum t/m. Standaard zijn de orders t/m vandaag zichtbaar. Hierdoor is het mogelijk om de orders van volgende  dagen / week standaard te zien.
- Nieuwe werkorder aanmaken Controle op dubbel gebruik van een servicenummer in een werkorder, als het servicenummer gewijzigd wordt.

Bij Instelling artikelen is de instelling HS-code toegevoegd, zie ook:

- Onderhoud HS-code / Customs code

Powerall Connect API, FAQ bijgewerkt.

Vanuit de Webshop kan een expeditiecode mee te geven naar Powerall Connect.

#### 2024 Versie v2407 juli

- Release notes 3.18
- Doorverwerken facturen is sneller gemaakt.
- Kassa De Betaal knop teksten zijn flexibel instelbaar. Er zijn 3 extra betalingsopties toegevoegd, totaal zijn er 5 knoppen optioneel.
- Werkorder offerte. Op een Offerte voor een werkorder wordt standaard de werkopdracht / factuurtekst weergegeven.
- De Barcode app is beschikbaar in de Google Playstore, zie Powerall Barcode. De Powerall Barcode app is alleen te gebruiken op de 'Powerall' barcodescanner.

Powerall Connect API nieuw

#### 2024 Versie v2406 juni

- Release notes 3.17
- Bankkoppeling De knop Bankkoppeling is toegevoegd, met gegevens over de koppeling. De toestemming kan gereset of de bankkoppeling kan ontkoppeld worden.

Hoe werkt picken / gereserveerd bij werkorders?

#### 2024 Versie v2405 mei

- Release notes 3.16
- Machine en GPS tracker nieuw
- De OCI of bestelkoppeling met DAF is vrijgegeven. Klik hier, voor meer informatie over dit onderwerp. Het volgende geldt hierbij: Met OCI is het mogelijk om direct vanuit een werkorder bij de DAF webshop te bestellen, met de keuze ‘auto confirm’ aan of niet.
- Hierbij worden de bestelde webshop artikelen toegevoegd op de werkorder en er wordt ook een inkooporder aangemaakt in Powerall Connect.
- Met de 'digital order' koppeling kan ook direct vanuit Powerall besteld worden. De order levering loopt via DAF en de dealer waar je klant bent. Voor meer informatie zie: DAF Bestelkoppeling.

Bij Opvragen artikelen is het mogelijk om de (afgesproken) prijs en voorraad op te halen d.m.v. zogenaamde ‘parts inquiry’.

- Voor meer informatie zie: Artikel info DAF.

Deze koppeling moet eerst aangevraagd worden en wordt door DAF geactiveerd.

#### 2024 Versie v2404 april

- Release notes 3.15
- Bij het zoeken naar een artikel, op de Powerall Werkbon App, kan er op meerdere zoektermen gezocht worden. Materiaalverbruik

Connect API logging

#### 2024 Versie v2402 februari / v2403 maart

- Release notes 3.13 en Release notes 3.14
- Barcode & scanners Barcodescanner registeren
- Barcode scanner nieuw Urovo scanner
- I.c.m. de barcodescanner kan er een serveradres ingevuld worden.

Bij het aanmaken van een catalogus artikel verschijnt er een melding, als het artikel vervangen is door de leverancier.

Invoeren kassabonnen nieuw functie toetsen bij afrekenen, bijv. F12.

- Nieuw incl. afronden bij Contant betaling op een apart grootboek. Neem contact op met de planning om dit in te richten.

Machine samenstelling nieuw

Klik hier voor meer informatie over Weergave afwijkende magazijn leverancier.

In onderstaand geval, is bij het magazijn waarmee ik ingelogd ben een afwijkende magazijn leverancier gekoppeld en getoond.

- Dit is bijv. het geval, bij een bepaalde vestiging, waar besteld wordt bij de leverancier om de hoek en niet bij het standaard magazijn.
- Het veld afwijkende bestelleverancier op tabblad Voorraad kan hiervoor gebruikt worden.
- | Afwijkende bestelleverancier | Selecteer hier de afwijkende bestelleverancier, voor het standaard magazijn van de gebruiker:- 0 Geen afwijkende leverancier (standaard). - . Deze geselecteerde leverancier gaat boven de voorkeur leverancier. Deze Magazijn verschijnt ook op tabblad Leverancier. Hierbij bestelt dit magazijn bijv. niet 'standaard', maar lokaal. | | --- | --- |

Werk registeren en uitvoeren

- Ritten nieuw

Werkorder uren registreren nieuw bij Urenregistratie controle selectie op afdeling.

#### 2024 Versie v2401 januari 3.12

- Release notes 3.12
- Inlezen/verwerken bankafschriften Bankkoppeling nieuw

Hoe, wat m.b.t. Peppol nieuw dit is een betaalde service

Hoe, wat m.b.t. de Firewall IP- subnets bijgewerkt

Inkooporder details toegevoegd

2023

#### 2023 Versie v2311 november 3.11 / v2312 december

- Jaarafsluiting bestaat uit: Jaarafsluiting - 3.0 menu
- Jaarafsluiting - klassiek menu

- Uitlezen barcode scanner bijgewerkt.

#### 2023 Versie v2310 oktober

- Afletteren grootboekmutaties nieuw kolom Kostendrager
- Wizard Nieuwe relatie nieuw zoeken op (Postcode,) KvK, BTW-nummer en Naam, ook voor Belgische bedrijven.
- De SendCloud verzendwijze is geïntegreerd i.c.m. order picken 2.0.
- Interne werkorder vrijgeven nieuw bij de optie 'direct doorverwerken' ja, huidige periode verschijnt er geen pop-up scherm meer.
- Welke leveranciers integraties zijn er? bijgewerkt
- Bij een verkoop van een kleine machine kan automatisch een servicemelding aangemaakt worden, vanaf versie 3.10.
- Release notes: powerall.nl/release-notes/3.11 verplaatst
- Systeemeisen minimale eis wordt Windows Server 2016 (was 2012)

#### 2023 Versie v2309 september 3.09

- Hoe, wat m.b.t. scan en herken? vernieuwd eenvoudiger in te stellen / te proberen.
- Servicemelding icm kleine machine nieuw
- Zoek relaties nieuwe kolommen mobiel en e-mail Incl. 'zoek'vinkjes Afleveradressen en Contactpersonen.

50x35.tspl schapkaart nieuw

- Aanmelden vervoerder opnieuw Aanmelden zending bij een vervoerder.
- Systeemeisen in de Firewall moet poort 1433 uitgaand openstaan.

#### 2023 Versie v2308 juni / juli / augustus 3.08

- Favorieten 3.0 menu en F4
- Klik hier voor meer informatie over de wijzigingen in deze documentatie: Nieuw hoofdstuk bij Verkoop voor: Verkooporders
- Bonnen

De volgende hoofdstukken zijn hernoemd:

- Inkoopfacturen was Crediteuren
- Verkoopfacturen was Debiteuren

De volgende hoofdstukken zijn verplaatst:

- Powerall CRM app naar Relaties (was Verkoop)
- Keuringen naar Machines (was Service)

Artikel verwijzing aanleggen nieuw wijzigen inkoop artikelcode met leveranciers selectie.

Hoe maak ik een creditnota? nieuw

Hoe herstart ik de Service Host? nieuw

Hoe, wat m.b.t. kleine machines (vernieuwd) vernieuwd

E-facturen verbeterd

Kramp catalogus update

Selecteren servicemeldingen nieuwe kolom ordergegevens

Opvragen werkorders per debiteur

Een nieuwe licentie module WMS (warehouse management systeem) is toegevoegd.

#### 2023 Versie v2305 april / mei

- Overzicht orders (te picken) 2.0 het volgende is aangepast. Klik hier, voor meer informatie over dit onderwerp. Tabblad Gepickt gewijzigde knop Correctie picklist Nieuw vinkje automatisch vernieuwen.
- Nieuw bij Voorgestelde levering Print colli label (printer-knopje) en de knop Correctie picklist.

Tabblad Te verzenden en nieuwe knop Correctie zending en nieuwe kolommen Factuur, bedrag en Fiat(tering) met een selectie hierop.

- Nieuw het zoeken op collinummer / colli-barcode (naast zending) is hierbij mogelijk.

Tabblad Nog vrij te geven nieuwe knop Correctie zending

Hoe, wat m.b.t. kleine machines (vernieuwd) vernieuwd

Selecteren machines.

- Het vinkje Directe selectie is toegevoegd, de tabbladen worden hierbij direct gevuld.
- De knoppen Nieuw en Wijzigen zijn op elk tabblad beschikbaar.

Zoek afleveradressen, nieuwe wijzig en toevoeg knop.

#### 2023 Versie v2303 maart 3.03/4

- De garantie omschrijving wordt getoond bij: Nieuwe servicemelding aanmaken.
- Een Machine transactie.

Selecteren verkoopfacturen

#### 2023 Versie v2302 februari 3.02

- Hoe, wat m.b.t. takenlijst i.c.m. Werkbon App nieuw
- Opmaak van deze documentatie is bijgewerkt conform Powerall Connect 3.0 Hoe, wat m.b.t. het 3.0 menu? nieuw

Nieuw machine aanmaken of kopiëren RDW vinkje gewijzigd naar Online.

Overzicht orders (te picken) 2.0 het volgende is aangepast.

- Tabblad Te picken nieuwe knop Wijzig picklist en Print picklist
- Tabblad Nog vrij te geven, nieuwe knop Vrijgeven alle

Installatie Werkbon App bijgewerkt.

Webshop

- Webshop koppeling info webx3interface.creeksites.net/connect-api

Zoek contactpersonen

De volgende modules zijn samengevoegd tot één module Artikelen catalogi:

- Artikelen catalogi leveranciers
- Artikelen Parts locator
- Artikelen integratie EPC
- Inkooporders EDI

#### 2023 Versie v2301 januari 3.01

- Hoe, wat m.b.t. de betaallink nieuw
- Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders? nieuw
- Hoe, wat m.b.t. scan en herken? nieuw
- Kopieren bonnen of orders
- Koppeling werk-/verkooporder met inkooporder bijgewerkt
- Bij de volgende Selecteren programma's is ook het veld Direct zoeken bon of order toegevoegd. Selecteren bonnen
- Selecteren inkooporders
- Selecteren offertes
- Selecteren werkorders Een werkorder kan hiermee ook ingescand worden.

Hierbij kan direct het betreffend ordernummer ingegeven worden.

2022

#### 2022 Versie v2210 t/m v2212 oktober t/m december 3.00

- Hoe voer ik een jaarwissel uit? bijgewerkt
- Einde werk Werkbon App bijgewerkt
- Hoe, wat m.b.t. het 3.0 menu? nieuw
- Hoe, wat m.b.t. verzamelfacturen ter info
- Verwachte goederenontvangst, ophalen ASN ook voor Kramp.
- Bij Instellingen bedrijf (BIB) is het adres 2 en de postcode 2 gesplitst in twee aparte velden postcode en woonplaats.
- Nieuwe wizard voor Instellingen externe communicatie (BAC)intern

#### 2022 Versie v2207 t/m v2209 juli / augustus / september 2.61

- Bij een BtB koppeling is het inkoopnummer / omschrijving van de leverancier toegevoegd.
- Bij de order ingave is het veld postcode en woonplaats gesplitst in twee aparte velden. Dit om mogelijke problemen bij vervoerders te voorkomen.

Taakplanner instellen nieuwe overzichten toegevoegd:

- E-inkoopfacturen, automatisch ophalen

Invoeren kassabonnen bij Kassa afrekenen, referentie en ordergegevens toegevoegd.

Toegevoegd valutateken bij Onderhoud valutacodes

- Instellingen bedrijf valutacode incl. valutateken.
- Het valutateken wordt gebruikt bij de Machines CRM app voor de artikel en machine prijzen.

#### 2022 Versie v2206 juni 2.60

- CBS aangifte bijgewerkt m.b.t. 2022
- Overzicht orders (te picken) 2.0, tabblad Te picken, controle of order nog in gebruik is.
- Taakplanner instellen nieuwe overzichten toegevoegd: Proef- en saldibalans
- Balans / Winst & verlies

Verwachte goederenontvangst nieuwe zoek velden referentie, artikel en ordernummer.

#### 2022 Versie v2205 mei 2.59

- Periodewissel, de nieuwe of volgende periode wordt automatisch bepaald.
- Selecteren servicemeldingen toegevoegd Vinkje alleen lege voorkeursmonteur.
- Wat doe ik als het betaalbestand / incassobestand afgekeurd wordt?

#### 2022 Versie v2204 april 2.58

- Onderhoud machines nieuwe gebruikstatus Demo
- Powerall CRM app nieuwe versie Nieuwe notitie CRM app bijgewerkt
- Machine transacties

Verwerken prijswijzigingen (artikelen)

#### 2022 Versie v2203 maart 2.57

- Taakplanner instellen nieuwe programma's toegevoegd.
- De Plus-knop en een Pennetje-knop zijn toegevoegd bij: Zoek artikelen
- Zoek contactpersonen
- Zoek machines
- Zoek relaties

Onderhoud standaard journaalposten voorbeeld tabel toegevoegd.

Powerall Werkbon App

- Bij Instellingen werkorders kunnen artikelen met de volgende artikelstatus uitgevinkt worden, zodat deze niet meer zichtbaar zijn nieuw: Niet meer leverbaar, Op aanvraag en Uitlopend.

Collega uitnodigen

Eerder geregistreerd

- Retourneren eerder geregistreerd

Verzending leveringen

#### 2022 Versie v2202 februari 2.57

- Dossier Werkbon App nieuw
- Overzicht orders (te picken) 2.0 nieuwe optie Gepickt (was Te leveren) / Te verzenden / Nog vrij te geven
- Onderhoud machines t.b.v. Advertentiekoppeling (machines) nieuw veld Prijs weergave incl. / excl. BTW.
- Onderhoud standaard journaalposten automatische verwerking
- Teksten en (sub) totalen
- Verwachte goederenontvangst nieuw Ontvangstlabels.
- Taakplanner instellen nieuw

#### 2022 Versie v2201 januari 2.56

- Afletteren grootboekmutaties nieuw vinkje om alles aan te vinken.
- E-inkoopfacturen (geavanceerd). tabblad Betaalbaar nieuw kolom Openstaand bedrag is toegevoegd.
- Overzicht orders (te picken) 2.0 nieuw Te picken ordersoort en totaal orders / regels in de voet.
- Selecteren inkooporders nieuw inkoop ordertype selectie. Bij Inkoop rapportages is dit veld inkoop ordertype toegevoegd en kan er op geselecteerd worden.

Zoek machines

Nieuwe filter overzichten toegevoegd m.b.t. het alleen zoeken in de overzichten programma's, bijv. zoeken op de term analyse:

- #search-analyse?f=Overzichten Belangrijk: Vergeet niet om de filter terug te zetten naar Alle bestanden.

2021

#### 2021 Versie v2112 december 2.55

- Boeken goederenontvangst, bij machine inkoopfactuur kan het SN en kenteken bijgewerkt worden in de lopende orderteksten.
- Hoe werkt de Gemiddelde Inkoop Prijs (GIP) waardering?
- Onderhoud machines nieuwe vinkje Buitenlands kenteken bij soort bedrijf is Agrotechniek.
- Print artikellabels

#### 2021 Versie v2111 november 2.54

- CBS aangifte i.p.v. CBS aanpassing per 1-1-2022.
- Bij de opvraag programma's worden de velden weergegeven zonder rand, als 'scherm' veld. Opvragen relaties F6
- Opvragen artikelen
- Opvragen machines (MO)

#### 2021 Versie v2110 oktober 2.54

- Opvragen inkooporders
- Van welke leveranciers is een EDI koppeling beschikbaar? nieuw Homburg en Manitou en nieuwe kolom Digitale order.
- Selecteren inkooporders nieuwe kolom Digitale order
- Goederenmatching bijgewerkt Selecteren matching manco's apart topic, nieuw Wijzig reden.

#### 2021 Versie v2109 september 2.53

- Contract indexering
- Onderhoud / overzicht budgetten
- Hoe komt het dat artikelen 'verdwijnen' van de werkorders i.s.m. de Werkbon App?
- Hoe werk ik de APK of Tachograaf datum bij? nieuw Tachograaf tabblad Services
- Beheer servicemelding nieuwe knop Gereed melden
- Verwerken intercompany mutaties

#### 2021 Versie v2108 augustus 2.52

- Opvragen artikelen per machine
- Overzicht configuratie elementen
- Goederenmatching voorbeelden toegevoegd o.a. machine matching
- EORI nieuw
- Onderhoud keuringscodes nieuw Tachograaf-keuring Hoe werk ik de APK of Tachograaf datum bij? geldt ook voor geplande Tachograaf-keurings datum

Selecteren machines nieuw tabblad Offerte

#### 2021 Versie v2107 juli 2.51

- Hoe, wat m.b.t. de tellerstand registratie? kilometer registratie RDW
- Aanmaken/verwerken tellijst
- Advertentiekoppeling | Instellingen / basis controle machine op hoofd- en subgroepen
- Installatie Werkbon App

#### 2021 Versie v2106 juni 2.50

- Afletteren grootboekmutaties bij Boekstuk details nieuw knop Matchingdetails
- Opmerking: Het is mogelijk om standaard BTW-codes voor binnenland, EU en buitenland in te stellen. Dit kan bij instellingen debiteuren en Instellingen crediteuren, standaard zijn deze al ingesteld.• Door dit te doen wordt automatisch bij Nieuwe relatie aanmaken de juiste BTW-code gekozen als een buitenlandse relatie wordt aangemaakt.
- Overzicht dagstatistiek nieuw per land / BTW-code
- Lay-out wijzigen toevoegen Artikellabels op A4 in 3 kolommen, zie FAQ
- Van welke leveranciers is een EDI koppeling beschikbaar? nieuw Hikoki/Hitachi

#### 2021 Versie v2105 mei 2.49

- Export productregistratie Stihl bijgewerkt
- Onderhoud blokkeringscodes
- Powerall CRM app

#### 2021 Versie v2104 april 2.48

- Opvragen bonnen per debiteur
- Onderhoud dagboeken nieuw oudste boekingsperiode
- Powerall CRM app
- Powerall Connect informatie
- Selecteren audit trail artikel mutaties bijgewerkt
- Ophalen weborders / Orders verwerken 2
- Zoek artikelen bijgewerkt

#### 2021 Versie v2103 maart 2.47

- Opvragen artikelencatalogus
- Goederenmatching 3.0 nieuw dagboek Matching
- Hoe update ik het Powerall Connect Werkstation? bijgewerkt
- Standaard journaalposten
- Taakplanner nieuw / in menu Opvragen geplande taken
- Taakplanner monitor

#### 2021 Versie v2102 februari 2.46

- Multimagazijn overboeken bijgewerkt serienummer
- Nieuwe offerte aanmaken nieuwe optie offertesoort Werkorder, met tabblad Werkomschrijving
- Onderhoud artikeltracering multimagazijn
- PP400 installatie PostNL nieuw
- Powerall Werkbon App Registratie en Orderdetails
- Werk controleren en aftekenen nieuwe optie in- / direct verwerken

Advertentiekoppeling (machines) bijgewerkt:

- Advertentiekoppeling | Publiceren machine
- Advertentiekoppeling | Instellingen / basis

Selecteren inkoopfacturen

Hoe verwijder / disconnect ik een gebruiker(sessie)?

#### 2021 Versie v2101 januari 2.45

- Hoe, wat m.b.t. de kenteken registratie?
- Kramp catalogus update nieuw
- Standaard journaalposten importeren / boeken
- Selecteren programma's:Selecteren contracten
- Selecteren offertes
- Selecteren projecten 2.0
- Selecteren verhuurorders

Onderhoud artikellocatie per magazijn (bijgewerkt)

Print prijsaanvraag

Webshop

Opmerking: De hoofdstukken (in de inhoudsopgave links) met een * zijn nieuw of gewijzigd.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Historie 2017 - 2021

---
## Historie 2017 - 2021

#### Historie Powerall Connect

Klik op het gewenste jaar, voor meer informatie.

2020

#### 2020 Versie v2012 december 2.45

- Hoe, wat m.b.t. een actief / inactief relatie? nieuw
- Export productregistratie Stihl optie eindklantgegevens
- Selecteren programma's:Selecteren servicemeldingen extra kolom 'Uren' en Totaal De arbeidscapaciteit kan hierdoor beter ingeschat en ingezet worden.
- Selecteren bonnen
- Selecteren inkooporders
- Selecteren verkooporders
- Selecteren werkorders

Opvragen verkooporders

Overzicht machine website gegevens

PP400 printer kop afstellen, label en lintplaatsen

#### 2020 Versie v2011 november 2.44

- Afschrijvingen machines
- Artikelen, online info leverancier Stierman De Leeuw
- Uitlezen barcode scanner aangepast
- Opvragen mutaties kostenplaats
- Hoe controleer ik op dubbele relaties? nieuw
- Hoe kan ik kosten achteraf op een machine boeken zonder werkorder?
- PP400 printer PP400 printer kalibreren

Export productregistratie Stihl  nieuw
Rentenota's

Windows gebruikersaccount melding

EDI leveranciers koppeling nieuw: AVA cooling en NRF

Opvragen verkooporders

#### 2020 Versie v2010 oktober 2.43

- Nieuwe offerte aanmaken PDF offerte
- Credit nota
- Powerall Schaduwkopie Kopie delen met helplijn
- Selecteren inkooporders controle op minimum orderbedrag
- Systeemeisen vernieuwd

#### 2020 Versie v2009 september 2.42

- Barcode scanningen Barcode scanner nieuw + QR-code scannen

Controle BTW aansluiting

Fedecom benchmark

EDI leveranciers koppeling  nieuw: Fabory, Nilfisk en Reesink

Mijn Powerall / klantenportaal

Kopie facturen

Wat is een kostendrager?

Powerall Connect Outlook Inboxbijgewerkt
Werkorder tekening

#### 2020 Versie v2008 augustus 2.42

- Advertentiekoppeling (machines) Hoe pas ik bij een machine rubriek op website?

Hoe, wat kan ik met de artikelstatus?

Hoe pas ik de achtergrond PDF's aan van de  facturen etc.?

Doorverwerken machine-transacties

Opvragen machines tabblad Offertes

Rapportage

Wat doe ik als de financiële voorraad niet aansluit met de  machines?

#### 2020 Versie v2007 juli 2.41

- Doorverwerken interne werkorders
- E-inkoopfacturen (geavanceerd) eigen Inbox
- Hoe kan ik een opslag toepassen bij bepaalde artikelen, bij de kassa?
- Hoe werkt een vooruit- of aanbetaling bij een verkoop- of werkorder?
- Machine marge regeling

#### 2020 Versie v2006 juni 2.40

- Onderhoudsschema's machines artikelen toevoegen per beurt
- Zoek artikelen

#### 2020 Versie v2005 mei 2.39

- Kopiëren uit catalogus of online informatie
- Koppeling werk-/verkooporder met inkooporder
- Zoeken leveringen

#### 2020 Versie v2004 april 2.39

- EDI / Digitale inkooporder aanmaken + Digitale order Technische Unie
- Van welke leveranciers is een EDI koppeling beschikbaar?
- Invoeren kassabonnen pin-code en retour scan
- Machine VA-Keur
- Multimagazijn overboeken
- Overzicht orders (te picken) 2.0 nieuw
- Berekenen verhuurtarieven

#### 2020 Versie v2003 maart 2.38

- Opmerking: Er kan een eigen lay-out voor de betaallijst of incassolijst gebruikt worden.• Betere integratie met de Technische Unie, digitale inkooporder kunnen met één druk op de knop besteld worden.
- Hoe geef ik een vast IP-adres aan de PowerPrint?
- Hoe werk ik de lopende orders bij, (m.b.t. NAW-gegevens)?
- Werkorder planbord + FAQ bijgewerkt.
- Welke opties zijn er bij servicemeldingen / werkorders en Werkbon App? vernieuwd

#### 2020 Versie v2002 februari 2.37

- E-inkoopfacturen (geavanceerd) uitbreiding autorisatie / log
- Werkorder planbord + FAQ
- Hoe, wat kan ik ... m.b.t. dashboard / selecteren programma's? sortering op kolommen
- Wat doe ik bij de e-mail melding 'Powerall CRM  for IOS is now available to test'?
- Werk controleren en aftekenen (Werkbon App)

#### 2020 Versie v2001 januari 2.36

- CBS aangifte toegevoegd Intrastat en CBS handleiding 2020
- Onderhoud reiszones nieuw in menu
- Opvragen machines
- Opvragen relaties
- Vaste activa (module)
- Powerall Werkbon App Artikelen scannen Werkbon App
- Spoed bestelling

2019

2019 Versie v1911 november 2.34

- Hoe, wat m.b.t. Powerall werkstation?
- Selecteren machines Wijzigen machine
- Vrijgeven offerte naar werkorder tellerstand opgave

2019 Versie v1910 oktober 2.33

- Afschrijvingen machines
- Nieuw artikel aanmaken, Kopiëren artikel
- Inkooporderregels in backorder
- Onderhoud HS-code / Customs code
- Onderhoud taalcodes
- Overzicht dagstatistiek
- PowerPrint
- Powerall Werkbon App

2019 Versie v1909 september 2.32

- Afletteren grootboekmutaties
- Hoe lijn ik de uitgebreide machine verkoop teksten uit?
- Goedkeuren besteladvieslijst knop Import beschikbaar
- Projecten
- Wat is het verschil tussen verhuur en contracten?
- Hoe installeer ik een Powerall update? Opschonen verouderde back-ups

2019 Versie v1908 augustus 2.31

- Exporteren
- Hoe haal ik mijn nieuwe inkoopfacturen op?
- Hoe, wat kan ik ... m.b.t. wijzigen van korting op regelniveau?
- Vrijgeven verkooporder
- Wat betekent de ... status? nieuw

2019 Versie v19.07 juli 2.30

- Het menupad is verkort, zie bijv. ../#search-BRR.
- Artikelen, online info leverancier Sparex
- Hoe kan ik artikelen inlezen vanuit Excel in orders of offertes?
- Servicemelding aanmaken vanuit keuringsherinnering bijgewerkt en voorbeeld toegevoegd
- Verkoop prijsafspraken
- Webshop instructies

2019 Versie v1906 juni 2.30

- Artikelen, online info leverancier BartsParts
- Dossier CRM
- Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties?
- Power BI Dashboard nieuw
- Verhuur beschikbaarheidsplanning

2019 Versie v1905 mei 2.29

- Barcode scanner Memor X3
- CBS aangifte, bijgewerkt
- Incasso's
- bijgewerkt
- Download catalogus
- Wijzigen verhuurorder Huurstop

2019 Versie v1904 april 2.28

- Artikelen, online info leverancier
- Dossier, voorbeelden E-facturen met bijlagen
- E-Inkoopfacturen inboeken E-facturen inboeken (eenvoudig)
- E-inkoopfacturen (geavanceerd)

FAQ Crediteuren

FAQ Machinisten App

Hoe maak ik een nieuwe Werkbon App gebruiker aan?

2019 Versie v1903 maart 2.27

- Contract Nieuwe contract aanmaken
- Periodieke facturering contract
- Onderhoud contractsoorten

Dossier

Opmaak e-mail berichten/facturen  in .html formaat bij SMTP

E-inkoopfacturen (geavanceerd)

Boeken Onderhanden Werk (OHW)

2019 Versie v1902 februari 2.26

- Goederenmatching nieuw Overzicht matchingmutaties.
- Hoe werk ik de APK of Tachograaf datum bij?
- EPC bestand importeren
- Powerall CRM app
- Proforma facturen
- Verwerken artikelmutaties
- Werkorders en reiszones

2019 Versie v1901 januari 2.25

- Goederenmatching
- Overnemen beginbalans
- Bevestigen offerte
- Bevestigen verkooporder
- Documentbeheer per relatie
- Handleiding 3, Opticon OPN2006 scanner troubleshooting met de Werkbon App
- Filiaal communicatie
- Powerall Werkbon App
- Hoe, wat kan ik m.b.t. de dynamische bestelhoeveelheid? methode Seizoen

2018

2018 Versie v1812 december 2.24

- Verwerken koersverschillen
- Nieuwe relatie aanmaken, wizard relatie
- Wat wordt er gewijzigd bij een BTW-tarief wijziging?
- Inlezen/verwerken bankafschriften
- Hoe stel ik WiFi op de Datalogic Memor X3 scanner in?

2018 Versie v1811 november 2.23

- Beheer servicemelding
- FAQ Goederenmatching
- FAQ Werkbon App
- Hoe maak ik een kopiebon of order? nieuw kopiëren korting
- Hoe kan ik bij zoek machines bepaalde machines niet laten zien?
- Instellingen CRM procesnotities
- Periode / maand afsluiting bijgewerkt, kolom doel toegevoegd.
- Onderhoud selectiecodes (artikelen)
- Powerall Connect beheer services

2018 Versie v1810 oktober 2.22

- Afmelden verhuurorder
- Hoe mail ik de uren naar een personeelslid?
- Hoe maak ik een nieuwe verhuurgroep aan?
- Hoe werkt de besteladvieslijst?
- Instellingen servicemeldingen per proces
- Verkoopfactuur boeken (handmatig)

2018 Versie v1809 augustus/september 2.21

- Hoe, wat kan ik m.b.t. de minimum en maximum voorraad?
- Hoe, wat m.b.t. als de bestelhoeveelheid verschilt?
- Hoe, wat kan ik m.b.t. de dynamische bestelhoeveelheid?
- Hoe installeer ik Powerall Werkstation / Planbord / Outlook Inbox?
- Hoe verwijder / disconnect ik een gebruiker(sessie)?
- Hoe wijzig ik het uurtarief?
- Hoe werkt partnershop order doorfacturering (Kramp / Granit)?
- Welke instellingen zijn van belang bij het installeren van Powerall Connect?
- Instellingen bedrijf
- Inlezen/verwerken bankafschriften
- FAQ Artikelen
- FAQ Gebruikers
- FAQ Powerall Connect foutmeldingen
- Urenregistratie touchscreen
- Werkorder gereed melden / vrijgeven

2018 Versie v1807 juli 2.20

- Tips & Tricks zie kopiëren en zoeken in regels.
- Hoe, wat kan ik ... m.b.t. artikel afschrijvingen?
- Hoe repareer of wijzig ik de Powerall werkstation installatie?
- Afrekenen verkoop- of werkplaats factuur
- Artikel verwijzing aanleggen
- Artikel voorraad corrigeren
- FAQ Inkoop(orders)
- Klantcombinatie relaties
- Machine consignatie
- Powerall Schaduwkopie nieuw
- Schade taxatie
- SMS / WhatsApp versturen werkgereed
- Nieuwe relatie aanmaken zie dossier
- Verkoopprojecten
- Verwerk prijswijzigingen
- Verhuur machine aanmaken

2018 Versie v1806 juni 2.19

- Hoe, wat kan ik ... m.b.t. artikel afschrijvingen?
- FAQ Elektronische Part Catalogus (EPC)
- FAQ Case New Holland (CNH)
- Mailmerge
- FAQ VA-Keur
- Zoeken in Catalogus

2018 Versie v1805 mei 2.18

- Integraties
- Hoe, wat kan ik ... m.b.t. PostNL?
- FAQ Machines, tellerstanden
- Zoekvensters van de basistabellen / modules: Er kan overal (in elke kolom) gezocht worden, op de ingegeven filtertekst.

Versie v1804 april 2.17

- FAQ Apps
- 
- Doorverwerken facturen
- Hoe, wat m.b.t. Eigen keuring?
- Gebruikersrollen
- Machine omschrijvingen
- Webshop afhandeling met iDEAL / Wero, zie Hoe, wat kan ik ... m.b.t. Webshoporders?

Versie v1803 maart 2.16

- E-facturen: E-facturen inboeken (eenvoudig) en E-facturen
- Hoe, wat kan ik ... m.b.t. het verkoopproces?
- Verhuur

Versie v1802 jan/feb 2.14/2.15

- Instellingen documentbeheer
- Machines / Offerte
- Hoe, wat kan ik ... m.b.t. de voorraadaansluiting / artikelprijsmutaties?
- Mijn Powerall / web portal en Catalogi

2017

Versie v1703 / v1704

- Basis, onderhoud en stamgegevens / Instellingen modules / processen
- CRM / verkoopondersteuning
- Inkoop / Verkoop
- Kassa
- Magazijn
- Service
- Veelgestelde vragen FAQ
- Hoe werkt SMS?

Versie v1702

- Dashboard online / Basisprincipes / Algemeen / Financieel
- Woordenlijst

Versie v1701

- Online Release notes

- Wat is de historie van de online documentatie?

---
## Hoe pas ik de achtergrond PDF's aan van de  facturen etc.?

# Hoe pas ik de achtergrond PDF's aan van de facturen etc.?

De PDF's die achter de facturen etc.(als achtergrond) afgedrukt worden, staan in een aparte map namelijk PDFTMPL. Deze map PDFTMPL staat in de Datamap van de betreffende administratie.

Om deze aan te passen, doorloopt u de volgende stappen:

1. Ga in het Systeemmenu naar Systeembeheer > Onderhoud administraties. Tip: Kies voor de knop Wijzigen en Kopieer (via Rechtermuis > Kopiëren) de Datamap en plak deze in de verkenner.
2. Open de Windows verkenner (op de server of de hoofdcomputer waarop Powerall Connect geïnstalleerd is).
3. Ga naar de data map en open de map PDFTMPL.
4. Kopieer de oude pdf's naar een BACKUP map bijv. met de naam Old.
5. Voeg de nieuwe PDF lay-outs toe met dezelfde naam, zoals deze in de map stonden. Bijv.

De nieuwe PDF achtergrond lay-outs zijn gekoppeld.

#### FAQ

Hoe werkt de achtergrond PDF?

Dat gaat automatisch. Bijv. als je een E-factuur stuurt met de lay-out G dan kijkt Powerall Connect staat er in de map PDFTMPL een IIN73-G dan wordt die pdf als achtergrond gekoppeld.

- Er is dus geen koppeling ingesteld bij onderhoud lay-outs.

Wanneer wordt dit gedaan?

Als er nieuw briefpapier gebruikt gaan worden, dan moet de achterliggende of achtergrond PDF's vervangen worden.

Op welke zoektermen kan ik zoeken?

Rechts boven kan op onderstaande termen gezocht worden:

#### PDF-template, pdftemplate en pdf template

Belangrijk: De naam van de PDF bestanden moet precies hetzelfde zijn.

---
## Hoe voeg ik een dossier template toe, voor Relaties of Artikelen of Machines?

Bij het Onderhoud relaties, Artikelen of Machines, tabblad Dossier, is het mogelijk om een dossier automatisch aan te maken d.m.v. de kopieer-knop .Bij de betreffende administratie moet bij de Windows map DOSSIER de map TEMPLATE eenmalig aangemaakt worden.

#### Template map aanmaken

Opmerking: Bij Onderhoud administraties moet het dossier pad ingevuld zijn bij Dossier relaties, artikelen en machines, bijv. voor relaties C:\Beversoftware\PW\\DOSSIER\R\.

Eénmalig moet er een template map TEMPLATE voor Relaties, Artikelen of Machines aangemaakt worden. Om dit te doen doorloopt u de volgende stappen:

1. Open Windows Verkenner.
2. Ga naar de hoofdmap van de relatie- artikelen of machinedossier, van de betreffende administratie.bv C:\Beversoftware\PW\\DOSSIER\R\
3. Maak hierin een nieuwe map aan.
4. Noem deze map TEMPLATE.

In deze map komen de standaard dossier templates te staan.

#### Dossier template vullen

De standaard template map moet gevuld zijn. Om dit te doen, doorloopt u de volgende stappen:

1. Open Windows verkenner (Windows toets + R).
2. Ga naar de map TEMPLATE in Relatie, Artikelen of Machines.bv C:\Beversoftware\PW\\DOSSIER\R\
3. Kopieer de benodigde bestanden of documenten naar deze map.

Al deze bestanden kunnen met één druk op de knop gekopieerd worden naar een (nieuwe) relatie, artikel of machine.

#### Kopiëren of aanmaken (nieuwe) map vanuit template map

Om de standaard template gegevens te kopiëren, doorloopt u de volgende stappen:

1. Ga naar: | Onderhoud artikelen | Onderhoud machines | Onderhoud relaties | | --- | --- | --- |
2. Ga naar tabblad Dossiers.
3. Kies voor de knop (Kopiëren). Onderstaand scherm verschijnt:
4. Kies voor de knop Ja.

De template gegevens zijn gekopieerd naar de betreffende dossier map.

- Dossier

---
## Hoe voeg ik voor Relaties of Machines een sjabloon toe?

Bij het raadplegen van relatie- of machinegegevens is het mogelijk om deze gegevens te exporteren naar een Word document d.m.v. de knop Naar Word.

- Bij de betreffende administratie moet in de Windows map DOSSIER de sjablonen eenmalig aangemaakt worden.

#### Sjabloon aanmaken

Eenmalig moet er een sjabloonmap TEMPLATES voor Relaties en Machines aangemaakt worden. Om dit te doen doorloopt u de volgende stappen:

1. Open Windows Verkenner.
2. Ga naar de hoofdmap van de relatie- of machinedossier, van de betreffende administratie. bijv. C:\Beversoftware\PW\A01\DOSSIER\M\
3. Maak hierin een nieuwe map aan.
4. Noem deze map .

In deze map komen de sjablonen te staan.

#### Sjabloon toevoegen

Om een sjabloon toe te voegen, doorloopt u de volgende stappen:

1. Ga naar de map TEMPLATES in map Relatie of Machines.bijv. voor Relaties C:\Beversoftware\PW\A01\DOSSIER\R\TEMPLATES
2. Download het standaard sjabloon:
3. Sjabloon Machines
4. Sjabloon Relaties
5. Open het Word sjabloon en/of sla het bestand op in de bovengenoemde map TEMPLATES.

of maak in deze map een eigen sjabloon aan.

Het sjabloon document mag een vrije naam hebben, zolang dit maar een .docx document is.

#### Afdrukken naar Word

In Powerall Connect kunt u dit sjabloon gebruiken om gegevens naar Word te exporteren. Om dit te doen doorloopt u de volgende stappen:

1. Ga naar Opvragen relaties of F6 of Ga naar Opvragen machines (MO) of F8.
2. Kies voor de knop Naar Word. Het scherm Print naar Word verschijnt.
3. Selecteer het sjabloon en bij Relaties het eventuele Contactpersoon en/of Afleveradres optioneel.
4. Kies voor de knop Afdrukken.
5. Als het document gereed is, wordt deze geopend in Microsoft Word. Het programma Word licht op, in de Windows taakbalk.
6. Open dit Word document en indien nodig pas het aan of druk het af.

Nadat de gegevens in de gekozen Word-sjabloon zijn ingevoegd, wordt het document opgeslagen in de relatie- of machinespecifieke dossier, in de submap MSWORD.

Het document krijgt dezelfde naam als het sjabloon met het revisienummer tussenhaakjes als achtervoegsel.

- Word layout of Sjabloon aanmaken
- Welke Offerte/Machine/Relatie bladwijzers kan ik gebruiken in Word?

---
## Hoe zoek ik in deze documentatie iets op?

#### Zoeken documentatie

In deze Powerall Connect documentatie kan gemakkelijk gezocht worden op een onderwerp of zoekterm, of een gedeelte hiervan. Om te zoeken, doorloopt u de volgende stappen:

1. Ga naar het tekstvak Zoeken rechtsboven.
2. Het is ook mogelijk om in diverse onderwerpen te zoeken. Hierbij wordt gezocht op de term artikelen in de machine hoofdstukken, wat minder resultaten geeft. Belangrijk: Vergeten niet om de filter weer te resetten naar Alle bestanden.
3. De volgende onderwerpen zijn doorzoekbaar: Artikelen Zie ook
4. Barcode-app Zie ook
5. CRM-app Zie ook
6. Inleiding Zie ook
7. Grootboek Zie ook
8. Overzichten Zie ook
9. Machines Zie ook
10. Relaties Zie ook
11. Werkbon-app Zie ook
12. Instellingen Zie ook
13. Vul hier de zoekterm in, bijv. . Tip: Bij het zoeken op meerdere termen, zet deze tussen aanhalingstekens bijv. "Onderhoud artikelen".Om op meerdere zoekwoorden te zoeken gebruik is het volgende mogelijk• AND of + beide of &(beperkter resultaat)• OR een van beide termen.
14. Druk op de Enter toets of klik op Zoek/Vergrootglas knop .
15. In het volgende scherm, selecteer het betreffend onderwerp.

Informatie over het geselecteerde onderwerp wordt weergegeven.

#### Woordenlijst

Daarnaast kan ook gezocht worden in de Woordenlijst, deze geeft een korte omschrijving van de gebruikte termen of afkortingen in Powerall Connect.

Om te zoeken, doorloopt u de volgende stappen:

1. Ga naar de Woordenlijst linksboven.
2. Vul bij het Tekstvak zoeken, de zoekterm in.
3. Druk op Enter.
4. Selecteer het betreffend woord.

De uitleg wordt weergegeven.

#### Release notes

In de release notes kan ook gezocht worden op bepaalde woorden. Dit kan per module en/of per versie of in alle versies. Voor meer info zie Wat is nieuw in Powerall Connect?.

---
## Welke regels gelden voor deze  help documentatie?

# Welke regels gelden voor deze help documentatie?

#### Algemeen

De hoofdstukken van Powerall Connect Help zijn als volgt ingedeeld:

- Er wordt een algemene beschrijving gegeven per bedrijfsproces, met vaak een overzicht van het algemeen bedrijfsproces of schema.
- Vervolgens wordt het bedrijfsproces verdeeld in stappen d.m.v. sub hoofdstukken. Per stap wordt er beschreven wat er gedaan/uitgevoerd moet worden.
- Waar nodig is een schermafdruk of plaatje toegevoegd ter verduidelijking.
- Tenslotte wordt er een link naar de gerelateerde onderwerpen weergegeven.

#### Online Help

De nieuwste versie van de Powerall Connect documentatie wordt automatisch weergegeven als u een internetverbinding heeft en als update notificatie ja is ingesteld bij de gebruiker.

Druk op F1 als u meer wilt weten over een bepaald venster in het programma. De Help-pagina voor het venster of module dat u op dat moment bekijkt, wordt dan weergegeven.

#### Lay-out

Boven en onderaan elke scherm wordt, in de turquoise balk, het zogenaamde Kruimelpad of Breadcrumbs weergegeven, bijv. :

Hiermee is het duidelijker waar u zich bevindt. Ook kunt u middels dit systeem eenvoudig terugspringen naar eerder bezochte pagina's of niveaus, en 'tussenliggende' pagina's of niveaus overslaan, door er op te klikken met de muis.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

#### Modules

Bij deze documentatie is er vanuit gegaan dat alle modules beschikbaar zijn.

#### Navigatie menu

Aan de linkerzijde staat het in-/uitklapbaar navigatie menu. Deze is gekoppelde met de rechter- en linkerzijde.

Opmerking: De hoofdstukken gemarkeerd met een * zijn nieuw of vernieuwd sinds de laatste wijziging.

#### Overzichten, lijsten of prints

Alle standaard overzichten worden kort beschreven en de belangrijkste kenmerken worden hierbij genoemd.

#### Standaarden

In deze documentatie worden de benamingen gebruikt, zoals die voorkomen in Powerall Connect. Het gebruik van knoppen wordt als volgt weergegeven:

Toevoegen of aanmaken nieuw item:

- Kies voor de knop Opvoer.

Afdrukken gegevens:

- Kies voor de knop Afdrukken. (link)

Een programma kan op de volgende manieren weergegeven worden:

- Ga naar Kopie facturen (oud)
- Ga naar Onderhoud layouts (BPO).
- Ga naar Opvragen artikelen (AO) of F7.
- Ga naar Onderhoud artikelen (ABA), tabblad Voorraad. Linken zijn blauw gekleurd, d.w.z. een koppeling waarop geklikt kan worden, naar een onderwerp.

Het menupad ABG (Artikelen > Basisgegevens > Onderhoud artikelgroepen) wordt vermeld achter de programma naam.

Een scherm 'naam' wordt conform Powerall weergegeven bijv. Opvragen artikelen.

Tip: Hier worden handige Powerall Connect tips weergegeven.

Opmerking: Hier worden opmerkingen weergegeven, die waardevolle informatie bevatten.

Belangrijk: Dit vereist uw aandacht. Wij adviseren om dit niet over te slaan, het gaat om belangrijke informatie.

Let op! Hier worden belangrijke waarschuwingen weergegeven. Het negeren hiervan kan de werking van bepaalde programma's schaden!

#### Veld help

Bij verschillende schermen is een veld help beschikbaar, hierin wordt in het kort het veld beschreven. Deze velden worden in alfabetische volgorde weergegeven.

Hieronder een uitleg van de velden van scherm Onderhoud gebruikers:

| Kop |  |
| --- | --- |

| Gebruikersnummer | Het unieke nummer van de gebruiker. |
| --- | --- |

| Gebruikersnaam | De (uitgebreide) naam van de gebruiker. |
| --- | --- |

| Loginnaam | De naam waarmee ingelogd wordt in Powerall Connect. Deze naam verschijnt ook bij de programma informatie onderin het venster en op de overzichten. De loginnaam is maximaal 20 tekens.- De loginnaam mag geen spatie of ongeldig karakter / tekens zoals :" \ / \| ? * bevatten. |
| --- | --- |

| Loginmethode | De optie/methode waarmee ingelogd wordt:- Wachtwoord (Standaard)- Active directory, hierdoor is het niet meer nodig om het wachtwoord per gebruiker in te stellen en loopt dit mee met het domein. |
| --- | --- |

| Nieuw wachtwoord | Het nieuwe wachtwoord, geldt alleen bij login methode wachtwoord.- NB. Nadat een gebruiker ingelogd is, wordt het wachtwoord gehashed of versleuteld. Het wachtwoord kan max. 20 lang zijn. |
| --- | --- |

| Autorisatie | De autorisatiecode, zie Onderhoud autorisaties.- De autorisatie geldt voor alle administratie(s) waar de gebruiker toegang voor heeft.- Autorisatie Z geldt o.a. voor Hoe herstart ik de Service Host? |
| --- | --- |

| Update notificatie ontvangen | Optie voor update melding van Powerall Connect:- Nee (standaard)- Ja, de gebruiker krijg een melding boven in de menubalk, zie ook Hoe zie ik dat er een nieuwe versie van Powerall Connect is? |
| --- | --- |

| Menu 3.0 | Optie voor Menu 3.0. In het menu kan deze aan- of uitgevinkt worden, deze instelling wijzigt dan mee.- Ja (standaard) - Nee |
| --- | --- |

| 'Details': |  |
| --- | --- |

| Administratie | De administratie(s) waarvoor de gebruiker geautoriseerd is of toegang heeft. |
| --- | --- |

- | Administratie: | (onderstaand geldt per administratie. | | --- | --- | | Standaard magazijncode | De standaard magazijncode van de gebruiker, zie Onderhoud magazijnen. Deze wordt automatisch gevuld waar nodig is.Het volgende geldt bij gebruik van bedrijflocaties: - 900 Selectie van bedrijflocatie.- >900, wordt de betreffende bedrijfslocatie (magazijn) gebruikt.Deze locatie wordt rechtsboven getoond i.p.v. de administratienaam. | | --- | --- | | Standaard personeelscode | De standaard personeelscode van de gebruiker. Deze wordt automatisch ingevuld, bijv. bij Selecteren servicemeldingen en controle uren registratie.Bij gebruik van de Powerall CRM app en Werkbon app is deze code verplicht. Zie ook Onderhoud personeelscodes. | | --- | --- | | Gebruikersrol 1 t/m 5 | De rollen waarvoor de gebruiker geautoriseerd is. Maximaal zijn er vijf rollen mogelijk.- Zie ook Gebruikersrollen.- Voorwaarde: bij de betreffende administratie moet Gebruik gebruikersrollen op Ja staan. | | --- | --- |

#### Vragen

De belangrijkste en meest voorkomende vragen zijn opgenomen bij Veelgestelde vragen FAQ.

#### Woordenlijst

De belangrijkste begrippen of afkortingen die gebruikt worden in Powerall Connect worden hierin weergegeven.

#### Zoeken

In deze documentatie kan gemakkelijk (rechtsboven) gezocht worden op bepaalde woorden, zie Hoe zoek ik in deze documentatie iets op?

Tip: Bij zoeken in de help krijgen de zoektermen een kleur. Om deze markering/kleur te verwijderen gebruik de markeer-knop linksboven.

Hierin worden de onderwerpen weergegeven, die verband houden met dit onderwerp.

- Hoe zoek ik in deze documentatie iets op?
- Aan de slag

---
## FAQ Taal

In dit hoofdstuk staan de meestgestelde vragen over de taal in Powerall Connect.

Powerall Connect

Is het mogelijk om Powerall of het Planbord in een andere taal weer te geven?

Ja, dit is mogelijk, in de Engelse of Franse taal.

- Vanaf de stabiele versie 3.28 is dit ook mogelijk in de Duitse taal.Voor het Planbord is dit nog niet mogelijk.
- De standaard taal is Nederlands. Tip: Neem hiervoor contact op met de helpdesk of verkoopafdeling.

Hoe is de relatie aan een taal gekoppeld?

- Aan de relatie is een landcode gekoppeld, aan de landcode weer de taalcode.
- | Taalcode | De taalcode wordt gebruikt om artikel / machineomschrijvingen of factuur e.d. in een andere taal weer te geven.- 1 Nederlands (standaard)- 2 Engels - (Frans / Duits) | | --- | --- |

Hoe kan ik artikelen

of machines
in een andere taal op - of weergeven?

- Bij artikelen of machines is het mogelijk om meerdere talen te gebruiken. Hiervoor moet bij Instellingen artikelen (BIA), tabblad Scherminvoer, Meertalige artikelomschrijving op Ja staan.
- De artikelen kunnen in de betreffende taal worden ingegeven, zie Artikelomschrijvingen (ABA).
- De machines kunnen in de betreffende taal worden ingegeven, zie Machine omschrijvingen (MBB).

Hoe geef ik een andere of nieuwe taal(code) op?

Het is mogelijk een taalcode in gebruik te nemen of toe te voegen.

- Bij Onderhoud taalcodes (BTA) kan een extra taalcode worden opgegeven.
- Koppel de landcode bij Onderhoud landen (BTL) aan deze taalcode.

Tip: Neem hiervoor contact op met de helpdesk of verkoopafdeling.

- Bij het opslaan of verzenden van een email, in de Previewer, wordt de titel van het bestandsnaam in de juiste (klant) taal weergegeven, vanaf versie 3.29. Dit geldt bij een Bevestiging, Pakbon, Leverbon, Offerte, Inkooporder, Factuur of Kassabon, bij D/E/F/N.

Apps

Is het mogelijk om de Powerall CRM App of Werkbon App in een andere taal weer te geven?

- Ja, dit is mogelijk, in de Engelse of Nederlandse taal, zie: FAQ CRM App Via de instellingen.

FAQ Werkbon App

- Via de standaard taal van het apparaat / device.

Vanaf versie 3.29 is dit ook mogelijk in het Duits.

Er wordt er van uitgegaan dat de administratie in de betreffende taal opgesteld is.

Tip: Neem hiervoor contact op met de helpdesk of verkoopafdeling.

#### Vertalen / Translate / Traduire

Klik hier voor meer informatie over de stappen:

Om teksten de vertalen, doorloopt u de volgende stappen:

1. Ga naar DeepL.
2. Kopieer de tekst (of gebruik CTRL+A).
3. Plak de tekst (of gebruik CTRL+V).

De tekst is vertaald.

Opmerking: To translate these Powerall Connect help texts into english/français, please use the following link: DeepL.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Onderhoud taalcodes

---
## Hoe autoriseer ik een gebruiker voor een module, menu of tabblad?

Dit kan door het toekennen van een gebruikersrollen aan de gebruiker.

- Voor meer informatie zie Gebruikersrollen.

Is het mogelijk om een gebruiker te autoriseren voor bepaalde tabbladen?

Ja, dit is mogelijk voor de volgende programma's:

- E-inkoopfacturen (geavanceerd) (KE)
- Onderhoud relaties (BRR)
- Opvragen artikelen of F7
- Opvragen machines (MO) of F8
- Opvragen relaties F6

Een tabblad wordt met de volgende opmaak weergegeven bijv. Algemeen.

- Onderhoud autorisaties

---
## Hoe verwijder / disconnect ik een gebruiker(sessie)?

Om de verbinding of sessie met een (niet actieve) gebruiker te verbreken, doorloopt u de volgende stappen:

1. Ga in het systeemmenu naar Systeembeheer > Actieve taken. De actieve gebruikers/taken worden weergegeven. 2. Selecteer de gebruiker. 3. Kies voor de knop Verwijderen. 4. Kies voor de knop Ja. De betreffende taak van de gebruiker geannuleerd of beëindigd.

Opmerking: Het tabblad Verbindingen is alleen beschikbaar in de Thin-Client en niet bij de lokale runtime. • De openstaande verbinding m.b.t. SYSPATH (Systeembeheer) kan niet verwijderd worden.

#### Sessie afsluiten werkstation

Op een werkstation lukt het vaak niet om een taak te deactiveren.

- De melding Fout bij verwijderen: record gelockt verschijnt dan. In dit geval was er nog een actieve verbinding.

Let op! Controleer altijd of de gebruiker nog actief / aan het werk is, anders kan er bijv. een boeking abnormaal beëindigd worden.

Om deze te verwijderen, doorloopt u de volgende stappen:

1. Ga naar tabblad Taken en controleer Proces-ID van de gebruiker, in de kolom PID.
2. Ga naar tabblad Verbindingen. Opmerking: Controleer Gebruiker en/of Start datum/tijd. NB In bovengenoemd geval was er de vorige dag niet goed uitgelogd, bij het afsluiten.
3. Zoek daar hetzelfde Proces-ID op.
4. Kies voor de knop Verwijderen. De melding Aanvraag voor het verwijderen van de verbinding is verzonden! verschijnt.
5. Kies voor de knop OK.
6. Ga naar tabblad Taken.
7. Verwijder de taken met het zelfde Proces-ID één voor één. Powerall Connect controleert stap 5 en 6 automatisch bij het inloggen.

De niet actieve taken zijn verwijderd.

---
## FAQ Gebruikers

In dit hoofdstuk staan de meest gestelde vragen m.b.t. gebruikers.

- Hoe autoriseer ik een gebruiker voor een module, menu of tabblad? - Hoe verwijder / disconnect ik een gebruiker(sessie)? - Hoe maak ik een nieuwe Werkbon App gebruiker aan? - Wat doe ik bij de melding: 'Het maximaal aantal gebruikers is ingelogd'? 
- Onderhoud autorisaties
- Gebruikers

---
## Wat kan ik allemaal doen met een overzicht?

Het is mogelijk om elk overzicht, lijst of print, af te drukken of te exporteren naar PDF of Excel, (Word) of te e-mailen.

In de previewer (afdrukvoorbeeld) is het ook mogelijk om een overzicht te e-mailen of te exporteren naar:

- Af te drukken op een printer, zie Afdrukken.
- Excel Standaard volledige Excel integratie bij elke overzicht.
- Word (niet standaard)
- Standaard PDF optie, inclusief mailfunctie. 1. Het scherm Rapport opslaan als PDF verschijnt. 2. Kies voor de knop Verder. 3. Het PDF bestand verschijnt in de PDF-reader.

#### FAQ

- Bij het opslaan of verzenden van een email, in de Previewer, wordt de titel van het bestandsnaam in de juiste (klant) taal weergegeven, vanaf versie 3.29. Dit geldt bij een Bevestiging, Pakbon, Leverbon, Offerte, Inkooporder, Factuur of Kassabon, bij D/E/F/N.

Opmerking: Bij het exporteren naar Excel kunnen, vooraf diverse export instellingen bepaald worden (bijv. welke velden, veldlengte, scheidingsteken, bestandstype en bestandspad).NB Bij overzichten met een datum zijn deze meestal t/m vandaag, pas indien nodig de datum t/m aan.

Klik hier voor meer informatie over het afdrukvoorbeeld:

Bij het bekijken van een overzicht of factuur in het afdrukvoorbeeld, geldt het volgende:

- Gebruik van de 'Mijn documenten' map om PDF, Excel of Word document op te slaan.
- Bij mailen kan het e-mailadres geselecteerd of direct ingegeven worden.

Bonnen, facturen en offertes:

- Gebruik van titel van het aanroepende programma als voorgestelde bestandsnaam.
- Bij een bon, factuur, offerte of bevestiging wordt het betreffende nummer meegegeven in de bestandsnaam of de e-mail omschrijving.

Het e-mail adres is alleen beschikbaar bij de module E-factuur uitgaand (debiteuren).

Als de Previewer verschijnt, wordt er in de ADM map een tijdelijk bestand aangemaakt.

- Na het sluiten van de previewer wordt dit bestand verwijderd.
- Bij Annuleren, tijdens het 'builden' van de previewer, blijft dit bestand staan, en wordt de volgende keer overschreven.

Is het ook mogelijk om het e-mail adres niet in te vullen?

Bij Instellingen bedrijf, tabblad Algemeen kan de instelling E-mailadres vullen schermvoorbeeld hiervoor gebruikt worden.

- | E-mailadres vullen schermvoorbeeld | Optie voor het vullen van het vullen van het E-mail adres in het schermvoorbeeld of Previewer:- Ja (standaard)- Nee het emailadres wordt niet standaard gevuld. Dit voorkomt dat een e-mail per ongeluk naar het verkeerde adres verzonden wordt. | | --- | --- |

Welke e-mailadressen verschijnen hierbij?

Dit zijn de e-mail adressen van de relatie van het Tabblad Contacten.

Wat is er verbeterd in laatste wijziging van de Powerall Connect overzichten?

De basis en belangrijkste overzichten zijn aangepast:

- Alle basis - en belangrijkste rapporten zijn gemoderniseerd.
- Lettertype is aangepast.
- Bedragen zijn voorzien van duizendtal notatie.
- In de voet regel staat het programma, versie, datum, gebruiker, bedrijfsnaam en bladzijde.

- Bedrijfsnaam 1 staat in de voettekst.
- Bedrijfsnaam 2 staat rechtsboven in de koptekst.

Klik hier voor meer informatie over een voorbeeld:

- Overzicht BTW-codes

- Zie ook
- Afdrukken

- Instellingen - wat je moet weten

---
## Wat zijn de nieuwste Powerall Connect functies?

Op het Bever/ Powerall Event zijn de volgende functies worden gedemonstreerd:

- Hoe, wat m.b.t. scan en herken? Mogelijkheid om feedback te geven op een ingescande pdf bon of factuur, vanaf versie 3.21. Hoe werkt de feedback functie? Het is mogelijk om een reactie of feedback te geven op het ingescande document, bijv. als een factuurbedrag niet klopt, vanaf versie 3.21. Om dit te doen, doorloopt u de volgende stappen: 1. Druk op de regel Klik hier om feedback te geven. Rechts verschijnen de Herkende waardes. 2. Corrigeer de Juiste waarde, indien nodig. 3. Markeer de betreffende waarde, d.m.v. een rode rechthoek, op het PDF. 4. Kies voor de knop Versturen. 5. De pop-up De feedback is verzonden verschijnt. Kies voor de knop OK. 6. De tekst Feedback verstuurd verschijnt.
- Hoe werkt WhatsApp? nieuw vanaf versie 3.20
- Hoe, wat m.b.t. de betaallink QR-code op factuur
- Machine en GPS tracker nieuw
- Selecteren machines nieuwe selectie op configuratie en element
- Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders?

#### Overige nieuwe en handig functies:

- Nieuwe bankkoppeling Ophalen van online bankgegevens Bankkoppeling

Hoe, wat m.b.t. scan en herken?(feedback-optie)

- Het digitaal verwerken van een bonnetje of factuur.

Peppol-integratie

- Het verzenden van E-facturen naar overheidsinstanties m.b.v. Peppol Hoe, wat m.b.t. Peppol

Betaallink op factuur

- Een QR-link op de factuur voor snellere betalingHoe, wat m.b.t. de betaallink

Whatsapp-integratie

- Nieuwe bericht service met WhatsApp Hoe werkt WhatsApp?

Digital order koppelingen

- Digitale inkooporder koppeling met diverse leveranciers

OCI bestelkoppelingen

- Voor werkorders online artikelen selecteren / bestellen Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders?

Picken Werkorder

- Voor grotere bedrijven die gebruik maken van orderpickenHoe werkt picken / gereserveerd bij werkorders?

Machine selectiescherm

- Handige extra selecties met inkoop / verkoopstatus Selecteren machines

GPS tracker voor machines

- Actuele GPS locatie en registratie van draaiuren Machine en GPS tracker

Artikelen met serienummers (kleine machines)

- Van artikelen met serienummer wordt een machine Hoe, wat m.b.t. kleine machines (vernieuwd)

Offerte typen (machineverkoop en reparatie)

- Handig voor het maken van offerte Nieuwe offerte aanmaken

Gebruik HS-code

- Naast CBS-code ondersteunen we ook de HS-code voor de Douane Onderhoud HS-code / Customs code

CBS- aangifte

- De CBS-aangifte a.d.h.v. de Powerall gegevens. CBS aangifte

Connect API / Powerall Connect API

- Koppeling webshop en Powerall data met externe applicaties
- Import van weborders

Online / RDW koppeling

- Ophalen machine gegevens bij RDW Nieuw machine aanmaken of kopiëren

Algemeen

- Nieuwe relatie aanmaken verbeterde Kvk opzoek functie, ook voor België
- Powerall Connect API integratie met bijv. Webshops / Exact e.d.

Financieel

- Bankkoppeling Hoe meld ik mij aan voor de bankkoppeling?

Hoe maak ik een creditnota?

Hoe, wat m.b.t. Peppol

Kassa

- Kassa pin terminal nieuw
- Invoeren kassabonnen nieuw functie toetsen bij afrekenen, bijv. F12. Nieuw incl. afronden bij Contant betaling op een apart grootboek.
- Een Machine of een Kleine machine kunnen afgerekend worden, vanaf versie 3..25.

Kassa De Betaal knop teksten zijn flexibel instelbaar. Er zijn 3 extra betalingsopties toegevoegd, totaal zijn er 5 knoppen optioneel.

Machines

- Hoe, wat m.b.t. kleine machines (vernieuwd) serienummer registratie
- Machine samenstelling
- Machine portaal vernieuwd

Order proces

- Overzicht orders (te picken) 2.0 Hoe werkt picken / gereserveerd bij werkorders?
- SendCloud Onderhoud expeditiecodes i.c.m. order picken

Werkorders / servicemelding

- Handige selectie / melding bij Werkorder(s): Selecteren werkorders De werkorder datum t/m. Standaard zijn de orders t/m vandaag zichtbaar. Hierdoor is het mogelijk om de orders van volgende  dagen / week standaard te zien.
- Nieuwe werkorder aanmaken Controle op dubbel gebruik van een servicenummer in een werkorder, als het servicenummer gewijzigd wordt.

Werkorder uren registreren nieuw bij Urenregistratie controle selectie op afdeling.

Verhuur 2.0 - nieuwe module -

- Verhuur / Contracten 2.0 Verhuur planbord 2.0
- Verhuur App

### Powerall Apps

Barcode & scanners

- Barcode scanner

Powerall Werkbon App

- Ritten
- Takenlijst
- Zoeken op meerdere termen bij relatie en artikel. Bijv. bij Materiaalverbruik het opzoeken van een artikel met de omschrijving moer en rvz.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

- Wat is de historie van de online documentatie?

---
## Welke Offerte/Machine/Relatie bladwijzers kan ik gebruiken in Word?

In Word is het mogelijk om Powerall Connect gegevens te gebruiken. Hiervoor worden zogenaamde bladwijzers gebruikt.

Onderstaande Powerall Connect gegevens kunnen weergegeven worden in Word:

### Offerte bladwijzers

Onderstaande bladwijzers gelden ALLEEN voor de Word offertes:

| Beschikbare Powerall Connect gegevens voor Word bladwijzers |
| --- |
| Bladwijzer offerte | Omschrijving | Opmerking |
| adresregel1 | Offerte adres: Straatnaam en nr. / Postbus nr. |  |
| adresregel2 | Offerte adres: Postcode /Plaatsnaam |  |
| offerteplaats | Plaatsnaam |  |
| datum | Offertedatum |  |
| naam1 | Relatie naam 1 |  |
| naam2 | Relatie naam 2 |  |
| offertenummer | - |  |
| referentie | - |  |
| offerterelatiecode | - |  |
| factuurrelatiecode | - |  |
| expeditietekst | Expeditietekst omschrijving |  |
| leveringsconditie | Leveringsconditie omschrijving |  |
| kvknummer |  |  |
| btwnummer |  |  |
| eorinummer |  |  |
|  |  |  |
| regelsbegin | Begin van offerte regels | Verplichte hulp bladwijzer. Noodzakelijk voor het onderscheiden tussen productregels en tekstregels. Voor correcte functionering hiervan moet een artikel “regelsbegin” in de offerteregels in Powerall opgenomen worden.Voorbeeld: Als men een “aanhef” regel in een offerte wil opnemen, moet deze voor de “regelsbegin” regel in Powerall geplaatst worden. De “aanhef” regel wordt dan voor deze bladwijzer geplaatst. |
| regelseinde | Einde van offerte regels | Verplichte hulp bladwijzer. Noodzakelijk voor het onderscheiden tussen productregels en tekstregels. Voor correcte functionering hiervan moet een artikel “regelseinde” in de offerteregels in Powerall opgenomen worden.Voorbeeld: Als men een “slot” regel in een offerte wil opnemen, moet deze na de “regelseinde” regel in Powerall geplaatst worden. De “slot” regel wordt dan na- en de product regels voor deze bladwijzer geplaatst. Commerciële tekst van de artikelen in de regeltabel worden ook bij deze bladwijzer geprint. |
| verkoper | Naam van de verkoper |  |
| verkopertelnr | Telefoonnr. van verkoper |  |
| verkoperfunctie | Functie van verkoper/personeel |  |
| vervaldatum | Offerte vervaldatum |  |
| totaalbedragexclusief | Offerte totaal excl. BTW |  |
| totaalbedraginclusief | Offerte totaal incl. BTW |  |
| betaalconditie | Betaalconditie tekst |  |
| Contactgegevens: |  |  |
| tav | Ter attentie van |  |
| aanhef | Aanhef |  |
| contactpersoon | Relatie contactpersoon | Volledige contactpersoon naam: Voornaam + voegsel + achternaam. NB Als geen contactpersoon bij de offerte gevuld is, worden de algemene relatiegegevens gebruikt. |
| contactmobiel | Mobielnummer van contactpersoon |  |
| contacttelefoon | Telefoonnummer van contactpersoon |  |
| contactemail | E-mail van contactpersoon |  |
| voornaam | voornaam contactpersoon |  |
| tussenvoegsel | tussenvoegsel contactpersoon |  |
| achternaam | achternaam contactpersoon |  |
| regelsbegin_fotos | Begin van offerte regels foto | Zelfde werking als de regelsbegin bladwijzer met als extra dat een artikelfoto na de commerciëletekst toegevoegd wordt (zie Foto’s toevoegen).Deze bladwijzer vervangt de regelsbegin bladwijzer. |
| regelseinde_fotos | Einde van offerte regels | Zelfde werking als de regelseinde bladwijzer met als extra dat een artikelfoto na de commerciële tekst toegevoegd wordt (zie Foto’s toevoegen). Deze bladwijzer vervangt de regelseinde bladwijzer. |
| Bladwijzers, alleen gebruik in een tabel: |  |  |
| regelkorting | Korting op de verkoopprijs |  |
| regelaantal | Geoffreerde aantal van het product | Bij bijv. 3 stuks. |
| regelaantalheel | Geoffreerde aantal van het product in hele getallen | Bijv. 3 |
| regelartikel | Artikelcode van het product |  |
| verkoopprijs | Product verkoopprijs |  |
| regelbedragexclusief | Totaalbedrag van de regel |  |
| regelomschrijving | De omschrijving in de regel van het artikel/product |  |
| regeluitgebreid | Uitgebreide omschrijving zoals deze ook wordt afgedrukt op een offerte. |  |
| commerciëletekst | Commerciële tekst van de artikel | De MS Word offertes tekst, zie Artikelomschrijvingen. |
| omschrcommtekst | regelomschrijving + enter + commerciëletekst |  |
| uitgebrcommtekst | combinatie van de bladwijzers  en . |  |
| artikelfoto | Foto van artikel |  |
| dossierfoto1 | Afbeelding 1 | Afbeelding uit dossier, in alfabetische volgorde |
| dossierfoto2 | Afbeelding 2 | Afbeelding uit dossier, in alfabetische volgorde |
| dossierfoto3 | Afbeelding 3 | Afbeelding uit dossier, in alfabetische volgorde |
| dossierfoto4 | Afbeelding 4 | Afbeelding uit dossier, in alfabetische volgorde |
| Machine offertes |  | Opmerking: Alleen te gebruiken in machinespecs |
| machineadvprijs | Adviesprijs machine |  |
| machinebouwjaar | Bouwjaar machine |  |
| machinebtwbedrag | BTW bedrag machine |  |
| machineconfig | Configuratie |  |
| machineelem_[elementcode] | Configuratie element | Een configuratie element kan ook los worden gelinked met een bladwijzer. Voordeel is dat de tekstkolom ervoor ook kan worden vertaald.Bijvoorbeeld: machineelem_M0052 Maximaal 25 elementen! |
| machinekleur | Kleur |  |
| machineoms1machineoms2etc. | Machine omschrijving 1 t/m 6 |  |
| machinesernr1machinesernr2machinesernr3 | Serienummer 1 t/m 3 | NV 'Machineserienummer 4' bestaat niet. |
| machineteller1machineteller2 | Tellerstand 1 en 2 |  |
| machinemerktype | Machine merk en type |  |
| machinenummer | Servicenummer |  |
| machinefoto1_machinefoto2_etc. | Foto’s 1 t/m 9 | De machine website foto's van tabblad Website.- Voor (standaard) formaat wijzen zie Gebruik foto's onderaan. |
| machinehoofdgroep | Hoofdgroep |  |
| machinesubgroep | Subgroep |  |
| machinegewicht | Gewicht |  |
| machinekenteken | Kenteken |  |
| machinemagazijn | Magazijn |  |
| machinemerk | Merk |  |
| omschrijving1 | Omschrijving1 |  |
| machineoverigeinfo | Overige informatie |  |
| machinetype | Type |  |
| serienummer | serienummer |  |
| servicenummer | servicenummer |  |
| tellerstand1 | Tellerstand 1 |  |
| machineverkoopeenheid | Verkoop eenheid machine |  |
| machinevloot | Vlootnummer |  |

Opmerking: Houd bij het gebruik van machinetemplate met het volgende rekening:• Er kan slechts 1 bladwijzer per cel in een tabel gebruikt worden.• Indien machineconfig gebruikt wordt moet dat in een rij gezet worden met 3 kolommen. In kolom 1 komt de elementomschrijving; in kolom 2 een dubbele punt; in kolom 3 de waarde.Wanneer er gewerkt wordt met machinespecs houd met het onderstaande rekening:• Machinespecs moeten voorafgaan en opgevolgd worden met een ENTER• Eén tabel is verplicht, 2 tabellen is niet mogelijk.• 2 machinespecs naast elkaar is niet mogelijk.• Verticale merged cells is niet mogelijk• Meerdere bladwijzers in 1 cel is niet mogelijk• Werken met bladwijzers in tekstblokken kan niet als je met machinespecs werkt.• Als het voorvoegsel npb (no page break) toegevoegd wordt aan de machinespecs-template (bijv. npbspeca.docx), wordt er geen nieuwe pagina toegevoegd.

### Machine bladwijzers

Klik hier voor meer informatie over machine bladwijzers:

Deze bladwijzers gelden alleen voor Opvragen machines (MO) bij de export Naar Word.

| Beschikbare Powerall Connect gegevens voor Word bladwijzers |
| --- |
| Machinegegevens | Omschrijving |
| servicenummer | - |
| merk | - |
| type | - |
| omschrijving1 | - |
| omschrijving2 | - |
| omschrijving3 | - |
| omschrijving4 | - |
| omschrijving5 | - |
| omschrijving6 | - |
| kenteken | - |
| hoofdgroep | - |
| subgroep | - |
| bouwjaar | - |
| serienummer1 | - |
| serienummer2 | - |
| serienummer3 | - |
| vlootnummer | - |
| gewicht | - |
| magazijnnaam | - |
| locatie | - |
| leveranciercode | - |
| leveranciernaam | - |
| inkooporderdatum | - |
| inkoopordernummer | - |
| inkoopfactuurdatum | - |
| inkoopfactuurnummer | - |
| leverancierreferentie | - |
| inkoopprijs | - |
| balanswaarde | - |
| eigenaarcode | - |
| eigenaarnaam | - |
| verkooporderdatum | - |
| verkoopordernummer | - |
| verkoopfactuurdatum | - |
| verkoopfactuurnummer | - |
| verkoper | - |
| adviesprijs | - |
| handelsprijs | - |
| verkoopprijs | - |
| tellerstand1 | - |
| tellerstand2 | - |
| eindgebruikercode | - |
| eindgebruikernaam | - |
| datumingebruik | - |
| einddatumgarantie | - |
| urenstandgarantie | - |
| websitecategorie | - |
| websitehoofdgroep | - |
| websitesubgroep | - |
| overigeinformatie | - |
| uitvoering | - |
| websitefoto001 | Voor foto resizen zie paragraaf foto |
| websitefoto002 | - |
| websitefoto003 | - |
| websitefoto004 | - |
| websitefoto005 | - |
| websitefoto006 | - |
| websitefoto007 | - |
| websitefoto008 | - |
| websitefoto009 | - |
| configuratie | Deze bladwijzer moet in de eerste cel van een tabel met 1 rij en 3 kolommen geplaatst worden. De configuratie wordt dan in deze tabel ingevoegd. Slechts de configuratie-elementen waar een vinkje bij 'Offerte' is gezet, worden ingevoegd. |
| configelem_ | Bladwijzer voor het invoegen van een specifieke configuratie-element. De elementcode moet op de plaats van  plaatshouder gezet worden, bijv. configelem_M0017 |

### Relatie bladwijzers

Klik hier voor meer informatie over de relatie bladwijzers:

Deze bladwijzers gelden alleen voor Onderhoud relaties bij de export Naar Word.

| Beschikbare Powerall Connect gegevens voor Word bladwijzers |
| --- |
| Relatiegegevens | Omschrijving | Relatie Contactgegevens | Omschrijving |
| relatiecode | - | contactvoornaam | De contact-bladwijzers worden slechts gevuld als in het scherm een contactpersoon gekozen is. |
| relatienaam1 | - | contactvoegsel | - |
| relatienaam2 | - | contactvoornaam | - |
| relatieadres | - | contactachternaam | - |
| relatiepostcode | - | contactaanhef | - |
| relatieplaats | - | contacttav | - |
| relatiepostbus | - | contactfunction | - |
| relatiepostbuspostcode | - | contactadres | - |
| relatiepostbusplaats | - | contactpostcode | - |
| relatieland | - | contactplaats | - |
| relatiecontact | - | contacttelefoon | - |
| relatiecontact | - | contactmobiel | - |
| relatiemobiel | - | contactfax | - |
| relatiefax | - | contactemail1 | - |
| relatievoip | - | contactemail2 | - |
| relatiemail | - | contactvoip | - |
| relatiewebsite | - |  |  |
|  |  |  |  |
| Relatie-Afleveradres gegevens | De afleveradres-bladwijzers worden slechts gevuld als in het scherm een afleveradres gekozen is. | Relatie Alflever gegevens 2 | Omschrijving |
| afleveradresnaam1 | - | afleveradrestelefoon | - |
| afleveradresnaam2 | - | afleveradresmobiel | - |
| afleveradresadres | - | afleveradresfax | - |
| afleveradrespostcode | - | afleveradresemail | - |
| afleveradresplaats | - |  |  |
| afleveradresland | - |  |  |

Tip: De bladwijzers zijn te zien in Word onder tabblad Invoegen > Bladwijzers.

### Gebruik bladwijzer in Word

1. De bladwijzersnamen worden altijd in kleine letters opgegeven en mag geen spatie bevatten, gebruik daarom het _ (onderstrepings)teken. 2. Binnen het bladwijzerbereik mag geen alineamarkering voorkomen, er kan dan een fout ontstaan bijv. .

### Gebruik foto's

Foto’s kunnen geresized (verkleind of vergroot) worden met behulp van een _W en een _H voor respectievelijk breedte en hoogte. Indien niet opgegeven, 'regelt' Microsoft Word dit. Voorbeeld: machinefoto1_W0160_H0120 (maten in pixels).

### Gebruik van dezelfde gegevens

Dezelfde gegevens kunnen meermalen gebruikt worden in een sjabloon. Als de relatienaam1 tweemaal voorkomt, voeg dan het _ teken toe aan de bladwijzernaam, bijv. relatienaam1_1 en relatienaam1_2.

- Hoe voeg ik voor Relaties of Machines een sjabloon toe?
- Word layout of Sjabloon aanmaken Word aanmaken tabellen

---
## Welke lay-out code wordt gebruikt voor...?

Onderstaande Layout / lay-out / formulier code worden standaard gebruikt:

| Module/Naam | Formuliercode | Omschrijving / voor een | Menupad | Programma |
| --- | --- | --- | --- | --- |
| Factuur | FMK | Normale factuur (standaard)Marge factuur, zonder BTWContante factuur | BIF | Instellingen Facturering, tabblad Uitvoer printer |
| Kassa | B A | KassabonKassabon op A4 | FKA | Onderhoud kassa's |
| Lever- of pakbon | P | Lever of Pakbonnen | BIF | Instellingen facturen, tabblad Uitvoer printer |
| Machines | OL | Machine ontvangenMachine leveringen | BIM | Instellingen machines, tabblad Print voorkeuren |
| Verkooporders | LP | LeverbonnenPakbonnen | BIV | Instellingen verkooporders, tabblad Uitvoer printer |
| Offertes | OV | OffertesOfferte bevestigingen | BIO | Instellingen offertes, tabblad Uitvoer printer |
| Inkooporders | O | Inkooporders | BII | Instellingen inkooporders, tabblad Uitvoer printer |
| Werkorders | W | Werkorders | BIW | Instellingen werkorders, tabblad Uitvoer printer zie opmerking |
| Contracten en verhuur | H | Contracten of verhuurGebruikt voor pak-, huur-, retourbon en factuur | BIV | Instellingen contract en verhuur, tabblad Uitvoer printer |
| Verhuur 2.0 | ABCO | ContractContractafsprakenOfferteOverdracht | HOV | Instellingen verhuur/contract, tabblad Algemeen |
| Servicemeldingen | A | Servicemeldingen | BIM | Instellingen servicemeldingen, tabblad Algemeen |

- Bij werkorders is de lay-out gekoppeld aan de werkordersoort.Als deze niet is gevuld, wordt Layout W gebruikt.
- Voor de factuur / Pakbon layout, kan per relatie bij Order (print) opties een afwijkende layout ingesteld worden.

- Lay-outs

---
## FAQ&#160;Lay-outs / Word

# FAQ Lay-outs / Word

In dit hoofdstuk staan de meestgestelde vragen over de Lay-outs in Powerall Connect en over het gebruik van Powerall Connect gegevens in Microsoft Word.

- Hoe voeg ik voor Relaties of Machines een sjabloon toe?
- Hoe geef ik de bladwijzerindicatoren weer in Word?
- Welke Offerte/Machine/Relatie bladwijzers kan ik gebruiken in Word?
- Welke lay-out code wordt gebruikt voor...?

Hoe kan het komen, dat de lay-out tekst niet goed afgedrukt wordt?

Controleer bij de lay-out van het programma, of de betreffende lettertype geïnstalleerd is op de pc.

- Dit kan voorkomen als er de layout geïmporteerd is.

Kan ik extra velden op mijn overzichten / lijsten / lay-out toevoegen?

Het is mogelijk om de lay-out aan te passen, zie Lay-out wijzigen.

- De bepaalde velden kunnen toegevoegd worden op de layout. Denk hierbij bijv. aan: het BTW-nummerGMB350 op overzicht relaties.
- de expeditie omschrijving op de werkbon.

Opmerking: Bij een update worden de standaard lay-outs weer teruggezet naar oorspronkelijke situaties.

Belangrijk: Als velden bij Onderhoud print velden toegevoegd zijn, deze s.v.p. doorgeven anders zijn deze bij een update van Powerall Connect weer kwijt. De velden worden dan toegevoegd aan het standaard set, zodat ze blijven staan.

Neem hiervoor contact op met de helpdesk om een bepaald veld toe te voegen.

- Lay-outs
- FAQ Offerte en Word

---
## Hoe geef ik de bladwijzerindicatoren weer in Word?

Als u een bladwijzer aan een tekstblok of item toewijst, wordt de bladwijzer tussen vierkante haken […] op het scherm weergegeven. Als u een bladwijzer aan een locatie toewijst, wordt de bladwijzer als een I-vormig symbool weergegeven. De haken en het invoegteken worden niet afgedrukt.

Opmerking: Standaard worden in Word de bladwijzerindicatoren niet weergegeven.

Om de bladwijzerindicatoren [ ] in Word weer te geven, doorloopt u de volgende stappen:

1. Ga naar tabblad Bestand.
2. Klik op Opties.
3. Ga naar Geavanceerd.
4. Blader of rol naar beneden.Bij Documentinhoud weergeven selecteer het selectievakje Bladwijzers weergeven.
5. Kies voor de knop OK.

De bladwijzersindicatoren worden weergegeven in Word.

---
## FAQ Apps

In dit hoofdstuk staan de meestgestelde vragen over de Powerall Connect Apps.

- FAQ CRM App
- FAQ Werkbon App
- FAQ Machinisten App

Wat doe ik bij de melding: 'Uw Licentie is verlopen' of 'Uw licentie is ongeldig'?

De huidige licentie is verlopen of ongeldig.

- Bij ongeldig, controleer de licentie key bij de administratie.
- Neem contact op met de helpdesk.

---
## FAQ Voorraad / magazijn

In dit hoofdstuk staan de meestgestelde vragen over de voorraad of magazijn module.

- FAQ Elektronische Part Catalogus (EPC)
- Hoe geef ik een gewicht op bij artikel of machine?
- Hoe, wat kan ik ... m.b.t. de voorraadaansluiting / artikelprijsmutaties?
- Hoe zoek ik in artikelen/bonnen/orders naar een bepaalde omschrijving?
- Het is mogelijk op Powerall te koppelen met een geautomatiseerd magazijnsysteem zoals Modula, Kardex of Händel lift, zogenaamde VLM's (Vertical Lift Modules).

Hoe maak ik een nieuw magazijn aan?

Om een nieuw magazijn aan te maken, ga naar Onderhoud magazijnen (ABM).

Hoe stel ik multimagazijn in?

1. Ga naar Instellingen artikelen (BIA), tabblad Koppelingen.
2. Bij Servicebussen (multimagazijn) wijzig instelling naar Ja. | Servicebussen / Multimagazijn | Optie voor het gebruik van meerdere - / multi magazijnen en/of servicebus(sen):- Nee (standaard), veld magazijn is grijs en het standaard magazijn.- Ja, het veld is invulbaar. | | --- | --- |

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Kan ik machines met een serienummer (o.a. kleine machines) gebruiken bij multimagazijn?

Ja dit is mogelijk, voor meer info zie:

- Wat is artikeltracering?

Waar kan ik het standaard magazijn invullen?

Het volgende geldt bij een standaard magazijn:

- Het standaard weergave magazijn wordt bij Instellingen artikelen tabblad Voorraad/Bestelmethodiek ingevuld.
- Per gebruiker instelbaaar.
- Per module instelling instelbaar
- Bij gebruik van bedrijfslocatie kan per locatie een eigen magazijn gekoppeld worden. Als deze gekoppeld is aan een gebruiker, wordt dit magazijn als standaard gebruikt.
- Bij het gebruik van servicemeldingen i.c.m werkorders geldt de volgende instelling: | Voorkeur werkordermagazijn | Optie het magazijn bij aanmaken van een werkorder, vanaf versie 3.24.- Monteur magazijn (standaard)- Hoofdmagazijn, standaard wordt het magazijn uit de instelling WO gebruikt.NB Bij het gebruik van Bedrijfslocaties, wordt altijd het werkorder magazijn van de betreffende locatie gebruikt. | | --- | --- |

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

#### Voorraad

- Hoe maak ik van een artikel een voorraad-artikel?
- Hoe werkt de Gemiddelde Inkoop Prijs (GIP) waardering?
- Wat is / betekent de ... voorraad?

Hoe maak ik de voorraad inzichtelijk van een andere administratie of vestiging?

Dit is mogelijk met - en zonder gedeelde bestanden.

Opmerking: Neem hiervoor contact op met de helpdesk.

Klik hier voor meer informatie over GIP / LIP verwerking i.c.m Matching  met moment van prijsbijwerken is 'matchen'.

Journalisering en bijwerken voor GIP en LIP met instelling 'moment van bijwerken' is 'matching'.

In deze methodiek wordt ontvangsten voor de GIP/LIP ook zo gejournaliseerd.

- Er wordt dus geen prijsverschil geboekt, ook niet bij een afwijkende ontvangst.
- Het gehele prijsverschil wordt geboekt bij de matching (op rekening voorraad).

Deze methodiek/instelling is bedoeld voor bedrijven waar de inkoper/ontvangst echt een beperkt beeld heeft van de daadwerkelijke prijs. Het heeft dan geen toegevoegde waarde al bij ontvangst te gaan boeken. Ook voor situaties waar bij ontvangst kostprijs geautoriseerd is.... dan weet je ook nooit (zichtbaar) wat er gebeurt, behalve als de inkoper alles heel 'strak' in de inkooporder heeft staan.

Kan ik bij order ingave een melding krijgen, als mijn artikel voorraad negatief loopt?

Ja, dit is mogelijk bij de volgende programma's, indien ingesteld:

- Nieuwe bon aanmaken
- Nieuwe verkooporder aanmaken
- Nieuwe werkorder aanmaken

Het scherm Voorraad details verschijnt als de voorraad negatief loopt bij de instelling Melding voorraadniveau is lijst.

- | Melding voorraadniveau | Optie voor melding (negatief) voorraadniveau: - Nee (standaard)- Ja, het scherm Waarschuwing voorraadniveau (voorraad > maximum voorraad) verschijnt.- Lijst, het scherm Voorraad details verschijnt. | | --- | --- |

Waar kan ik de minimum / maximum voorraad per magazijn invullen?

Dit is mogelijk per magazijn, per artikel bij:

- Onderhoud artikellocatie per magazijn (ALM).

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- FAQ Artikelen
- Magazijn
- Multimagazijn overboeken
- Onderhoud magazijnen
- Onderhoud magazijnlocaties
- Voorraad

---
## FAQ Artikelen

In dit hoofdstuk staan diverse vragen over artikelen.

- FAQ Catalogi & leveranciers
- FAQ Voorraad / magazijn
- FAQ Inkoop(orders)

- Hoe kan ik artikelen inlezen vanuit Excel in orders of offertes?
- Hoe maak ik van een artikel een voorraad-artikel?
- Hoe vraag ik een voorraadwaardelijst aan?
- Hoe, wat kan ik ... m.b.t. artikel afschrijvingen?
- Hoe, wat kan ik met de artikelstatus?
- Hoe, wat m.b.t. als de bestelhoeveelheid verschilt?
- Hoe, wat kan ik m.b.t. de dynamische bestelhoeveelheid?
- Hoe, wat kan ik m.b.t. de minimum en maximum voorraad?
- Hoe werkt de besteladvieslijst?
- Hoe werkt partnershop order doorfacturering (Kramp / Granit)?
- Wat is de ABC analyse?
- Wat is artikeltracering?
- Wat is het verschil tussen een artikellijst en samenstelling?
- Het is mogelijk op Powerall te koppelen met een geautomatiseerd magazijnsysteem zoals Modula, Kardex of Händel lift, zogenaamde VLM's (Vertical Lift Modules).

Berekening

*Hoe wordt de balanswaarde of boekwaarde van de artikelvoorraad berekend? De formule is: Balanswaarde = (aantal * ((kostprijs * verkoopeenheid) / prijseenheid)). Voorbeeld 1: - financiële voorraad = 10 - kostprijs = 12,50 - verkoopeenheid 1 - prijseenheid is 1 balanswaarde 125,00 = 10 * (12,50 * 1) / 1 Voorbeeld 2; je koopt olie per kan of vat in, en verkoopt het per liter. - financiële voorraad = 20 (liter) - kostprijs = 100,00 (per vat) - verkoopeenheid 1 (liter) - prijseenheid is 25 (liter) Balanswaarde 80,00 = 20 * (100,00 * 1) / 25 Hoe kan ik een alternatieve - of equivalentcode bij een artikel opgeven? Ja dit is mogelijk, als dit ingesteld is, bijv.: Opmerking: Deze velden zijn ook af te drukken op een artikellabel Overzichten Hoe druk ik een overzicht af met alle artikelfoto's? Het is mogelijk om een artikeloverzicht af te drukken met foto's. Om dit te doen, doorloopt u de volgende stappen: 1. Ga naar Overzicht artikel basisgegevens (AAB). 2. Bij alleen met artikelfoto selecteer Ja. 3. Bij layout selecteer B- Artikellijst met foto. 4. Kies voor de knop Afdrukken. Een overzicht van de artikelen met afbeeldingen of foto's wordt weergegeven. Opmerking: Alleen de eerste foto wordt afgedrukt. Welke label moet ik gebruiken bij een andere / bepaalde label rol? Op labelrollen, zit een etiket met de label omschrijving. 1. Hierbij een voorbeeld van z'n label: 2. Ga naar Onderhoud layouts (BPO). (zie Lay-out wijzigen) Layout F heeft het zelfde formaat, gebruik deze. Opmerking: Voor vragen raadpleeg de helpdesk. Belangrijk: Let op of je een PowerPrint of Zebra printer hebt. Omschrijving / extra tekst Wat gebeurt er als ik de artikelomschrijving wijzig? In de bestaande orderregels en productstructuur regels blijft de artikelomschrijving hetzelfde. Er wordt soms een extra tekst opgegeven bij de regels om iets te verduidelijken. - Indien nodig pas de omschrijving aan. - Als een artikel ingegeven wordt in de regels, krijg deze de actuele artikelomschrijving. Hoe kan ik een extra artikeltekst toevoegen? Het is mogelijk om een uitgebreide artikeltekst toe te voegen. Dit kan bij: - Artikelomschrijvingen Deze omschrijving wordt ook standaard afgedrukt op de factuur, bij de Bon tekstregel. Waar zie ik deze tekst? Deze omschrijving of tekst is o.a. zichtbaar: - In de orderregels bij de kolom Omschrijving, onder de knop drie puntjes . - Bij de Selecteren programma's onder de knop Details. - Op de factuur, bij de Bon tekstregel. Overige Hoe autoriseer ik de prijzen bij Opvragen artikelen? De bepaalde prijzen kunnen zichtbaar zijn of niet (alleen sterretjes). - Voor meer informatie zie: Autorisatie prijzen. Hoe wordt de gemiddelde levertijd berekend? De gemiddelde levertijd wordt weergegeven bij Onderhoud artikelen (ABA) en op tabblad Leverancier. Formule: Van alle ontvangsten van een artikel het totaal berekenen van ( aantal geleverd * aantal dagen tussen bestellen (inkooporderdatum) en leveren ) en dit delen door het totaal aantal ontvangen van dat artikel. Hierbij een voorbeeld van de berekening van de gemiddelde levertijd: | Ontvangst-nummer | Aantal geleverd | Aantal dagen tussen bestellen en leveren | Totaal aantal ontvangen | Gemiddelde levertijd | | --- | --- | --- | --- | --- | | 1000002 | 1 | 5 | 1 | (1x5) = 5 / 1 = 5 | | 1000020 | 1 | 12 | 2 | 5+ (1x12) = 17 / 2 = 9 | | 1000022 | 2 | 12 | 4 | 5+12+ 24 (2x12) = 41 / 4 = 10,25 | | 1000025 | 2 | 5 | 6 | 5+12+24+10(2x5) = 51 / 6 = 9 | Hoe komt het dat bij zoek artikelgroep* een *artikelgroep* niet weergegeven wordt?

- Controleer bij het zoeken via artikel, dat de artikelgroep de soort groep Artikel of Artikel/Machine heeft.
- Controleer bij het zoeken via machine, dat de artikelgroep de soort groep Machine of Artikel/Machine heeft.

*Hoe kan ik nieuwe kortingsafspraken van mijn leverancier inlezen? Zie Hoe lees ik nieuwe kortingsafspraken van mijn leverancier in? Hoe zie ik alle artikelen van een bepaalde leverancier? Om de artikelen van een bepaalde leverancier te zien, doorloopt u de volgende stappen: 1. Ga naar overzicht Artikelbasisgegevens (AAB). 2. Vul het de leverancier in bij vanaf en t/m. 3. Kies voor de knop Afdrukken. Alle artikelen worden weergegeven van deze leverancier. - Het is ook mogelijk om bij Zoek artikelen te filteren op Leverancier. Hiervoor is het nodig dat de leverancierscode bekend is. Wat betekent in de kolom Btb 'BO' of 'BR'? In de regels, rechts, kan bij de kolom BtB (Back to Backorder) BR staan. Dit betekent dat er een BestelRegel aangemaakt is, bij optie Centraal bestellen. - Als de bestelling geplaatst is, dan staat er op de plek van BR, VO of WO. BO betekent BestelOrder. Samenstelling of Structuur Hoe zie ik of een artikel een structuur-artikel is? Dit is mogelijk op meerder manieren: - Bij Opvragen artikelen of F7, tabblad Where used is te zien wat de structuur is van het artikel (snelst). - Bij Onderhoud artikelstructuren. Hoe ziet er een artikelsamenstellingen of assembly uit? ## Artikellijst samenstelling of assembly Hierbij een voorbeeld voor het samenstellen van een hydrauliekslang (HS) benodigdheden of reparatie. - Slang van een bepaalde diameter. - Huls die hierbij hoort. - Het structuur-artikel HS ziet er als volgt uit: Bij de keuze van bijv. artikel verschijnt het selectie scherm Artikel keuzelijst: 1. Optie A keuzelijst is nee: Dubbelklik op de artikelcode, in de regels. Het scherm artikelkeuze lijst verschijnt. 2. Selecteer het betreffend artikel. 3. Opmerking: Bij de kolom Afdruk factuur, is de optie Intern alleen toestaan bij tekstartikel in artikellijst. 4. Doe dit ook voor de andere artikelen. Optie b keuzelijst is ja: 1. Kies voor de knop Opslaan. 2. Powerall Connect maakt één regel aan met 'Hydrauliekslang geassembleerd' met daaronder de artikelen die zijn opgebouwd uit de betreffende onderdelen: 3. Geef de overige order gegevens in. 4. Kies voor de knop Einde order / bon. De gegevens zijn opgeslagen. Hoe ziet de artikelstructuur eruit? 1. Optie A keuzelijst is nee: Opmerking: Voordeel keuze is verplicht geen kans op fouten, er moet er een keuze gemaakt worden, nadeel keuze maken kost iets meer tijd 2. Optie B keuzelijst is ja: Belangrijk: Het aantal artikelcodes is hierbij verschillend, is meer een 'platte keuze' structuur. Opmerking: Voordeel snellere keuze, keuze is niet verplicht. Nadeel kans op mogelijke fouten. Voor meer informatie zie: Onderhoud artikelstructuren. Wat gebeurt er bij een wijziging in de productstructuur* of *samenstelling* met de verrekenprijs?

De inkoop- of verrekenprijs wordt wel/niet bijgewerkt bij Onderhoud artikelen (ABA), tabblad:

1. Bijgewerkt in tabblad Algemeen als er geen leverancier gevuld is in tabblad Leverancier.
2. Bijgewerkt in tabblad Algemeen en - Leverancier, als de interne leverancier is gevuld in tabblad Leverancier waarop bestel en prijsvoorkeur staan.
3. Bijgewerkt tabblad Leverancier, als de interne leverancier is gevuld in tabblad Leverancier, waarop geen bestel en prijsvoorkeur staan.
4. Niet bijgewerkt in tabblad Algemeen als er een externe leverancier als bestel en prijsvoorkeur is opgegeven.

De interne leverancier productie wordt opgegeven bij Instellingen projecten, tabblad Productie

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Artikelen Onderhoud artikelen
- Zoek artikelen

Audit trail

EPC bestand importeren

---
## FAQ Catalogi &amp; leveranciers

# FAQ Catalogi & leveranciers

In dit hoofdstuk staan diverse vragen over catalogussen.

*Hoe vraag ik een nieuwe catalogus aan? - Login op het Mijn Powerall / klantenportaal en vraag bij Prijslijsten de catalogus aan, zie Mijn Powerall / web portal, Prijslijsten. Kan ik een eigen prijslijst* importeren in Powerall Connect?

Ja, het is mogelijk om een eigen bestand te importeren. De inhoud van dit bestand moet dan beschreven zijn.

- Voor meer informatie zie Import eigen catalogus / prijslijst.

Hoe koppel ik een leverancier aan een catalogus, zodat ik de catalogus kan downloaden?

1. Ga naar Onderhoud catalogi (AGT).
2. Voeg de betreffende cataloguscode toe (via Opvoer of Wijzig).
3. Op tabblad Algemeen vul bij leverancier de betreffende leverancier in. Opmerking: Koppel de juiste artikelgroep en leverancier aan de catalogus
4. Kies voor de knop Opslaan.

De catalogus kan gedownload worden.

Waar kan ik meer informatie vinden over catalogi?

- Over leveranciers, zie Leverancierscatalogi
- Over het downloaden, zie Download catalogus.

- Catalogus & leveranciers

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## FAQ&#160;Elektronische Part Catalogus (EPC)

# FAQ Elektronische Part Catalogus (EPC)

### Importeren Elektronische Part(artikel) Catalogus (EPC) bestand

*Hoe importeer ik een EPC order? Het is mogelijk om diverse soorten EPC bestanden te importeren in een order. - Voor meer info zie EPC bestand importeren. ### Import EPC Waar stel ik de locatie in, om gegevens te importeren vanuit de webshop of bestelsysteem van leverancier? Zie bijv. Invoeren/wijzigen inkoop of werkorders bij de knop Import regels. - Selecteer éénmalig dit pad en het pad wordt opgeslagen. Wat doe ik bij de melding 'Import regels niet correct ingesteld*'?

Bij het importeren van inkooporder regels, is het mogelijk dat de volgende pop-up verschijnt:

Neem contact op met de helpdesk.

Wat moet er hierbij ingesteld zijn?

Bij Onderhoud catalogi (AGT), tabblad Import specificatie, moet bij EPC bestandsformaat het juiste bestandsformaat geselecteerd zijn.

| EPC bestandsformaat | Optie voor het EPC import bestandsformaat, incl. scheidingsteken en extensie:- Nvt (standaard) - AgcoNet (, csv)- Bulthuis (xml) *- CNH (, csv)- Granit webshop (; csv)- Kramp webshop (xml) *- Mechan (tab csv)- Yahama (tab csv)- Nettoprijzen (; csv). vanaf versie 3.0* = zelfde formaat. |
| --- | --- |

Daarnaast moet dit in te lezen bestand bovengenoemde formaat .csv of .xml bevatten.

- EPC bestand importeren

---
## Hoe geef ik een gewicht op bij artikel of machine?

Controleer bij Instellingen artikelen of het veld gewicht op Ja staat. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Instellingen artikelen (BIA).
2. Ga naar tabblad Scherminvoer.
3. Kies voor de knop Wijzigen.
4. Selecteer bij Gewicht Ja.
5. Kies voor de knop Opslaan.

Bij de artikelen en/of machines kan het gewicht opgegeven worden.

Opmerking: Bij CBS aangifte plicht is het gewicht en een CBS-code verplicht.

---
## Hoe kan ik artikelen inlezen vanuit Excel in orders of offertes?

#### Inleiding

Het is mogelijk om eigen / dummy artikelen in te lezen vanuit Microsoft Excel in orders of offertes, d.m.v. de EPC koppeling.

- Deze artikelcodes staan/komen niet in het artikelbestand, het zijn vrije artikelen.
- Vrije artikelen worden niet ondersteund op de matchingscontrolelijst, komen als onbekend artikel onder de bovenliggende ontvangst op de lijst te staan.

#### Voorwaarde

Een 'hulp' catalogus bijv. TES moet ingesteld worden, deze dient alleen voor de koppeling met EPC import-bestand.

Klik hier voor meer informatie over dit onderwerp:

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud catalogi (AGT).
2. Kies voor de knop Toevoegen.
3. Geef bij Cataloguscode  op. Met omschrijving .
4. Ga naar tabblad Import specificatie.
5. Bij EPC bestandformaat selecteer bijv. Granit webshop.
6. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

#### Inlezen artikelen

Als de artikelen in het bestand Inlezen_in_order.csv bestand staan, kunnen deze ingelezen worden in orders zie:

- EPC bestand importeren

#### Inkooporders & twee administraties

Het is ook mogelijk om een EDI-layout te gebruiken waardoor een klant tussen 2 administraties inkooporders, volgens bijgevoegd formaat naar een andere administratie kan sturen. Deze order wordt dan via bovengenoemde werkwijze geïmporteerd in een verkooporder.

- Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

#### FAQ

Hoe ziet een voorbeeld bestand eruit?

Klik op onderstaand artikel (dummy) bestand, om deze te downloaden:

- Inlezen.in.order.csv Puntkomma - gescheiden: Artikelnummer;Aantal;nvt;Artikelomschrijving

Inlezen.voorbeeld.AgcoNet1.csv

- Komma - gescheiden: Artikelnr,Aantal
- Hoe krijg ik als scheidingsteken een komma? Excel gebruikt standaard de puntkomma ; als scheidingsteken, om dit te wijzigen naar een komma, doorloopt u de volgende stappen: 1. Ga naar Configuratiescherm > Klok en regio / Land regio. 2. Kies voor de knop > Meer instellingen 3. Wijzig het scheidingsteken. 4. Kies voor de knop TOEPASSEN.

Waar kan ik dit voor gebruiken?

Bij diverse portals kunnen er .csv files gedownload worden van bijv. de benodigde onderdelen van een beurt.

- Deze moeten handmatig worden overgenomen op een werkorder.
- Met deze EPC koppeling kan het bestand ingelezen worden in de werkorder.

- Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders?

---
## Hoe maak ik van een artikel een voorraad-artikel?

#### Instellingen artikelen

Als er gebruik wordt gemaakt van een voorraad administratie, moet dit ingesteld zijn. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Instellingen artikelen (BIA).
2. Ga naar tabblad Koppelingen.
3. Kies voor de knop Wijzig.
4. Selecteer bij Gebruik voorraad Ja. Belangrijk: Neem contact op met de planning om dit in te richten.
5. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Belangrijk: Als er gebruik wordt gemaakt van andere modules met voorraadbeheer, moet dit per module ingesteld worden.

#### Onderhoud artikelen

Om van een artikel een voorraad-artikel te maken, doorloopt u de volgende stappen:

1. Ga naar Onderhoud artikelen (ABA).
2. Ga naar tabblad Voorraad.
3. Kies voor de knop Wijzig.
4. Selecteer bij Voorraad bijhouden Ja. Opmerking: Geef eventuele overige voorraadgegevens in, zoals minimum of maximum voorraad.
5. Kies voor de knop Opslaan.

Het artikel kan op voorraad geboekt worden.

---
## Hoe vraag ik een voorraadwaardelijst aan?

Het is mogelijk om een voorraadwaardelijst af te drukken. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Voorraadwaardelijst (ALW).
2. Maak een selectie.
3. Bij Prijs voorraadwaarde selecteer:Voorraadwaarde (standaard)
4. Verkoopprijs
5. Verreken(inkoop)prijs
6. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

#### FAQ

Tip: Sla de voorraadwaarde lijst bij elke periodewissel op als PDF bestand voor eventuele controle.

Welke berekeningen worden gebruikt?

De volgende berekeningen worden gebruikt:

- Voorraadwaarde; aantal x verrekenprijs = (voorraad)waarde
- Verkoopprijs; aantal x verkoopprijs = (verkoop)waarde
- Verreken(inkoop)prijs; aantal x verrekenprijs = (inkoop)waarde

Opmerking: Bij de huidige periode kan er verschil zijn in boven genoemde gegevens, als de voorraad herwaardering nog niet uitgevoerd is (zie gerelateerd onderwerp).• Het aantal is het aantal aan het einde van de periode, bij periodewissel.

Hoe kan het dat als ik een voorraadlijst afgedrukt met de optie 'nul artikelen printen' nee, dat er toch artikelen op de lijst waar de voorraad 0 is?

Dit is mogelijk als de herwaardering van bepaalde artikelen nog niet verwerkt is.

1. Ga naar Herwaarderen voorraadwaarde (GPV).
2. Verwerk de herwaardering

Vraag bovengenoemd overzicht opnieuw op.

- Hoe, wat kan ik ... m.b.t. de voorraadaansluiting / artikelprijsmutaties?

- Wat kan ik allemaal doen met een overzicht?

---
## Hoe werkt partnershop order doorfacturering (Kramp / Granit)?

Op diverse websites is het mogelijk om bijv. direct onderdelen van Kramp of Granit te bestellen. Deze bestellingen kunnen ingelezen en verwerkt worden in Powerall Connect.

Partnershop leveranciers:

- kramp.com/shop-nl geeft toegang tot het grootste assortiment technische onderdelen van Europa.
- granit-parts.nl, vanaf versie 3.22.

- Partnershop, onderdelen online vanuit de buurt. Klik hier voor meer info over een partnershop: Een partnershop is een samenwerking tussen twee bedrijven waarbij ze elkaars producten of diensten verkopen, bijvoorbeeld via een ‘shop-in-shop’, waarbij één partij commissie ontvangt op de partner verkopen.

Overige leveranciers

- Welke leveranciers integraties zijn er?

#### Partnershop order doorfacturering

Onderstaand een voorbeeld van zo'n inlog / proces.

- Een  bestelt op de website van uw  partnershop artikelen. Bijv. een loonwerker bestelt op de site van een LMB online onderdelen. of
- De partnershop stuurt een E-invoice naar de LMB of .
- De factuur wordt in de Inbox ingelezen en ingeboekt, zie E-facturen inboeken (eenvoudig) of E-inkoopfacturen (geavanceerd). Na Boeken verschijnt het scherm E-factuur inkomend verwerking. Bij verkooporder selecteer Nieuw / bestaand.
- Geef de relatie en ordertype in. Het speciale ordertype, door facturatie is vaak niet het standaard ordertype en wordt daarom niet standaard gevuld. Bij de instelling KOS, wordt de financiële groep automatisch gevuld en is verplicht.

Vervolgens kan het LMB  met één druk op de knop, deze doorbelasten aan de .

Met Partnershop / KOS

Het inkoopnummer komt in het veld Referentie te staan.

Er wordt rekening gehouden met 100% korting icm factuurregelcodevanaf versie 3.24.

Zonder KOS

Het voordeel hiervan is:

- De order behoeft niet meer handmatig worden overgenomen, dit scheelt tijd en geld.
- Kleinere kans op fouten.
- Bij instelling KOS / partnershop: Artikelen worden niet meer van de voorraad afgeboekt.
- De bestel artikelcode wordt in de kolom klantreferentie weergegeven.

#### Artikel KOS

Het artikel  is een normaal artikel, zonder voorraad. De (financiële) artikelgroep is hierbij belangrijk voor de doorboeking in de financiële administratie.

Opmerking: Het is mogelijk om bij de doorfacturatie van de verkooporderregels, de artikelen niet meer van de voorraad af te boeken. • Neem contact op met de planner om dit in te stellen.

Als artikel  nog niet aanwezig is, verschijnt de melding:

- Artikelcode doorfacturatie niet gevuld bij Instellingen verkooporders.

#### FAQ

Welke Powerall Connect modules zijn hierbij vereist?

De volgende Powerall Connect modules zijn nodig bij het proces doorfacturatie inkoopfacturen:

- E-factuur Inkomend
- Verkooporders Basis

#### EDI UOM Eenheden

Welke eenheden UOM (Unit Of Measurement) gebruikt Kramp bij EDI?

| UOM | Omschrijving / Afkorting | EDI (Engels) |
| --- | --- | --- |
| FLE | Fles * | BOTtle |
| DOO | Doos | BOX |
| BUN | Bundel * / BUN | BUN |
| KAN | Kan | CAN |
| STU | Stuk / Stuks / STU | EA |
| KGM | Kilogram * | KG |
| KIT | Kit * | KIT |
| LTR | Liter / LTR | LTR |
| MM | Millimeter * / MM | MM |
| MTR | Meter / MTR | MTR |
| PAK | Pak | PAC |
| PAA | Paar | PAI |
| ROL | Rol | ROL |
| SET | Set | SET |
| VAT | Vat / DRUM | DRU |
| ZAK | Zak | BAG |

* zijn toegevoegde eenheden.

- Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders?

---
## Hoe zoek ik in artikelen/bonnen/orders naar een bepaalde omschrijving?

Om informatie te zoeken in de artikel-, bon- of (verkoop)order omschrijving(en), doorloopt u de volgende stappen:

1. Ga naar Informatie artikelen (ABI).
2. Geef een selectie op: Relatiecode, datum vanaf, status of artikelcode.
3. Geef de omschrijving / tekst bevat in.
4. Bij Zoeken in selecteer Alle of maak een andere selectie.
5. Kies voor de knop Selecteer.
6. Indien aanwezig, worden de artikelgegevens weergegeven. Selecteer de regel.
7. Kies voor de knop Details.
8. De bon details worden weergeven, zie ook: Bon / orderdetails

Opmerking: In de uitgebreide tekst-velden wordt er ook gezocht.

- Zoek artikelen

---
## Wat is artikeltracering?

#### Doel

Door artikeltracering is het mogelijk om een artikel beter te traceren door het toekennen van een uniek nummer / serienummer (SN) aan een artikel.Met behulp van deze nummers is het mogelijk om te traceren:

- Waar artikelen vandaan komen (productieserie leverancier).
- Welke artikelen in welk eindproduct verwerkt zijn (intern).
- Waar artikelen naartoe zijn gegaan (klant).

#### Werkwijze

Bij een ontvangst van een artikel wordt er aan ieder artikel een SN toegekend.

- Bij Boeken goederenontvangst wordt het serienummer ingegeven en gekoppeld aan de betreffende verkooporder(s) indien van toepassing.
- Dit artikel wordt dan bijv. voorzien van een label met dit SN.

Bij afgifte / verkoop van dit artikel wordt dan het SN geselecteerd en opgeslagen.

- Als bij een verkoop het artikel niet voorradig is, kan dit artikel op de normale wijze besteld worden (via en BtB-koppeling).

#### FAQ

Hoe zit het met het crediteren van serienummer gedragen artikelen?

Artikelen met een serienummer worden gecrediteerd via een creditnota, het serienummer komt dan weer op voorraad.

Waar kan ik artikelcodes met tracering of serienummers zien?

Om de serienummers te bekijken en/of te wijzen zie:

- Onderhoud artikeltracering (ABT)

Wat is het verschil tussen Lot- en Serienummers?

Overeenkomsten:

- Gebruikt voor (voorraad/verkoop) tracering van (een) artikel(en).
- Gebruikt voor terugroepacties (productiefout, garanties).
- Vastgelegd op moment van ontvangst en afgifte.

Verschillen:

- Lotnummer voor een serie artikelen, serienummer voor één specifiek artikel.
- Lotnummer vaak voor grondstoffen en halffabricaten (productieproces), serienummer voor een geproduceerd eindproduct.
- Lotnummer kan verkocht zijn aan meerdere klanten, serienummer altijd maar aan één klant.

Welke smaken zijn er bij het gebruik van serienummers?

De volgende artikel smaken zijn er bij het gebruik van een serienummer met of zonder machine:

| Smaak | Machine adm. 3.0 | Soort artikel | Gebruik tracering | Voorraad | Machine aangemaakt | Opmerking |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | - | Normaal | Nee | - | Nee | Geen SN |
| 2 | - | Normaal | Ja | - | Nee | Geen servicenummer zichtbaar |
| 3 | Ja / Nee | Machineverkoop | Ja | Ja (verplicht) | Ja | Kleine machine 3.0 SN overgenomen |
| 4a | Nee | Machineverkoop | Nee | Ja | Ja | SN wordt zelf ingevuld bij machine |
| 4b | Ja | Machineverkoop | Nee | Nee | Ja | idem |
| 5a | Nee | Machineverkoop | Nee | Ja | Ja | SN wordt zelf ingevuld bij machine |
| 5b | Ja | Machineverkoop | Nee | Nee | Ja | idem |

Werkt artikeltracering ook met meerdere magazijnen in een gedeelde omgeving?

Ja, het is mogelijk om artikeltracering te gebruiken bij meerdere magazijnen en in een gedeelde omgeving.

In welke modules wordt het gebruikt?

Artikel tracering geldt voor de modules:

- Verkoop Bonnen / facturering
- Offerte
- Kassa

Vanaf versie 3.27 werkorders, geldt dit alleen voor artikelen met een serienummer.

Op de Barcode app kan dit ook gebruikt worden, vanaf versie 3.27.

Welke transacties zijn er m.b.t. tracering / kleine machines?

De volgende kleine machine transacties / mutatietype zijn er:

- A= Afgifte (bon of verkoop)
- I = Inkoop *
- L = Retour leverancier of negatieve voorraad correctie / verwijderen SN

N = Correctie (-) Negatief , vanaf versie 3.27.

O = Ontvangst *

- of positieve voorraad correctie / toevoegen SN
- of Correctie (+) *, vanaf versie 3.27.

R = Credit

* is + / toename, rest is afname / -.

#### Instellingen

Hoe stel ik artikeltracering in?

Bij Instellingen artikelen (BIA), tabblad Beheer, kan bij het veld Gebruik artikeltracering de artikel tracering ingesteld worden.

- | Gebruik artikeltracering | Optie om artikel tracering te gebruiken:- Nee, (standaard)- Inkoopnummer- Lotnummer- Serienummer- Lot- en SerienummerNB Het vinkje Serienummers koppelen aan BtB verkooporderregel verschijnt bij Boeken goederenontvangst (AVO). | | --- | --- | | Voorloopcode lot-serienummer | Dit is de voorloopcode van het betreffend lot of serienummer. Het artikeltracing nummer is bijv. SN-0001001, waarbij SN- de voorloopcode is. | | --- | --- | | Volgnummer lotnummers | Dit is het actuele volgnummer. Bij een nieuw artikeltracering, wordt dit nummer met 1 verhoogd. Het artikeltracing nummer is bijv. SN-0001001, waarbij 0001001 het volgnummer is. | | --- | --- |

Bij Onderhoud artikelen (ABA), tabblad Algemeen, wordt de selectie bij veld Gebruik tracering bepaald bij Instellingen artikelen bijv. Serienummer.

- | Gebruik tracering | Optie om voor het artikel tracering toe te passen:- Nee (standaard)- ...nummer (afhankelijk van de selectie, zie veld Gebruik artikeltracering)NB bij de optie Serienummer is de knop Servicemelding beschikbaar, vanaf versie 3.21. | | --- | --- |

Opmerking: Neem contact op met de planner om dit in te stellen / hiermee te beginnen.

- Onderhoud artikeltracering
- Hoe, wat m.b.t. kleine machines (vernieuwd)

---
## Wat is / betekent de ... voorraad?

Hieronder worden de verschillende begrippen m.b.t. de voorraad uitgelegd.

| Voorraad | Omschrijving | Opmerking |
| --- | --- | --- |
| Plankvoorraad | Financiële voorraad - In bonnen/werkorders - Werkbon App (nog te verwerken)+ Ontvangen- aantal in kratten | Bijv.: |
| Economische voorraad | Financiële voorraad - Gereserveerd verkoop- Gereserveerd werkorder- In bonnen/werkorders- Werkbon App (nog te verwerken)- in kratten + In bestelling (definitief) + Ontvangen + In bewerking productie | Economische voorraad is de voorraad waarover een onderneming prijsrisico loopt. |
| Beschikbare (vrije) voorraad | Financiële voorraad- Gereserveerd verkoop - Gereserveerd werkorder - In bonnen/werkorders - Werkbon App (nog te verwerken) - Gereserveerd productie - in kratten + In bestelling voor orders (verkooporders/werkorders) + Ontvangen |  |
| Financiële voorraad | Het absolute financiële of werkelijke voorraad aantal.Bij goederenontvangst of correctie/telling wordt het aantal opgeboekt op deze voorraad en bij levering aan klant als de mutaties doorverwerkt zijn, wordt het aantal afgeboekt. | De financiële voorraad wordt ook gebruikt voor het berekenen van de balanswaarde. |
|  |  |  |
| In bonnen / werkorders | In bonnen en werkorders: Is de aantal/voorraad in bonnen en werkorders die nog niet gefactureerd zijn, maar ook de facturen en de vrijgegeven werkorders die nog niet doorgeboekt zijn. |  |
|  |  |  |
| In bestelling | Artikelen die in een inkooporder staan, en definitief besteld zijn (bestelbon is afgedrukt en nog niet geleverd). |  |
| In bestelling (tijdelijk) | Artikelen die al wel in een inkooporder staan, maar nog niet definitief besteld zijn (er is nog geen bestelbon afgedrukt).+ de aantallen die in bestelregels staan, als hiermee gewerkt wordt. |  |
| In bestelling voor werkorders | Aantal artikelen die vanuit een verkoop-/werkorder op een inkooporder gezet zijn. Deze artikelen zijn dus in principe al bestemd voor de verkoop of gebruik in de werkplaats. |  |
| In bestelling voor verkooporders | Aantal artikelen dat vanuit een verkooporder op een inkooporder staat/besteld is. |  |
| Ontvangen | Ontvangen aantal via Boeken goederenontvangst (AVO). |  |
| In kratten / colli | Het aantal dat gepickt is en in de krat of colli zit, vanaf versie 3.15. |  |
|  |  |  |
| Gereserveerd voor verkooporders | Aantal in kolom Besteld, d.w.z. 'gereserveerd' is op een verkooporder (nog niet geleverd). |  |
| Gereserveerd voor werkorders | Artikelaantal dat als backorder op een werkorder geregistreerd staat. |  |
| Toegekend aan verkoop-/ werkorders was: Gereserveerd backorders | Het aantal dat toegekend of gealloceerd is op een verkoop- of werkorder. Bij een VO de kolom Gereserveerd. Bij een WO de kolom Te picken instelling, vanaf versie 3.15. |  |
| Gereserveerd productieorder | Toekomstig gebruik. Artikelen die bestemd zijn voor een productieorder. |  |
|  |  |  |
| In bewerking productie | Aantal dat bezig is geproduceerd te worden (interne inkoop). |  |
| Correctie (nog te verwerken) | Voorraad correcties die nog niet verwerkt zijn. |  |
| Werkbon App (nog te verwerken) | Aantal op de Werkbon App dat bij Materiaalverbruik in de kolom Geleverd staat, in een openstaande werkorder, d.w.z. nog niet getekend zijn. | Als de WO verwerkt is, gaat het aantal naat In bonnen / werkorders |
| Werkbon App (gereserveerd) | Aantal dat gereserveerd is voor de Werkbon App. |  |

Opmerking: Op bovenstaande volgorde worden de diverse voorraden bij Onderhoud en Opvragen artikelen onder de knop Uitgebreid weergegeven.

---
## Wat is de ABC analyse?

Bij het afsluiten van de artikelperiode kan Powerall Connect op basis van de verkoophistorie een A, B of C codering van het artikel berekenen.

Klik hier voor meer informatie over de ABC analyse:

De ABC-voorraadanalyse wordt gedefinieerd als het proces om de inventaris te onderzoeken, om precies te bepalen hoeveel er moet worden onderhouden. Met de informatie die deze analytische aanpak oplevert, kunnen bedrijven belangrijke mogelijkheden identificeren om de voorraadniveaus te verlagen. De ABC-analyse is de meest voorkomende vorm van voorraadanalyse.

De voorraad/inventaris wordt verdeeld in drie hoofdcategorieën op basis van zijn strategisch belang. De 'A' zijn essentiële producten en vereisen een strikte controle*, terwijl de C-items de minst belangrijke producten zijn.

- Artikelen A: producten die belangrijk zijn en daarom een strikte controle* vereisen, met hoogste het servicesniveau.
- Artikelen B: producten van ondergeschikt belang, maar die nog steeds met een middelmatige mate van controle moeten worden beheerd.
- Artikelen C: minder belangrijke producten die een zo eenvoudig en eenvoudig mogelijke controle vereisen.
- * = De voorraad moet in de gaten gehouden worden, mag bijv. niet onder minimum voorraad komen. Het management moet ook geoptimaliseerde nabestelniveaus, veiligheidsvoorraden (waaronder het aanbod niet mag dalen) en een gemiddeld voorraadniveau vaststellen om de kosten te beperken.

Zodra de artikelen zijn gegroepeerd, zal elke categorie anders worden beheerd, omdat er meer aandacht en middelen moeten worden besteed aan de artikelen van klasse A, minder aan die van B en nog minder aan die van groep C.

Tip: Hierbij enkele tips om de waarde van uw voorraad analyse te maximaliseren: 1. Onderscheiden serviceniveaus, als sleutel tot het bereiken van het juiste service niveau. 2. Bepalen van optimale voorraadniveau. 3. ABC voorraad analyse om betere beslissingen te nemen. 4. Toekomstige voorraadverminderingskansen prioriteren. 5. Tracking en rapportage.

#### Instellingen

Standaard staat de ABC-Analyse bij periodewissel op Ja, bij Instellingen artikelen (BIA), tabblad Voorraad/Bestelmethodiek.

De volgende instellingen worden gebruikt:

- | Standaardcode ABC bij invoer artikel | De standaardcode ABC bij invoer artikel: - A (standaard) | | --- | --- | | Grens in dagen tussen klasse A en B | De grens in dagen tussen klasse A en B:- 365 (standaard) als artikel niet verkocht is, wijzigt de klasse van A naar B. | | --- | --- | | Grens in dagen tussen klasse A en C | De grens in dagen tussen klasse A en C: - 720 (standaard) als artikel niet verkocht is, wijzigt de klasse van A of B naar C. | | --- | --- | | Klasse na verkoop klasse C | De klasse na verkoop klasse C: - A (standaard) als artikel verkocht is, wijzigt de klasse van B of C weer naar . | | --- | --- |

Ook kan hierbij opgegeven worden na hoeveel dagen een artikel wisselt van A naar B of C.

#### Onderhoud of Opvragen artikelen

Bij het veld ABC-analyse is direct te zien, wanneer dit artikel voor het laatst verkocht is.

- | ABC-analyse | De A/B/C analyse van het artikel. Zie ook Wat is de ABC analyse?- leeg (standaard)- A (standaard: artikel is dit jaar verkocht:

---
## Wat is het verschil tussen een artikellijst en samenstelling?

#### Doel artikelstructuur.

Door het gebruik van een artikelstructuur is het mogelijk om artikelen snel in te geven bij een bon, order of project.

#### Onderhoud artikelstructuur

Bij Onderhoud artikelstructuren (ASO) wordt bij het structuur-artikelcode / artikel het veld soort structuur opgegeven:

- | Soort structuur | Optie voor structuur soorten:- Artikellijst (met keuzelijst)- Samenstelling, het structuur artikel mag geen voorraadhoudend artikel zijn.- Productstructuur (voor productie/projecten)- Machineverkooplijst, alleen icm gebruik machineadministratie 2.0 is ja.Opmerking: De structuur machineverkoop (artikel)lijst wordt gekoppeld aan een artikelgroep zie Onderhoud artikelgroepen. | | --- | --- | | Dynamisch | Vinkje voor een dynamische samenstelling instelling, bij soort structuur is samenstelling, vanaf versie 3.22.NB Artikelen kunnen toegevoegd worden voor deze samenstelling, bij- het scherm Artikel samenstelling (Dynamisch) of - de Barcode app op een Werkorder, door de artikelen te scannen,NB Een dynamische artikelstructuur heeft meestal geen regels. | | --- | --- |

#### Wat is precies het verschil?

|  | Artikellijst | Samenstelling | Machineverkooplijst | Productstructuur |
| --- | --- | --- | --- | --- |
| Aantal | Variabel | Variabel- Het aantal kan gewijzigd worden (prijs wordt herberekend indien van toepassing). | Het aantal is altijd 1, (maximaal 6 artikelen). | Variabel |
| Afdruk | Afhankelijk van instelling 'Afdruk factuur'. | Afhankelijk van instelling 'Afdruk factuur'. | Afhankelijk van instelling 'Afdruk factuur'. | Afhankelijk van instelling 'Afdruk factuur'. |
| Doel | Wordt gebruikt om als een soort hulp(lijst) om snel artikelen toe te voegen. | Vaste samenstelling, alle artikelen worden toegevoegd. | Machine verkoop, met daarbij komende kosten zoals, klaarmaak kosten, etc. | Vaste samenstelling, alle artikelen worden toegevoegd. |
| Dynamisch (nieuw) |  | Dmv vinkje, er kunnen dan artikelen toegevoegd worden op de samenstelling, vanaf versie 3.22. |  |  |
| Frequentie | Meest gebruikt | Specifieke gevallen | Gebruikt bij machine inkoop of verkoop. | Alleen bij projecten |
| Selectie | Alleen geselecteerde artikelen worden overgenomen. | Alle artikelen worden overgenomen op de order.Als het hoofdartikel verwijderd wordt op de order, worden alle regels verwijderd. | - Artikelen/kosten kunnen aan/- of uitgevinkt worden.- Bedragen kunnen aangepast worden. |  |
| Soort | Flexibel door selectie | Statisch of vast, geen selectie | Flexibel door selectie | Specifieke instellingen mogelijk. |
| Voorbeeld | - Een kleine beurt / APK- Bepaalde keuringen | - Actie pakket.- Gebruikt voor vaste werkzaamheden met altijd hetzelfde artikel aantal of verbruik.- Voor onderdelen die uit een vast aantal artikelen zijn samengesteld. | - Accessoire artikel- Bedrijfsklaar maken- Overige | Gebruikt voor Project module |
| Voorraad | Per artikel | Geen voorraad bij hoofdartikelBij Order picken 2.0 wordt er voor de onderliggende artikelen van een samenstelling geen rekening met de voorraadaantallen voor de kolom Gereserveerd in de verkooporder. Bij een artikellijst wel. | - Geen voorraad / Voorraad wel mogelijk afhankelijk van bedrijf bij verkooporder. - Geen voorraad artikel bij inkooporders mogelijk. | Per artikelmaar ook per structuur-artikelcode, zie *. |
| Mutaties | - Wijzigen alleen in order- Verwijderen 1 voor 1 handmatig. | - Wijzigen vanuit de order, via Rechtermuis > Wijzigen- Verwijderen, alles in 1x verwijderd. |  |  |
| Opmerking | Bij weborders, zijn subregels niet grijs. | Het hoofd artikel en sub-artikelen zijn grijs niet wijzigbaar. | De artikelomschrijving wordt gebruikt, niet die van de structuurregel. | De verrekenprijs kan berekend worden a.h.v. de samenstelling. |

- Bij samenstellingen staat het hoofdartikel op voorraad bijhouden nee en de onderliggende op ja.
- * Bij artikellijsten of productstructuren kan je het hoofdartikel wel op voorraad bijhouden ja zetten.
- De verkoopprijs is afhankelijk van de instelling Berekenen artikel VK-prijs ja of nee.

Voorbeelden

- Onderhoud artikelstructuren (ASO) zie FAQ.

---
## Hoe stel ik WiFi&#160;op de Datalogic Memor X3 scanner in?

# Hoe stel ik WiFi op de Datalogic Memor X3 scanner in?

Start de scanner op en sluit het Hoofdmenu af d.m.v. het kruisje rechtsboven.

1. Druk op Wi-Fi. Het scherm Summit Client Utility verschijnt.
2. Er moet een nieuw profiel aangemaakt worden als wifi nog niet ingesteld is op de scanner. NB Standaard is bij Actief profielDefault ingesteld.
3. Ga naar tabblad Profile:
4. Druk op Scan. Een overzicht van wifi netwerken verschijnt.
5. Selecteer het juiste wifi netwerk en druk op Configure.
6. Druk op Yes bij aanmaken nieuw profiel. Voer het Wifi  in.
7. Druk op OK.

Druk op Commit.

Ga terug naar tabblad Main.

Selecteer het wifi profiel wat zojuist aangemaakt is bij Active Profile.Dit profiel is actief

Druk op OK (rechtsboven).

#### Controleer status

Contoleer op het tabblad Status of er verbinding is met het wifi netwerk.De groene balk onderin geeft aan of er verbinding is, er moet bij IP een IP-adres staan (bijv. 172.16.12.202).

- Barcode scanner Memor X3

---
## Wat doe ik als NACK melding bij het uitlezen op de Opticon 1700/2700 scanner verschijnt?

#### Oplossing

1. Scanner uitzetten door op PW knop in te drukken.
2. Configuratie menu openen, door de knoppen 7 + 0 + PW ingedrukt houden.
3. Optie 2: Restart.
4. Scanner aanzetten: PW.
5. Optie 2: Parameters.
6. Op de 2e regel vanaf onder staat S/M/O/F : S dat moet F zijn.
7. Druk op ENT.
8. Maak er een F van door 3 x op de toets 8 te drukken.
9. Druk op ENT.
10. Druk daarna op Q1.
11. Herhaal stap 7 t/m 9 meerdere keren. Opmerking: Als er niets achter S/M/O/F: staat mag deze stap overgeslagen worden.
12. Nadat alle opties aangepast zijn (Q1 = ongeldige keuze) druk op CLR.
13. Druk daarna op Start Program.

De scanner start weer op en kan weer uitgelezen worden.

---
## FAQ Case New Holland (CNH)

In dit hoofdstuk staan de meest gestelde vragen m.b.t. Case New Holland.

Belangrijk: Bij CNH is parts locater alleen instelbaar voor dealers en regiodealers maar niet voor subdealers (bestellen onderdelen én machines via een andere dealer).

Hoe haal ik mijn nieuwe inkoopfacturen op (invoice inquiry)?

#### Voorwaarden

Bij Instellingen externe communicatie moet CNH invoice inquiry ingesteld zijn, anders is de knop Facturen ophalen niet zichtbaar bij E-Inkoopfacturen inboeken.

#### Invoice inquiry

Om nieuwe facturen op te halen, doorloopt u de volgende stappen:

1. Ga naarE-factuur inkomend (KEI).
2. Kies voor de knop Facturen ophalen.
3. Kies voor de knop Ja.

De nieuwe facturen worden opgehaald en toegevoegd.

Hoe exporteer ik mijn gerepareerde CNH machines?

Voor de klanttevredenheid registratie heeft New Holland elke maand gegevens nodig, betreft de verkoop en naverkoop van New Holland producten.

Om deze aan te vragen, doorloopt u de volgende stappen:

1. Ga naarExporteren gerepareerde machines CNH (MX?)
2. Geef betreffende gegevens in.
3. Kies voor de knop Export.

De gegevens zijn geëxporteerd.

Wat zijn de export instellingen CNH?

Bij de export instellingen kunnen specifieke groepen gekoppeld worden aan elkaar.

1. Ga naar Instellingen export CNH, (MX?).
2. Kies voor de knop Wijzigen. of Kies voor de knop Opvoer.
3. | Instellingcode | De instellingscode m.b.t. CNH exportgegevens:- Agriculture equipment - Repaired machines | | --- | --- | Selecteer bij CNH groep, de juiste hoofd- en subgroepen.
4. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Welke artikel informatie van CNH kan ik in Powerall Connect zien?

Het is mogelijk om online informatie van CNH op te halen.

- Voor meer informatie zie: Artikelen, online info leverancier, CNH.

- EPC is alleen beschikbaar voor CNH.
- Een digitale order is ook mogelijk voor CNH (GUA02 instelling mbt afleveradres.)
- Bij CNH PRIM komt het digitale-order-nummer in referentie.
- In deze documentatie wordt ook gesproken over EPC bij het importeren van een inkooporder in Powerall Connect, zie onderstaande link.

- digitale order
- E-Inkoopfacturen inboeken
- EPC bestand importeren

---
## Hoe controleer ik de verbindingsstatus of versie op CRM&#160;App?

# Hoe controleer ik de verbindingsstatus of versie op CRM App?

Om de verbindingsstatus te controleren van de Powerall CRM App, doorloopt u de volgende stappen:

1. Ga naar Instellingen.
2. Klik rechtsboven op het verbindingssymbool. Het volgende scherm verschijnt: De Powerall Connect - en PWS versie wordt hierbij weergegeven. Opmerking: Als de PWS versie nog niet bijgewerkt is, kan onderstaande pop-up voorkomen:

---
## Wat doe ik bij de e-mail melding 'Powerall CRM &lt;versie&gt; for IOS is now available to test'?

# Wat doe ik bij de e-mail melding 'Powerall CRM  for IOS is now available to test'?

Inleiding

Bepaalde klanten krijgen de nieuwste Beta test versie van de Powerall CRM App.

- Hiervoor wordt de app TestFlight gebruikt.

Als deze vrijgegeven wordt, krijgt men een e-mail, dat de nieuwe versie getest kan worden.

- Bijv.:

### Installeren beta versie

Om de nieuwste versie te installeren, doorloopt u de volgende stappen:

1. Ga (in de e-mail) naar de app TestFlight. In de mail druk op Test Flight link om deze te openen.
2. NB Na 90 dagen wordt deze (Build) verwijderd.
3. Kies voor de knop Volgende.
4. Kies voor de knop Installeer. of Open.

De CRM app wordt geopend, deze nieuwe versie is actief.

#### FAQ

Opmerking: De Beta versie van de Powerall CRM App is maximaal 90 dagen geldig. • Als deze verlopen is, moet de actuele versie geïnstalleerd worden.

Hoe ga ik weer terug naar de actuele versie van de Powerall CRM App?

Het is mogelijk om weer terug te gaan naar de actuele versie. Om dit te doen, doorloopt u de volgende stappen:

1. Installeer vanuit de app store opnieuw de Powerall CRM App, zie ook: FAQ CRM App

Wat doe ik bij de melding 'De beta van Powerall CRM is verlopen'?

De beta versie is verlopen, installeer de actuele versie. Om dit te doen, doorloopt u de volgende stappen:

1. Kies voor de knop OK.
2. Installeer vanuit de app store opnieuw de Powerall CRM App, zie ook: Installatie CRM app

- Installatie CRM app

---
## FAQ CRM

In dit hoofdstuk staan de meestgestelde vragen over de CRM module.

Opmerking: Het is mogelijk om CRM kenmerken van relaties te importen. Neem contact op met de planner om dit te doen.

Hoe kan een CRM-notitie afgehandeld worden?

- Open de betreffende notitie. Geef terugkoppeling door de notitie te vullen.
- Kies voor de knop Opslaan. Dus geen vervolgactie aanvinken.

De CRM notitie is dan afgehandeld.

- CRM / verkoopondersteuning
- Powerall CRM app

- FAQ CRM App

---
## FAQ Verhuur &amp; contract

# FAQ Verhuur & contract

In dit hoofdstuk komen de veelgestelde vragen over de Contract en Verhuur module.

- Hoe maak ik een nieuwe verhuurgroep aan?
- Wat is het verschil tussen verhuur en contracten?

Contract

#### Facturatie tellerstanden contracten

*Hoe factureer ik de tellerstanden van mijn contracten? Facturatie van tellerstanden kan op 2 manieren: - Gerealiseerde eenheden. - Geschatte eenheden. - Bij geschatte eenheden wordt rekening gehouden met de standen zoals ingegeven in de pop-up van de contractregel. Voor kortlopende (eenmalige) contracten moet dan ook het vinkje 'Definitief' aangezet worden. Dit geeft aan dat het contract ook werkelijk wordt beëindigd en niet stilzwijgend doorloopt. Op deze manier wordt het verschil tussen begin- en eindstand contract uit de pop-up gefactureerd. Verhuur Wat moet ik doen bij de pop-up Geen tarieven tabel gevonden. Voor: 0 uur.*

Bij het toevoegen van een verhuurorder krijg ik bovenstaande melding.

- Bij Onderhoud verhuurtarieven is de juiste machine hoofd/subgroep niet goed gekoppeld. Hierdoor is er nog geen tarief bekend.

Hoe kan ik van een al gefactureerde huurorder de verhuurdetails bekijken?

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Wijzigen verhuurorders (WH).
2. Geef het ordernummer in.

De gegevens verschijnen op het scherm.

Hoe komt het dat het vlootnummer niet wordt weergegeven, bij Selecteren verhuurorders?

Bij gebruik van een verhuurordersoort met de instelling Meerdere machines ja, wordt het vlootnummer niet weergegeven.

- Om de vlootnummers te zien:
- Kies voor de knop Details.

Is het mogelijk om meerdere machines uit verschillende verhuurgroepen op 1 order te zetten.

Ja, er kunnen verschillende machines, uit verschillende groepen op één order gezet worden. De verhuur wordt volgens de betreffende tarieven tabel berekend.

- Bij Onderhoud verhuursoorten moet bij deze verhuursoort de optie Meerdere machines koppelen op ja staan.

- Verhuur
- Contract

---
## Hoe werk ik de lopende orders bij, (m.b.t. NAW-gegevens)?

#### Inleiding

Klik hier voor meer informatie over de achtergrond:

De NAW -gegevens worden opgeslagen in de diverse orders. Als er een naam wijzigt in Onderhoud relaties moet deze naam ook gewijzigd worden in de betreffende lopende orders. Het volgende is hierbij mogelijk:

- In enkele stappen de NAW gegevens te wijzigen, zowel voor het factuuradres als ook voor het afleveradres.
- Er kan geselecteerd worden welke NAW-gegevens gewijzigd moeten worden. Standaard worden alleen de gewijzigde gegevens aangevinkt.

Alle openstaande orders zijn te zien, bij deze functie.

#### Wijzigen NAW -gegevens

Bij Onderhoud relaties verschijnt bij het wijzigen van de NAW-gegevens een melding met de vraag of de lopende orders bijgewerkt moet worden:

1. Kies voor de knop Ja. (of Enter). Het scherm Adreswijziging orderoverzicht verschijnt.
2. Bij een gedeelde administratie, verschijnt eerst het scherm Administratie overzicht. Selecteer hier de te wijzigen gegevens.
3. Opmerking: Bij alleen een wijziging van afleveradres-gegevens, wordt deze optie direct aangevinkt.
4. Vink de orders aan.
5. Kies voor de knop Bijwerken. Kies voor de knop Ja. (of Enter).
6. De gegevens zijn bijgewerkt, er verschijnt een melding VERWERKING GEREED.
7. Kies voor de knop OK. .

Optioneel Vink O Afleveradres aan.

- Opmerking: Alleen bij een factuuradres (postbus) verschijnt deze radio-knop Afleveradres.

Vink de orders aan, bijv.:

Kies voor de knop Bijwerken.

1. Kies voor de knop Ja.
2. De geselecteerde gegevens zijn bijgewerkt.

Doe dit (stap 5 en 6) ook als er verhuurorders aanwezig zijn:

- Vink O Retouradres aan.
- Vink O Doorzet-adres aan.

Sluit het programma af d.m.v. een kruisje.

Opmerking: Bovenstaande schermen verschijnt ook bij het wijzigen van de NAW-gegevens van de afleveradressen, in tabblad Afleveradressen.

Belangrijk: Er wordt geen rekening houden met de rollen-autorisatie. Als iemand een relatie mag wijzigen, mag hij ook alle NAW gegevens van alle orders bekijken/wijzigen.

#### FAQ

Hoe komt het dat ik gelijk naar het Afleveradres ga?

Als er geen factuurgegevens gewijzigd zijn, gaat het programma direct na het afleveradres (radio-knop).

Wat gebeurt er als een order bezet is?

Als een order openstaat op een ander scherm, verschijnt er een melding:

- Bon / order is geblokkeerd op ander scherm.
- Sluit de bon / order op het andere scherm of kies Nee.

Welke NAW-gegevens worden onderaan aangevinkt?

Alleen de NAW die gewijzigd zijn, worden onderaan aangevinkt, bij nieuw adres.

- Het is ook mogelijk om de 'niet gewijzigde' adres gegevens aan te vinken / wijzigen.

Wat wordt er precies allemaal bijgewerkt?

De volgende (order) gegevens kunnen wel/niet bijgewerkt worden:

| Bestand | Factuuradres | Afleveradres | Retouradres | Doorzetadres | Opmerking |
| --- | --- | --- | --- | --- | --- |
| Bonnen | Ja | Ja |  |  |  |
| CRM |  |  |  |  | Nee (Naam) |
| Inkooporders | Ja | Ja |  |  |  |
| Kassa |  |  |  |  | Nee (NAW) |
| Offertes | Ja | Ja |  |  |  |
| Servicemeldingen | Ja | Ja |  |  |  |
| Verhuurorders | Ja | Ja | Ja | Ja |  |
| Verkooporders | Ja | Ja |  |  |  |
| Werkorders | Ja | Ja |  |  |  |

De NAW gegevens zijn automatisch gekoppeld via de relatiecode bij:

- Contracten (afspraken)
- Projecten

Opmerking: Bij een gedeelde administratie, verschijnt eerst het scherm Administratie overzicht. Selecteer hier de te wijzigen administratie gegevens.

---
## Hoe controleer ik op dubbele relaties?

In verband met het voorkomen van dubbele relaties of vervuiling van het relatiebestand en eventuele fraude, is het mogelijk om bij het aanmaken van een relatie te controleren op dubbele gegevens.

Op de volgende velden of gegevens wordt gecontroleerd:

- KVK nummer
- IBAN nummer
- BTW-nummer
- Postcode+ huisnummer (geldt niet voor België)
- E-mailadres (algemene email bij relaties).

#### Instellingen

Bij Instellingen bedrijf (BIB), tabblad Relaties wordt de volgende instelling toegepast:

- | Controle op dubbele | Optie voor controle op dubbele relatiecodes bij: - Bij toevoegen (standaard) - Ja (bij toevoegen en wijzigen)- Nee (geen controle)Zie Hoe controleer ik op dubbele relaties? | | --- | --- |

#### FAQ

Toevoegen

Wat gebeurt er als ik een dubbele relatie opvoer?

Bij een dubbele relatie verschijnt er een melding. Hierbij doorloopt u de volgende stappen:

1. Er zijn een of meerdere relaties gevonden met deze dezelfde gegevens!
2. Kies voor de knop Ja. Het scherm Controle overzicht dubbele relaties verschijnt.
3. Controleer de klant.De rode velden bestaan al bij onderstaande klant(en)
4. Kies voor de knop Annuleer. Klant wordt niet opgeslagen, het vorige scherm verschijnt.
5. Kies voor de knop Opslaan. De dubbele klant wordt opgeslagen.

Wijzigen

Opmerking: Bij de instelling controle op dubbele bij toevoegen, wordt er niet gecontroleerd op dubbele gegevens bij wijzigen.

Wat gebeurt er als ik een dubbel veld in geef bij wijzigen?

Bij het wijzigen, doorloopt u de volgende stappen:

1. Bij het wijzigen van een 'dubbel' veld Adres en / of Postcode, verschijnt de melding:
2. Kies voor de knop Opslaan.De volgende melding verschijnt:
3. Kies voor de knop Ja.Het scherm Controle overzicht dubbele relaties verschijnt.
4. Controleer de gegevens, en kies voor Opslaan of Annuleer.
5. Bij Nee:Het scherm Dubbele gegevens gevonden verschijnt.

Wat gebeurt er als ik niets wijzig?

Als er niets gewijzigd wordt op het scherm en er wordt voor Opslaan gekozen, worden de gegevens op dubbele gecontroleerd. Als dit het geval is, verschijnt de melding:

- Er zijn een of meerdere relaties gevonden met deze dezelfde gegevens!

Hoe vraag ik een overzicht op van de dubbele relaties?

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Overzicht relaties (BRP).
2. Bij sorteren op kies Ontdubbelen.
3. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

Opmerking: Er wordt hierbij alleen gecontroleerd op huisnummer en postcode.

#### Nieuwe webshop klanten

Waar wordt nog meer op dubbele relatiegegevens gecontroleerd?

Als een nieuwe webshop klant of relatie toegevoegd wordt.

Er wordt gecontroleerd of de combinatie huisnummer en postcode al voorkomt in de relatiegegevens.

Voor meer informatie zie:

- Nieuwe relatie invoeren via webshop

- Onderhoud relaties

---
## FAQ Relaties

**FAQ Relaties In dit hoofdstuk staan de meestgestelde vragen over de relaties. - FAQ CRM - Hoe controleer ik op dubbele relaties? - Hoe, wat m.b.t. een actief / inactief relatie? - Hoe werk ik de lopende orders bij, (m.b.t. NAW-gegevens)? #### Onderhoud relaties Is het mogelijk om bij relaties, E-documenten** een standaard vinkjes in te stellen?

Ja het is mogelijk om bij Instellingen bedrijf, tabblad Relaties deze in te stellen:

- | E-documenten | Zie Onderhoud relaties, tabblad E-document | | --- | --- | | Standaard E-mail / PDF | Optie om standaard (allen) E-mail / PDF aan te vinken, bij een nieuwe relatie:- Ja (standaard), hierbij moet het algemene E-mailadres gevuld zijn!- Nee | | --- | --- | | Standaard XML | Optie om standaard XML factuur te sturen: - Nee - XML (UBL), (standaard) - XML (S@les in Bouw) NB Bij PDF en/of XML is bij de relatie een e-mailadres verplicht! | | --- | --- |

- Bij een nieuwe relatie of webshop klant, worden deze instellingen toegepast.

Klik hier voor meer informatie over de kortingsgroep en kortingspercentage:

Op tabblad Debiteurinfo en Crediteurinfo kan een kortingsgroep of kortingspercentage ingegeven worden:

- | Kortingsgroep | De kortingsgroep ('prijslijst'), de standaard groepen zijn: - 1 = Verkoopprijs - 2 = Adviesprijs - 9 = verreken(inkoop)prijs Zie Onderhoud kortingsgroepen. Wordt bij relaties / werkorders alleen bij 'toepassen bij' type relaties of werkorders weergegeven, indien toegestaan bij module. | | --- | --- |
- | Kortingspercentage | Het kortingspercentage op de (bruto) verkoopprijs van het artikel. - Dit percentage wordt standaard gevuld bij een bon, verkooporder of werkorder, als er geen andere kortingen van toepassing zijn. Kan ook gebruikt worden bij werkorders m.b.t. negatieve toeslag op de uren instelling.NB Kan gebruikt worden als er geen prijsafspraken module is. | | --- | --- |

Wat gebeurt er als beide ingevuld zijn?

Als de kortingsgroep en percentage gevuld zijn, wordt de kortingsgroep toegepast.

- Als er artikelen verkocht worden die niet in de kortingsgroep vallen, dan wordt ook het standaard kortingspercentage gebruikt.

Wat gebeurt er als er ook een factuurrelatie is?

De kortingsgroep van de factuurrelatie of eigenaar wordt dan toegepast i.p.v. de klant.

- Dit kan bijv. bij een machine het geval zijn. De machine staat bij franchiser/klant X maar is van eigenaar Y.

Waar kan een nieuwe relatie aangemaakt worden?

Op de volgende manieren kan een nieuwe relatie aangemaakt worden, indien geautoriseerd:

- Onderhoud relaties (BRR)
- Bij Zoek relaties via de 'Plus' knop.
- Via weborders Webportal gebruikers / Relatie registraties 1
- Nieuwe relatie CRM app

Wat is het verschil m.b.t. het adres tussen Nederland en België?

De Belgische adressering verschilt niet veel van de Nederlandse. Het volgende geldt:

- #### Adres In België is het gebruikelijk om de naam van de ontvanger bovenaan te zetten en daaronder de bedrijfsnaam.
- Voor Nederland is dit precies andersom.

#### Postcode

- In België bestaat de postcode alleen uit vier cijfers.
- In Nederland is de postcode en huisnummer combinatie uniek.

#### BTW / BTW-code

Hoe zit het met de BTW-code bij toevoegen?

De volgende standaarden worden toegepast bij toevoegen / wijzigen van een relatie:

Instellingen debiteuren, tabblad Standaard:

- BTW-code (1)
- BTW-code binnen EU (8)
- BTW-code buiten EU (9)

Instellingen crediteuren, tabblad Standaard:

- BTW-code (11)
- BTW-code binnen EU (18)
- BTW-code buiten EU (19)

Bij het toevoegen van een nieuwe klant worden de volgende regels worden toegepast:

- Als geen BTW-nummer is ingevuld -> altijd op standaard BTW-code (meestal 1 en 11).
- Debiteur: Als deze binnen EU aangemaakt wordt én het BTW-nummer is ingevuld dan standaard BTW-code binnen EU gebruiken (meestal 8).
- Als deze buiten EU aangemaakt wordt én het BTW-nummer is ingevuld dan standaard BTW-code buiten EU gebruiken (meestal 9).

Bij een Intercompany relatie wordt de Intercompany BTW-code meestal 7 (IC), d.w.z 0% gebruikt.

Crediteur:

- Als deze binnen EU aangemaakt wordt én het BTW-nummer is ingevuld dan standaard BTW-code binnen EU gebruiken (meestal 18).
- Als deze buiten EU aangemaakt wordt én het BTW-nummer is ingevuld dan standaard BTW-code buiten EU gebruiken (meestal 19).

| Omschrijving | BTW- code | BTW-code | Opmerking |
| --- | --- | --- | --- |
| Geen BTW-nummer / eigen land | Debiteur | 1 | BTW |
| ,, | Crediteur | 11 |  |
| Intercompany |  | 7 | 0 % |
| Binnen EU | Debiteur + BTW nummer | 8 | geen BTW |
| ,, | Debiteur + geen BTW | 1 | BTW |
| Buiten EU | Debiteur | 9 | geen BTW |
| Binnen EU | Crediteur + BTW nummer | 18 | geen BTW |
| Buiten EU | Crediteur | 19 | geen BTW |
| Overzeese gebieden binnen EU |  | 9 | geen BTW |

Deze BTW-code wordt toegepast in de orderregels.

#### Werkorder

Bij een werkorder aan een EU-klant (intracommunauteair) wordt als volgt geregistreerd:

- uren als diensten (btw-code 8) en, Als er uren in zitten en materialen is dit ook een dienst.

materialen als goederen (btw-code 7).

Waarom krijg ik de melding BTW-codes aanpassen?

Als het BTW-nummer wordt ingevuld of het land wordt gewijzigd verschijnt de melding:

- Wilt u de BTW-codes aanpassen naar de standaard waarde? Deze standaard waardes staan bij de betreffende instelling debiteuren / crediteuren.

Hoe zit het met de BTW betreft klanten binnen EU, in overzeese gebieden?

- Deze klanten horen wel bij de EU. Maar qua BTW regeling gelden ze buiten de EU. Moeten op aparte landencodes opgevoerd worden. Bijv. het niet EU-gebied Helgoland, Duitsland met instelling 'Land binnen EU' is nee.
- | Land binnen EU (ICT) | Optie of het land binnen/buiten de EU valt.- Ja, (standaard) het land behoort tot de EU (ICV).- NeeBij sommige EU-landen horen gebieden die niet voor de BTW behandeld worden als niet EU-landen, voor meer informatie zie Belastingdienst: Niet EU gebieden. | | --- | --- |
- Bij Onderhoud relaties, tabblad Debiteur- en/of Crediteurinfo, moet de BTW-code 9 zijn.

- Hoe controleer ik het BTW-nummer?

Overige

Hoe zit het met het al of niet verplicht invullen van de referentie of ordergegevens.

Er kan aangegeven worden of deze al of niet verplicht zijn.

1. Op module niveau, bijv. referentie is verplicht. Per relatie kan hiervan afgeweken worden, bijv. bij klant x, is ook het veld ordergegevens verplicht.

De referentie komt op de factuur (extern) en de ordergegevens zijn meer voor intern gebruik.

Hoe verstuur ik per e-mail aan bepaalde relaties een mailing?

Het is mogelijk om een mailing te sturen naar bepaalde relaties.

- Gebruik hiervoor bijv. een bepaalde mailcode.
- Voor meer informatie zie Mailmerge.

Hoe is de relatie aan een taal gekoppeld?

- Aan de relatie is een landcode gekoppeld, aan de landcode weer de taalcode.
- | Taalcode | De taalcode wordt gebruikt om artikel / machineomschrijvingen of factuur e.d. in een andere taal weer te geven.- 1 Nederlands (standaard)- 2 Engels - (Frans / Duits) | | --- | --- |

Hoe kan ik zoeken op een relatie?

Voor meer informatie zie:

- Zoek relaties

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Relaties Onderhoud relaties
- Zoek afleveradressen
- Zoek contactpersonen
- Zoek relaties

---
## Hoe, wat m.b.t. een actief / inactief  relatie?

# Hoe, wat m.b.t. een actief / inactief relatie?

Het is mogelijk om bij een relatie aan te geven of deze relatie actief is of niet meer actief.

Het volgende geldt voor een niet actieve relatie:

- Een melding verschijnt er bij invoer van een order.
- Bestaande orders kunnen nog afgerond worden.
- Zowel aan verkoop als aan inkoopkant geïmplementeerd.
- Verschijnt niet in het zoekvenster Zoek relaties, behalve als het vinkje niet actieve tonen aangezet wordt.

Kan in de relatie overzichten uitgesloten (standaard) of juist geprint worden.

- zie ook FAQ.

#### Onderhoud - en Opvragen relaties

Bij Onderhoud relaties (BRR) en Opvragen relaties F6 is het veld Actief toegevoegd:

- | Actief | Optie of relatie actief is of niet:- Ja (standaard) - Nee | | --- | --- |
- Er kan geen nieuwe order ingevoerd worden voor een niet actieve relatie.

#### Zoeken relaties

Bij Zoek relaties is het vinkje Niet actieve tonen beschikbaar:

- Als deze aangevinkt wordt, worden ook de inactieve relaties getoond.

#### FAQ

Welke melding verschijnt er als ik een order maak voor een 'niet actieve' relatie?

Als er een order gemaakt wordt, wordt gecontroleerd of deze relatie actief is.

- De melding: Relatie is niet actief.  invoer is geblokkeerd verschijnt bij een bon.

Dezelfde melding verschijnt ook als de relatie, bij tabblad Debiteuren, Orders voor klant op blokkeren orders staat.

Welke overzichten kan ik de relaties in- of uitsluiten?

Bij de volgende Relatie rapportages kunnen relaties uit- of ingesloten worden:

- Overzicht relaties (BRP)
- Etiketten relaties (BRE)
- Mailmerges relaties (BRM)

Het veld Alleen Actieve is toegevoegd:

- | Alleen actieve | Optie om in- / actieve relaties weer te geven:- Alle (standaard) - Actieve - Inactieve | | --- | --- |

Wordt dit ook toegepast bij de Werkbon App en de Powerall CRM App

Dit status hiervan is als volgt de Powerall Connect apps:

- Nee, voor de Powerall CRM app.
- Ja, bij de Powerall Werkbon App (als referentie data is bijgewerkt, is de relatie niet meer zichtbaar bijv. bij een nieuwe servicemelding.

In welke programma's wordt een inactieve relatie gecontroleerd?

In de volgende programma's wordt dit toegepast:

- Invoeren/wijzig bonnen
- Invoeren kassabonnen
- Verwerken bestelvoorstel
- Besteladvieslijst
- Invoeren/wijzigen offertes
- Invoeren/wijzigen verkooporder
- Back-to-back naar inkooporder
- Invoeren/wijzigen inkooporders
- Aanmaken werkorder
- Urenregistratie touchscreen
- Project planningsadvies
- Contractenbeheer
- Invoeren/wijzigen huurorders
- Invoer servicemelding (Machinist App)
- Invoer servicemelding (Werkbon App)
- Beheer servicemelding

- Onderhoud relaties

---
## Wat doe ik als de balans / dagboek niet in evenwicht is?

Bij het controleren van de Proef- & Saldibalans (GLS) kan het voorkomen dat de balans niet in evenwicht is.

Om te controleren welk dagboek (met welk stuknummer) hiervan de oorzaak is, doorloopt u de volgende stappen:

1. Ga naar Overzicht mutaties per dagboek (GLD). In Menu 3.0 onder Financieel > Financieel overzichten > Mutaties per dagboek.
2. Vul het dagboeknummer in. Indien het dagboek niet bekend is, begin met 1.
3. Vul bij periode 01-25 t/m 13-25 in.
4. Bij subtotalen/boekstuk selecteer Recapitulatie alleen.
5. Kies voor de knop Afdrukken. Indien er geen melding Attentie verschil verschijnt, is het dagboek in evenwicht.
6. Ga vervolgens naar het volgende dagboek, zie stap 2.

Bij een verschil verschijnt de pop-up: Attentie verschil.

Kies voor de knop OK.

Het volgende scherm verschijnt: met achter VERSCHIL het stuknummer:

Ga weer terug naar Overzicht mutaties per dagboek om een gedetailleerd overzicht van het stuknummer aan te vragen.

Vul hiervoor het eerste boekstuknummer in, bijv. 370791 bij vanaf en t/m.

Bij subtotalen/boekstuk selecteer Ja.

Kies voor de knop Afdrukken. Een gedetailleerd overzicht verschijnt:

Corrigeer de boeking van het betreffende stuknummer in de juiste periode van het dagboek.

1. Bij Inkoopboek: Ga naar Inkoopfactuur boeken (KI).
2. Bij Verkoopboek: Ga naarVerkoopfactuur boeken (handmatig) (DV).
3. Bij Kas of bank: Ga naar Memoriaal boeken (GJ).

Indien nodig, doe dit doet ook voor de andere stuknummers.

Controleer nogmaals de balans, als het goed is, moet deze in evenwicht zijn.

Bij verschil

Geeft bovenstaand geen handvatten voor het oplossen van eventuele verschillen, hertel het grootboek.

Om de grootboeksaldi te hertellen, doorloopt u de volgende stappen:

1. Druk op de toetsen SHIFT + F2. Een pop-up scherm verschijnt.
2. Geef bij opdracht / programma FGL86 in. Het scherm Hertel grootboeksaldi verschijnt.
3. Vul bij periode 01-25 t/m 13-25 in. Grootboekrekeningen vanaf 1 t/m 9999999. Beginbalans meenemen Ja.
4. Kies voor de knop Verwerken.

Controleer of het verschil nog aanwezig.

- Wat doe ik als het grootboek niet in evenwicht is?

---
## Hoe kan ik een opslag toepassen bij bepaalde artikelen, bij de kassa?

#### Instellingen

Het is mogelijk om met prijsafspraak opslag % te werken. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Verkoop prijsafspraken (APA).
2. Selecteer bij kortingsgroep Kortingsgroep 1 (Relatie:Verkoopprijzen).
3. In combinatie met hoofd-/subgroep. Vul de Hoofd-/Subgroep / Cat. in.
4. Selecteer bij basisprijs berekening Verkoopprijs.
5. Geef het opslag % / percentage in.
6. Kies voor de knop Opslaan.

De opslag is opgeslagen / actief vanaf de startdatum.

Artikelen

Artikel met deze hoofd- en subgroepen, wordt de korting /toeslag toegepast.

Zie Onderhoud artikelen (ABA).

#### Kassa / toepassing

Bij de kassa wordt de verkoopprijs als volgt berekend:

- (Verkoopprijs + Opslag) + BTW = (10,00 + 30% =) 13,00 + 2,73 (13,00 x 1,21) = 15,73.

- FAQ Kassa

---
## Hoe stel ik de kassagegevens in?

De volgende gegevens moeten per administratie aanwezig zijn, als u gebruik wilt maken van de Kassa module.

- Onderhoud kassa's
- Onderhoud kassa mutatiecodes
- Kassa instellingen
- Onderhoud betalingscondities

Belangrijk: • Bij het instellen van de kassa module moet één en ander ingericht worden. Voor de juiste werking moet dit correct gebeuren. • Neem hiervoor contact op met de helpdesk of planning.

#### Onderhoud kassa's

Om een kassa toe te voegen of te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud kassa's (FKA).
2. Geef de kassanummer in. Bij F4 verschijnt het scherm Zoek kassa's.
3. Kies voor de knop Wijzigen. of Kies voor de knop Opvoer.
4. Vul de gegevens in of wijzig deze.
5. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Belangrijk: Bij meerdere kassa's gebruik per kassa een andere grootboek(tussen)rekening en dagboek.

#### FAQ

Hieronder een uitleg van de velden van scherm Onderhoud kassa's:

| Kassanummer | Het nummer van de betreffende kassa.NB Indien dit een webshopkassa is, kan deze niet gekozen worden bij Invoeren kassabonnen. |
| --- | --- |

| Afkorting | De afkorting van deze code. |
| --- | --- |

| Omschrijving | De 'betreffende' omschrijving. |
| --- | --- |

| Gekoppeld aan | Dit kan gebruikt worden als een kassa standaard aan een bepaalde pc gekoppeld is. Bij het inloggen (op deze pc) verschijnt dan deze (standaard) kassa. |
| --- | --- |

| Automatisch afmelden | Optie om automatisch af te melden (ter beveiliging) na een bepaalde tijd.- Nooit (standaard)- Na elke transactie- Na inactiviteit van X secondenHet scherm Aanmelden bij kassa verschijnt dan. |
| --- | --- |

| Aanmelden met pincode | Optie voor het aanmelden met een pincode (wachtwoord):- Nee (standaard)- Ja, de verkoper / gebruiker moet een pincode invullen, als deze ingegeven is bij Onderhoud personeelscodes. |
| --- | --- |

|  |
| --- |

| Financiële verwerking |  |
| --- | --- |

| Dagboek | Het dagboek Kassa (elke kassa heeft een apart dagboek bijv. 2 = Kassa balie, 3 = Kassa werkplaats). |
| --- | --- |

| Tussenrekening overboekingen | Op deze (kassa) grootboekrekening worden de overboekingen (bijvullen en afromen) geboekt. |
| --- | --- |

| Kostenplaats | De betreffende Kostenplaats. |
| --- | --- |

| Overige |  |
| --- | --- |

| Printlayout voor kassabon | Dit is de standaard lay-out die gebruikt wordt bij het afdrukken, A=A4-factuur en B=Kassabon. Indien deze niet is ingevuld, verschijnt er een selectie bij het afdrukken. - Bij gebruik van printvoorkeuren / deze niet invullen / leeg laten, er kan dan een printer geselecteerd worden. Gebruik een Voorkeur printer / layout. |
| --- | --- |

| Printer voor printen kassabon | De (label)printer voor het afdrukken van de kassa bon.- Leeg (standaard)NB er kan een Voorkeur printer ingesteld worden. |
| --- | --- |

| Automatisch printen na afrekenen | Optie om na een transactie de kassabon (automatisch) af te drukken:- Ja (standaard) geen pop-up- Nee, pop-up- Vragen, pop-up Pop-up melding: Wilt u de kassabon afdrukken? / Factuur afdrukken / verzenden verschijnt. |
| --- | --- |

| Kopieën | Het aantal kopieën van de kassabon (losse opdrachten).- 1 (standaard). |
| --- | --- |

|  |
| --- |

| Kassalade aangesloten | Optie of een kassa-lade aangesloten is:- Nee (standaard)- Ja, er wordt een kassa-lade gebruikt. De knop Lade openen wordt getoond bij deze kassa. |
| --- | --- |

| Bedragingave bij dagafsluiting | Optie voor het tellen van de/het kassa totaalbedrag(en) bij dagafsluiting (Ingave begin/eindstand): - Telveld (Standaard)- HandmatigBij een verschil, wordt het berekend bedrag overgenomen bij de telling. Bij tekstveld verschil verschijnt Akkoord  . Dit om de kassa snel af te sluiten (terwijl er maar 1x geteld wordt per week), vanaf versie 3.0 |
| --- | --- |

| Bijvullen en afromen toestaan (bij) dagafsluiting | Optie om bij een dagafsluiting de kassa wel/niet af te romen of bij te vullen:- Ja (standaard)- Nee, niet toegestaan. |
| --- | --- |

| PIN-betalingen | Optie voor PIN / 'Bancontact' betaling:- Handmatig, (standaard) de huidige / niet gekoppelde manier.- CCV betaalautomaat, via de koppeling met de CCV betaalautomaat. EN vul de betaalautomaat poort in.- MultiSafepay |
| --- | --- |

| Betaalautomaat poort | De poort of terminal waaraan de betaalautomaat gekoppeld is.- Leeg (standaard)-

Deze poort kan gezien worden onder Apparaatbeheer > Poorten, bijv. COM2 - Bij MultiSafepay is dit het terminalnummer (TID). | | --- | --- | | Betaalautomaat API-key instelling | De API-key van het betaalautomaat apparaat / terminal bij PIN- betaling via MultiSafepay.- Leeg / niet zichtbaar (standaard) | | --- | --- |

#### Onderhoud kassa mutatiecodes

De kassa mutatiecodes worden gebruikt om de kassamutaties op een bepaalde grootboek(tussen)rekening te boeken. Dit zijn de geldstromen of eventuele verschillen tussen de kassa en de kas (kluis).

Om een kassa mutatiecode toe te voegen of te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud kassa mutatiecodes (FKM).
2. Geef de mutatiecode in. Bij F4 verschijnt het scherm Zoek kassa mutatiecodes.
3. Kies voor de knop Wijzigen. of Kies voor de knop Opvoer.
4. Vul de gegevens in of wijzig deze.
5. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

FAQ

Hieronder een uitleg van de velden van scherm Onderhoud kassa mutatiecodes:

| Mutatiecode | De mutatiecode voor een bepaalde kassa transactie. Deze codes worden gebruikt bij de Instellingen facturering, tabblad Kassa (nieuw). |
| --- | --- |

| Afkorting | De afkorting van deze code. |
| --- | --- |

| Grootboekrekening | De grootboekrekening, moet voorkomen in het grootboek, wordt op overzichten rechts uitgelijnd. |
| --- | --- |

| Omschrijving | De 'betreffende' omschrijving. |
| --- | --- |

| Te verrekenen BTW | Dit is het te verrekenen BTW % van de betreffende grootboekrekening. |
| --- | --- |

| Vereiste autorisatieniveau. | Het vereiste autorisatie niveau van de verkoper/personeelscode van de betreffende kassa. De personeelscode kan gekoppeld zijn aan een gebruiker. - standaard leeg |
| --- | --- |

Deze mutatiecode kan gebruikt worden bij de Instellingen facturering, tabblad Kassa (nieuw).

Opmerking: • De mutatiecodes afromen, verschillen en bijvullen moeten aanwezig zijn voor de kassa instellingen.• Bij de mutatiecode van afroom en bijvullen wordt de (grootboek)tussenrekening van de betreffende kassa gebruikt.

#### Kassa instellingen

Om een kassa instelling te muteren doorloopt u de volgende stappen:

1. Ga naar Instellingen Facturering, tabblad Kassa (nieuw) (BIF).
2. Kies voor de knop Wijzig.
3. Vul de gegevens in of wijzig deze. Minimaal moeten de eerste 3 betalingscondities, d.w.z. Contant, PIN en Op rekeing, gevuld zijn, vanaf versie 3.18.
4. Kies voor de knop Opslaan.

Als relatie, betaalcondities en mutatiecodes zijn ingevuld en er een kassa aanwezig is, kan het kassa programma gebruikt worden.

Opmerking: Voor deze instellingen is een kassalicentie vereist.

Hieronder een uitleg van de velden m.b.t. de kassa in het scherm 'Instellingen facturering':

| Tabblad Algemeen |  |
| --- | --- |

|  |
| --- |

| Externe referentie | Optie voor de externe referentie in de orderkop:- Nee, veld blijft zichtbaar maar het is niet mogelijk deze te vullen.- Ja, (standaard) vrij invulbaar of niet. - Verplicht, referentie moet ingevuld worden. |
| --- | --- |

| Interne referentie | Optie voor de interne referentie of ordergegevens van de betreffende orderkop:- Nee, veld blijft zichtbaar maar het is niet mogelijk deze te vullen.- Ja, (standaard) bent u vrij om dit veld in te vullen of niet. - Verplicht, ordergegevens/referentie moet ingevuld worden. |
| --- | --- |

|  |
| --- |

| Tabblad Kassa (nieuw) |  |
| --- | --- |

| Standaard relatie | De relatiecode die standaard verschijnt bij het Kassa programma, bijv. Contante verkopen. Deze NAW- gegevens kunt u wijzigen. |
| --- | --- |

|  |
| --- |

| Betalingsconditie | Zie Onderhoud betalingscondities. |
| --- | --- |

| Betalingsconditie contant | De betaling moet direct contant betaald moet worden *. |
| --- | --- |

| Betalingsconditie PIN | De betaal conditie code voor PIN of BANCONTACT betaling, zie *. |
| --- | --- |

| Betalingsconditie op rekening | De betaal conditie code voor betaling op rekening, zie *. |
| --- | --- |

| Betalingsconditie cadeaubon / 1 | De betaalconditie code voor cadeau bon betaling, zie *. |
| --- | --- |

| Betalingsconditie creditcard / 2 | De betaalconditie code voor creditcard betalingen *. |
| --- | --- |

| Betalingsconditie optie 3 t/m 5 | De betaalconditie code optie 3 t/m 5, vanaf versie3.18, zie *. - Leeg (standaard, knop wordt niet getoond)- , knop wordt getoond met verplichte . |
| --- | --- |

|  | * Per betaalmethode moet een unieke betalingsconditie gekoppeld zijn. Als een factuur betaald wordt via de kassa, wordt de betalingsconditie van de betaalwijze overgenomen. NB als de betalingscode leeg is, wordt knop niet getoond, vanaf versie 3.30. |
| --- | --- |

| Bij PIN stand tellen | Optie om deze betaling op te tellen bij de 'PIN-automaat' stand.- Leeg (standaard)- Bij PIN / Credit card is deze aangevinkt. |
| --- | --- |

|  |
| --- |

| Betalingsconditie afronden | Optie voor het afronden van een contant betaling, vanaf versie 3.13:- 0 (standaard) er wordt niet afgerond. -  de contant betalingen worden afgerond en op de betreffende grootboekrekening geboekt, zodat er geen kassa verschil meer ontstaat. |
| --- | --- |

|  |
| --- |

| Korting artikelcode | Het artikel voor de korting. De knop Korting kan gebruikt worden bij het scherm Bon afrekenen.NB Dit (normaal) artikel moet aanwezig zijn. |
| --- | --- |

| Autorisatie korting | De autorisatiecode als er voor het verlenen van korting een gebruikersautorisatie geldt. |
| --- | --- |

| Max. ongeautoriseerde korting | Het kortingsbedrag dat maximaal gegeven mag worden. Boven dit bedrag moet men geautoriseerd zijn. |
| --- | --- |

|  |
| --- |

| Kas mutatiecode afromen | De mutatiecode voor het afromen van geld van de Kassa naar de Kas (kluis), zie *. |
| --- | --- |

| Kas mutatiecode verschillen | De mutatiecode voor de kassa verschillen, zie *. Belangrijk: * De kas mutatiecodes zijn verplichte velden, zie ook Onderhoud kassa mutatiecodes. |
| --- | --- |

| Kas mutatiecode bijvullen | De mutatiecode voor het bijvullen van geld van de kassa; van de Kas (kluis) naar de Kassa, zie *. |
| --- | --- |

#### Onderhoud betalingscondities

Om een betalingsconditie toe te voegen of te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud betalingscondities (BTB). In Menu 3.0 via Systeem > Stamgegevens.
2. Geef de betalingsconditie in. Bij F4 verschijnt het scherm Zoek betalingscondities.
3. Kies voor de knop Wijzigen. of Kies voor de knop Opvoer.
4. Vul de gegevens in of wijzig deze. Bij Kassa betaalconditie selecteer Ja.
5. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Opmerking: Indien de kassa betaalcondities op Ja staat, kan deze gebruikt worden voor de kassa instellingen.

Hieronder een uitleg van de velden van scherm Onderhoud betalingscondities:

| Betalingsconditie | De betalingsconditie, zie Onderhoud betalingscondities.- Hierdoor bepaalt u o.a. de betaalwijze, betalingstermijn en eventuele korting. |
| --- | --- |

| Code/afkorting | De code of afkorting. |
| --- | --- |

| Omschrijving | De 'betreffende' omschrijving. |
| --- | --- |

|  |
| --- |

| Betaaltermijn in dagen | De betalingstermijn van de factuur in dagen. De vervaldatum wordt a.h.v. deze termijn berekend, bijv. voor een UBL factuur. |
| --- | --- |

| Einde maand | Vinkje / optie voor betalingsconditie einde maand (OEM). D.w.z. de betalingstermijn start pas  dagen na het einde van de maand.Bijv. 30 EOM factuurdatum 01-03-2026 is de vervaldatum van de factuur 30-04-2026. |
| --- | --- |

|  |
| --- |

| Factuur kortingsoort | Optie voor de de factuur kortingssoort:- N.v.t. (standaard)- Kredietbeperking, is een toeslag over het gehele factuurbedrag inclusief BTW (SYS423).- Betalingskorting, is een korting, die gebaseerd is op het goederenbedrag, over gehele factuurbedrag exclusief BTW (SYS242).- Afhaalkorting, is een korting over het gehele orderbedrag exclusief BTW, daarna wordt de BTW berekend.(SYS241).Opmerking: Voor een voorbeeld berekening, klik op de afbeelding rechts.Het kortingbedrag kan op de factuur afgedrukt worden. Het gewenste SYS-veld met label SYS350 moet dan toegevoegd worden op de factuur lay-out, in de factuur voet. |
| --- | --- |

| Factuur dagen | De factuur dagen. Dit aantal berekent het aantal dagen na factuurdatum, wanneer een aanmaning of herinnering gestuurd mag worden. Ook wordt deze toegepast bij kredietbeperking / betalingskorting. |
| --- | --- |

| Factuur korting % | De factuur korting percentage |
| --- | --- |

| Factuur tekst | De tekst op de factuur (SYS350). |
| --- | --- |

| Kassa betaalconditie | Optie voor de kassa betalingsconditie:- Nee (standaard)- Ja, de betaalconditie kan gebruikt worden bij de kassa (instellingen). |
| --- | --- |

|  |
| --- |

| Tussenrekening kassysteem | De grootboekrekening van de tussenrekening van het kassasysteem (standaard 9999). - Geef hier de grootboekrekening of omschrijving in. |
| --- | --- |

|  |
| --- |

| Webshop betalingen via kassa | Optie voor webshop betalingen via een 'kassa':- Nee (standaard)- Ja, voor de weborders, wordt een factuurnummer vanuit de 'webshopfactuurnummer reeks' toegekend. |
| --- | --- |

---
## FAQ Kassa

In dit hoofdstuk staan de meestgestelde vragen over de CRM module.

- Kassa pin terminal
- Hoe kan ik een opslag toepassen bij bepaalde artikelen, bij de kassa?
- Hoe stel ik de kassagegevens in?

*Hoe is de barcode samengesteld? De barcode is samengesteld door een "@", het kassanummer "001" en het kassabonnummer "0007". - Bijv. @0010007 of @0017. De barcode wordt afgedrukt op de kassabon bij layout A. Dit kan ook op de klant layout bijv. F of K. - Het database veld / barcode SYS480 is beschikbaar in de kop van programma Print kassabon . Kan ik van één kassa gebruik maken op meerdere pc's? Ja, het is mogelijk om één kassa te gebruiken op meerdere pc's. Het volgende is hierbij van belang: - Stel 1 PC aan als 'hoofd-kassa'. Hierop moet 's morgens als eerste de kassa opgestart worden, voor de beginstand - en 's avonds de Dagafsluiting voor de eindstand. Gebruik verschillende verkopers / kassières (bij aanmelden). Klik hier voor meer informatie over een voorbeeld van opslag berekening: De opslag wordt als volgt berekend: (Verkoopprijs + Opslag) + BTW = Verkoopprijs incl. btw. - (10,00 + 30% =) 13,00 + 2,73 (13,00 x 0,21) = 15,73. Zie ook Hoe kan ik een opslag toepassen bij bepaalde artikelen, bij de kassa? Kan ik automatisch afronden? Ja, het is mogelijk om de contant betalingen automatisch af te laten ronden op 5 cent, vanaf versie 3.13. - Bij de Instellingen facturering, Tabblad Kassa (nieuw) kan hiervoor het veld Betalingsconditie afronden gebruikt worden. - De afronding wordt op het betreffende grootboekrekening geboekt, zodat er geen kassa verschil meer ontstaat. - Bij Bon afrekenen verschijnt dan onder Contant de tekst Afronden contant met het bedrag. Kan ik de tekst wijzigen van de knoppen bij het afrekenen? Ja, het is mogelijk om de tekst van de knoppen te wijzigen, vanaf versie 3.18. Bij Instellingen facturering, Tabblad Kassa (nieuw) kan de Kassa button tekst gewijzigd worden. - Als de betalingsconditie leeg is, wordt de knop niet weergegeven. - Er zijn naast de standaard (Contant, PIN en Op rekening) knoppen, maximaal 5 extra knoppen beschikbaar. D.m.v. het ampersand & teken, voor een letter, kan de Alt functie ingesteld worden bij de betreffende knop. Kan ik ook een (kleine) machine via de kassa verkopen? Ja, dit is mogelijk, vanaf versie 3.25. Opmerking: Een inruil via de Kassa is niet mogelijk. Wanneer maak ik gebruik van Vrijgeven kassabonnen*?

- Normaal gebeurt dit automatisch, na het afrekenen van een kassabon.

Mocht een kassabon niet vrijgegeven en gefactureerd zijn, nadat de kassabon afgerekend is, dan kun je via dit programma (FKV) dit alsnog handmatig uitvoeren.

Opmerking: Dit zelfde geldt ook voor het Doorboeken kassatransacties (FKD). Als de kassatransacties bij dagafsluiting niet automatisch doorgeboekt zijn, kun je proberen om dit alsnog handmatig via dit programma te doen.

Belangrijk: Bel altijd eerst de helpdesk in zo'n situatie, omdat er mogelijk een fout opgetreden is.

*Wat doe ik bij 'Fout bij doorboeken transactie ; geen openpost aanwezig'?*

Als dit probleem zich voordoet, neem dan contact op met de helpdesk.

Is het mogelijk om, naar keuze, de kassabon op A4 of een kassabon af te drukken?

Ja, dit is mogelijk.

- Neem hiervoor contact op met de helpdesk

Tip: Lees Invoeren kassabonnen de aandachtig door, hierin worden de vele mogelijkheden en opties uitgelegd.

- Hoe kan ik een opslag toepassen bij bepaalde artikelen, bij de kassa?
- Kassa

---
## FAQ Crediteuren

In dit hoofdstuk staan de meestgestelde vragen over de Crediteuren module.

#### Betaalbatch

Hoe komt het dat de post niet meegenomen wordt in de batch?

Als in de kolom status ** staat, betekent dat bij betreffende crediteur een van de volgende gegevens ontbreken:

- IBAN-nummer
- Automatisch betalen moet op ja staan.
- Vanaf versie 3.20 ook: Naam1
- Plaats
- ISO landcode

Pas deze gegevens aan Onderhoud relaties .

De post wordt dan niet mee verzameld, dit is het geval bij de laatste twee posten / regels.

Hoe verwijder ik een (lege) betaalbatch?

Het is mogelijk om een betaal batch te raadplegen of te verwijderen. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Raadplegen betaalbatches (KAT).
2. Selecteer de betaallijstcode.
3. Indien de betaalbatch leeg is, d.w.z. totaal bedrag is 0, kan deze verwijderd worden. Kies voor de knop Verwijder.
4. Bij de pop-up melding Werkelijk verwijderen, kies voor de knop Ja.
5. De batch is verwijderd.

Anders verschijnt er de pop-up Batch verwijderen niet toegestaan CLIEOP-bestand is al aangemaakt!

Opmerking: Alleen betaalbatches met status 1 of 2 kunnen verwijderd worden.

Wat doe ik als de bank een betaalbatch afkeurt?

Foutief IBAN-nummer

- Wanneer het IBAN-nummer of de BIC-code niet goed is, vul deze dan in bij Onderhoud relaties (BRR).

ING

Zit u bij de ING, bel dan de helplijn. De ING accepteert een betaalbatch niet meer als hij opnieuw aangeboden wordt. De batch moet dan verwijderd worden en opnieuw aangemaakt.

RABO / ABNAMBRO

Zit u bij de Rabo of ABNAMRO dan kan de betaalbatch herverwerkt worden via Aanmaken betaalbestand (KAA)

Wat doe ik bij de melding 'Betaallijsttabel' vol?

Deze melding verschijnt als de betaal- of incassotabel vol is.

- Neem contact op met de helpdesk om dit op te lossen.

Inkopen

Is het mogelijk om de inkoopprijs te verbergen voor de gebruiker?

Ja het is mogelijk om een autorisatie voor de inkoopprijs in te stellen.

- In plaats van de inkoopprijs worden dan sterretjes *** getoond.
- Dit is het geval bij (IS) en Opvragen inkooporders (IO)
- Belangrijk: Het is wel mogelijk om de adviesprijs te wijzigen en daardoor kan op de achtergrond ook de inkoopprijs wijzigen.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Overige

Hoe kan zien dat een klant een crediteur is?

Het vinkje Crediteur is aangevinkt bij:

- Opvragen relaties F6
- Onderhoud relaties (BRR) Op tabblad Crediteurinfo staan de belangrijkste crediteur- / leveranciersgegevens.

Waar kan ik de fiatteringscode zien?

De fiatteringscodes worden opgegeven in E-inkoopfacturen (geavanceerd) en bij Nieuwe inkooporder aanmaken. De kolom Fiatcd is zichtbaar bij:

- Opvragen crediteurposten
- Opvragen relaties, tabblad Openposten, vink Crediteuren aan.
- E-Inkoopfacturen, tabblad Openstaand of Alle

#### Crediteuren betalingen

Hoe worden de betalingen verwerkt als er een betaalbatch aangemaakt is?

Situatie

Er is een betaalbatch aangemaakt/verzonden en daarmee zijn de betalingen verwerkt bij de crediteuren.

Vraag

Hoe wordt dit bedrag weggewerkt?

Antwoord

Zodra de betaling wordt afgeschreven, kan dit totale bedrag geboekt worden op de grootboekrekening 'betalingen onderweg'.

- Bij Kas of bank boeken (GKK) wordt dit gedaan.
- Deze grootboekrekening kunt u vinden in Onderhoud dagboeken (GBD) in het bank dagboek bij Betalen crediteuren de betreffende grootboekrekening.

| Betalen crediteuren | Optie voor betalen crediteuren: - Nee (standaard) - Handmatig- Tussenrekening, geef hierbij de grootboekrekening op bijv. 'Tussenrek. Betalingen onderweg'. |
| --- | --- |

#### Journalisering

- Bij het verzenden van de betaalbatch wordt bijv. de volgende journaalpost geboekt: | Grootboek | Omschrijving | debet | credit | | --- | --- | --- | --- | | 3100 | Crediteur | 100,00 | | | aan 2200 | Betalingen onderweg | | 100,00 |
- Als het bedrag van de bankrekening wordt afgeschreven, wordt geboekt: | Grootboek | Omschrijving | debet | credit | | --- | --- | --- | --- | | 2200 | Betalingen onderweg | 100,00 | | | aan 1100 | Bank | | 100,00 |
- De tussenrekening 2200 loopt hierdoor 'glad', d.w.z. het totaal (debet en credit) is 0.
- De journalisering kan gecontroleerd worden bij Overzicht mutaties per dagboek (GLD).

- Inkoopfacturen Crediteuren betalingen

---
## FAQ Debiteuren

De volgende onderwerpen worden behandeld:

- Hoe stel ik E-aanmaningen of herinneringen in?
- Hoe wijzig ik de aanmaningstekst?

Hoe kan ik zien of er een aanmaning verzonden?

Bij de aanmaning historie zijn de aanmaningen te zien van een bepaalde factuur. Om deze op te vragen, doorloopt u de volgende stappen:

1. Ga naar Opvragen relaties of F6.
2. Ga naar tabblad Openposten.
3. Selecteer de factuur.
4. Druk op de knop Aanmaning info.

Wat doe ik bij de melding 'Betaallijsttabel' vol?

Deze melding verschijnt als de betaal- of incassotabel vol is.

- Neem contact op met de helpdesk om dit op te lossen.

### Krediet limiet

Bij de ingave van een order wordt het kredietlimiet gecontroleerd. Als het krediet overschreden wordt, verschijnt de melding:

- De kredietlimiet is overschreden.
- De order kan ingegeven worden.

Voorwaarde

Het volgende geldt hierbij:

- Een order kan vrijgegeven worden, als het krediet limiet overschreden is.
- Bij de klant moet het kredietlimiet bedrag ingevuld zijn. Bij de betreffende module moet het veld Krediet controle op ja staan.

Hoe wordt het kredietlimiet berekend?

Berekening

De volgende twee velden kunnen opgegeven worden bij Onderhoud relaties, tabblad Debiteurinfo en/of Crediteurinfo.

| Kredietlimiet bedrag | Het maximale bedrag aan krediet. |
| --- | --- |

| Kredietlimiet dagen | Het maximale aantal dagen aan krediet. |
| --- | --- |

Het kredietlimiet dagen is het aantal dagen van de betalingscondities + het aantal dagen overtijd (zie kolom Dgn ovt), als deze groter is dan het limiet, verschijnt er een melding. Houd rekening met het volgende:

- De al ingegeven orderbedragen worden niet meegeteld.
- Ook de orders die gefactureerd zijn, maar nog niet doorverwerkt, worden ook niet meegeteld.

Hierbij een voorbeeld:

Opmerking: Als het bedrag en dagen ingevuld zijn, worden de condities afzonderlijk gecontroleerd. In bovenstaand voorbeeld is het kredietlimiet dagen, morgen verstrekken.

- Dgn ovt, dagen overtijd wordt als volgt berekend: De huidige datum - betalingstermijn van de betalingsconditie - factuurdatum.

Waarom krijg ik de melding: Let op Kredietlimiet is overschreden.

Bij ingave van een order kan deze melding voorkomen, als het kredietlimiet(dagen) overschreden is.

- Voor meer informatie zie hierboven.

- Verkoopfacturen

---
## Wat doe ik als het grootboek niet in evenwicht is?

Als het verschil in het grootboek niet gevonden kan worden, doorloopt u de volgende stappen:

1. Vraag een audit lijst aan, per periode, zie Auditfile financieel (GUA). Opmerking: Bij periode moet het jaar hetzelfde zijn, er kan hierbij maximaal maar één boekjaar worden geselecteerd
2. De periode waarin het verschil is geeft een melding: Het volgende wordt weergegeven in de melding:- bedrag debet- bedrag credit- stuknummer- dagboek
3. Corrigeer het aangegeven stuknummer in het betreffend dagboek.
4. Controleer daarna of grootboek in evenwicht is.

- Wat doe ik als de balans / dagboek niet in evenwicht is?

---
## Hoe controleer ik of de eindbalans gelijk is aan de beginbalans?

Om de eindbalans van 2024 met de beginbalans van 2025 te controleren, doorloopt u de volgende stappen:

1. Ga naar Proef- en saldibalans (GLS). In Menu 3.0 onder Financieel bij Financieel overzichten.
2. Bij Periode vul in 12-24.
3. Kies voor de knop Afdrukken.
4. De eindstand staat in de rechterkolom onder Eind saldo.

Sluit het raadpleeg venster.

1. Bij Periode vul in 01- 25.
2. Kies voor de knop Afdrukken.
3. De beginstand staat in de linkerkolom onder Beginbalans.

Per grootboekrekening moet de eindstand gelijk zijn aan de beginstand.

- De beginbalans van 2025 kan je ook controleren via Overzicht mutaties per dagboek (GLD). Dagboek 99 (Beginbalans huidig jaar) en dan bij periode vanaf en t/m 01-25.
- Alleen het resultaat van het voorgaande jaar komt meestal op de algemene reserve erbij/af of anders op de tussenrekening Beginbalans

---
## Hoe controleer ik het BTW-nummer?

Het is het mogelijk om het (EU) BTW-nummer te controleren op geldigheid. De controle moet bij het betreffend land aan staan, anders verschijnt de controle knop niet.

#### Instellingen

Klik hier voor meer informatie om dit te doen:

1. Ga naarOnderhoud landen (BTL).
2. Kies voor de knop Wijzig.
3. Vul de ISO-Landcode in.
4. Bij BTW-nummer controle, selecteer Ja.
5. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Opmerking: Doe dit voor elk (EU) land dat gebruikt wordt.

#### Taak

Om bij een relatie het BTW-nummer te controleren, doorloopt u de volgende stappen:

1. Ga naar Onderhoud relaties (BRR), Of via Opvragen relaties.
2. Selecteer de relatie.
3. Kies voor de controle knop . Het BTW-nummer wordt gecontroleerd. Bij een geldig nummer verschijnt de melding: Dit BTW-nummer is geldig!
4. Als de BTW-validatie-services niet bereikbaar is, verschijnt de volgende melding: vanaf versie 3.23 Probeer het opnieuw, dit komt bijv. voor bij controle van BTWnummers die beginnen met DE of FR.
5. Kies voor de knop OK.

#### Resultaat

De wijziging is opgeslagen en achter het BTW-nummer verschijnt een groen V-vinkje met de laatste controle datum.

#### FAQ

Hoe komt het dat ik bij Opvragen relaties F6 geen controle knop zie?

Controleer of bij het betreffend land, de BTW-nummer controle op ja staat.

- zie Instellingen.

Waar kan ik het BTW-nummer allemaal controleren?

Bij de volgende programma's is de controle knop beschikbaar:

- Opvragen relaties F6
- Onderhoud relaties (BRR)
- Nieuwe relatie invoeren via webshop

- FAQ Relaties

---
## Hoe maak ik een creditnota?

Opmerking: Bij een credit nota kunnen geen (artikel) regels toegevoegd of aantallen gewijzigd worden.

Om een credit nota te maken, doorloopt u de volgende stappen:

1. Ga naar Opvragen debiteurposten (DO).
2. Geef de relatiecode in. De open staande posten verschijnen.
3. Selecteer de regel met de factuur die gecrediteerd moet worden.
4. Kies voor de knop Credit nota. Het scherm Aanmaak Creditnota verschijnt.
5. Op de eerste regel staat standaard Creditnota van factuur: .
6. Geef de referentie of ordergegevens in.
7. Vink eventueel de regels uit, die niet gecrediteerd moet worden. Het totaalbedrag wordt aangepast / herberekend.
8. Kies voor de knop Aanmaken credit. Het aantal wordt gecrediteerd d.w.z. met -1 vermenigvuldigd. Het scherm Lay-out selectie verschijnt instelling. Selecteer de gewenst lay-out en Kies voor de knop Ja.
9. De factuur verschijnt.
10. De creditnota wordt direct doorverwerkt en verschijnt bij Opvragen debiteurposten in de regels.

#### FAQ

- Er kunnen alleen regels uit of aangevinkt worden. Als er niets is aangevinkt, verschijnt de melding Geen regels geselecteerd bij de knop Aanmaken credit.

Als een factuur bestaat uit bijv. meerdere bonnen en deze wordt gecrediteerd, worden alle bonnen op één credit bon gezet.

Een werkorder met een vast bedrag excl. btw kan niet gewijzigd worden. Bij het uitvinken verschijnt de melding Regels uitvinken niet toegestaan bij vastprijs factuur!

Een credit nota wordt direct door verwerkt, met de huidige boekingsdatum en deze bepaald de boekingsperiode a.d.h.v. de betreffende periode tabel (bij gebruik van datumcontrole).

Bijv. op 01.06.2026 wordt geboekt in periode 06.2026.

Een Kleine machine komt weer op voorraad met de mutatie Credit.

Een creditnota zelf kan ook gecrediteerd worden.

Een rood rondje betekend, bij crediteren dat de machine statussen niet goed staan.

Hierdoor kan de machine regel niet gecrediteerd worden.

Tip: Als een bon op een verkeerde relatie gemaakt is, wordt deze eerst gecrediteerd en dan kan de bon gekopieerd worden naar de juiste relatiecode, zie onderstaande link.

Wat gebeurt er met een creditnota van een machine?

Bij een credit van een machine (verkoop) wordt de machine weer op voorraad geboekt.

- De inkoopstatus wordt voorraad. Klant wordt de leverancier en ordernummer / factuurdatum worden bijgewerkt.

De verkoopstatus wordt nvt.

- Eigenaar en ordernummer / factuurdatum worden op 0 gesteld.

Gesloten machine administratie

Het crediteren van een machine geldt volgende i.c.m. status is niet mogelijk:

- Als credit van een machine die nog op voorraad staat
- Als credit van een inruil die niet status voorraad is.

Hoe komt het dat ik de openpost nog niet zie?

Bij het aanmaken van een creditnota wordt de factuur direct doorverwerkt. Als de huidige periode niet overeenkomt kan het zijn dat de factuur nog niet wordt doorverwerkt.

Normaal moet een, afgedrukte factuur, eerst nog door verwerkt worden, dan verschijnt deze in de open post, zie:

- Doorverwerken facturen

Hoe komt het dat een bon in het grijs wordt weergegeven?

Als er meerdere bonnen aanwezig zijn, worden ter onderscheid de oneven bonnen grijs weergegeven, bijv.:

- Opvragen factuur
- Opvragen debiteurposten
- Hoe maak ik een kopiebon of order?

---
## Hoe maak ik een kopiebon of order?

In Powerall Connect kan op een gemakkelijke manier een 100% kopie van een bon, order gemaakt worden. Dit is mogelijk bij:

- Bonnen
- Verkooporders
- Inkooporders
- Offerte
- Werkorder
- Projecten

- Onderstaand wordt er vanuit gegaan dat bonnen gebruikt wordt, maar dit kan ook een ander programma zijn.
- Voor het maken van een credit nota zie: Hoe maak ik een creditnota?

Om een kopiebon te maken, doorloopt u de volgende stappen:

1. Ga naar Selecteren bonnen (FS).
2. Kies voor de knop Nieuw. Het scherm Invoeren/wijzigen verschijnt.
3. Selecteer de relatiecode en druk op twee keer op Enter. De knop Kopie van bon /  order verschijnt.
4. Vul de verplichte velden in de kop in.
5. Kies voor de knop Kopie van bon. Het scherm Kopiëren bonnen verschijnt.
6. Selecteer de relatiecode bron of bonnummer bron.
7. Selecteer bij aantallen de optie: Overnemen, aantallen worden overgenomen.
8. Nulstellen, aantallen wordt 0.
9. Positief <> negatief, aantallen worden bij positief negatief (en andersom) bij Creditbon of nota. Tip: Selecteer deze optie bij een creditnota.

Indien nodig wijzig de opties actuele prijzen / alleen tekstregels / kortingen overnemen.

Kies voor de knop Kopiëren.

- De melding Bon is gekopieerd verschijnt.
- Kies voor de knop OK.

De gegevens zijn gekopieerd naar de bon of order.

#### FAQ

Tip: Als een bon op een verkeerde relatie gemaakt is, kan de bon gekopieerd worden naar de juiste relatiecode.

- Deze optie kan ook gebruikt worden bij regelmatige terugkerende grote in-, verkoop of werkorders.
- Bij kortingen overnemen nee, wordt een prijsafspraak korting wel berekend.
- Een creditbon van een (kleine) machine kan alleen vanuit bonnen.
- Kopiebon van orders in vreemde valuta is niet mogelijk.

Belangrijk: Bij een credit werkorder worden de uren (d.m.v. urenregistratie) niet gecrediteerd, negatieve uren zijn niet mogelijk op een werkbon.

*Wat wordt er niet gekopieerd? Het volgende wordt niet gekopieerd: - Kopgegevens, zoals referentie en ordergegevens. - Interne notitie(s). - Kleine machine artikelen (met serienummer). - Machines. - Artikelen met alleen serienummer tracering worden wel gekopieerd (met eventuele melding bij bonnen). Deze moeten handmatig ingegeven worden. Hoe kan ik een gefactureerde werkbon* crediteren?

Het handigste is om de bon te crediteren (bij urenregels staan deze er ook op).

- Hoe maak ik een creditnota?

---
## Hoe stel ik E-aanmaningen of herinneringen in?

Voor aanmaningen en herinneringen per e-mail te versturen, moet er een e-mail server aanwezig zijn of kan de Powerall Connect- mail server gebruikt worden. De volgende gegevens zijn hierbij nodig om deze e-mails te kunnen verzenden.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Instellingen documentbeheer (BIE)
2. Kies voor de knop Wijzig.
3. Op tabblad Algemeen moeten de gegevens, afzender, en server in (gebruikersnaam en wachtwoord zijn niet verplicht) gevuld zijn.
4. Ga naar tabblad Aanmaningen.
5. Vul de gegevens in, zoals afzender, onderwerp, bodytekst, etc.
6. Kies voor de knop Opslaan.

De aanmaningen of herinneringen kunnen per e-mail verzonden worden.

#### Standaard tekst

In onderstaande administratie , met submap Mail, is een standaard tekst in bestand E-herinnering.txt opgenomen worden, die in de e-mail komt te staan, bijv.

Hieronder een uitleg van de velden van scherm Instellingen documentbeheer:

| Tabblad Algemeen |  |
| --- | --- |

| Afzender mailadres | De afzender van de e-mail adres. |
| --- | --- |

| Gebruik Powerall Connect-mailserver | Optie om de Powerall mailserver te gebruiken:- Nee (standaard) - Ja Opmerking: Hiervoor moet uw domeinnaam eenmalig ingericht worden, neem contact op met de helplijn om dit te activeren.• Aan het gebruik van de Powerall-mailserver zijn geen extra kosten verbonden. |
| --- | --- |

| Server uitgaande mail SMTP | De server van de uitgaande e-mails (SMTP) van uw internet provider, bijv. smtp.

.nl..Opmerking: Het is ook mogelijk om een specifieke poort aan te geven, door achter de uitgaande mailserver of IP-adres een dubbele punt gevolgd door het poortnummer, toe te voegen. Bijvoorbeeld smtp.office365.com:587 of 88.164.49.9:25 (25=SMTP of 465= SSL of 587=TLS). | | --- | --- | | Gebruikersnaam | Dit is de gebruikersnaam, waarmee ingelogd wordt op de e-mail server, is niet verplicht. | | --- | --- | | Wachtwoord | Dit is het wachtwoord, waarmee ingelogd wordt op de mailserver. Bij opgave is wachtwoord niet zichtbaar. | | --- | --- | | Gecodeerde verbinding (SSL) | Er is sprake van geen of wel een beveiligde verbinding.- Nee, (standaard)- Ja, bij deze instelling moet de server gecodeerde verbindingen via STARTTLS ondersteunen. Dit wordt vaak toegepast in combinatie met poort 587. Directe SSL-verbindingen over poort 465 worden niet ondersteund. | | --- | --- | | Instellingen testen | | | --- | --- | | Testmail verzenden aan | Vul hier het in, waar naar de testmail verzonden moet worden. NB De domeinnaam van het emailadres moet geregistreerd zijn. | | --- | --- | | Tabblad Facturering | | | --- | --- | | Bodytekst bestandspad credit | In dit tekst bestand kan de standaard tekst bij een creditnota (zonder betaallink) ingegeven worden, vanaf versie 3.31.- Leeg (standaard) | | --- | --- | | | | --- | | Voorvoegsel factuurbijlagen | Het voorvoegsel van de factuurbijlagen: - leeg (standaard)- d.w.z. alle bestanden in de factuur dossier map, die beginnen met , kunnen worden toegevoegd bij het versturen van de factuur. ( kan ook een andere naam zijn bijv. ) | | --- | --- | | Verstuur werkbonnen als bijlage | Optie voor het versturen van de werkbonnen als bijlage:- Nee (standaard) - Ja De _Werkbon wordt automatisch toegevoegd bij Einde werk, en als bijlage meegestuurd. | | --- | --- | | Tabblad Facturering / Aanmaningen / Incasso | | | --- | --- | | Verzend modus | Optie voor het verzenden van e-mail:- Geen selectie, (standaard).- Outlook, hierbij is de afzender de betreffende gebruiker.- Fallback, er wordt eerst via Outlook geprobeerd te verzenden en als dat niet lukt via SMTP.- SMTP direct. | | --- | --- | | Afzender mailadres | De afzender van de e-mail adres. | | --- | --- | | Onderwerp | Het onderwerp van de betreffende e-mail.Bijv. bij facturering: Uw factuur van | | --- | --- | | Bodytekst bestandspad | In dit tekstdocument (inclusief bestandspad) wordt de standaard tekst van de e-mail weergegeven.Opmerking: • Als er in dit veld emailbody.txt staat zonder pad ervoor, kijkt Powerall Connect naar dit bestand in de administratiemap .• Bij emailbody\emailbody.txt kijkt Powerall Connect in de map emailbody in de administratiemap.* Alleen bij verzend modus SMTP kan er ook een .html bestand verzonden worden, zie ook Opmaak e-mail berichten/facturen in .html formaat bij SMTP. | | --- | --- | | Standaard BCC adres | Dit is het e-mail adres dat een kopie ontvangt van de verzonden e-mail, deze afzender BCC (Blinde Carbon Kopie) is niet zichtbaar voor de ontvanger van de e-mail. Dit adres kan handig zijn, om de verzonden e-mails te controleren. | | --- | --- | | Pop-up | Optie hoe een e-mail verzonden wordt:- Nee, (standaard) - Ja, er verschijnt een Outlook Pop-up scherm. | | --- | --- | | Tabblad Inkooporders | | | --- | --- | | | | --- | | Bijlagen gecomprimeerd verzenden | Optie om de bijlage(s) gecomprimeerd te verzenden, bij Selecteren inkooporders >, knop E-mail, bij Ja zie je een pop-up met de te verzenden e-mail. - Ja direct verzenden, alleen PDF wordt verzonden. - Ja apart opslaan, er wordt ook een apart .zip bestand opgeslagen. - Nee, alleen PDF word verzonden. | | --- | --- | | Tekening bestandstype | De bestandstype van de (eventuele) te verzenden tekeningen, bijv. JPEG, STL, DFX, IGES of STEP. De bestanden staan in de artikel Dossiermap. De opmaak van de te verzenden bestanden dient vooraf ingesteld te worden binnen GSY12, tabblad Tekeningen . | | --- | --- | | tabbladen Offerts Kassa/bonnen Verkooporders | | | --- | --- | | Tabblad Werkorders / Werkbonnen | M.b.t. werkorders zie ook FAQ. | | --- | --- | | Tabblad Uren / Keuringsherinneringen | | | --- | --- | | Standaard BCC adres | Dit is het e-mail adres dat een kopie ontvangt van de verzonden e-mail, deze afzender BCC (Blinde Carbon Kopie) is niet zichtbaar voor de ontvanger van de e-mail. Dit adres kan handig zijn, om de verzonden e-mails te controleren. | | --- | --- | | Tabblad Verhuur | | | --- | --- | | Tabblad Machines | Vanaf versie 3.29, zie Machine kaart verzenden. | | --- | --- |

#### Onderhoud klanten

Als een klant standaard een e-aanmaning krijgt, kunt u dit instellen. Om dit in te stellen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud relaties (BRR).
2. Ga naar tabblad E-document.
3. Kies voor de knop Wijzig.
4. Vink Aanmaning, E-mail/PDF aan.
5. Kies voor de knop Opslaan.

Bij aanmaningen, wordt bij deze klant automatisch de kolom aangevinkt, met het printer en PDF symbool.

---
## Hoe voer ik een jaarwissel uit?

Kies afhankelijk van wat gebruikt wordt voor:

- Jaarafsluiting - 3.0 menu
- Jaarafsluiting - klassiek menu

Deze jaarwissel heeft betrekking op de wissel van 2025 naar 2026.

- Periode / maand afsluiting Periodiek

Artikelen openen nieuwe periode

Overnemen beginbalans

FAQ Periodewissel

---
## Hoe voer ik een periodewissel uit?

Om dit te doen, zie:

- Periodewissel

- FAQ Periodewissel
- Jaarafsluiting
- Taakplanner instellen

---
## Hoe wijzig ik de aanmaningstekst?

Om de tekst op de aanmaningen te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud layouts (BPO).
2. Selecteer het programma en lay-out, bijv. FDE59 met layout H. De volgende aanmaningsprogramma's worden gebruikt: FDE58 - Print herinneringen FDE59 - Print aanmaningen FDE60 - Periodieke aanmaningen Gebruik periodieke aanmaningen moet op ja staan.
3. Bij een gedeeld relatie bestand wordt het veld "Geen datum controle" getoond. NB Als deze uitgevinkt wordt, wordt er geen datum gecontroleerd.
4. Ga naartabblad Detail kies Pagina kop.
5. Selecteer het veld LBL016.
6. Dubbel klik bij Waarde op het ... 3-puntjes-icoon.
7. Kies voor de knop Wijzig. Wijzig de tekst, bijv. het banknummer of IBAN-nummer.
8. Kies voor de knop Opslaan.De tekst is opgeslagen.

Om meer tekstcodes op te voeren, doorloopt u de volgende stappen:

1. Vink Label aan. (bij tabblad Detail kies Pagina kop)
2. Kies voor de knop Toevoegen. Label wordt toegevoegd.
3. Klik op het nieuwe label, de eigenschappen verschijnen.
4. Pas de Hoogte en Breedte aan.
5. Bij meer dan 40 teken wijzig type van F naar .
6. Klik bij Waarde op de drie puntjes ... Een pop-up met Omschrijving verschijnt, Bij volgnummer vul  in.
7. Bij taalcode vul  in of andere taal.
8. Vul de  in.
9. Kies voor de knop Opslaan.
10. Verplaats de tekst naar de gewenste (afdruk) positie.

Kies voor de knop Opslaan.

De aanmaningstekst is gewijzigd.

- Lay-out wijzigen

---
## Hoe wijzig ik de factuurtekst?

#### Voordat u begint

De vaste tekstregel 1 en 2 moeten op de betreffende factuur lay-out staan.

Tip: Indien deze tekstregels niet op de factuur lay-out staan kunt u deze velden SYS330 en SYS340 toevoegen in de 'factuur voet' zie Lay-out wijzigen.

#### Taak

Om de twee tekstregels op de factuur te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Kopie facturen (FFK) of Print facturen (FFK). Het scherm Print (kopie) facturen verschijnt.
2. Wijzig bij Vaste tekstregel 1 en 2 de .
3. Indien nodig wijzig het t/m relatiecode naar 1, anders worden alle facturen afgedrukt.
4. Kies voor de knop Afdrukken. De facturen worden getoond. Opmerking: De factuurteksten worden pas opgeslagen bij het gebruik van de knop Afdrukken.
5. Sluit de facturen.
6. Sluit Print (kopie) facturen.

#### Resultaat

De factuurtekstregels zijn opgeslagen en worden getoond bij alle opties van het menu Factureren.

---
## Hoe wijzig ik een factuur?

f

# Hoe wijzig ik een factuur?

In Powerall Connect is het mogelijk een aangemaakte factuur te wijzigen t/m factuurstatus (2) Factuur, zie onderstaand afbeelding bij filter. De factuur is dan nog niet verwerkt in het grootboek en openposten.

- Dit kan vooral handig zijn als er fouten constateert worden in een factuur voordat deze naar de klant gestuurd wordt. Hierdoor is het niet nodig de factuur te crediteren en een nieuwe factuur aan te maken.

Om een factuur te wijzigen, doorloopt u de volgende stappen:

1. Zoek de betreffende factuur op en onthoud het bonnummer van de bon die gewijzigd moet worden.
2. Ga naar Selectie te wijzigen facturen (FDW). Kies de betreffende relatie en voer het bonnummer in of zoek direct het bonnummer op F4 (kopieer deze, zie stap 3b).
3. Kies voor de knop Wijzigen.De status wordt Pakbon (1).

Ga vervolgens naar Wijzigen bonnen (FW).

1. Selecteer de relatiecode.
2. Open vervolgens in het veld Bonnummer het zoekvenster door F4 of het vergrootglas te kiezen (plak het bonnummer).
3. Selecteer bij filter Factuur. Belangrijk: Dit zijn alleen wijzigingen van teksten, artikelen, aantallen en prijzen. Factuuradresgegevens kunnen niet aangepast worden.
4. Dubbelklik vervolgens op de te wijzigen bon.
5. Wijzig de benodigde gegevens.
6. Kies voor de knop Einde Bon.

Ga naar Kopie facturen (FFK).

- Het scherm Print kopie facturen verschijnt.

1. Geef het factuurnummer in bij vanaf (bij t/m wordt deze automatisch ingevuld).
2. Kies voor de knop Afdrukken.

De gewijzigde factuur is afgedrukt.

#### FAQ

Opmerking: De factuur kan altijd opnieuw afgedrukt worden, via Kopie facturen (FFK).

Wat zijn de factuureisen van de balastingdienst?

In onderstaande link staan de eisen voor de (BTW) factuur.

- belastingdienst.nl/.../factuureisen

---
## FAQ Facturatie

In dit hoofdstuk staan de meestgestelde vragen over de facturatie e.d.

- Hoe maak ik een kopiebon of order? Hoe maak ik een creditnota?

Hoe wijzig ik de factuurtekst?

Hoe wijzig ik een factuur?

Hoe, wat m.b.t. de betaallink

Hoe, wat m.b.t. Peppol

Hoe, wat m.b.t. verzamelfacturen

Algemeen

Tip: Gebruik Overzicht bonnen / rapportages uitgebreid, lay-out B waar alle velden te zien zijn, om te controleren als een factuur fout is, wat er precies fout gegaan is.

*Hoe kan ik opnieuw een factuur sturen? Het is mogelijk om een factuur opnieuw naar de klant te sturen, dit is afhankelijk van: 1. Het gebruik van E-facturen. Zie E-facturen , vink hierbij Al verzonden aan. 2. Zo niet, dan via Opvragen relaties F6, tabblad Bonnen of Open posten. Via de knop Kopie factuur. Voor meer info zie Kopie facturen. Hoe kan ik een al verzonden e-factuur nog een keer verzenden? Om een factuur opnieuw te verzenden, doorloopt u de volgende stappen: 1. Ga naarVerkoop > Facturen > E-facturen. 2. Zet bovenaan de radio-knop op al verzonden. 3. Vul gewenste selectie in. 4. Kies voor de knop Selecteer. 5. Vink de te verzenden factuur aan. 6. Kies voor de knop Afdrukken en verzenden. De factuur is verzonden, de Verzenddatum is bijgewerkt. Hoe voeg ik een bijlage toe aan mijn factuur? Het is mogelijk om één of meerdere bijlage(n) automatisch toe te voegen aan een E-factuur. - Voor meer informatie zie Dossier - Dossiers Bijlage samenvoegen. Bij Peppol kunnen alleen PDF bijlage mee gestuurd worden. Hoe zie ik de facturen die nog niet doorverwerkt zijn? 1. Ga naar Overzicht bonnen / rapportages kort (FLV). 2. Kies bij Status Gefactureerd vanaf 2 t/m . 3. Kies voor de knop Afdrukken. Hoe zie ik of een factuur al betaald is en wanneer? Bij Opvragen debiteurposten (DO) kan per debiteur de openstaande posten bekeken worden. Standaard staan hier de actuele open posten. - Wanneer de post er niet tussen staat, zal die in de meeste gevallen al betaald zijn. Dan kan er in het scherm geklikt worden op historisch en is de datum selectie aan te passen. - Selecteer de verkoopfactuur. - Kies voor de knop Betaalinfo. - Er verschijnt dan een scherm wanneer en via welke bank de factuur betaald is. E-facturen Belangrijk: Het gebruik van verzamelfacturen wordt sterk afgeraden bij E-facturatie.• Uitgangspunt is dat alles herleid-/koppelbaar is, dus 1 order = 1 pakbon = 1 factuur. Instellingen Hoe gebruik ik de bedrijfsnaam 2 in de XML bestand bij E-facturen? - Standaard wordt de bedrijfsnaam 1 gebruikt in het UBL .XML bestand. - Het is ook mogelijk d.m.v een specifieke instellingen de bedrijfsnaam 2 te gebruiken. - Neem hiervoor contact op met de helpdesk. Instellingen bedrijf voor elektronisch factureren: Bij Instellingen bedrijf (BIB) moeten de volgende velden gevuld zijn: - | IBAN-nummer | Het International Bank Account Number (IBAN) identificeert elke rekeninghouder, inclusief bank en vestigingsland, van de relatie of bedrijf. Het nummer is in feite een internationaal bankrekeningnummer en moet geldig zijn.- Het IBAN-nummer van het bedrijf is o.a. nodig voor UBL facturen. | | --- | --- | | BIC-code | Het Bank Identifier Code (BIC) van betreffende bank. Gebruikt voor internationale betalingsoverdrachten. Moet gevuld zijn bij buitenlandse betalingen. | | --- | --- | | BTW-nummer | Dit is het BTW nummer van het bedrijf.- Dit nummer is nodig voor UBL facturatie. | | --- | --- | | KvK-nummer /Ondernemersnr (BE) | Het Kamer van Koophandel nummer (CoC) of Ondernemersnummer / KBO voor België. - Dit nummer is o.a. nodig voor UBL en Peppol (e-facturatie). | | --- | --- | Van Onderhoud relaties (BRR), tabblad E-document, worden de instellingen overgenomen, hoe de factuur verzonden moet worden. #### Mailserver Ook moet er een (mail)server ingesteld zijn, die de facturen verzendt, zie: - Instellingen documentbeheer E-facturatie werkwijze Hoe stuur ik een E-factuur ook naar een CC? Een E-factuur kan ook naar een cc e-mailadres gestuurd worden. Om dit te doen,doorloopt u de volgende stappen: 1. Ga naar Onderhoud relaties (BRR). 2. Selecteer de relatie. 3. Kies voor de knop Wijzig. 4. Ga naar het tabblad E-document. 5. Vink Gebruik algemene contactgegevens uit. Bij pop-up E-document instellingen wijzig. 6. Kies voor de knop Ja. Selecteer bij Contact een contactpersoon (deze moet(en) op het tabblad Contacten wel aangemaakt zijn). Vink CC sturen aan. - Het e-mailadres verschijnt. Kies voor de knop Opslaan. Bij het verzenden van een e-factuur gaat er een cc e-mail naar de geselecteerde contactpersoon. Kan ik van een gewone factuur nog een E-factuur maken? - Dit is niet mogelijk, de factuur is al aangemaakt. - Druk de factuur naar PDF af en e-mail de factuur naar de klant. Hoe zit het met de order referentie* of *ordergegevens*?

Referentie komt in het veld Note (vrije notitie), omdat hier vaak iets als 'Rep. maaier' staat.

Ordergegevens gaat naar OrderReference, wat specifiek is voor een inkoopordernummer.

Via Peppol kan Extra informatie verzonden worden, vanaf versie 3.30.

*In welke map staan de XML en PDF facturen? In de map VERKOOPFACTUUR wordt voor elke pdf een submap aangemaakt, bijv.: - \\\PW\\VERKOOPFACTUUR\ Wat doe ik als bij Office365 bij het verzenden van een grote mail batch, de volgende foutmelding 'De externe host heeft de verbinding' verschijnt? Office 365 hanteert een message rate limit / vast limiet van 30 berichten per minuut per mailbox, om misbruik en smap tegen te gaan. - Maak gebruik van de SMTP server van de provider of van de gratis Powerall Connect-mailserver. - Bij E-factuur uitgaand wacht even, met het verzenden van de facturen. Overige Hoe lang kan mijn factuurnummer* zijn?

Maximaal kan een factuurnummer 8 cijfers lang zijn. Het factuurnummer wordt rechts uitgelijnd.

Hoe stel ik een aparte factuurnummers voor (machine) Verkopen, Werkorders of Verhuur/contracten in?

De bonnen worden standaard verzameld worden op één factuur.

- Bij Onderhoud relaties, tabblad Debiteurinfo, staat het veld verzamelfactuur dan op ja.

Het is mogelijk om aparte facturen aan te maken voor / door in de betreffende module onderstaand veld(en) te wijzigen:

- Bij Instellingen werkorders, tabblad Beheer, veld werkorders apart factureren, op ja te zetten.
- Bij Instellingen verkooporders, tabblad Beheer, veld orders apart factureren op ja te zetten.
- Bij Instellingen verhuur/contract, tabblad Uitvoer printer, veld print verzamelfactuuren op nee te zetten.

Daarnaast moet bij Instellingen facturering, tabblad Beheer, de betreffende module op apart facturen ja gezet worden.

Kan ik een order direct factureren?

Ja dit is mogelijk, als deze optie ingesteld en geautoriseerd is. Dit kan alleen bij de volgende programma's:

- Invoeren/wijzigen bonnen.
- Invoeren/wijzigen verkooporders.
- Selecteren werkorders via Meer functies > Direct factuur
- Invoeren/wijzigen- en Selecteren contracten / verhuurorders

Neem contact op met de planner om dit in te laten stellen.

Belangrijk: Direct facturering werkt niet goed / bij met gebruik van E-factuur uitgaand, dit is opgelost vanaf versie 3.30

Welke xml-formaten worden allemaal ondersteund bij E-facturen inkomend?

De volgende formaten worden ondersteund:

- Granit open TRANS XML-facturen
- Grimme
- John Deere
- Mechan
- Simplerinvoicing
- UBL2.1 bestanden (Kramp)

UBL

Klik hier, voor meer informatie over dit onderwerp.

Wat is UBL?

UBL (Universal Business Language) is het standaard formaat voor elektronisch factureren. Het is een XML bestand die speciaal is uitgedacht voor facturen. Een e-factuur is géén PDF-bestand.

- Een UBL factuur maakt het mogelijk om factuurdata van boekhoudpakket A naar boekhoudpakket B te sturen. De UBL factuur kan hierdoor direct ingelezen worden zónder handmatige invoering.
- Het is daarbij mogelijk om via het Europese PEPPOL netwerk e-facturen te sturen naar KvK- en OIN nummers. Hoe, wat m.b.t. Peppol

In de Powerall Connect E-facturen staat het volgende, over de UBL versie in de XML:

- 2.1
- UBL-formaat SI-UBL 2.0

De variant die ondersteund wordt, is SI-2.0 / NLCIUS. Deze versie sluit goed aan bij externe systemen.

Welke gegevens zijn belangrijk bij E-facturen met name SI-UBL 2.0?

De volgende gegevens moeten gevuld zijn om te voldoen aan de 'business rules':

- Bij de klant, het KvK-nummer.
- Bij de order, de referentie en ordergegevens.

De 'business rules' zijn vastgelegd door de Nederlandse Peppol autoriteit (NPa).

Waar vind ik nog meer informatie over UBL?

Op de website van softwarepakketten staat meer informatie over UBL ketentest. Hier staat Powerall Connect vermeldt als 'leverancier bedrijfsprocessen in meerdere branches'.

- Voor meer informatie zie UBL ketentest.

Waar of hoe kan ik een UBL bestand controleren?

#### UBL validator / factuur wordt niet herkend

Om een UBL bestand te controleren, doorloopt u de volgende stappen:

1. Ga naarhttps://test.peppolautoriteit.nl/validate ofhttps://ecosio.com/en/peppol-and-xml-document-validator/
2. Kies bij Rule set UBL Invoice 2.1. Kies bij een credit nota UBL Credit note 2.1
3. Selecteer het .xml bestand, bij Select file. Het bestand wordt gecontroleerd.

Er verschijnt een melding of het bestand al of niet voldoet.

Tip: Handig: E-facturen versturen via de Powerall mailserver.

- Facturatie

- Wiki UBL Invoice (factuur)

---
## FAQ Periodewissel

In dit hoofdstuk staan de meestgestelde vragen over de periodewissel.

- Hoe voer ik een periodewissel uit?

Kan ik de periodewissel ook automatisch uit laten voeren?

Ja, dit is mogelijk via de Taakplanner.

Belangrijk: Bij de Jaarafsluiting moet de Periodewissel altijd de handmatig uitgevoerd worden.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

### Jaarwissel

- Hoe voer ik een jaarwissel uit? Hoe controleer ik of de eindbalans gelijk is aan de beginbalans?
- Wat doe ik als de balans / dagboek niet in evenwicht is?
- Wat doe ik als debiteuren of crediteuren niet aansluiten met het grootboek?
- Wat doe ik als het grootboek niet in evenwicht is?

Kan de Jaarwissel automatisch uitgevoerd worden?

Nee, de jaarwissel kan niet automatisch worden uitgevoerd via de Taakplanner.

Belangrijk: Bij de Jaarafsluiting moet de Periodewissel altijd de handmatig uitgevoerd worden.

Wanneer moet je de jaarwissel precies doen, op de eerste werkdag van het nieuwe jaar of op de laatste werkdag van vorig jaar?

Het maakt niet uit of de jaarwissel in het oude of nieuwe jaar uitgevoerd wordt.

- Deze moet uitgevoerd worden, voor er geboekt kan worden in het nieuwe jaar.

Belangrijk: Zorg er voor dat de facturen, van het oude jaar, gemaakt - en doorgeboekt zijn.

- Periodiek

---
## Wat doe ik als debiteuren of crediteuren niet aansluiten met het grootboek?

Het volgende kan zich voordoen bij de subadministratie van debiteuren en/of crediteuren:

- Het saldo van de Debiteuren open posten (DLP) zie #2 is niet gelijk aan de grootboekrekening(en) debiteuren (GO).
- Het saldo van de Crediteuren open posten (KLP) zie #3 is niet gelijk aan het grootboek crediteuren (GO).

- In Menu 3.0 is dit: #=nummer

#### Controles

Om de saldo's te controleren (in dit geval van de debiteuren), doorloopt u de volgende stappen:

1. Ga naar Opvragen grootboekmutaties (GO). In Menu 3.0 onder Financieel > Financieel basis.
2. Ga naar tabblad Cumulatief 5 jaar.
3. Controleer of het eindsaldo van dit jaar (A) gelijk is aan het beginsaldo van het volgend jaar (B). Als het verschil geldt voor het huidige jaar, neem dan de beginbalans over: Zie Overnemen beginbalans (GPA).
4. Als het vorig jaar betreft, neem dan contact op met de helpdesk.

---
## Wat doe ik als het betaalbestand / incassobestand afgekeurd wordt?

Doel

Deze validator geeft aan op welke positie er een fout zit in het incasso- of betaalbestand. Vaak is er een IBAN-nr of BIC-code foutief ingevoerd in Powerall Connect.

#### Validator

Onderstaande validator is verouderd, werkt niet voor nieuwste sepa versies:

- Debiteuren incasso - pain.008.001.08
- Crediteuren betalingen - pain.001.001.009

Om dit bestand te controleren, doorloopt u de volgende stappen:

- Ga naar https://www.mobpain.001.001.009 ilefish.com/services/sepa_xml_validation/sepa_xml_validation.php 1. Bij Upload XML file kies voor de knop Bladeren. Selecteer het .xml bestand. 2. Kies het juiste schema bij XSD input (standaard No XSD schema). Voor een betaalbestand pain 001.001.03of 3. Voor een incassobestand pain.008.001.02.
- Geef de Acces Code in. Neem deze over van het scherm.

Kies voor de knop Validate.

Controleer de output.

Als alles goed is staat er:

- XML document is well-formed.
- XML document does validate against XSD schema.

In onderstaand voorbeeld is de BIC-code niet correct.

.

Om dit op te lossen, doorloopt u de volgende stappen:

1. Zoek in het XML bestand de klant op, waarbij de gegevens niet juist zijn.
2. Rechtermuisknop > Openen met > Microsofte Edge.
3. Om de klant te zoek, druk op de knoppen CTR + F, een geef hier de foute waarde in.

Corrigeer bij Onderhoud relaties de foutieve gegevens van deze klant.

Bij een betaalbestand:

1. Maak de batch op nieuw aan bij Aanmaken betaalbatch (KAA).
2. Importeer deze opnieuw bij de bank.

- Crediteuren betalingen
- Incasso's

---
## Wat is een kostendrager?

Een kostendrager is een eindproduct (bijv. machine) of project, waaraan kosten toegeschreven worden.

- Uitgezonderd de kosten kunnen ook inkomsten toerekenen worden aan kostendragers.
- Zo kan d.m.v. marge-analyses het resultaat berekend worden.

#### Overzicht kostendrager

Om een overzicht aan te vragen, doorloopt u de volgende stappen:

1. Ga naar Mutaties per kostendrager (GDM).
2. Maak eventueel een selectie.
3. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

FAQ

Wat is zijn de verschillen tussen kostenplaatsen, kostensoorten en kostendrager?

Hierbij een overzicht:

| Soort | Bijvoorbeeld |
| --- | --- |
| Kostenplaats | Afdelingen, locaties of teams binnen een onderneming |
| Kostensoort | Huisvestingskosten, materiële kosten, reiskosten of opleidingskosten etc. |
| Kostendrager | De eenheid waaraan je de kosten en opbrengsten toeschrijft zoals machines, producten of projecten.Een kostendrager kan op een balans- en V&W rekening geboekt worden, een kostenplaats alleen op een V&W rekening. |

Waar kan ik o.a. de kostendrager zien / gebruiken?

Bij de volgende programma's kan een kostendrager ingegeven worden:

- Boeken inkooporder machines
- Vanaf versie 3.28 bij: Kas of bank boeken
- Inlezen/verwerken bankafschriften

Bij een kostendrager machinegroep icm machine administratie 2.0 is nee, worden deze Referentie Verkoop-/exploitatiekosten geboekt op tabblad Transacties.

Standaard journaalposten importeren / boeken vanaf versie 3.28.

De kostendrager (kolom) is zichtbaar bij diverse grootboek programma's:

- Opvragen grootboekmutaties
- Afletteren grootboekmutaties
- Overzicht mutaties per dagboek

Waar kan ik een voorbeeld zien van een kostendrager boeking?

Voor meer info zie Boeken inkooporder machines FAQ.

Opmerking: De module Kostendrager is een aparte module, naast de kostenplaatsen.

Waar wordt op de module kostendrager gecontroleerd?

Bij de volgende programma's wordt gecontroleerd of er voor deze module een licentie is, vanaf versie 3.22.

- Mutaties per kostendrager (GDM).
- Controle machine inkopen (MVC).

Deze controle gebeurt als in Instellingen financieel Kostendragers op Ja staat.

Welke soorten kostendragers zijn er?

Bij Onderhoud grootboekrekeningen kan aan een grootboekrekening de volgende kostendragers worden toegekend:

| Kostendrager | Optie voor het soort kostendrager:- N.v.t. (standaard)- Machine (bij een inkoop machine factuur wordt een machine transactie hierbij weggeschreven).gebruikt bij Interne werkorders .- Project- Werkorder- Activa, gebruikt bij Inkoopfactuur boeken. |
| --- | --- |

- Onderhoud kostenplaatsen

---
## Wat wordt er gewijzigd bij een BTW-tarief wijziging?

#### Wijziging

Op 1 januari 2019 is lage BTW-tarief (NL) verhoogd van 6% naar 9% in Nederland.

Belangrijk: Dit programma wijzigt het BTW percentage van 6 naar 9% en past de diverse BTW omschrijvingen aan.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Bijwerken BTW-percentage (BAS).
2. Kies voor de knop Update.
3. Kies voor de knop OK.
4. Het volgende PDF bestand wordt geopend: Opmerking: Als er geen PDF-reader aanwezig is, open in de WRK map het .html bestand in de browser bijv. IE of Chrome.
5. Controleer of deze lijst volledig is.

De BTW is bijgewerkt.

Belangrijk: Bij filiaalcommunicatie moet de BTW-update op alle laptops lokaal ook uitgevoerd worden!

---
## FAQ Financieel

In dit hoofdstuk staan de meestgestelde vragen over de Financiële modules.

- FAQ activa
- FAQ Crediteuren
- FAQ Debiteuren
- FAQ Periodewissel
- Wat doe ik als het betaalbestand / incassobestand afgekeurd wordt?
- Hoe controleer ik het BTW-nummer?
- Wat doe ik als de financiële voorraad niet aansluit met de machines?
- Wat is een kostendrager?
- Wat wordt er gewijzigd bij een BTW-tarief wijziging?

Hoe kan ik zien welke facturen geboekt zijn, op een BTW-code?

Om de facturen te zien, met een bepaalde BTW-code, doorloopt u de volgende stappen:

1. Ga naarMutaties per BTW-code (GWM).
2. Laat Details of totalen op details printen staan.
3. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

Hoe controleer ik een afwijking in de BTW aangifte?

Als er een afwijking in de BTW aangifte zit, kunt u snel controleren waar een foutje gemaakt is, tijdens het boeken. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naarControle BTW aansluiting (GWC).
2. Geef de

op. 3. Kies voor de knop Afdrukken. Alle afwijkingen van het goede BTW percentage worden hier weergeven. Indien nodig kunt u de boekingen herstellen en de BTW-aangifte kloppend maken.

Hoe controleer ik of het BTW-tarief gewijzigd is?

Om het BTW-tarief te controleren, doorloopt u de volgende stappen:

1. Ga naar Onderhoud BTW-codes (BTC)
2. Selecteer de BTW laag.

Hier moet het juiste BTW % staan, bijv. voor Nederland 9%.

Hoe importeer ik journaalposten in Powerall Connect vanuit een Excel bestand in het memoriaal?

- Voor meer informatie zie Importeren bij Memoriaal boeken.

Waar kan ik mijn bankgegevens, zoals bestandsformaat opgeven?

Bij Onderhoud dagboeken kunnen de incasso / betaalgegevens en de in te lezen bankgegevens opgegeven worden.

Wat doe ik bij verschillen in de balans of het grootboek?

Voor het oplossen van een verschil zie FAQ Periodewissel.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Financieel

---
## FAQ Algemeen

In dit hoofdstuk staan de meestgestelde vragen over de Powerall Connect algemene module(s).

- FAQ Beheer
- FAQ Gebruikers
- FAQ Lay-outs / Word
- FAQ Relaties
- FAQ Taal
- Hoe, wat kan ik ... m.b.t. dashboard / selecteren programma's?
- Hoe voeg ik een dossier template toe, voor Relaties of Artikelen of Machines?
- Hoe zoek ik in deze documentatie iets op?
- Hoe werkt SMS?
- Hoe werkt WhatsApp?
- Wat kan ik allemaal doen met een overzicht?
- Welke regels gelden voor deze help documentatie?
- Wat is de historie van de online documentatie?

Waar kan ik een bestand importeren?

Importeren van regels is mogelijk bij alle order invoerprogramma's:

- Invoeren/wijzigen bonnen / offertes / verkooporders / werkorders

Daarnaast bij;

- Selecteren inkoopfacturen
- Goedkeuren besteladvies, importeren besteladvies in bestelregels.

Dit kan door gebruik te maken van de knop Importeren.

Wat moet ik doen als de Dossier knop niet meer werkt?

Probleem

Als ik op de Dossier knop drukt, gebeurt er niets.

Oorzaak

Mogelijk is het dossierpad niet goed ingesteld en/of gewijzigd.

Oplossing

Controleer de dossier mappen bij de betreffende administratie.

- Neem hiervoor contact op met de helpdesk, om dit op te lossen.

- Algemeen / basis

---
## FAQ gedeelde (administratie) gegevens

In Powerall Connect kunnen de relaties, artikelen en machinegegevens gedeeld worden met meerdere administraties.

Opmerking: De CRM gegevens worden altijd gedeeld.

Waar kan een gedeeld bestand ingesteld worden?

Bij Onderhoud administraties kan ingesteld worden dat een administratie gedeeld wordt.

Tip: Neem hiervoor contact op met de helpdesk of verkoopafdeling.

Let op! Doe dit niet zelf, want een aantal bestanden moeten dan samengevoegd worden.

Wanneer gebruik je gedeelde gegevens?

- Gedeelde gegevens worden alleen gebruikt indien er meer dan één administratie aanwezig is.
- Als de relaties en/of artikelen en/of machines hetzelfde zijn bij de betreffende administraties.

Welke gegevens kunnen gedeeld worden?

De volgende gegevens kunnen met een andere administratie gedeeld worden:

- Relaties
- Relaties + artikelen
- Relaties + artikelen + machines

Welke tabbladen worden bij Opvragen relaties gedeeld?

Bij gedeelde relatiegegevens, zijn bij Opvragen relaties F6 alleen de volgende tabbladen hetzelfde:

- Algemeen
- Contact
- Afleveradressen
- Dossier
- Machines

De overige tabbladen zijn administratie afhankelijk.

Is het ook mogelijk zonder gedeelde gegevens, de voorraad inzichtelijk te krijgen van een andere administratie of vestiging.

Ja, dit kan alleen voor de artikelvoorraad, zie FAQ Voorraad / magazijn.

Is het mogelijk om de open posten van meerder administraties op een overzicht te krijgen?

Ja, dit is mogelijk voor zowel debiteuren als crediteuren.

- Neem hiervoor contact op met verkoop.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## Hoe geef ik een vast IP-adres aan de PowerPrint?

Een vast IP adres kan op 3 manieren ingesteld worden:

1. DHCP reservering maken in de DHCP server: IP adres wordt dan gekoppeld aan het MAC-adres van de printer waardoor de printer geen ander IPadres meer krijgt. Opmerking: Deze optie heeft de voorkeur / wordt aanbevolen.
2. Met de Diagtool: Kies bovenin bij interface: Ethernet en klik op Setup.
3. Selecteer de printer en kies voor Change IP Address.
4. Zet onderstaande instelling op Static IP en voer handmatig een  in. (LET OP: Kies voor een IP adres buiten de DHCP scope om IP conflicten te voorkomen).

In de web-interface van de printer.

1. Typ het  van de printer in een willekeurige browser in.
2. Klik in het linkermenu op Network.
3. Om de printer van een vast IP te voorzien, zet de instelling op Static IP en voer een  in. Belangrijk: LET OP: Kies voor een IP adres buiten de DHCP scope om IP conflicten te voorkomen.

- PowerPrint

---
## Hoe haal ik mijn nieuwe inkoopfacturen op?

Het is mogelijk om nieuwe (digitale) inkoopfacturen op te halen bij diverse leveranciers.

- Voor meer informatie over deze leverancier raadpleeg de helpdesk.

#### Voorwaarden

Bij Instellingen externe communicatie moet bij deze klanten invoice inquiry ingesteld zijn, anders is de knop Facturen ophalen niet zichtbaar.

#### Invoice inquiry

Om nieuwe facturen op te halen, doorloopt u de volgende stappen:

1. Ga naar E-factuur inkomend (KEI).
2. Kies voor de knop Facturen ophalen.
3. Kies voor de knop Ja. of

De nieuwe facturen worden opgehaald en toegevoegd.

Opmerking: De facturen komen standaard in de volgende map te staan: C:\\PW\\INBOX\FACTUUR\\

- E-Inkoopfacturen inboeken
- Taakplanner instellen voor het automatisch ophalen.

---
## Hoe herstart ik de Service Host?

Het is mogelijk om de Service Host te starten in Powerall Connect.

- Deze service zorgt voor de diverse interne - en externe verbindingen.

Om de Service host te herstarten, doorloopt u de volgende stappen:

1. Ga in het systeemmenu naar Systeembeheer > Actieve taken.
2. Ga naar tabblad Service Host.
3. Controleer de status, deze moet Actief zijn en is het Proces-ID gevuld.
4. Als de status Gestopt is, moet deze weer gestart worden d.m.v. de knop Starten. Tenzij er een technische reden is om deze taak tijdelijk te stoppen, bijv. bij het opnieuw laden van configuratie, etc. Bij Starten wordt de status actief en het Proces-ID verschijnt.

#### FAQ

Opmerking: Het gebeurt zelden dat de ServiceHost zelf stopt.

Wie mogen deze services stoppen en / of starten?

Alle gebruikers mogen deze status bekijken, maar alleen gebruikers met autorisatie Z (systeem beheer) kunnen de Service Host stoppen / starten.

- De autorisatie wordt bepaald voor de gebruiker bij Onderhoud gebruikers.

- Als de gebruiker niet geautoriseerd is, is de knop Stoppen, niet bruikbaar / grijs.
- Als dit programma via Powerall Lokaal opgestart wordt, kan er een foutmelding verschijnen, omdat dit programma onvoldoende rechten heeft.Start Powerall Lokaal via Rechtermuis > Als administrator uitvoeren op.

Opmerking: De Pws service is geïntegreerd in de Powerall Service Host vanaf versie 3.07.

- FAQ Beheer

---
## Hoe meld ik mij aan voor de bankkoppeling?

Instellingen

Allereerst moet onderstaand ingesteld zijn / uitgevoerd worden:

- Hoe stel ik de bankkoppeling in? voor mijn  dagboek.
- Hoe activeer ik de bankkoppeling?

#### Aanmelden Bankkoppeling via IBANXS

Om zich aan te melden bij IbanXS is een KvK uittreksel nodig en een geldig ID document (rijbewijs of paspoort). Om dit te doen, doorloopt u de volgende stappen:

1. Bankkoppeling instellen. Kies de juiste Juridische vorm en vul het e-mailadres in. Klik hier voor meer informatie over de juridische vorm. De volgende mogelijkheden zijn er bij de juridische rechtsvorm: | Juridische vorm | Optie voor juridische (rechts) vorm: - Bedrijf (standaard)- Privépersoon- ZZP-er- Stichting | | --- | --- |
2. Kies voor de knop Starten.

Het autorisatie scherm van IbanXS verschijnt.

- Kies voor de knop GA DOOR NAAR .

Vul het invulformulier in zoals vermeld, voor meer info zie IbanXS.../FAQ.

#### 1 Bedrijfsgegevens

1. Vul de bedrijfsgegevens in.
2. Vul het KvK nummer in.
3. Upload het Uittreksel van de Kamer van Koophandel.
4. Geef de SBI code(s) in

2 Gegevens contactpersoon

1. Vul de contactpersoon gegevens in.
2. Upload het Document ID.

3 Identificatie van bestuurslid / 4 Identificatie belanghebbende UBO

1. Geef de bestuursleden in.
2. Geef de uiteindelijke belanghebbende in.
3. Upload de benodigde bestanden / gegevens.

5 Politiek prominente personen (PEP) en 6 Handtekening

Kies voor de knop Doorgaan met ondertekenen.

*Klik hier voor meer informatie over juridisch vorm Privepersoon*:

#### Aanmeldingsformulier: Privé persoon

1. Bij volledige naam geef de naam in, zoals op het ID-document vermeld is.
2. Bij ID-document upload het rijbewijs of paspoort.
4. Kies voor de knop Doorgaan met ondertekenen.

De IBANXS onboarding form verschijnt.

1. Selecteer de bank: NB Deze éénmalige toestemming geldt ook voor uw andere banken. Kies voor de knop Verzoek Toegang.
2. Het scherm U staat op het punt om ons toegang te verlenen tot  verschijnt. Kies voor de knop GA DOOR NAAR .

Mobiel bankieren app

Geef toestemming tot de rekening(en).

1. Vink de rekening aan. De toegang is 180 dagen geldig:
2. Bevestig de toegang in de Mobiel Bankieren App.

Na de bevestiging verschijnt het volgende scherm.

#### Aanvraag status 'evaluating'

IbanXS valideert de aanvraag, afhankelijk van de juridische vorm kan dit ongeveer 24 uur duren.

In de mail verschijnt het volgende bericht:

- Bij Bekijk onboarding verschijnt het scherm:

#### Aanvraag 'afgerond'

Als de aanvraag goed gekeurd is, verschijnt er een e-mail.

#### Rekening(en) koppelen

Nadat de mail van onboarding succesvol ontvangen is, moeten de transacties opgehaald worden in Powerall. Hierbij wordt dan de bankrekening gekoppeld.

- Dit gebeurt bij Inlezen/verwerken bankafschriften, zie ook Bankkoppeling.
- Dit is ongeveer hetzelfde proces als stap 4 en 5. Als dit gedaan is, verschijnt het scherm Rekening  koppelen, zie onderstaand scherm, onder 'Opvragen rekening informatie'.

Opvragen rekening informatie

Het opvraag proces verloopt als volgt:

Wacht tot bovenstaand proces gereed is.

Bankkoppeling

Bij de knop Bankkoppeling bij Inlezen/verwerken bankafschriften verschijnen de gekoppelde rekeningen.

Met als provider IbanXS.

#### FAQ

Voor IbanXS vragen zie:

- IbanXS.../FAQ

Voor ID-document(en) zie rijksoverheid.nl/../...ID-document

Wat moet ik doen als ik de link niet goed kan openen?

Als bij het toestemming geven van een rekening in de Rabobank-omgeving een pagina niet laadt, of een fout geeft, probeer dan de browser link te openen in een andere browser of incognitomodus.

- De melding Deze site is niet bereikbaar kan verschijnen.

Voor meer informatie zie Hoe kan ik een link van de  openen?

- Bankkoppeling
- Inlezen/verwerken bankafschriften

---
## Hoe werkt MultiSafepay import?

Bij het gebruik van MultiSafepay (MSP) is het mogelijk om de mutaties te importeren, vanaf versie 3.21.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Klik hier, voor meer informatie over dit onderwerp.

Vanuit Powerall Connect kunnen met één druk op de knop de mutaties van de betaallink, de MultiSafepay pin en de kosten worden opgehaald en direct geboekt.

De gegevens die opgehaald worden zijn de mutaties van de betaallink aan de hand van de bedrijfsinstelling en de mutaties van de gekoppelde Multisafepay pinautomaten aan de hand van de gekoppelde API in de instelling Kassa.

De mutaties die worden opgehaald van de betaallink worden in inlezen bankafschriften direct herkend voor de klant en de factuur. De transacties voor de pin en de kosten worden dat niet. De pin transacties komen wel per bedrag binnen. Dit is normaal voor Powerall niet nodig als je met de kassa module werkt. Daar wordt per dag of per afsluiting van de kassa een totaalbedrag op de tussenrekening pin geboekt. Het is dus straks makkelijk dat de meeste onbekende betalingen standaard op de goede rekening worden voorgesteld.

Daarnaast is het zo dat de kosten worden getotaliseerd met kosten en BTW bij elkaar. De verwerking van deze kosten kun je beter een verwerking van de MultiSafepay factuur noemen. Er wordt door MultiSafepay voor de kosten nog een factuur gestuurd met een specificatie van de kosten en de BTW. De verwerkte kosten vanuit MSP zullen dan op een rekening in de balans geboekt moeten worden als vooruitbetalingen MSP.

#### Werkwijze

- De facturen die van MSP komen worden met de BTW specificatie normaal ingeboekt.
- Deze worden later via het dagboek 'Verrekeningen' afgeboekt tegen de ingestelde grootboekrekening 'Vooruitbetaling MSP'.
- Verwerking mutaties Multisafepay als het inlezen bankafschrift.
- Aangezien de uitbetalingen van MSP niet met de mutaties meekomen, moeten deze handmatig geboekt worden in Boeken Kas en Bank en dan het dagboek van MultiSafepay. Op het moment dat de uitbetaling van de bank binnen komt, wordt deze op een tussenrekening of kruispostenrekening geboekt. Dit kan een algemene zijn, maar specifiek 'Kruispost uitbetaling MSP' is beter. Na deze boeking moet dit bedrag in Boeken Kas en Bank voor dagboek MultiSafepay worden afgeboekt.

Inlezen

Bij Inlezen/verwerken bankafschriften kunnen de MultiSafepay betalingen geïmporteerd worden.

- betaallink i.c.m. MultiSafepay
- Kassa pin terminal

- MultiSafepay (inlog)

---
## Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders?

#### Wat is OCI?

OCI (Open Catalogus Interface) is een gestandaardiseerde uitwisseling van catalogusgegevens tussen het leveranciers online bestelsysteem en Powerall Connect.

Voorwaarde

De volgende voorwaarde gelden hierbij:

- De leverancier moet OCI bestellen ondersteunen op zijn webshop en moet een OCI-koppeling hebben met Powerall Connect. Voor welke leveranciers is een OCI koppeling mogelijk? Bij de volgende leveranciers kan OCI gebruikt worden: Bulthuis
- Bepco
- DAF voor eindgebruikers / op aanvraag beschikbaar. Wordt altijd via de dealer besteld, waarbij de afgesproken prijzen met de fleetowner gehanteerd worden.

Granit Parts

INDI vanaf mei 2025

LKQ vanaf november 2025

- Let op: order wordt ook direct besteld.

Kramp

- Het volgende moet aangevinkt zijn bij Kramp.com/MyAccount > Mijn profile OCI gebruiker,anders verschijnt de knop OCI bestelling plaatsen niet.

Trex Parts (Heftrucks onderdelen)

- Vanaf 2025.

TVH

- Hierbij verschijnt boven in het scherm de melding: Je bevindt je momenteel in een punchout-sessie.

#### Hoe werkt het?

Om artikelen vanuit de leverancierswebsite op een werkorder toe te voegen, doorloopt u de volgende stappen:

1. Maak een nieuwe werkorder aan. Zie Nieuwe werkorder aanmaken.
2. Kies voor de knop

Het scherm OCI resultaat verschijnt in de browser.

- Eerst verschijnt de eerste regel daarna de volgende.
- Sluit dit scherm bij de melding Resultaat door Powerall ontvangen.
- Het scherm Resultaat OCI verschijnt. Hierbij geldt: 1. Bij BtB keuze maak een keuze. | BtB keuze | Optie voor het bestellen van artikelen:- Niet aanwezig bestellen (standaard), bijv. als er 8 in de order staan en 5 op voorraad, worden er 3 besteld.- Niets bestellen- Alles bestellenNB. Bij het bestellen wordt een inkooporder of bestelregel aangemaakt. | | --- | --- | 2. Bij Prijzen bijwerken in eigen bestand, vink aan of de leveranciersprijzen bijgewerkt moeten worden. Als de leverancier de voorkeursleverancier is, wordt de artikelprijs ook bijgewerkt. 3. T.a.v. de prijzen geldt het volgende: Groen als de OCI prijs lager. 4. Rood als de OCI prijs hoger. 5. Wit als de OCI prijs gelijk is. De prijs wordt vergeleken met de prijs van de leverancier.

De OCI artikelen, van de webshop, worden toegevoegd op de werkorder.

Kies voor de knop Einde order.

De gegevens zijn opgeslagen.

FAQ

*Waarmee wordt o.a. rekening mee gehouden? Met de volgende situaties wordt rekening gehouden, als OCI artikelen toegevoegd worden op de werkorder: - Belangrijk: Bij het ontbreken van de inkoop of catalogus module is de OCI functie niet beschikbaar. - Er wordt korting berekend, indien van toepassing. - Bij interne werkorders wordt de kostprijs toegepast en geen korting. - Als de prijzen bijwerken wordt aangevinkt, vindt er bij de voorraadwaardering VVP een herwaardering plaats, als er voorraad is. - Als de leverancier niet aanwezig is, wordt deze toegevoegd (ook bij een bestaand artikel). - Bij een nieuw artikel, wordt de artikelcode van de website gebruikt in Powerall Connect. - Als er geen leverancier niet aanwezig is, wordt deze de bestel- en voorkeursleverancier. - Onderstaande catalogus instellen m.b.t. de omschrijving, bij nieuwe artikelen . | Omschrijving aanpassen | Optie om de artikel omschrijving aan te passen: - Als origineel (standaard)- HOOFDLETTERS - Kleine lettersNB wordt ook gebruikt als via OCI een artikel wordt toegevoegd aan eigen artikelbestand. | | --- | --- | De bestelhoeveelheid van de leverancier. - Bij een nieuw artikel wordt op tabblad Algemeen de prijs per 1 stuk berekend. - Indien de leverancier een merkcode gebruikt wordt deze overgenomen op het artikel. Vervangende artikelen. Al of niet voorraad bijhouden wordt overgenomen van Instellingen artikelen, vanaf versie 3.04. Hoe komt het dat ik geen leverancier zie? Als er geen leverancier bij het scherm OCI leverancier zichtbaar is, is het niet mogelijk om OCI artikelen toe te voegen. - Voor meer informatie zie boven voorwaarde. Welke voorraad wordt weergegeven bij Resultaat OCI*?

De beschikbare voorraad wordt getoond.

- Het scherm Resultaat OCI verschijnt nadat de weborder zijn overgehaald naar Powerall Connect.

Kan ik ook eerst op de webshop mijn winkelwagen vullen en daarna de artikelen binnen halen?

Ja, het is mogelijk. Om dit te doen, doorloopt u de volgende stappen:

1. Bestel eerst de artikelen op de webshop.
2. Doorloop bovenstaande stappen (1 t/m 5). Maak een werkorder aan, Kies voor de knop  Online browsen. Selecteer de leverancier.
3. Op de webshop ga direct naar het winkelmandje (x), hierin staan de artikelen gereed.
4. Ga verder met stap 5 c Doorgaan met bestellen > OCI bestelling plaatsen. Deze knop is afhankelijk van de webshop van de leverancier.
5. Vervolg bovenstaande stappen.

(x) = aantal artikelen

- Integraties

---
## Hoe werkt SMS?

In Powerall Connect is het mogelijk om een SMS bericht te verzenden, om bijvoorbeeld u klanten te informeren dat een werkorder gereed is of dat de bestelde artikelen binnen zijn.

Belangrijk: Dit is een betaalde service.

Hoe stel ik SMS in?

Standaard is de SMS functie al ingesteld.

Bij Instellingen bedrijf (BIB), tabblad Relaties, selecteer SMS.

- | Gebruik berichten service | Optie voor het gebruik van berichten service:- Nee- SMS (standaard), het is mogelijk om een SMS-bericht te versturen. - WhatsApp, via de browser is het mogelijk om WhatsApp bericht te versturen.NB bij Nee zijn de Bericht / SMS knoppen grijs. | | --- | --- |

Bij Onderhoud relaties, tabblad E-Document, zijn 2 document formaten SMS-notificatie aanwezig voor:

- Werkgereed
- Verkoopbestelling

Hiermee kan worden aangegeven of de klant automatisch een SMS-bericht wilt ontvangen. De tekst SMS-notificatie is gewijzigd naar Bericht-notificatie.

Hoe stel ik een standaard SMS (template) in?

Er zijn 3 soorten standaard SMS templates:

- Standaard tekst; sms_std.txt
- Werkorder; sms_wo.txt
- Verkooporder; sms_vo.txt

Deze templates staan in de submap SMS van de betreffende administratie map.

Opmerking: Indien deze bestanden nog niet aanwezig zijn, ga naar Opvragen relaties F6 en druk op de 'bericht' knop. De templates worden dan éénmalig aangemaakt.

Waar kan in  een SMS verzenden?

Een SMS kan vanuit de volgende programma's verzonden worden:

- Opvragen relaties F6 SMS-knop achter het mobiele nummer.
- Verkooporders, knop  Verstuur SMS.
- Bij het ontvangen van bestelde goederen van een verkoopbestelling.
- Als een werkorder gereed is en als dit bij deze relatie ingesteld is.
- Selecteren werkorders (WS) > Invoeren/wijzigen werkorders, knop  Verstuur SMS. Zie SMS / WhatsApp versturen werkgereed

Waar zie ik de verzonden SMS-en?

Bij Opvragen relaties, tabblad CRM, zijn alle verzonden SMS-en te zien met het onderwerp en bericht.

Welke gegevens kunnen automatisch  in een SMS template ingevuld worden?

Bij het versturen van een SMS vanuit de processen goederenontvangst, verkoop en werkorders kunnen  gebruikt worden, die automatisch gevuld worden. De volgende machine  kunnen gebruikt worden in de templates (zie voorbeeld):

- Merk =
- Type =
- Kenteken =

Een voorbeeld van sms bericht:

Tip: Het aantal tekens kan gemakkelijk geteld worden, door deze te kopiëren naar een nieuwe Word document.1. Kies voor tabblad Controleren.2. Kies voor de functie Aantal woorden.Het aantal tekens wordt weergegeven.

Wie is de afzender?

De afzender is afhankelijk van het 'abonnement'.

- Standaard, bij geen abonnement is dit: Powerall Connect.

Bij een abonnement:

- is dit de , neem contact op met de verkoopafdeling om deze in te stellen.

In de standaard templates, geef of wijzig de bedrijfsnaam in de tekst als afzender, zie standaard SMS.

Belangrijk: • De afzender of bedrijfsnaam mag maximaal 11 tekens lang zijn.• Alleen de volgende tekens zijn mogelijk: A t/m Z, a t/m z en 0 tot 9. Geen spaties, andere symbolen of tekens zijn toegestaan.

Belangrijk: Een SMS bericht bestaat uit maximaal 160 tekens, als er meer gebruikt worden, wordt dit beschouwd als een 2e of 3e (vanaf 320 tekens) SMS-bericht.

- Bij het sms'en naar of vanuit het buitenland moet het landnummer voor het 06 nummer staan bijv. +31612345678.
- Deze SMS berichten kunnen niet beantwoord worden.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Hoe werkt WhatsApp? vanaf versie 3.20.

---
## Hoe werkt  WhatsApp?

# Hoe werkt WhatsApp?

In Powerall Connect is het mogelijk om een WhatsApp bericht te verzenden.

Hoe stel ik WhatsApp in?

Bij Instellingen bedrijf (BIB), tabblad Relaties selecteer WhatsApp.

- | Gebruik berichten service | Optie voor het gebruik van berichten service:- Nee- SMS (standaard), het is mogelijk om een SMS-bericht te versturen. - WhatsApp, via de browser is het mogelijk om WhatsApp bericht te versturen.NB bij Nee zijn de Bericht / SMS knoppen grijs. | | --- | --- |

Klik hier voor meer informatie over de WhatsApp functie:

Beste manier van werken:

- Download WhatsApp..whatsapp.com/download en installeer deze op uw computer.
- Start de WhatsApp, zodat deze actief of open staat op de computer. 1. De eerste keer, als de Powerall WhatsApp functie gestart wordt, verschijnt de volgende melding: Deze site probeert WhatsApp te openen. api.whatsapp.com altijd toestaan. 2. Vink deze aan en kies voor de knop Openen. NB a en b zijn eenmalig! 3. Kies voor de knop Doorgaan naar chat .

#### WhatsApp versturen

Een WhatsApp bericht kan verstuurd worden:

1. Bij Opvragen relaties F6. D.m.v. de knop .
2. De standaard berichten verschijnen. Kies voor de knop Versturen.
3. Druk op Doorgaan met chat in de browser.
4. WhatsApp verschijnt.

Via de knop  Verstuur WhatsApp vanaf versie 3.20:

1. Selecteren verkooporders (VS) en Invoeren/wijzigen verkooporders
2. Selecteren werkorders (WS) en Invoeren/wijzigen werkorders.

Waar zie ik de verzonden berichten?

Bij Opvragen relaties, tabblad CRM, zijn alle verzonden berichten te zien.

- Het mobielnummer moet een WhatsApp account hebben, anders verschijnt de melding: Het telefoonnummer  geeft geen WhatsApp-account.

Belangrijk: Als er gekozen is voor WhatsApp kan er geen SMS verzonden worden, en andersom.

Hoe stel ik een standaard WhatsApp (template) in?

Er zijn 3 soorten standaard WhatsApp templates:

- Standaard tekst; wa_std.txt
- Werkorder; wa_wo.txt
- Verkooporder; wa_vo.txt

Deze templates staan in de submap WhatsApp van de betreffende administratie map.

- De tekst is maximaal 600 tekens.

Opmerking: Indien deze bestanden nog niet aanwezig zijn, ga naar Opvragen relaties F6 en druk op de 'bericht' knop. De templates worden dan éénmalig aangemaakt.

Hoe komt het dat bijzondere tekens en letters niet goed weergegeven worden?

Om deze tekens goed weer te geven moeten de standaard templates (zie hierboven) opgeslagen worden als een ANSI bestand. Om dit te doen, doorloopt u de volgende stappen:

1. Open de whats app template / bestand.
2. Kies bij Bestand > Opslaan als.
3. Selecteer bij codering ANSI.
4. Kies voor de knop Opslaan. Bij de pop-up melding wa.xxx.txt bestaat al, wilt u het vervangen?, kies Ja.

Belangrijk: Dit moet bij elke wijziging gebeuren, de codering wordt namelijk niet opgeslagen.

Klik hier, voor meer informatie over dit onderwerp.

Het volgend is van toepassing:

- Er wordt gebruik gemaakt van de standaard WhatsApp, d.w.z. geen Business versie.
- Een bericht wordt altijd handmatig verstuurd.
- Bij Onderhoud relaties (BRR), tabblad E-document, is de tekst, in kolom Formaat , gewijzigd naar Bericht-notificatie, dit was eerst SMS-notificatie.
- Als er bij een order al een WhatsApp bericht verstuurd is, verschijnt de melding: Voor deze order is al een WhatsApp verstuurd, toch doorgaan?
- Na Versturen wordt altijd de standaard browser geopend in een nieuw tabblad.
- Bij het whatsappen naar of vanuit het buitenland wordt het landnummer gebruikt. Er wordt geen rekening gehouden met een mobiel nummer uit buitenland, er wordt er van uitgegaan dat het 'landnummer' van de relatie overeenkomt met mobielnummer.

De Landcode telefoon van het land moet ingevuld zijn, zie Onderhoud ISO-landcodes - intern -. Deze zijn standaard ingevuld voor Europa.

Bij een test administratie verschijnt de standaard pop-up:

Kies voor de knop Ja.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Hoe werkt SMS?

---
## Hoe werkt picken / gereserveerd bij werkorders?

#### Inleiding

Bij picken kan er rekening gehouden worden, met artikelen die gereserveerd zijn voor een werkorder.

Klik hier voor meer informatie over de knelpunten in de 'oude' situatie:

1. Er ligt 1 artikel op voorraad die al gereserveerd is voor een verkooporders. Zodra de werkplaatschef deze toevoegt op een werkorder (besteld 1, geleverd 0) komt deze in SOR13 als te picken voor de werkorder.De werkorder wordt gepickt waardoor het artikel niet uitgeleverd kan worden aan de verkooporder waar deze voor gereserveerd was.
2. De werkplaatschef plant een werkorder voor over een week en geeft aan dat hij een artikel nodig heeft. Hij zet deze op besteld 1, geleverd 0. De klant draait regelmatig de Uitleveradvieslijst . Na een nieuwe ontvangst wordt deze Uitleveradvies lijst door de klant gedraaid.Hierbij wordt nog geen rekening gehouden met de artikelen op de werkorders die nog gepickt moeten worden.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

### Oplossing

De volgende onderdelen zijn aangepast:

- Werkorder
- Picken werkorder
- Werkbon app en picken
- Werkorder vrijgeven
- Uitleveradvieslijst

Processchema: Werkorders i.c.m. order picken

Instellingen

Klik hier voor meer informatie om dit te doen:

Het volgende moet ingesteld zijn bij Instellingen werkorders (BIW), tabblad Orderpicken:

Dit reserveren voor werkorders wordt ondersteund d.m.v. twee velden bij een werkorder regel te weten:

- Te picken: is de hoeveelheid die gereserveerd wordt van de aanwezige voorraad.
- Gepickt: is het aantal wat uit de aanwezige voorraad is gehaald, waardoor de plankvoorraad wijzigt. Dit aantal gepickt is alleen te zien bij het scherm Werkorder details.

Deze velden komen naast de al aanwezige velden benodigd en geleverd, waarbij benodigd een economische reservering doet in de voorraad, zonder rekening te houden met de aanwezige plankvoorraad en geleverd is het aantal dat daadwerkelijk gemonteerd/versleuteld is.

Overige criteria

- Bij Instellingen werkorders is de koppeling inkoop verplicht, anders verschijnt de kolom Benodigd niet.
- Met de bestel (en back-to-back) functie wordt rekening gehouden.
- Integratie met Overzicht orders (te picken) 2.0.

Werkorder

De kolom Te picken is toegevoegd bij:

- Invoeren / wijzigen werkorders Als bij Benodigd een aantal ingevuld wordt, wordt het aantal te picken ook gevuld, indien er voldoende voorraad is. Dit werkt net zoals bij verkooporders. Als je alles wilt bestellen, zet dan het aantal te picken op 0 (als er een gedeelte op voorraad is).

Belangrijk: Als in de regel, de kolom Geleverd wordt ingevuld, wordt het Te picken op 0 gesteld.

Werkorder details

- In de kolom Te picken is het aantal gereserveerd te zien van de WO. Dit moet nog gepickt worden.
- In de kolom Gepickt is het aantal dat al gepickt is te zien. D.w.z. het aantal dat in de krat zit. Of zat als de monteur de krat al of niet verbruikt heeft.
- Onder de knop Kratinhoud is te zien wat er in de krat 'zit'.

De kolom Gepickt is ook zichtbaar bij Invoeren / wijzigen werkorders vanaf versie 3.22.

Werkorder en bestellen

Als er voldoende voorraad is, wordt de kolom Te picken gevuld.

Als er te weinig voorraad is, wordt er een BtB inkooporder aangemaakt.

- Bij de ontvangst van de inkooporder, wordt het aantal gepickt bijgewerkt op de WO.En kan deze weer gepickt en verder afgehandeld worden.

Picken werkorder

Bij Overzicht orders (te picken) 2.0 (VC) worden de werkorders gepickt.

1. Selecteer Werkorders bij Te picken order soort.
2. Kies voor de knop Picken order. De te picken werkorders (WO) verschijnen.
3. Selecteer de WO.
4. Kies voor de knop Picken order.
5. Bij Pick order wordt het aantal te picken opgeteld bij aantal gepickt. De order verdwijnt dan uit dit lijstje en komt onder Gepickt te staan. Opmerking: De knop Picken alle werkt niet voor werkorders, alleen voor verkooporders.

#### Gepickte werkorders

Op tabblad Gepikt komen de werkorders, die gepickt zijn.

- Bij Correctie picklijst, kunnen de artikelen die teruggenomen worden, gecorrigeerd worden.
- Als de werkorders vrijgegeven worden, verdwijnen ze uit de regels.
- Opmerking: Bij Gepickt is de knop Inpakken grijs of disabled bij een werkorder.

Bij de Voorraadinformatie uitgebreid is het aantal in kratten/colli te zien.

Klik hier, voor meer informatie over dit onderwerp.

- Toegevoegd: | In kratten / colli | Het gepickte aantal van verkooporder(s) en werkorder(s) in een (virtuele ) krat.- Bij het vrijgeven van een VO / WO wordt het aantal verminderd, of het aantal gaat terug naar het magazijn (optie bij WO). | | --- | --- | | Werkbon app (gereserveerd) | Het aantal dat gereserveerd is voor de Werkbon app. | | --- | --- | | Toegekend aan verkoop- /werkorders(was eerst: Gereserveerd backorders) | Het aantal toegekend / gealloceerd van verkooporders en werkorders. - Bij instelling picken is dit het aantal 'te picken'. Als er gepickt is, wordt deze 0 / verminderd en gaat het aantal naar 'in kratten/colli', vanaf versie 3.17. | | --- | --- | Was eerst: | Gereserveerd backorders | Artikelaantal dat als backorder op een verkooporder geregistreerd staat. | | --- | --- |

Servicemelding met voorbereide artikelen en inplannen

Als een servicemelding ingepland wordt, verschijnt er een extra veld aantal gereserveerd vullen.

| Aantal gereserveerd vullen | Optie om het aantal gereserveerd / te picken te vullen instelling:- Voorraad (standaard)- Nee |
| --- | --- |

| BtB-orders aanmaken | Optie om BtB orders aan te maken bij een inplannen WO icm Picken:- Ja (standaard) icm aantal gereserveerd is Voorraad.- Nee icm aantal gereserveerd is nee. |
| --- | --- |

Dit veld verschijnt ook bij het vrijgeven van een offerte naar een werkorder.

#### Werkbon app en picken

Bij het starten van een werkorder of bij het vernieuwen van de dagplanning, kan het volgende scherm verschijnen, als er iets gepickt is.

Bij het zoeken op de Werkbon App is de eigen voorraad te zien.

Alleen bij de eerste 10 artikelen wordt de Eigen voorraad getoond, d.w.z. een groen of rood bolletje.

Werkbon app en einde werk

In onderstaand voorbeeld is de werkorder verwerkt op de Werkbon app, met de optie Verwerken / verzenden Direct.

- In onderstaand voorbeeld is van de artikelen op regel 2 en 3 het Materiaalverbruik wat geleverd is, geregistreerd. Het aantal Geleverd wordt gevuld vanuit de Werkbon app.

Werkbon app en bestellen

Bij het Bestellen is het mogelijk om een gedeelte te bestellen, als er iets op voorraad is.

- Als het aantal niet volledig in het magazijn aanwezig is, verschijnt onderstaand scherm. 1. Direct bestellen (spoedbestelling). 2. X uit voorraad en rest (Y) bestellen. 3. Alles bestellen. Bij voldoende voorraad verschijnt de opmerking: De bestelling kan volledig uit voorraad geleverd worden. Bij niet op voorraad: Dit artikel is niet op voorraad in het hoofdmagazijn en zal besteld worden.
- Verwerking op de Werkorder na bestelling: Het aantal uit voorraad komt in de kolom Te picken terecht, nadat registratie 'gereed' gemeld is. Hierdoor is het aantal voor deze WO 'gereserveerd'.
- Verwerking Werkbon / registratie naar gereedmelding (optie Direct). In onderstaand voorbeeld is van de artikelen op regel 2 en 3 het materiaal verbruik (geleverd) geregistreerd. En de WO is gereed gemeld. Het aantal Geleverd wordt gevuld vanuit de Werkbon app.

Werkorder vrijgeven

Bij het Vrijgeven van een WO verschijnt, als er nog wat in de krat(ten) zit, de melding: Werkorder  is nog aanwezig in krat . Er kan bijv. minder verbruikt zijn.

Bij Ja verschijnen het scherm Openstaande kratregels.

Het volgende is mogelijk:

1. Optie Alles op werkorder Het aantal gepickt wordt (op 0 gezet) en opgeteld bij aantal geleverd.
2. Optie Alles retour magazijn Het aantal wordt retour op het magazijn geboekt, d.w.z. het aantal geleverd blijft hetzelfde. Het aantal in kratten/colli wordt op 0 of verminderd en de plank voorraad wordt verhoogd.
3. Per regel kan de registratie op werkorder of retourmagazijn bepaald worden.

- Kies voor de knop Opslaan. De pop-up melding Inhoud van de krat wordt hiermee geleegd, weet u dit zeker? verschijnt. Kies voor de knop Ja. Bij het gebruik van de Werkbon App wordt geleverd ingevuld.

De WO kan vrijgegeven worden, zie Werkorder gereed melden / vrijgeven.

#### Offerte en werkorder

Bij Vrijgeven offerte wordt het aantal gepickt ingevuld, als er voldoende voorradig is.

#### Uitleveradvieslijst

Bij de Uitleveradvieslijst orders, wordt er ook (standaard) rekening gehouden met werkorders.

| Uitleveradvies voor | Optie voor het uitleveradvies orderpicken i.c.m. WO voorraad reservering:- Verkooporder - Werkorder, openstaande en behalve status servicemelding werk gereed.- Beide (standaard) i.c.m. de Taakplanner is altijd Beide. |
| --- | --- |

| Direct verwerken | Optie voor direct verwerken of bijwerken van het aantal:- Nee (standaard) - Ja Bij Ja icm Order picken is ja, is dit bij VO aantal gereserveerd en bij WO gepickt, vanaf versie 3.17. |
| --- | --- |

- Als Direct verwerken is ja en de werkorder gelocked is, verschijnt er een melding.
- Werkorders met de status Werk gereed worden overgeslagen.
- Een werkorder gaat voor een verkooporder. Als er 1 artikel X beschikbaar is en dit artikel staat op een verkoop- en een werkorder, wordt deze aan de werkorder toegekend.

Zie ook Uitleveradvieslijst.

Werkbon App en picken

#### FAQ

Hoe zit het als ik geen Werkbon App gebruikt?

Als de Powerall Werkbon App niet gebruikt wordt, verschijnt er bij het Controleren of Vrijgeven van een werkorder een melding: Werkorder  is nog aanwezig in krat . Wilt u deze registeren?

- Bij ja kunnen de kratregels op de werkorder (standaard) of terug naar het magazijn geboekt worden.

Zie ook Werkorder vrijgeven.

Wat gebeurt er bij het verwijderen van een orderregel met een BtB

Bij het verwijderen verschijnt er een vraag of de gepickte delen teruggeboekt moeten worden.

Bij Ja gebeurt het volgende, vanaf versie 3.23:

- Werkorderregel wordt verwijderd.
- Onderdelen gaan weer terug naar voorraad, deze wordt bijgewerkt
- Kratregels worden verwijderd. Krat wordt verwijderd als deze leeg is en virtueel (anders worden de gegevens van de krat gereset).

Picklistregels worden verwijderd.

- Picklist wordt verwijderd als deze leeg is en anders worden de aantallen opnieuw berekend.

- Overzicht orders (te picken) 2.0

---
## Hoe werkt ondertekenen offerte i.c.m. Stiply?

#### Doel

Als gebruiker wil ik een offerte digitaal kunnen laten ondertekenen zodra ik deze heb opgesteld, zodat ik een schriftelijk akkoord heb op mijn offerte, vanaf versie 3.23.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Instellingen

*Klik hier voor meer informatie over de instellingen: - Alleen beschikbaar voor klanten met All-In licentie. - In Instellingen externe communicatie (BAC) moet een geldig Stiply account toegevoegd worden / aanwezig zijn. - Op de Offerte Layout moet bij SQU71 Print offerte/opdrachtbevest. in de offerte voet de volgende velden staan: SYS500 - handtekening0 deze heeft standaard al de juiste hoogte en breedte. - SYS501 - datum0 (ondertekening) . Instellingen offertes, tabblad Beheer: Tabblad Uitvoer printer de layoutcode: - | Offerte 'Ondertekenenverzoek' | De offerte layout, voor het ondertekenen via Stiply die gebruikt wordt via Offerte, bij Selecteren offertes (OS), vanaf versie 3.23. | | --- | --- | Belangrijk: Bovenstaand is verplicht, anders verschijnt er geen pop-up melding of werkt de knop Offerte niet meer. Tabblad Beheer - | Gebruik ondertekenverzoek | Optie voor een ondertekening verzoek m.b.v. Stiply vanaf versie 3.23:- Nee (standaard)- Ja- Vanaf bedrag - Vrije keuze | | --- | --- | Om een offerte te laten ondertekenen, doorloopt u de volgende stappen: 1. Ga naar Selecteren offertes (OS). 2. Selecteer de offerte. 3. Kies voor de knop Offerte. 4. Het scherm Ondertekenverzoek verzenden verschijnt. Er kan een ander e-mail adres geselecteerd worden, indien beschikbaar. 5. Vink aangepast aan om een eigen bericht / tekst in te geven, vanaf versie 3.24. 6. Kies voor de knop Verzenden. De offerte krijgt de status Wacht op ondertekening. De offerte is verzonden. Opmerking: Als de offerte ondertekend is, krijg deze de status Ondertekend. Ondertekenen door klant Om de offerte te ondertekenen, doorloopt u de volgende stappen: 1. Ga naar de Outlook Inbox. 2. Selecteer de mail / offerte. 3. Druk op de knop Document bekijken en ondertekenen. Ondertekenen De offerte wordt geopend. 1. Kies voor de knop Vul in en onderteken. Als de offerte niet akkoord is, kan deze geweigerd worden d.m.v. de knop Weigeren, voor meer info zie Offerte weigeren / afwijzen. 2. Selecteer de datum van ondertekening. 3. 'Klik op het groene veld om uw handtekening te zetten'. 4. Vul de handtekening in. 5. Kies voor de knop Handtekening invoegen. 6. Vink aan: Akkoord met dit document en met de volgende toepasselijke voorwaarden: . 7. Vul uw voor- en achternaam in. 8. Druk op de knop Akkoord. 9. De melding Succesvol ondertekend verschijnt. Bij de Browser pop-up Toegang tot uw locatie door app. stiply.nl toestaan?, kies Toestaan. Verzenden ondertekening. Het document met de handtekening wordt verzonden, per email. In het Powerall Dossier wordt ook het _ondertekend en _bewijsdocument toegevoegd met de handtekening. #### FAQ - Een ondertekeningsverzoek kan nogmaals verstuurd worden. - Als een ondertekeningsverzoek geweigerd wordt, krijgt de gebruiker een bericht met de reden. In het Dossier is dit ook te zien. - Stiply onthoudt de handtekening a.d.h.v. het mailadres en laat deze zien bij het volgende ondertekeningsverzoek. Onderteken proces: Hoe komt het dat mijn offerte Verlopen* is?

Als de offerte vervaldatum voorbij is, wordt de offerte als verlopen beschouwd.

- Ongeachte of de status Wacht op ondertekening of Afgewezen is of niet.

Wat gebeurt er bij offerte weigeren?

#### Offerte weigeren / afwijzen

Als de klant de offerte afwijst, om wat voorreden dan ook, wordt dit automatisch gemaild met opgave van de reden.

Bij Selecteren offertes (OS) wordt de status dan Afgewezen.

- In het Dossier is de reden te zien.

Na aanpassing van de offerte kan opnieuw een ondertekeningsverzoek gedaan worden, via de knop Offerte.

- Selecteren offertes

- Stiply / digitaal-ondertekenen

---
## Hoe werkt een vooruit- of aanbetaling bij een verkoop- of werkorder?

Het is mogelijk om een aan - of vooruitbetaling te doen bij een verkooporder of werkorder vanaf versie 3.23.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Nieuwe verkooporder aanmaken (VS).
2. Geef de gegevens in.
3. Kies voor de knop  Vooruitbetaling. Het scherm Vooruitbetaling verschijnt.
4. Geef het percentage of bedrag in.
5. Kies voor de knop Opslaan.

Het volgende gebeurt:

- Een aan - of vooruitbetalingsregel wordt toegevoegd op de werk-/verkoooporder, met artikelcode .
- Een bon wordt aangemaakt, die betaald kan worden. Achter de bon in het Dossier wordt er een PDF van de order aangemaakt, vanaf versie 3.23.

Kies voor de knop  Einde order.

De verkooporder is opgeslagen.

#### Bon / Voorlopige factuur

Tegelijkertijd wordt er een order bon aangemaakt met de aan - of vooruitbetaling.

Deze bon / order kan gefactureerd en verzonden worden.

#### Definitieve factuur

Om later de definitieve factuur te verzenden, wordt de verkooporder vrijgegeven zie Vrijgeven verkooporder.

De (definitieve) orderbon ziet er dan als volgt uit:

#### Betaling

Bij de betalingen van de facturen vallen de aan - of vooruitbetalingsrekeningen tegen elkaar weg.

#### FAQ

- Bij aanbetalingen is deelfacturatie bij een verkooporder niet mogelijk.
- Een VO met een vooruitbetaling kan niet verwijderd worden.

Hoe werkt de vooruitbetaling i.c.m. een webshop?

Werking vanaf versie 3.27, is als volgt:

- Het betaalde bedrag vanuit de webkassa wordt teruggerekend excl. BTW en als vooruitbetalingsregel op de verkooporder gezet. Op de achtergrond wordt er een bon/factuur en openpost (betaald) gemaakt van deze vooruitbetaling.
- Ook wordt er een record aangemaakt in het vooruitbetalings-bestand met dit bedrag met het bon-/factuurnummer en verkooporderregel.

Bij het (deel)leveren van de verkooporder wordt eerst bepaald wat het bedrag (incl. BTW) van de levering is. Dit is nodig omdat er meerdere BTW tarieven gebruikt kunnen worden op een verkooporder.

- Dit bedrag wordt dan verminderd met de BTW waartegen het vooruitbetalingsartikel wordt gefactureerd.
- Op de verkooporder/bon/factuur wordt dit als negatieve vooruitbetalingsregel gezet (verrekening van het reeds betaalde bedrag per levering). Van dit bedrag wordt ook een record in FDPPAY geschreven.

Door te ‘plussen en minnen’ wordt bepaald wat er nog verrekend moet worden.

- Is er teveel vooruitbetaald (doordat er bv een verkooporderregel is verwijderd) dan wordt dit bedrag op de laatste bon gecrediteerd, bij te weinig volgt nog een nabetalingsfactuur.
- Bij de relatie wordt de Openposten bijgewerkt zodat het Factuurbedrag gelijk is aan Betaald.

Met de volgende situatie is rekening gehouden:

- volledige levering van een order
- deellevering
- order met verschillende BTW tarieven
- buitenlander
- in order prijzen aanpassen na vooruitbetaling
- aantallen wijzigen
- orderregels verwijderen Alleen als alle artikelregels verwijderd worden, wordt de vooruitbetaling niet gecrediteerd.

Wat is het verschil tussen de oude aanbetaling en nieuwe vooruitbetaling?

Bij de nieuwe vooruitbetaling zijn er meer mogelijkheden.

| Soort automatische boeking | Aanbetaling (oud) | Vooruit betaling (nieuw |
| --- | --- | --- |
| Instellen via | Instellingen verkooporders (BIK) | Instellingen facturering (BIV) |
| Benodigde module | Verkooporder | Facturering |
| Layout | Standaard | In te stellen voor VO en WO |
| Verkooporder (VO) mee sturen | Nee | Ja, als bijlage |
| Werkorder (WO) | Niet mogelijk | Ja |
| Gebruik BTW-systematiek | Nee | Ja, in te stellen |

In het bonnen Dossier wordt de originele order opgeslagen, vanaf versie 3.23.

- Bij de vooruitbetaling via E-facturen , wordt de originele order meegezonden instelling.

Hoe zien de bonnen eruit?

Bij Selecteren bonnen (FS) komen 2 verkooporders:

- De eerste bon is de aan - of vooruitbetaling.
- De 2e bon is de definitieve verrekening die later vrijgegeven en verzonden wordt.

Hoe ziet er de journaalpost uit?

De grootboek boeking / journaalpost ziet er als volgt uit:

- De eerste post is de aan - of vooruitbetaling.
- De tweede post is de definitieve factuur.

De Vooruitbetaling / vooruitbetaal rekeningen vallen tegen elkaar weg.

Is aanbetaling ook mogelijk bij picken orders 2.0?

Ja, dit is mogelijk, bij tabblad Verzenden is bijv. te zien of een order al betaald is, zodat deze verzonden kan worden, voor meer info zie:

- Overzicht orders (te picken) 2.0

Welke criteria gelden bij werkorders?

Bij een aan - of vooruitbetaling op een werkorder geldt, vanaf versie 3.23:

- Alleen voor een externe werkorder. De werkorder kan niet naar intern omgezet worden.

De relatie kan niet gewijzigd worden.

Instellingen

Wat moet ingesteld zijn?

Bij Instellingen verkooporders, tabblad Beheer moet de artikelcode vooruitbetaling bijv. VOORBT ingevuld zijn.

- De artikel omschrijving van VOORBT is bijv. Vooruitbetaling  d.d. .
- Deze moet gekoppeld zijn aan een financiële artikelgroep met de balans grootboekrekening Vooruitbetaling.
- Hierbij een voorbeeld van een vooruitbetalings artikel met de tag  en  in de taal Engels.
- Neem hiervoor contact op met de helpdesk om dit eenmalig in te stellen.

Vanaf versie 3.23.

Bij Instellingen facturering, tabblad Vooruitbetaling gaat het om de volgende velden:

| Tabblad Vooruitbetaling | 'Aanbetaling' |
| --- | --- |

| Gebruik vooruitbetaling | Optie om vooruitbetaling te gebruiken, vanaf versie 3.23:- Ja (standaard) - Nee NB Bij Ja is de knop Vooruitbetaling zichtbaar, onder de knop Meer functies.NB Let op: Artikelcode niet wijzigen als er nog openstaande vooruitbetalingen zijn. |
| --- | --- |

|  |
| --- |

| Artikelcode vooruitbetaling | De artikelcode die gebruikt wordt voor een aanbetaling of vooruitbetaling. Soort artikel is Normaal. Voorraad bijhouden is Nee. Wordt gebruikt bij Verkopen. Indien ingevuld is deze functie beschikbaar onder de knop Meer functies > of bij Kassa onder de knop Aanbetaling, zie ook Hoe werkt een vooruit- of aanbetaling bij een verkoop- of werkorder? |
| --- | --- |

|  |
| --- |

| Gebruik BTW systematiek | Optie voor het gebruik van BTW systematiek, voor het artikel vooruitbetaling (VBT), vanaf versie 3.23:- Ja (standaard) - Nee NB Bij Nee kunnen onderstaande BTW-codes (meestal 0%) ingevuld worden. |
| --- | --- |

| BTW-code NL | De BTW-code voor het VBT artikel in eigen land.- Standaard n.v.t. |
| --- | --- |

| BTW-code EU | De BTW-code voor het VBT artikel binnen de EU.- Standaard n.v.t. |
| --- | --- |

| BTW-code niet / buiten EU | De BTW-code voor het VBT artikel buiten de EU.- Standaard n.v.t. |
| --- | --- |

|  |
| --- |

| Originele order als bijlage sturen | Optie om de originele order(bevesting) als bijlage mee te sturen, bij E-facturen .- Ja (standaard) - Nee Deze worden opgeslagen in de map VERKOOPFACTUUR. |
| --- | --- |

| Layout verkooporder | De lay-out voor de verkooporder (bevesting) SOR54.- Leeg (standaard)NB als deze leeg is, krijg je geen kopie. |
| --- | --- |

| Layout werkorder | De lay-out voor de werkorder OBA71.- Leeg (standaard)NB als deze leeg is, krijg je geen kopie. |
| --- | --- |

Opmerking: Dit kan ook voor vooruit-facturering of termijn-facturatie gebruikt worden.

- FAQ Verkoop
- FAQ Service / werkplaats

---
## Hoe wijzig ik de relatie van een offerte of werkorder?

Het is mogelijk om bij een Offerte of Werkorder de relatiecode te wijzigen, als dit ingesteld is. Een verkeerd gekozen relatie kan hierdoor gemakkelijk gecorrigeerd worden.

#### Instellingen

Klik hier voor meer informatie over de instelling:

Het volgende moet ingesteld zijn bij:

Instellingen offertes tabblad Beheer vanaf versie 3.30,

of

Instellingen werkorders tabblad Beheer:

- Toestaan relatie wijzigen moet ja zijn.

#### Wijzigen werkorder relatie

Om het relatie van een werkorder te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Selecteren werkorders (WS). of Ga naar Selecteren offertes (OS). Vanaf versie 3.30.
2. Selecteer de werkorder of offerte
3. Kies voor de knop Wijzigen.
4. Kies voor de pennetje-knop .
5. De volgende pop-up melding verschijnt: Wilt u de relatie van deze werkorder wijzigen?.
6. Kies voor de knop Ja. Het scherm Zoek relaties verschijnt.
7. Geef de relatie in of selecteer deze. Klik hier voor meer informatie over mogelijke meldingen: Bij een andere BTW-code: Het wijzigen van de relatie naar een relatie met een andere BTW-code wordt niet ondersteund
8. Bij een contactpersoon:
9. Bij een factuurrelatie:Bovenstaande melding wordt gegeven, als factuurrelatie was ingevuld op de WO of bij de (nieuwe) klant is een factuurrelatie(orders) gevuld op tabblad Debiteurinfo.
10. Bij artikelen met prijsafspraken: Opmerking: De opgegeven prijzen blijven hetzelfde, alleen wordt een nieuw kortingspercentage of de nettoprijs afspraak toegepast (indien voor prijzen bijwerken ja gekozen wordt).
11. Bij uren:
12. Bij een contract:

De relatiecode is gewijzigd.

- Controleer de adresgegevens, factuurrelatie / contactpersoon e.d. op tabblad Adres.

Kies voor de knop Einde order.

De gegevens zijn opgeslagen.

#### FAQ

Kan ik iemand autoriseren om een relatie te wijzigen?

- Nee, het is niet mogelijk om een gebruiker hiervoor te autoriseren.

Wanneer kan ik de relatie wijzigen?

Bij het wijzigen van een relatie van een offerte of werkorder gelden de volgende restricties:

- De relatie mag geen andere BTW-code hebben.
- De werkorder mag niet: aan een project gekoppeld zijn.
- door de Werkbon App opgehaald zijn.

Belangrijk: Indien van toepassing wordt bij een werkorder bij prijsafspraken of tariefafspraken gevraagd of deze toegepast moeten worden op de al geregistreerde artikelen/materialen of uren.

Wat gebeurt er precies bij een relatie wijziging?

- Het factuuradres / afleveradres wijzigt.
- Alleen de relatie-code wijzigt, alle gegevens blijven hetzelfde behalve: De rayon-code (mailcode 4) van gewijzigde klant wordt toegepast.
- Bij een contactpersoon, wordt deze leeg gemaakt.
- Bij werkorder met contract gegevens, worden deze op 0 gesteld.
- In de regels, mogelijke kortingen bij prijsafspraken als deze bijgewerkt worden, zie mogelijke meldingen hierboven. Behalve de kortingen op de uren.

Bij een werkorder met een servicemelding:

- wijzigt ook de relatiecode van de servicemelding.

Wat gebeurt er als er nog ingeklokt is op de werkorder?

Als er nog ingeklokt is bij Urenregistratie touchscreen op een werkorder verschijnt er de volgende melding:

1. Kies voor de knop Ja.
2. De werkorder waarop in geklokt is, wordt mee gewijzigd.

#### Factuurrelatie

Wat gebeurt er als ik de factuurrelatie wijzig bij een werkorder?

Als de factuurrelatie wijzigt, verschijnt er een melding:

- De factuurrelatie voor deze werkorder is gewijzigd van  naar . Wilt u de prijzen en kortingen en BTW-code ook bijwerken.

- Op tabblad Adres is het veld factuurrelatie afhankelijk van de instelling factuuradres ingave.
- NB Hierbij wordt bij een opslag / korting op de uren toegepast of bijgewerkt.

---
## Hoe maak ik een nieuwe verhuurgroep aan?

Als bedrijf, wil ik ook bijv.  gaan verhuren. Het volgende moet dan aangemaakt of toegevoegd worden:

- Een machine groep (hoofd-/subgroep) : Voeg deze toe bij Onderhoud machine (hoofd- en sub) groepen (MBG). Zet Verhuur groep op ja en voer het eventuele borg bedrag in.

De  (machine) zelf:

- Voeg deze toe bij Nieuw machine aanmaken of kopiëren (MBB). Koppel deze groep aan de juiste (verhuur) machine groep.
- Op tabblad Financieel zet de verkoopstatus op huur.

De verhuurtarieven voor deze aanhangwagens:

- Voeg deze toe bij Onderhoud verhuurtarieven (HBH). Koppel de machine hoofd-/subgroep aan het betreffende verhuurtariefcode. Anders verschijnt de pop-up Geen tarieven tabel gevonden.

Eventuele nieuwe artikelen.

Als deze groep  op aparte grootboekrekeningen geboekt moet worden en de artikelgroep nog niet aanwezig is, moet er een nieuwe artikelgroep aangemaakt worden, met de betreffende grootboekrekeningen.

- Voeg deze toe bij Onderhoud artikelgroepen (ABG). In de artikelgroep is aangegeven naar welke grootboekrekening de omzet van dit artikel geboekt wordt.

Opmerking: Doorboekproces: het doorboeken van verhuurgegevens naar de financiële administratie gaat met behulp van een artikel. Dit artikel is gekoppeld aan een artikelgroep, zie laatste punt.

---
## Wat is het verschil tussen verhuur en contracten?

Hierbij een overzicht van de verschillen tussen verhuur- en contractmodule:

| Onderwerp | Eigenschap | Contracten | Verhuur |
| --- | --- | --- | --- |
| Machine | Machine individueel | x |  |
|  | Meerdere machines op 1 | x | x (wel dezelfde prijs per machine) |
|  | Toevoegen machines op lopende orders | x |  |
|  | Wisselen machines | x | x |
| Facturatie | Facturatie vooraf | x | x |
|  | Facturatie achteraf | x | x |
|  | Facturatiewijze 1 malig | x | x |
|  | Facturatiewijze week | x | x |
|  | Facturatiewijze 2 weken |  | x |
|  | Facturatiewijze 4 weken | x | x |
|  | Facturatiewijze maand | x | x |
|  | Facturatiewijze kwartaal | x |  |
|  | Facturatiewijze half jaar | x |  |
|  | Facturatiewijze jaar | x | x |
| Tarieven | Tarieven volgens tabel |  | x (met automatisch omschakeling van bijvoorbeeld dag naar week naar maand tarief) * |
|  | Variabele tarieven | x (alleen handmatig) | x (handmatig, korting op standaard tabel) |
|  | Uurtarief (tijd) |  | x |
|  | Uurtarief (draaiuur) | x | x |
|  | Dagtarief |  | x |
|  | Weektarief | x | x |
|  | 4 wekelijks tarief |  | x |
|  | Maandtarief | x | x |
|  | Kwartaal | x |  |
|  | Half jaar tarief | x |  |
|  | Jaarlijks tarief | x | x |
|  | Vast tarief (eenmalig) | x | x |
| Planbord | Planbord algemeen |  | x (module VH planbord) |
|  | Planbord beschikbaarheid |  | x |
| Diverse | Basis werking module op inrichting machine groepen |  | x |
|  | Contract afspraken voor service | x |  |
| Bonnen e.d. | Afleverbon | x | X (icm contract) |
|  | Retourbon | x | x |
|  | (verhuur) contract | x |  |
| Financieel | Borg |  | x |
|  | Indexatie | x |  |
|  | Nacalculatielijst | x |  |
|  | Opbrengsten op machinekaart | x | x |
|  | Huurstop |  | x (bij afspraak vaste prijs) |

Opmerking: * bij een machine verhuur van:- 4 dagen wordt en een weektarief berekend, - 5 dagen wordt er een maandtarief berekend.

---
## FAQ Goederenmatching

In dit hoofdstuk staan de meest gestelde vragen m.b.t. goederenmatching.

- Bij goederenmatching wordt de inkooporder gekoppeld of gematcht aan de ontvangen inkoopfactuur(en) van de leverancier.

### Matchen / boekingen

Kan ik ook 1 factuurregel matchen met meerdere ontvangsten?

Ja het is mogelijk om 1 factuurregel te matchen met meerdere ontvangsten.

- Bijv. 1 factuurregel met 2 stuks, waarbij er bij de ontvangst 2 x 1 artikel is ontvangen.

Kan ik ook een catalogus of een vrij artikel matchen?

Ja, dit is mogelijk voor deze artikelen.

Wat doe ik als de inkooporder / ontvangst nog niet verwerkt is, maar de factuur al wel ontvangen is?

- De inkoopfactuur kan ingeboekt worden. Powerall Connect boekt de factuur dan automatisch in op de tussenrekening die ingesteld staat in Instellingen crediteuren. De factuur krijgt op dat moment de status: Open (niet gematcht).
- De tussenrekening nog te matchen moet in de gaten gehouden worden, op bedragen die nog niet afgeletterd zijn. Achteraf kan de factuur gewijzigd en alsnog de ontvangsten / inkooporders matchen worden.

Wat doe ik als de inkooporder / ontvangst helemaal verwerkt is?

- Op de inkoopfactuur verschijnt bij de leveranciers waarbij goederenmatching op ja is gezet, aan de rechterzijde een knop Matchen goederen.
- Daar kunnen alle inkooporders en ontvangsten gematcht worden met de factuur. Als dat gedaan is, klik in het matchings-scherm op de knop Definitief (boeken).

Powerall boekt de inkoopfactuur op de tussenrekening Nog te matchen. In dagboek Matching wordt de rekening Nog te matchen tegengeboekt op de tussenrekening Inkooponderdelen (hier kijkt Powerall weer naar de artikelgroep).

- Voor een voorbeeld zie Voorbeeld matching boeking.

Wat doe ik als bij matching het artikel niet op de inkoopfactuur staat?

Bij goederen ontvangst matching kan:

- Het artikel verwijderd worden uit de betreffende matching (via rechter-muis-knop op de regel).

Bij het boeken van een nieuwe inkoopfactuur (volgende matching) verschijnt het betreffende artikel op het inkoopnummer.

Wat doe ik als ik inkoop bij leverancier A en dat B factureert?

Geef bij Boeken inkoopfacturen bij relatiecode leverancier B in.

- en kies bij Matching, bij ontvangst relatie, leverancier A.

Wat zijn de uitgangspunten bij matchingsverschillen?

De volgende regels gelden bij het verwerken verschillen in de matching:

- Altijd in de huidige periode.
- Plankvoorraad blijft hetzelfde.
- Geeft altijd een grootboekboeking en altijd in dagboek Matching.

Er wordt nooit een regel opgesplitst.

Een verschil is: als het ontvangst aantal niet gelijk is aan het factuuraantal.

### Overige

Wanneer wordt de voorraad geboekt?

- Direct bij de goederen ontvangst. Zie Boeken goederenontvangst (AVO).

Wanneer wordt de inkoop geboekt?

- Na inboeken factuur.

Wanneer wijzigt de financiële voorraad?

- Direct bij de Ga naar Boeken goederenontvangst (AVO),
- Bij Overzicht voorraadmutaties kan er een overzicht aangevraagd worden van de matching status.

Wat doe ik met onterechte ontvangsten?

- Een negatief ontvangst doen. Daarna via Selecteren matching manco's de regels tegen elkaar wegboeken.
- Bij Goederenmatching kan het factuuraantal gewijzigd en een reden hierbij opgegeven worden.

Hoe zie ik wat er wel/niet gematcht is / de matching?

- Bij Overzicht voorraadmutaties (ALM) kan bij de optie matchingstatus de volgende statussen bekeken worden. 1. Alle 2. Ontvangen, de inkoop is ontvangen maar nog niet gekoppeld aan een factuur. 3. Proforma, de inkoop is met een factuur gekoppeld, maar nog niet doorgeboekt. 4. Gematcht, de inkoop is gekoppeld met de factuur en doorgeboekt. Bij matching relatiecode en factuur vanaf en t/m kan het overzicht verder gespecificeerd worden.

Welke methodes zijn er bij goederen matching?

Bij de goederen ontvangst matching kan in de regels het één of het ander opgegeven worden:

- Regelbedrag, in kolom Netto (regel).
- Stuksprijs, in kolom Inkoop.

Om dit in te stellen of te wijzigen, raadpleeg de helpdesk.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Goederenmatching Overzicht matching controlelijst

Overzicht voorraadmutaties

---
## Hoe lees ik nieuwe kortingsafspraken van mijn leverancier in?

Met een leverancier bijv. Kramp heeft u nieuwe kortingsafspraken. U heeft van deze leverancier een Excel document ontvangen met de nieuwe prijzen. Deze wilt u graag doorvoeren in het artikelbestand.

Om deze kortingstabel in te lezen, doorloopt u de volgende stappen:

1. Ga naar Import prijsafspraken inkoop (APK).
2. Selecteer de cataloguscode.
3. Geef het bronbestand in.
4. Vul de overige gegevens in.
5. Bij leverancier artikelgroepen selecteer de eventuele actie:
6. Geen actie (standaard)
7. Bijwerken
8. Toevoegen & bijwerken
9. Vervangen Opmerking: Afhankelijk van de actie worden de leverancier artikelgroepen (niet) bijgewerkt, zie ook Onderhoud leveranciersgroepen (AGG).Aan deze groepen kan een prijsafspraak gekoppeld worden bij Inkoop prijsafspraken (API).

Kies voor de knop Inlezen.

Prijsafspraken inkoop zijn ingelezen.

#### Prijsafspraken inkopen toepassen.

Om deze prijsafspraken toe te passen, doorloopt u de volgende stappen:

1. Ga naar Verwerk verwijzingen (AGV).
2. Kies voor de knop Prijsafspraak toepassen. Het scherm Prijsafspraken/catalogus bijwerken verschijnt.
3. Selecteer de Cataloguscode en maak eventueel nog een selectie.
4. Kies voor de knop Verwerken.

De prijsafspraken zijn bijgewerkt.

---
## Hoe werkt de besteladvieslijst?

## Besteladvieslijst

Een besteladvies wordt gemaakt voor de artikelen waarvan de voorraad onder het 'minimum' gekomen is.

Per leverancier wordt weergegeven, wat er besteld moet worden. Dit wordt berekend a.d.h.v. de ingestelde bestelmethode.

#### Voorwaarde

- De artikelen moeten voorraad artikelen zijn.
- Bij het werken met de besteladvieslijst is het nodig dat de minimum en/of maximum voorraad van de artikelen ingevuld is,uitgezonderd als het bepalen bestelpunt automatisch is.

Het volgende kan per artikel opgegeven worden:

| Bepaling bestelpunt | Optie voor het bepalen van het bestelpunt: - Handmatig (standaard) - Automatisch (dynamische bestelpunt), het volgende veld wordt zichtbaar:Verbruik afgelopen X weken bij methode Trend.Geschat verbruik komende X weken bij methode Seizoen. |
| --- | --- |

| Minimum voorraad | De minimum voorraad. Als de voorraad van dit artikel onder deze waarde komt, zal het artikel op de besteladvieslijst komen (om te bestellen). |
| --- | --- |

| Maximum voorraad | Dit aantal bepaalt (als Bestelmethode voorraad maximum is), tot welk aantal er besteld wordt.Bijv. minimum is 3, maximum is 10 en de plankvoorraad is 2. Powerall besteld tot de maximale voorraad, er worden er 8 besteld (max. - plankvoorraad: 10-2=8). |
| --- | --- |

| Bestelmethode voorraad | - Maximum er wordt tot het maximum aantal besteld, wanneer het voorraad aantal beneden het minimum komt.- Minimum er wordt tot het minimum aantal besteld, wanneer het voorraad aantal beneden het minimum komt.- Bestelhoeveelheid er wordt gebruik gemaakt van de 'Dynamische bestelpunt' parameters (uit Instellingen Artikelen, tabblad Voorraad/Bestelmethodiek) met een gemiddelde afname per week. |
| --- | --- |

- Dynamisch bestelpunt:

| Verbruik afgelopen X weken ofGeschat verbruik komende X weken (seizoen) | Dit veld wordt alleen getoond als bepalen bestelpunt automatisch is, tekst is afhankelijk van de methode Trend (standaard) of Seizoen.- Wordt automatisch berekend, als besteladvieslijst gedraaid wordt. Zie ook opmerking bij dit veld (Laatste berekend: dd/mm/jj)- X wordt bepaald door Instellingen artikelen, tabblad Voorraad/bestelmethodiek, veld Berekenen met verbruik afgelopen/komende  weken. |
| --- | --- |

#### Resultaat

Op de besteladvieslijst staat in kolom BstHvh het aantal dat besteld moet worden.

#### Voorbeeld

| Artikel | Minimum voorraad | Maximum voorraad | Bestelmethode | Voorraad | Aantal besteld | Formule/opmerking |
| --- | --- | --- | --- | --- | --- | --- |
| Olie filter | 2 | 0 | Minimum | 1 | 1 | 2-1=1 |
| Olie filter | 2 | 3 | Maximum | 1 | 2 | 3(max)-1=2, zie * |
| Motor olie | 1 | 2 | Minimum | 1 | 0 | 1-1=0 |
| Motor olie | 1 | 2 | Maximum | 0 | 2 | 2(max)-0=2, zie * |

Opmerking: * Hierbij wordt besteld tot de maximum voorraad, als deze gevuld is.

- Besteladvieslijst (goedkeuren)
- Hoe, wat kan ik m.b.t. de dynamische bestelhoeveelheid?
- Hoe, wat kan ik m.b.t. de minimum en maximum voorraad?

---
## Hoe, wat m.b.t. kleine machines (vernieuwd)

#### Algemeen

Het doel van de kleine machines is, op een gemakkelijke en snelle wijze machines aan te maken met de te registeren serienummers.

*Hoe werkt een 'kleine machine' administratie? #### Kleine machines Inkoop Bij Kleine machine worden van een (machineverkoop) artikel een aantal ingekocht, met registratie van de serienummers. Verkoop Bij de verkoop transactie, wordt het serienummer (SN) geselecteerd en automatisch wordt er een machine aangemaakt. De 'machine gegevens' van het artikel worden hierbij overgenomen. - Er kan per regel meer dan één kleine machine geselecteerd worden. - D.m.v. de knop Serienummers moeten de serienummers gekoppeld worden. Dit kan direct of later, bij een bon moet dit direct. - Een SN kan ook ontkoppeld worden, bijv. voor een spoed order van een balie klant.. - Machine(s) kan handmatig of automatisch aangemaakt worden. Bij vrijgave gebeurt dit automatisch. Afdruk mogelijkheid van de Machine labels d.m.v. Print label. Als een verkooporder regel besteld wordt, en later ontvangen, zijn de SN's al aangevinkt. Mogelijkheid voor opgave van garantie voor commercieel en particulier gebruikt. Er kan geen negatief aantal ingegeven worden. De melding Negatief aantal wordt bij 'Kleine machines' niet ondersteund verschijnt hierbij. Creditnota's lopen via Hoe maak ik een creditnota? De koppeling tussen het SN en de machine blijft bestaan. Op de machine kan immers een label met het SN bevestigd zijn. - Bij het scherm Artikeltracering is direct het servicenummer te zien als deze al gekoppeld is. - Bij de machine bijv. bij Opvragen machines (MO): Op tabblad Financieel staat de verkoper bij de eigenaar en komt de juiste inkoopprijs te staan en de nettoprijs komt in het veld verkoopprijs en bij gebruik van de adviesprijs wordt deze overgenomen. - Wordt een machine transactie weggeschreven met het regelbedrag, zie tabblad Transactie. Als een kleine machine ingeruild wordt, moet deze als machine behandeld / ingeruild worden. Bij de module Service of Verhuur kunnen kleine machine artikelen niet gebruikt worden. De melding Kleine machines worden niet ondersteund verschijnt dan. Bij Onderhoud artikeltracering is de kolom Servicenummer te zien. - Goederenontvangst - Bon / verkooporder - Offerte - Onderhoud en opvragen artikelen - Opvragen machines - FAQ - Voorraad correctie - Instellingen NB Voor serienummer wordt de afkorting SN gebruikt, voor servicenummer machine en voor Kleine machine artikel KL. #### Goederenontvangst Bij Boeken goederenontvangst (AVO) worden alle ontvangen serienummers geregistreerd. De ontvangen serienummers moeten ingegeven worden per regel bij Einde ontvangst. Klik hier, voor meer informatie over dit onderwerp. Opmerking: Er wordt er vanuit gegaan dat de serienummers bij ontvangst geregistreerd worden in Powerall Connect. Om de serienummers op te geven bij de goederen ontvangst, doorloopt u de volgende stappen: 1. Ga naar Boeken goederenontvangst (AVO)ofvia Selecteren inkooporders (IS) > selecteer de inkooporder > Ontvangst. 2. Geef de gegevens in. 3. Kies voor de knop Einde Ontvangst. Het scherm Artikeltracering verschijnt. 4. Geef de in, of Kies voor de knop Genereer nummers. 5. Meerdere serienummers kunnen ingegeven worden als het ontvangstaantal groter is dan één. 6. Kies voor de knop Einde Het artikel is ingeboekt met de betreffende serienummer(s). - NB Als de inkooporder aan een BtB order gekoppeld is, wordt het SN bijgewerkt, als het vinkje Serienummer(s) koppelen aan BtB verkopen orderregel is aangevinkt. - Het is mogelijk om een afwijkend aantal SN op te geven, bijv. bij een foutief ingave. De volgende melding verschijnt: Het aantal opgegeven serienummers is niet juist. Wilt u er X ontvangen? Er worden er hierbij X opgeboekt. Als er 0 ontvangen worden, wordt er niets geboekt! #### Bon / verkooporder Bij een bon verschijnt, na ingave van het artikel met een serienummer het scherm Artikeltracering. Selecteer hier het SN. Klik hier, voor meer informatie over dit onderwerp. Het volgende geldt bij serienummers: - Als het aantal geleverd ingevuld wordt, moet er een serienummer en servicenummer gekoppeld zijn bij Einde order, anders verschijnt de melding: Onvoldoende serienummers of servicenummers gekoppeld voor regel X. - Bij bonnen wordt als het serienummer aangevinkt is, automatisch een servicenummer aangemaakt bij Einde. - Als bon of een regel verwijderd wordt, blijft het serienummer met het servicenummer gekoppeld (er kan bijv. een sticker met het serienummer op de machine zitten). Dit geldt ook bij een creditnota, het serienummer komt dan weer op voorraad. Bij vrijgave van een verkooporder naar een bon, kan het aantal niet meer gewijzigd worden. - Het is wel mogelijk om de regel te verwijderen en deze opnieuw toe te voegen en het opnieuw te koppelen. Er kan geen BtB inkooporder aangemaakt worden in een bon. Voor de facturatie wordt er gecontroleerd of alles 'gekoppeld' is. #### Bon details en Verkooporder details Een knop Serienummers is beschikbaar bij een regel met een KL. #### Verkooporder Bij een verkoop van een kleine machine geldt het volgende: - Het serienummer wordt geselecteerd (uit het betreffend magazijn, bij de optie multimagazijn. of - Als het aantal gereserveerd ingevuld wordt, moeten er voldoende serienummers aanwezig zijn bij het vrijgeven. - Bij geen voorraad: Wordt er een Inkooporder (BtB) aangemaakt. - Artikel reservering bij inkoopstatus besteld. - Klik hier, voor meer informatie over dit onderwerp. Bij een Kleine machine er als de inkooporder besteld is voorkoop te staan, in de kolom status. Als voorkoop geselecteerd is, wordt de inkooporder gesplitst in stukje voorkoop / bestelling en BTB order. Bijv. er waren er 8 besteld en er wordt 1 BtB verkooporder toegevoegd, het aantal besteld wordt dan 7 bijv.: | Artikelcode | Besteld | Inkoop aantal | Bestemd voor | | --- | --- | --- | --- | | X | 7 | 7 | | | X | 1 | 1 | VO- | Opmerking: Het order aantal mag hierbij niet groter zijn dan het (nog niet gekoppelde) inkooporder aantal. Als de order gekoppeld is aan een bestelde inkooporderregel, kan deze order regel niet verwijderd worden. De melding Verwijderen regel is niet mogelijk, gekoppelde inkooporderregel al definitief verschijnt. Aan het einde van de regel wordt er een melding gegeven Wilt u direct serienummers koppelen? indien er vrije SN aanwezig zijn. Als er een SN al gekoppeld is en het aantal Besteld wijzigt, verschijnt de melding Aantal wijzigen voor deze KM is niet mogelijk, er is al een serienummer gekoppeld aan deze verkoopregel. Ook kan d.m.v. de knop Serienummers serienummers gekoppeld worden, bij een regel met een KL. Bij het scherm Artikeltracering is het volgende mogelijk: - Aanmaken nieuwe machine via de knop Maak servicenr. 1. Een servicenummer verschijnt in de regel en de knop Print label wordt actief. 2. De machine met een machine transactie wordt aangemaakt. - Print label, afdrukken van een machinelabel. Als het veld MVA281 Servicenummer_1 op de layout staat, wordt het SN afgedrukt. Bij Vrijgeven gebeurt het volgende: - Er wordt er gecontroleerd of er voldoende SN's gekoppeld zijn. - Het SN wordt verwijderd uit de VO regel tekst en op de bonregel weergegeven. - De machines worden aangemaakt, als dat nog niet het geval was. Het magazijn, prijzen e.d. worden bijgewerkt en de inkoop voorraadstatus wordt NVT. - Er wordt ook een machine transactie aangemaakt. #### Offerte Na ingave en vrijgave van de offerte kun je de serienummers aanvinken in de verkooporder. Een offerte van een kleine machine, wordt altijd vrijgegeven naar een verkooporder. Klik hier, voor meer informatie over dit onderwerp. Om een offerte aan te maken voor een kleine machine, doorloopt u de volgende stappen: 1. Ga naar Nieuwe offerte aanmaken, Geef de Kleine machine in en maakt de offerte aan. 2. Bevestig deze, zie Bevestigen offerte. 3. Kies voor de knop Vrijgeven. 4. Bij Vrijgeven offerte, wordt er vrijgeven naar verkooporder. 5. Hierbij kan alvast een artikel gereserveerd worden, als er een inkooporder / bestelling openstaat. Als er 2 besteld zijn, wordt deze gesplitst in 1 normale - en 1 BtB bestelling. 6. Bij het vrijgeven is, er bij een bestelling, de keuze reserveer voorkoop: | Aantal geleverd vullen | Optie om aantal geleverd alvast te vullen:- Nvt (standaard) bij optie Bon.- Ja (vul ja in bij een werkorder, anders wordt het vastbedrag niet gevuld).- Nee- Voorraad, er wordt rekening gehouden met aanwezige voorraad.- Reserveer voorkoop, instelling alleen bij kleine machines, mogelijkheid om uit een openstaande bestelling alvast artikel(en) te reserveren (BtB koppeling te maken). | | --- | --- | De verkooporder is aangemaakt en de serienummers kunnen daar geselecteerd worden. #### Onderhoud en opvragen artikelen Bij een artikel met een kleine machine is de knop Machinegegevens zichtbaar bij: - Opvragen artikelen - Onderhoud artikelen (ABA) De Kleine machine kenmerken worden overgenomen bij het aanmaken van een nieuwe machine. Klik hier, voor meer informatie over dit onderwerp. Bij Onderhoud artikelen (ABA) kan een kleine machine artikel aangemaakt worden. - Na ingave van het artikel, wordt via de knop Machinegegevens de gegevens ingegeven. Opmerking: Bij Doorgaan worden de gegevens opgeslagen! - De (financiële) artikelgroep moet soort groep artikel/machine hebben. - De standaard configuratie wordt overgenomen van de hoofd- en subgroepen, zie Onderhoud machine (hoofd- en sub) groepen. - D.m.v. de knop Kleine machines kan direct een kleine machine artikel aangemaakt worden. De melding Wilt u een kleine machine van dit artikel aanmaken verschijnt, bij ja wordt het volgende ingesteld: De soort artikel wijzigt naar Machineverkoop. - Gebruik tracering wordt ja. - Voorraad bijhouden wordt ja. Vervolgens verschijnt het scherm Kleine machine kenmerken. - De velden Merk, hoofd- en subgroepen en configuratie zijn verplicht. - Hieronder een uitleg van de velden van scherm Kleine machines kenmerken: | Kleine machine kenmerken | Via knop Machinegegevens. | | --- | --- | | Merkcode / merk | Het merk van de machine. Er kan ook een afkorting ingegeven worden. | | --- | --- | | Type | Het merk type van de machine. | | --- | --- | | | | --- | | Hoofdgroep | De hoofdgroep van de machine. D.m.v. hoofdgroepen kunnen machines gecategoriseerd worden, zie Onderhoud machine (hoofd- en sub) groepen. | | --- | --- | | Subgroep | De subgroep van de hoofdgroep. | | --- | --- | | | | --- | | Garantiecode | De garantiecode of garantieconditie, zie Onderhoud garantiecodes. | | --- | --- | | GarantiecodeCommercieel / Particulier | De garantiecode optioneel, zie Onderhoud garantiecodes, voor een kleine machine:- Commercieel.- particulier verkoop. | | --- | --- | - Opmerking: Als het artikel terug gewijzigd wordt naar een normaal artikel, moeten deze velden terug gezet worden. #### Opvragen machines Het volgende geldt hierbij: - Bij het aanmaken van een machine worden de gegevens van het artikel Machine gegevens overgenomen. Hierbij wordt er ook een machine transactie aangemaakt. - Een machine waaraan een SN gekoppeld is, kan niet verwijderd worden, de volgende melding wordt weergegeven: Machine is gekoppeld aan een serienummer, verwijderen niet mogelijk! #### Factuur en SN Bij facturatie wordt er gecontroleerd of er een SN gekoppeld is. Als dit niet het geval is, verschijnt de melding: - Onvoldoende serienummers gekoppeld. Op de factuur worden de SN's weergegeven. #### FAQ #### FAQ - De voorraad loopt via het artikel (daardoor behoeft er geen machine levering geregistreerd te worden). - Een serienummer artikel is bijna hetzelfde als een Kleine machine, behalve wordt er geen Machine aangemaakt. - Bij het scherm Artikeltracering is er de knop Servicemelding beschikbaar, vanaf versie 3.21.Van de geselecteerde regel(s) kan dan een servicemelding aangemaakt worden. Hoe kan ik een verkooporder met een Kleine machine picken? I.c.m. Overzicht orders (te picken) 2.0 wordt een verkooporder bij Invoeren/wijzigen verkooporders via onderstaande knop gepickt: - Kies voor de knop Picken order. Het aantal gereserveerd wordt opgeteld bij het aantal geleverd. Hoe komt het dat de knop Serienummers niet getoond wordt, bij mijn verkooporder? De knop Serienummers wordt alleen getoond als: - De geselecteerde regel een artikel met een serienummer is. - Het aantal gereserveerd + aantal gepickt > groter is als 0. - Het artikel Gebruik tracering serienummer is. Hoe zit het met de artikelen met een serienummer zonder machines? Bij artikelen met een SN (zonder het gebruik van servicenummers) is het volgende ingevuld. - Soort artikel is normaal. - Er zijn geen machinegegevens of Kleine machine kenmerken. - Gebruik tracering is hetzelfde serienummer. Het volgende geldt hierbij: - Bij de orders is ook de knop Serienummers beschikbaar. - De kolom Servicenummer wordt niet getoond. Er worden immers geen servicenummer of machines aangemaakt. Houdt de telfunctie in de barcodescanner ook rekening met serienummer tracering. Ja, voor meer informatie zie: Hoe, wat m.b.t. kleine machines (vernieuwd) bij Voorraad correctie. Kan ik bij een verkoop van een kleine machine ook een servicemelding aanmaken? Ja, het is mogelijk om een servicemelding aan te maken, bijv. voor het gereedmaken. Wijzig bij Instellingen servicemeldingen per proces het proces Verkoop kleine machines naar onzichtbaar of zichtbaar en vul de gewenste gegevens in. - Dit is bijv. handig voor een SN op de kleine machine of voor het gebruiksklaar maken. - De servicemelding is niet gekoppeld aan de (verkoop)order, deze kan immers geannuleerd of gewijzigd worden. Bij het scherm Artikeltracering is er de knop Servicemelding beschikbaar, vanaf versie 3.21. Wat doe ik bij de melding: 'Geen serienummers om te selecteren'? Bij de ingave van het artikel (bij bonnen) kan deze melding verschijnen als er geen serienummers (SN) voorradig zijn. Oplossing(en) - Zet het aantal geleverd op 0, en selecteer later het juiste SN. - Controleer via de knop Serienummers of er SN voorradig zijn. - Controleer of het juiste magazijn gekozen is. Wanneer gebruik ik kleine machines? In de volgende situaties worden kleine machines gebruikt: - Machines met lage marge, met zo min mogelijk administratieve handelingen. - Normaliter wordt hierbij geen werkorder gebruikt. Of één werkorder per maand voor alle kleine machines. Welke transacties zijn er m.b.t. tracering / kleine machines? De volgende kleine machine transacties / mutatietype zijn er: - A= Afgifte (bon of verkoop) - I = Inkoop * - L = Retour leverancier of negatieve voorraad correctie / verwijderen SN N = Correctie (-) Negatief , vanaf versie 3.27. O = Ontvangst * - of positieve voorraad correctie / toevoegen SN - of Correctie (+) *, vanaf versie 3.27. R = Credit * is + / toename, rest is afname / -. #### Credit ontvangst / inkoop Klik hier voor meer informatie over een credit inkoop / retour: Als een artikel retour gaat naar de leverancier, omdat bijv. een andere dealer deze verkoopt, kan een negatieve inkooporder geboekt worden. Bij het boeken Boeken goederenontvangst (AVO) moet na Einde ontvangst het serienummer selecteert worden, dat retour gaat. Dit serienummer wordt retour geboekt. - In dit voorbeeld is er sprake van een handmatig ontvangst (niet via een inkooporder). #### Creditnota Hoe maak ik een creditnota van een kleine machine? Voor meer informatie om een creditnota te maken zie: - Hoe maak ik een creditnota? Vink de regel met de kleine machine aan. Het serienummer komt weer terug op voorraad. - Het serienummer komt weer terug op voorraad met mutatietype Credit, zie Onderhoud artikeltracering. #### Verkooporder Kan ik achteraf alsnog een serienummer aan een machine koppelen? Bij Invoeren/wijzigen verkooporders is het mogelijk om achteraf (bij machineartikel bestellen zonder BtB koppeling) alsnog een serienummer aan de machine te koppelen. - Dit kan via de knop Serienummers. - Dit kan door het aantal gereserveerd van 0 naar 1 te wijzigen en dan een serienummer te selecteren. - Als het aantal gereserveerd op 0 wordt gesteld, is het weer mogelijk om de machine toch te bestellen (via BtB koppeling). #### Verkooporder en bestellen Klik hier voor meer informatie over een verkooporder met de optie bestellen: De verkooporder wordt op normale wijze ingegeven. Als er geen serienummers op voorraad zijn (in het magazijn), dan kan het KM artikel via een BtB besteld worden. Hierbij wordt het aantal gereserveerd op 0 gezet, zodat er een back-to-back (BTB) koppeling gemaakt kan worden met een inkooporder. - Enter door en bevestig de (BTB) inkooporder. #### Ontvangen van de artikelen met serienummers Bij ontvangst van Kleine machine wordt het serienummer ingegeven, en wordt het serienummer in de afgiftemutatie weggeschreven. Na de ingave van het serienummer bij Boeken goederenontvangst vindt het volgende plaats: - Het serienummer wordt afgedrukt op de pakbon. - Het serienummer wordt gekoppeld aan de betreffende verkooporder. - In de 'Artikel tracering', wordt de volgende mutatie geboekt SN X - Ontvangst - ontvangstnummer SN X - Afgifte - VO / klant De verkooporder tekst wordt aangepast met het serienummer. Belangrijk: Bovenstaand werkt alleen bij centraal inkooporders aanmaken is nee. #### Verkoop en nieuwe machine / servicenummer Welke gegevens wordt automatisch gevuld bij een nieuwe machine? De volgende gegevens worden overgenomen van het artikel (indien aanwezig) naar de machine: - Artikelgroep (financieel) - Hoofdgroep en subgroep.Van de machine, kan verschillen. Configuratie, wordt overgenomen van de standaard configuratie, zie Onderhoud machine (hoofd- en sub) groepen. Eigenaar (Verkoopgegevens) Garantie commercieel / particulier. Leverancier, invullen bij artikel! Magazijncode Merkcode - Van de machine, kan verschillen. Omschrijving 1 en 2 Inkoopstatus* Nvt
*Verkoopstatus* Verkocht
Serienummer 2
Bouwjaar (huidige jaar)
Prijzen: Inkoop-, advies- en verkoopprijs.
Klik hier voor een voorbeeld:

Opmerking: Bij een verkooporder, wordt de verkoopprijs gevuld op het moment dat de machine (aantal) geleverd wordt. Dit werkt ook zo voor normale machineverkoop.

#### Inkooporder & verkooporder (BTB) koppeling

Wat gebeurt er als ik een verkooporderregel die gekoppeld is aan een inkooporder regel verwijder?

De verkoop - en de inkooporderregel worden beide verwijderd.

Wat gebeurt er als ik een inkooporderregel die gekoppeld is aan een verkooporder regel verwijder?

Er verschijnt een melding met de vraag, of ook de gekoppelde verkooporder regel verwijderd moet worden?

Hoe zit het met de inkoopstatus van de kleine machine?

De inkoopstatus van een (kleine) machine blijft altijd op nvt staan.

- De voorraad loopt via het artikel / de artikeladministratie.

#### Prijsafspraken

Met welke prijsafspraken wordt er rekening gehouden bij kleine machineverkoop?

Bij kleine machineverkoop werken onderstaand prijsafspraken niet:

- Actieprijs, zie Onderhoud artikelen (ABA).
- Vaste verkoopprijs via verkoopprijsafspraken.

Een verkoopprijsafspraak met percentage werkt wél, zie Verkoop prijsafspraken (APA) bij een machineverkoopartikel.

#### Voorraad

Hoe zie ik de serienummers van mijn artikelvoorraad?

Om de voorraad van de artikels met een serienummer te bekijken, doorloopt u de volgende stappen:

Optie A

1. Ga naar Opvragen artikelen (AO) of F7.
2. Ga naar tabblad Voorraad.
3. Kies voor de knop Serienummers.
4. Alleen mutatietype ontvangst en positieve correctie zijn hierbij zichtbaar.

of

Optie B

1. Ga naar Onderhoud artikeltracering (ABT).
2. Geef het artikel in, of blader door de artikelen met de pijltjes toetsen.

Optie C

1. Ga naar Voorraadwaardelijst (ALW).
2. Geef een selectie op.
3. Kies voor de knop Afdrukken.

Onder de betreffende artikelen worden serienummer(s) weergegeven.

#### Voorraad correctie

Bij een voorraad correctie i.c.m. een kleine machine moeten serienummers toegevoegd of verwijderd worden.

Klik hier voor meer informatie over het corrigeren van de voorraad:

Om de voorraad van een 'kleine machine artikel' te corrigeren, doorloopt u de volgende stappen:

1. Ga naar Boeken correcties (AVC).
2. Geef de gegevens in, zie: Artikel voorraad corrigeren
3. Kies voor de knop Einde correctie.Bij een positieve correctie moet een serienummer(s) ingegeven worden.Voeg het serienummer(s) toe.
4. Kies voor de knop Einde.

Bij een negatieve correctie moet een serienummer(s) gecorrigeerd worden.

1. Vink het serienummer aan, dat 'verwijderd' moet worden.
2. Kies voor de knop Einde.

Klik hier voor meer informatie over corrigeren van de voorraad met barcode scanning:

Er worden 2 kleine machine artikelen ingescand. Het ene artikel met te weinig op voorraad, het andere met te veel op voorraad:

1. Één artikel te weinig op voorraad (correctie + / +), en
2. het ander artikel te veel (correctie - / -).

### Instellingen

#### Serienummers

- Serienummers kun je handmatig invullen, dan gebruik je het serienummer van de fabrikant; je gaat er vanuit dat deze uniek zijn.
- Serienummers kun je genereren, dan wel gebruik maken van een prefix (voorloopcode lotnummer) die aangeeft dat het van jou is en niet alleen een numeriek nummer.

Wat zijn de voorwaarden?

De volgende voorwaarde zijn hierbij van toepassing:

| Velden | Omschrijving |
| --- | --- |
| Hoofd - en subgroepen | De hoofdgroep en subgroep bij het artikel moeten onder dezelfde code als hoofd en subgroep bij de machinehoofd en subgroepen bestaan. |
| Configuratie | Kan niet overgenomen worden vanuit een artikel. Indien nodig zelf opgeven. |
| Eigenaar | Wordt gevuld als deze machine op een verkooporder verkocht wordt. |
| Leverancier | Controleer bij meerdere leveranciers of juiste leverancier gevuld is. |
| Merkcode | Bij artikelen en machines moeten dezelfde merkcodes gebruikt worden. |
| In - en verkoopstatus | Wordt niet overgenomen, maar gevuld a.d.h.v. de verkoop van deze machine/dit artikel. |

Wat moet ik instellen om dit te gebruiken?

#### Instellingen artikelen

Bij Instellingen artikelen, tabblad Beheer, moet gebruik artikeltracering op Serienummer of Lot- en serienummer staan.

- | Gebruik artikeltracering | Optie om artikel tracering te gebruiken:- Nee, (standaard)- Inkoopnummer- Lotnummer- Serienummer- Lot- en SerienummerNB Het vinkje Serienummers koppelen aan BtB verkooporderregel verschijnt bij Boeken goederenontvangst (AVO). | | --- | --- | | Voorloopcode lot-serienummer | Dit is de voorloopcode van het betreffend lot of serienummer. Het artikeltracing nummer is bijv. SN-0001001, waarbij SN- de voorloopcode is. | | --- | --- | | Volgnummer lotnummers | Dit is het actuele volgnummer. Bij een nieuw artikeltracering, wordt dit nummer met 1 verhoogd. Het artikeltracing nummer is bijv. SN-0001001, waarbij 0001001 het volgnummer is. | | --- | --- |

#### Instellingen machines

Bij Instellingen machines moet het volgende ingesteld zijn:

1. Op tabblad Scherminvoer, moet Machine autonummering op automatisch staan:

- | Machine autonummering | Optie voor de nummering van nieuwe machines:- Automatisch (standaard) het laatst gebruikte machine - / servicenummer wordt met 1 verhoogd.- Normaal, het nieuw servicenummer wordt handmatig opgegeven. | | --- | --- |

1. Op tabblad Koppelingen en beheer, moet Gebruik artikelcode op ja staan:

- | Gebruik artikelcode | Optie voor het gebruik van een artikel m.b.t. een machine:- Ja (standaard), gebruik voor Kleine machine.- Nee, de artikelcode is niet invulbaar of zichtbaar. | | --- | --- |

#### Onderhoud artikelen

Bij Onderhoud artikelen (ABA) moet bij het (machineverkoop) artikel het volgende ingesteld zijn:

1. Soort artikel is machine verkoop (tabblad Algemeen).
2. Gebruik tracering is Serienummer. NB serienummer registratie mag alleen gebruikt worden bij voorraadhoudende artikelen.
3. De financiële artikelgroep van het artikel en machine is hetzelfde.
4. Tabblad Voorraad, Voorraad bijhouden is Ja.

Bovenstaand kan d.m.v. de knop Kleine machine.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Hoe maak ik een creditnota?
- Invoeren kassabonnen
- Onderhoud artikeltracering
- Instellingen servicemeldingen per proces
- Wat is artikeltracering?

---
## Hoe lijn ik de uitgebreide machine verkoop teksten uit?

Het is mogelijk om de uitgebreide teksten bij een machineverkoop netjes uit te lijnen.

Klik hier, voor meer informatie over dit onderwerp.

Dit zijn de ingestelde teksten bij Instellingen machines, tabblad Printvoorkeuren.

- | Machine informatie | De volgende machinegegevens (max.10) kunnen weergegeven worden op de pakbon / factuur:- Bouwjaar - BPM: - Extra nummer - Garantieconditie - Merk/Type - Merk - Kenteken - Kleur - Omschrijving 1 t/m 6 - Servicenummer - Serienummer 1 t/m 3 - Tellerstand: - Type - Datum afgifte (of Eerste registratie, alleen bij Machine administratie 2.0) | | --- | --- |

Klik hier voor: Voorbeelden.

#### Instellingen & voorwaarden

1 Bedrijf

Bij Instellingen bedrijf, tabblad Algemeen kan bij scheidingsteken uitlijnen teksten een  opgegeven worden.

- Belangrijk: Als het scheidingsteken niet ingevuld is, wordt de tekst op de normale manier weergegeven.
- Gebruik hetzelfde scheidingsteken als bij de voorloopteksten bijv. .

2 Aanpassen lay-outs

Er is hiervoor een regeltekst uitgelijnd toegevoegd, met twee teksten:

- SYS370 ->1e deel van de uit te lijnen tekst.
- SYS371 ->2e deel van de uit te lijnen tekst.

Om lay-out te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud layouts (BPO).
2. Volg de stappen 1 t/m 3 bij Lay-out wijzigen.
3. Ga naar tabblad Rapport-2. Vink Regeltekst uitgelijn aan. | | Opmerking: Normale regel uitgebr. moet ook aangevinkt zijn! | | --- | --- |

Ga naar tabblad Onderdeel.

1. Selecteer Regeltekst uitgelijn.
2. Vul bij Hoogte pixels  in.

Ga naar tabblad Detail.

1. Selecteer Regeltekst uitgelijn(in de grijze balk).
2. Voeg de twee nieuwe teksten SYS370 en SYS371 toe: Belangrijk: Omdat de uitgelijnde tekst een herdefinitie is van de regeltekst (Normale regel uitgebreid) is het belangrijk dat de breedte van deze velden overeenkomen.- Gebeurt dit niet dan zal bij wat langere teksten de uitlijning niet goed gaan en wordt het 2e gedeelte op een nieuwe regel geprint.
3. Definieer de nieuwe velden SYS370 en SYS371:Selecteer eerst SYS370 en lijn deze als volgt uit:
4. Doe dit ook voor het veld SYS371.

Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

- Doe bovenstaand ook voor de andere programma met hun lay-outs.
- Opmerking: Het uitlijnen gebeurt 1x per regel, is een 2e scheidingsteken aanwezig in dezelfde regel dan wordt hier niets mee gedaan.

Klik hier voor meer informatie over de betreffende programma's:

Bij de volgende programma's kan de lay-out ingesteld worden:

- IIN54 Print pakbon
- IIN71 Print facturen
- IIN73 Print kopie factuur
- SOR54 Pakbon verkooporder
- SQU71 Print offerte / opdrachtbevestiging

Controle

Controleer of op de (pak)bon of factuur de gegevens correct worden weergegeven.

#### Werkwijze

Bij het aanmaken van een bon / factuur e.d. wordt gecontroleerd of het scheidingsteken voorkomt in de tekst, bij:

- Ja, wordt de tekst uitgelijnd indien regeltekst uitgelijn. aanwezig is.
- Nee, wordt de tekst afgedrukt m.b.v. onderdeel normale regel uitg.

Tip: Als er handmatig een tekst wordt toegevoegd met het scheidingsteken, wordt deze ook uitgelijnd, bijv. .

#### Voorbeelden

Klik hier voor meer informatie over hoe dit eruit ziet:

Hierbij enkele voorbeelden:

- Pakbon:
- Factuur:
- Orderbevestiging:

---
## Hoe maak ik een (verkoop)order voor een machine?

#### Onderhoud artikelen

Bij Onderhoud artikelen moet een 'machine' artikel aanwezig zijn. Hierbij is bij veld Soort Artikel Machineverkoop geselecteerd. Bijvoorbeeld artikelcode:

- , hiermee kan je inkopen, inruilen en verkopen.
- Artikelgroep en het eventuele merk in. Opmerking: De naam van de artikelcode is niet belangrijk, maar wel de (financiële) Artikelgroep met de daaraan gekoppelde grootboekrekening, zie Onderhoud artikelgroepen en het BTW-type Nieuw/gebruikt/marge e.d.

Selecteer op tabblad Voorraad bij voorraad bijhouden nee.

- Uitgezonderd bij artikeltracering op serienummer, selecteer dan bij voorraad bijhouden ja.

#### Order

Selecteer bij de (verkoop)order het betreffend artikel, daarna verschijnt er een pop-up waar bij de machine, d.m.v. serienummer, kan geselecteerd worden.

Machine informatie op pakbon of factuur.

#### Instellingen machines

Bij Instellingen machines, tabblad Printvoorkeuren, staat informatie over de machine. Als deze ingesteld is, kan onderstaande informatie weergegeven worden in de uitgebreide omschrijving en afgedrukt worden op de pakbon/factuur.

- | Machine informatie | De volgende machinegegevens (max.10) kunnen weergegeven worden op de pakbon / factuur:- Bouwjaar - BPM: - Extra nummer - Garantieconditie - Merk/Type - Merk - Kenteken - Kleur - Omschrijving 1 t/m 6 - Servicenummer - Serienummer 1 t/m 3 - Tellerstand: - Type - Datum afgifte (of Eerste registratie, alleen bij Machine administratie 2.0) | | --- | --- |

Wat moet de status zijn van de machine bij verkoop?

Bij Onderhoud machines, tabblad Financieel, moet het volgende staan:

1. De 'Inkoopstatus' moet Voorraad of besteld of inruil verwacht zijn.
2. De 'Verkoopstatus' moet nvt zijn.

Belangrijk: Bij een gesloten machine-administratie mag bij Onderhoud machines (MBB) de verkoopstatus niet aangepast worden, als de machine verkocht is maar nog niet geleverd is.

#### BTW-type

Controleer ook of de BTW- type of regeling correct is van de machine.

- | BTW-type | Het type BTW van de machine: - Nieuw - Gebruikt - Marge, zie Machine marge regeling Bij Onderhoud machines, en bij gebruik van een financiële machine administratie, vindt er een overboeking of grootboek correctie plaats als de inkoopstatus voorraad is en het BTW type gewijzigd wordt.Het BTW-type kan niet gewijzigd worden bij Inkoopstatus = Voorraad en Verkoopstatus = Verkocht / Eigendom. | | --- | --- |

---
## Hoe kan ik bij zoek machines bepaalde machines niet laten zien?

Door het instellen van een machine categorie is het mogelijk om bijv. speciale - of kleine machines zoals een boormachine of kettingzaag, niet te tonen bij het standaard zoekvenster.

#### Instellingen

Het volgende moet ingesteld worden:

Bij Onderhoud machine (hoofd- en sub) groepen moet voor elke groep een categorie ingesteld worden:

- | Categorie | De betreffende categorie. Deze categorie dient om bepaalde machines al of niet te tonen bij het zoekvenster machines vanuit werkorders. Bijv. kleine machines worden niet getoond. | | --- | --- |

De machines die je niet wil zien, zet je bijv. op categorie 1 en de rest hoger.

Opmerking: Bij alle machine groepen moet de categorie worden ingesteld, anders zijn de machines niet zichtbaar bij Zoek machines.

Bij Instellingen machines, tabblad Koppelingen en Beheer, kan de minimale categorie zoekvenster ingevuld worden.

- Zet deze bijv. op 2.

#### Zoeken machines

Bij Zoek machines is het aanvink vakje Geen filter op categorie zichtbaar.

Standaard worden de machines van categorie 2 of hoger getoond.

- Als dit vakje wordt aangevinkt, worden de kleine machines, categorie van bijv. STIHL wel getoond. MVAWIN

Standaard zijn de gele gearceerde machines niet zichtbaar.

- Zoek machines

---
## Hoe werk ik de APK of Tachograaf datum bij?

Powerall Connect is gekoppeld met het RDW. Hierdoor is het mogelijk om de APK datum bij te werken.

#### Voorwaarde

Om APK / Tachograaf datum bij te werken moet het volgende ingesteld zijn:

- De keuringscode bij Onderhoud keuringscodes.
- De keuringscode APK en of Tachograaf moet gekoppeld zijn aan keuring 1/ 2/3/4 zie Keuringen instellen. Bij Tachograaf kan gebruik gemaakt worden van een RDC account.

Het kenteken bij de Machine.

Belangrijk: Module Keuringen is hiervoor nodig.

#### Bijwerken APK / Tachograaf datums

Om de datum(s) bij te werken, a.d.v.d RDW gegevens, doorloopt u de volgende stappen:

1. Ga naar Selecteren machines (MS) Ga naar tabblad Service. Alle machines met een keuring(s info) verschijnen op het scherm.
2. Kies voor de knop Keuringsdatums / Bijw. APK-datums, Het scherm Keuringsdatums bijwerken? verschijnt. Afhankelijk van de ingestelde RDW keuringen verschijnt de juiste tekst APK / Tachograaf.
3. Kies voor de knop OK.
4. Na het bijwerken verschijnt er een melding. Controleer het aantal machines bijgewerkt.
5. Kies voor de knop OK. Tip: De geplande tachograaf-datum wordt ook bijgewerkt, als deze keuring ingesteld is.

(Optioneel) :

1. Selecteer bij welke keuring APK.
2. Vul eventueel een Keuringsdatum van en t/m in.
3. Kies voor de knop Selecteer. De machines die hieraan voldoen, verschijnen op het scherm.
4. Kies voor de knop Keuringsdatums / Bijw. APK-datums

Na het bijwerken verschijnt er een melding.

- Controleer het aantal machines bijgewerkt.

Kies voor de knop OK.

De APK-datums zijn bijgewerkt.

FAQ

Tip: Dubbel-klik op een Machine regel om de APK datum te bekijken, op tabblad Service bij Opvragen machines.

Tip: Voor gegevens opvragen via kenteken ook zie RDW, druk op Vervaldatum en historie of RDWdata.nl (kentekencheck), Kenteken&documentcontrole

Opmerking: Bij APK wordt er gerekend met de RDW data, niet met actuele APK datum en het aantal dagen.

#### Bijwerken APK-datum

Bij Onderhoud machines (MBB) en Opvragen machines (MO) is het ook mogelijk om de APK datum bij te werken, op tabblad Service d.m.v. de refresh knop .

- Zie Keuringstermijn ingeven

- Selecteren machines

---
## FAQ Machines, tellerstanden

In dit hoofdstuk staan diverse vragen over machine tellerstanden.

- Hoe, wat m.b.t. de tellerstand registratie?

Tellerstand 1 en 2 worden bijgehouden voor de onderhoudshistorie.

Waar geef ik tellerstanden op?

- Bij Onderhoud machines, tabblad Service, kunnen deze gewijzigd worden.
- Bij opgave van een werkorder of verkooporder kan een servicenummer opgegeven worden. 1. Kies voor de 3 puntjes knop. Het scherm (machine) Transactie verschijnt. 2. Geef de Tellerstand 1 en 2 in. 3. Kies voor de knop Opslaan.
- Bij een offerte Nieuwe offerte aanmaken, waarbij een servicenummer opgegeven is. Bij Vrijgeven offerte naar een werkorder kunnen de tellerstanden opgegeven worden.

Bij een Nieuwe verhuurorder aanmaken, alleen tellerstand 1.

Bij een Nieuwe contract aanmaken, bij selectie Eenheid facturatie contract Tellerstand.

- In de regels, in de 3e kolom, bij de 3 puntjes , kan in scherm Facturatie tellerstanden de tellerstanden opgegeven worden.

In de Werkbon App is het ook mogelijk om tellerstanden 1 en 2 op te geven.

Klik hier voor meer informatie over het opgeven van de tellerstand op de Werkbon App:

Om dit te doen, doorloopt u de volgende stappen:

1. Selecteer de werkorder.
2. Ga naar de werkorder ofMachinedetails, tabblad Service.
3. Kies voor de knop Wijzig transactie.
4. Geef de tellerstand 1 / 2 in.
5. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Voor de Werkbon App zie:

- Registratie en Orderdetails

Wanneer zie ik de tellerstanden bij Opvragen machines, tabblad Transacties?

Bij Opvragen machines (MO) tabblad Transacties geldt:

- Bij het vrijgegeven van een verkooporder naar een bon, worden de tellerstanden overgenomen van de machinetransactie van de verkooporder naar de machine transactie van de bon.
- Dit is ook het geval bij een Externe werkorder als je deze vrijgegeven wordt.

Opmerking: Alleen tellerstand 1 is zichtbaar in de kolom Teller.

De tellerstand is ook zichtbaar op tabblad:

- Services
- Onderhoud

- Teller vervanging registratie

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## FAQ VA-Keur

VA-Keur is het keurmerk voor veiligheidskeuringen arbeidsmiddelen en machines.

In dit hoofdstuk staan de meest gestelde vragen over VA-Keur.

Klik hier voor meer informatie over VA-Keur:

VA-Keur is de periodieke veiligheidskeuring voor arbeidsmiddelen. Deze veiligheidskeuring wordt uitgevoerd door bedrijven, die zijn aangesloten bij brancheorganisatie Fedecom. Arbeidsmiddelen zijn gereedschap, machines en werktuigen in de landbouw-, tuin & park-, intern transport- en industriesector.

- Eén keurmerk voor al uw arbeidsmiddelen
- Een completere keuring
- Gedigitaliseerde en inzichtelijke rapportage

VA-Keur is ISO 27001 gecertificeerd. U weet dus zeker dat we de informatie over uw gekeurde arbeidsmiddelen vertrouwelijk behandelen en opslaan.

### VA-Keur gegevens

Hoe komt het dat het de eerste keer lang duurt als de gegevens opgehaald worden bij VA-Keur?

Belangrijk: De eerste keer ophalen van de gegevens duurt lang (kan zomaar 20 minuten of langer duren), omdat Powerall Connect de gedownloade XML-gegevens volledig gaat analyseren en verwerken.

De VA-keuringsgegevens worden per machine vastgelegd.

Hoe zie ik de VA-Keur keuringsgegevens bij een machine?

In Powerall Connect is het mogelijk om de volgende keuringsgegevens te bekijken:

- Datum
- Stickernummer
- PDF keuringsrapport

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud machines (MBB), tabblad Service.
2. Bij Keuringsinfo worden de keuringsgegevens weergegeven.
3. D.m.v. de PDF 'icoon/knop' Actueel keuringsrapport opvragen kan het PDF rapport bekeken worden.

Opmerking: Bij de communicatie / synchronisatie met de VA-Keur wordt de geplande datum gevuld met de verloopdatum van de VA-Keur.

Welke machine gegevens zijn belangrijk voor VA-Keur?

De machine velden voor deVA-Keur worden bij onderstaande paragraaf:

- Machine VA-Keur

### VA- Keur omschrijving

Hoe wijzig ik de VA-Keur omschrijving?

De Technische Commissie van VA-Keur besluit soms om VA-codes samen te voegen of nieuwe codes aan te maken.

Bijvoorbeeld:

- | Datum | Nieuws | | --- | --- | | okt-2021 | R13 is R80 Overige Tuin en park machines geworden.Nieuw: R15a R27a R32 R60 | | 16-12-2020 | Nieuwe R15a lijst voor keuringen van eenvoudige elektrische apparatuur | | 16-12-2020 | Nieuwe R32 lijst voor de keuring van fietsen en brommers |

Om dit in Powerall Connect te doen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud PDF formulieren (per werkorder) (BAF).
2. Kies voor de knop Wijzigen. of Kies voor de knop Opvoer.
3. Geef juiste naam, type en keuring in.
4. Kies voor de knop Opslaan.

De nieuwe of gewijzigde formuliercode is actief.

Opmerking: Bij een nieuwe formuliercode, koppel deze code bij Onderhoud machines (MBB) tabblad Services, aan de betreffende machines.

Welke keuringscodes behoren bij welke machine?

Zie hiervoor de VA-Keurings checklist, incl. grote of kleine keuringssticker:

- VA-Keur.overzicht.2023.okt.pdf nieuw, laatste wijziging (okt 2023)
- VA-Keur.overzicht.2022.feb.pdf

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Machine VA-Keur
- Onderhoud PDF formulieren (per werkorder)

- https://keuren.va-keur.nl/, zie kop Nieuws en Wijzigingen.

---
## Waarom krijg ik de melding 'Wilt u de teksten van lopende orders bijwerken met de gewijzigde gegevens?'

Als bij Onderhoud machines één van de machine informatie teksten gewijzigd wordt, is het mogelijk om deze teksten in de actuele of openstaande orders aan te passen.

1. De volgende melding verschijnt:
2. Kies voor de knop Ja. Bij ja worden de lopende machine orderteksten of factuur teksten bijgewerkt. Dit geldt voor bonnen, inkoop- en verkooporders en offertes.
3. Belangrijk: Dit geldt alleen voor machines of machine artikelen die niet op voorraad bijhouden staan.
4. Hierbij een voorbeeld van machine teksten, in de tweede regel bij Type is de tekst oms 1-2 toegevoegd. Het serienummer of kenteken kan bijgewerkt worden.

#### FAQ

Opmerking: Als bijv. het kenteken niet was ingevuld, wordt deze informatie toegevoegd.

Hoe kan het komen dat de lopende orderteksten niet worden bijgewerkt worden?

Dit is mogelijk als bij Instellingen machines, tabblad Printvoorkeuren, de voorlooptekst veld(en) 1 t/m x niet zijn ingevuld (in de betreffende taal).

- Controleer deze instelling.
- Onderstaand zijn de teksten juist gevuld: Opmerking: In bovenstaand voorbeeld zijn bij velden 1 t/m 10 de cijfers cijfer 1. etc. toegevoegd, alleen ter controle/verduidelijking. In de praktijk worden er geen cijfers gebruikt. Belangrijk: De voorloopcode 1 t/m X s.v.p. invullen, de zoek en vervangfunctie binnen de lopende orderteksten gaat er vanuit dat er een voorlooptekst is ingevuld.

Waar kan deze melding (lopende teksten bijwerken) nog meer verschijnen?

Dit is mogelijk Boeken goederenontvangst van een inkoopmachine order, het serienummer en kenteken in te geven en bij te werken, zie:

- Is het mogelijk om het serienummer / kenteken op te geven van een machine?

Welke velden kunnen op de order / factuur worden weergegeven?

De volgende machine informatie velden kunnen weergegeven worden op order / factuur:

| Machine informatie | De volgende machinegegevens (max.10) kunnen weergegeven worden op de pakbon / factuur:- Bouwjaar - BPM:  - Extra nummer - Garantieconditie - Merk/Type - Merk - Kenteken - Kleur - Omschrijving 1 t/m 6 - Servicenummer - Serienummer 1 t/m 3 - Tellerstand:  - Type - Datum afgifte (of Eerste registratie, alleen bij Machine administratie 2.0) |
| --- | --- |

- Onderhoud machines

---
## Wat doe ik als de financiële voorraad niet aansluit met de  machines?

# Wat doe ik als de financiële voorraad niet aansluit met de machines?

Bij een gesloten machine administratie moeten de grootboekrekeningen van de machines, aansluiten met balanswaarde van de machines.

### Controle grootboek met machines

Gebruik de gewenste periode bijv. 01-25 t/m 12-25.

Opmerking: Bij de controle kan de waarde overgenomen worden in het Excel controle document.

#### 0 Proef saldibalans

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Proef en saldibalans (GLV).
2. Geef eventueel periode (t/m) in.
3. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

- Controleer/neem over het veld Eind-saldo van de voorraad machines / tussenrekening inkopen machines. Dit kan in kolom D.

#### 1 Voorraad machines

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Machine voorraad (MPP).
2. Selecteer sorteerwijze Financiële groep.
3. Selecteer bij soort lijst 1 Financieel voorraad.
4. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

- Controleer/neem over veld Balanswaarde.

#### 2 Vooruitgefactureerde machines

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Machine voorraad (MPP).
2. Selecteer sorteerwijze Financiële groep.
3. Selecteer bij soort lijst 7 Tussenrek. vooruitfactuur.
4. Kies voor de knop Afdrukken.

- Controleer/neem over veld Verkoopwaarde.

#### 3 Tussenrekening inkopen machines

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Controle machine inkopen (MVC).
2. Selecteer bij Alleen uitzonderingen Ja.
3. Kies voor de knop Afdrukken.

Het Eindsaldo -/- Beginsaldo = Saldo van grootboek Tussenrekening inkopen machines.

#### Voorbeeld

Hierbij een voorbeeld:

#### Excel controle document

Klik hier voor meer informatie over een Excel voorbeeld:

- Controle.machine.administratie.2025.xlsx

---
## Wat zijn de instellingen voor BPM?

#### Wat is BPM?

BPM is de Belasting van Personenauto’s en Motorrijwielen. Voor meer informatie zie BPM belastingdienst.

#### Onderhoud artikelen

Bij Onderhoud artikelen worden twee BPM artikelen toegevoegd:

- BPM Nieuw
- BPM Gebruikt

Belangrijk: De BTW-code is 0 (geen BTW).

Artikelen zitten gekoppeld aan verschillende artikelgroepen, zodat de grootboekrekeningen separaat aangestuurd kunnen worden, deze artikelen hebben geen voorraad.

#### Onderhoud artikelengroepen

Bij Onderhoud artikelgroepen, tabblad Voorraad, moeten de grootboeknummers voor BPM ingevuld zijn. Deze moeten aanwezig zijn of éénmalig aangemaakt worden.

#### Instellingen financieel

Bij Instellingen financieel, tabblad BTW systematiek, wordt voor BPM bijv. btw-code 2 gebruikt zie:

#### Instellingen machines

Bij Instellingen machines, tabblad Koppelingen en beheer, moet veld Gebruik BPM op ja staan.

| Gebruik BPM | Optie voor het gebruik van BPM (Belasting van Personenauto’s en Motorrijwielen):- Nee (standaard)- Ja, opgave of refresh BPM bedrag mogelijk. > vanaf versie 2.38 kan hierbij in FCR05 kosten op kostensoort BPM geboekt worden.• Bij een nieuwe machine kunnen gegevens van het RDW overgenomen worden.Opmerking: Bij Incl. kenteken * kan het kenteken zonder streepjes ingegeven worden, maar wordt 'opgemaakt' op scherm of afdruk met streepjes behalve bij buitenlandse kentekens. |
| --- | --- |

#### Onderhoud machines

Bij Onderhoud machines, tabblad Financieel, kan de BPM opgegeven worden, als bovengenoemde instelling op ja staat.

Opmerking: De balanswaarde wordt inclusief BPM opgegeven.

#### Verkoop transactie en actuele BPM

Bij een verkoop van een machine kan de actuele BPM waarde berekend worden a.d.h.v. het kenteken met de RDW BPM check.

1. Kies voor de knop .
2. Kies voor de knop Ja. Opmerking: Bij BTW-type Marge wordt er geen BPM gebruikt.

Het actuele BPM bedrag wordt overgenomen.

---
## FAQ Machine

**FAQ Machine In dit hoofdstuk staan de meestgestelde vragen over de Machine module. - FAQ Case New Holland (CNH) - FAQ Machines, tellerstanden - FAQ VA-Keur - Hoe maak ik een (verkoop)order voor een machine? - Hoe kan ik kosten achteraf op een machine boeken zonder werkorder? - Hoe kan ik bij zoek machines bepaalde machines niet laten zien? - Hoe werk ik de APK of Tachograaf datum bij? - Hoe, wat m.b.t. de kenteken registratie? - Hoe, wat m.b.t. de machine verkopenlijst? - Hoe, wat m.b.t. de tellerstand registratie? - Hoe, wat m.b.t. kleine machines (vernieuwd) - Waarom krijg ik de melding 'Wilt u de teksten van lopende orders bijwerken met de gewijzigde gegevens?' - Wat zijn de instellingen voor BPM? Onderhoud / Opvragen machines Hoe kan ik op machines zoeken? Via het 'loepje' of de vergrootglas knop of F4 kan naar een machine of servicenummer gezocht worden. Bij Zoek machines kan er gezocht worden op de volgende filters: - Servicenummer (* standaard) - Omschrijving - Merk - Serienummer 1 * - Type - Kenteken * - Vlootnummer * - Verkocht aan De kolom Leverancier wijzigt naar Verkocht aan. Alle * - Zoeken Serienummer 1 en - 2 is hierbij mogelijk * Deze filter kan standaard ingesteld worden. Tip: Gebruik de F4 toets om naar de volgende 'filter' te gaan, er kan ook op elke kolom gesorteerd worden. Afhankelijk van filteren op kunnen er wel of geen kleine letters gebruikt worden. Tip: • Er kan ook gezocht worden op een gedeelte van een tekst, vink hierbij bevat aan.• De standaard sorteer filter kan bij Instellingen machines, tabblad Scherminvoer, Standaard sortering machines aangepast worden. Kan ik ook de offerte(s) van de machine zien? Ja, dit is mogelijk bij Opvragen machines (MO), tabblad Offertes. Waarom wordt dat datum bij de machine configuratie vet** weergegeven?

Dit betekent dat de datum niet wijzigbaar is in de Powerall CRM App.

*Waaruit bestaat de balanswaarde van een machine? De balanswaarde van een machine bestaat uit de inkoopprijs / ontvangst - Interne werkorders kunnen de balanswaarde verhogend zijn, bij: Werkorder soort Intern waarbij het veld Type Interne boeking Voorraad verhogend is. Welke gegevens worden bij elkaar geteld in het veld Totale kostprijs? Op tabblad Financieel bij Tot. kostprijs: Totale kostprijs is een optelling van de inkoopprijs + accessoires + werkorders + werkorders lopend + overige + BPM. - Dit geldt bij de instelling machine administratie 2.0 is Ja. Welke machine gegevens worden in de tekst van de lopende ordergegevens bijgewerkt? Voor meer informatie zie, bij FAQ: - Waarom krijg ik de melding 'Wilt u de teksten van lopende orders bijwerken met de gewijzigde gegevens?' Machines en grootboekboekingen Is mogelijk om een ontvangen bonus te boeken op de machine, waarbij de inkoopwaarde verminderd wordt met het bonus bedrag? Ja, dit is mogelijk om een (inkoop) bonus te boeken op een machine. - Via Machine ontvangst / Levering (MVO) een ontvangst van een negatief bedrag op de machine.De Inkoop status moet nog wel voorraad zijn! De inkoopfactuur van de bonus boeken op de tussenrekening. Welke machine grootboek boekingen of mutaties worden er geboekt? Verkoopfactuur | Grootboek | Omschrijving | debet | credit | | --- | --- | --- | --- | | | Debiteuren | 1121 | | | | Aan BTW | | 121 | | | Aan Vooruit geboekte omzet machines | | 1000 | Verkoopfactuur met inruil Zelfde grootboekrekening, maar met de inruil machine boeking (laatste 2 regels) | Grootboek | Omschrijving | debet | credit | | --- | --- | --- | --- | | | Debiteuren | 1121 | | | | Aan BTW | | 121 | | | Aan Vooruit geboekte omzet machines | | 1000 | | | Voorraad machines (marge) | 500 | | | | Aan Kostprijs machines | | 500 | Levering Machine gaat van de voorraad af. Winst/verlies wordt geboekt. | Grootboek | Omschrijving | debet | credit | | --- | --- | --- | --- | | | Vooruit geboekt omzet machines | 1000 | | | | Aan omzet machines | | 1000 | | | Kostprijs machines | 750 | | | | Aan voorraad machines | | 750 | Ontvangst van de machine Machine komt op voorraad. | Grootboek | Omschrijving | debet | credit | | --- | --- | --- | --- | | | Voorraad machines | 1000 | | | | Aan tussenrekening machines | | 1000 | Machine status(sen) Klik hier voor meer informatie over de machine gebruikstatus: Bij de machine kan op tabblad Service de gebruikstatus ingevuld worden. | Gebruikstatus | De gebruik status van de machine:- In gebruik (standaard), alleen met deze status wordt deze op het Machine portaal of de Verhuur app getoond.- Demo (icm machine garantieportaal).- Gestolen- Buiten gebruik- Afgeschreven / defect | | --- | --- | Deze gebruikstatus wordt o.a. gebruikt bij: - Vinkje Incl. buiten gebruik bij:Zoek machines is dit standaard aangevinkt: - Bij Selecteren machines is dit uitgevinkt Bij een Keuring wordt alleen voor machines die ingebruik zijn een keuringsherinnering voorgesteld of aangemaakt. Bij Opvragen machines is de gebruikstatus zichtbaar. Op de CRM app is de gebruik status niet zichtbaar, alleen bij wijzigen of toevoegen. Op de Verhuur App worden alleen machines ingebruik getoond. De gebruiksstatus wordt gebruikt om machines goed te beheren, zichtbaar te houden en correct te laten functioneren. Wat moet de status van de machine bij inruil zijn? Bij Onderhoud machines, tabblad Financieel, moet het volgende staan: 1. De 'Inkoopstatus' moet nvt of consignatie zijn. 2. De 'Verkoopstatus' moet Verkocht / Eigendom zijn. - Zie: Machine verkoop met inruil Wat moet de status zijn van de machine bij verkoop? Bij Onderhoud machines, tabblad Financieel, moet het volgende staan: 1. De 'Inkoopstatus' moet Voorraad of besteld of inruil verwacht zijn. 2. De 'Verkoopstatus' moet nvt zijn. Belangrijk: Bij een gesloten machine-administratie mag bij Onderhoud machines (MBB) de verkoopstatus niet aangepast worden, als de machine verkocht is maar nog niet geleverd is. - Zie Machine verkoop Opmerking: Als een machine verkocht en geleverd is dan pas mag de inkoopstatus aan te passen zijn naar nvt, besteld of consignatie. #### Overige Hoe wordt de brutomarge berekend bij machine administratie 2.0? De bruto marge wordt als volgt berekend: | Inkoop | Verkoop | Brutomarge | | --- | --- | --- | | Inkoopprijs + | Verkoopprijs + | | | Accessoires + | Accessoires + | | | Werkorders + | Werkorders + | | | Overige + | Overige + | | | BPM = | BPM = | | | Totale kostprijs (A) | Totale verkoopprijs (B) | B -A = brutomarge | Wat doet vinkje transactie automatisch verwerken* bij een *Machine transactie* tijdens verwerken factuur?

#### Transactie automatisch verwerken tijdens verwerken factuur

Bij een verkoop of inruil van een voorraadhoudend machine-artikel kan aangegeven worden dat een levering of ontvangst bij het Doorverwerken facturen van de factuur automatisch geboekt en verwerkt wordt.

- De volgende transactie Levering wordt, als deze optie is aangevinkt, geboekt:
- Voor de betreffende machine hoeft dan niet meer handmatig een levering of ontvangst te worden geboekt via Machine ontvangst/levering.

*Wat houdt de margeregeling in? Bij de margeregeling wordt de BTW niet over de omzet berekend, maar over het verschil tussen verkoopprijs en inkoopprijs, de winstmarge. - Verkoopt u met winst, dan is de winstmarge positief en moet hierover BTW betaald worden. - Verkoopt u met verlies, dan is er een negatieve winstmarge. Hierover behoeft geen BTW betaald te worden, er is ook geen BTW teruggave. - Gaat per machine. - Voor meer informatie zie belastingdienst.nl/.../margeregeling. Voor uitgebreide informatie en een voorbeelden zie: - Machine marge regeling Wat houdt de globalisering regeling in voor machines? Je kijkt wat je inkoop van zgn. marge/globaliserings machines is over een maand gezien. Je kijkt wat in diezelfde maand je verkoop is. En over het verschil draag je de BTW af. - Dit gaat dus per periode o.b.v. inkoop/ verkoop. - Deze wordt niet verwerkt in de btw-aangifte uit Powerall Connect, en dien je handmatig uit te zoeken/op te tellen. Wat houdt eigendomsvoorbehoud* regeling bij verkoop in?

Standaard

Het komt vaak voor dat een koop-/verkoopovereenkomst wordt gesloten voor bepaalde goederen, terwijl de koper de koopprijs nog betaald moet worden. Er wordt dan ‘op krediet’ geleverd met bijvoorbeeld een betalingstermijn van 30 dagen. In dat soort gevallen is het verstandig om gebruik te maken van een eigendomsvoorbehoud.

Eigendomsvoorbehoud

De goederen die worden verkocht, worden dan onder de opschortende voorwaarde geleverd, totdat de koper de koopsom betaalt. Wordt de betaling (tijdig) gedaan, dan wordt de koper de nieuwe eigenaar.

Wanneer de koper van het niet conform de afspraken het overeengekomen bedrag betaald, kan de verkoper het eigendomsvoorbehoud worden ingeroepen. De verkoper eist de verkochte goederen dan op als eigenaar van deze goederen en werkt de koper onverhoopt niet mee aan de gevorderde teruggave, dan heeft de verkoper – of beter gezegd de rechtmatige eigenaar – de mogelijkheid om dit via de rechter af te dwingen. Mocht de koper onverhoopt failliet worden verklaard, dan kan de verkoper zich direct tot de curator wenden met het verzoek de betreffende goederen terug te geven.

Voor meer informatie zie https://nl.wikipedia.org/wiki/Eigendomsvoorbehoud.

Opmerking: Zonder eigendomsvoorbehoud verliest u bij wanbetaling zowel uw geld als uw producten.

#### Website e.d.

Hoe worden de website foto's van de machines genoemd in Powerall Connect?

De website foto's in Powerall Connect worden als volgt ge- of hernoemd:

- -

Hoe voeg ik een website toe, om op te adverteren?

Het is mogelijk om een website toe te voegen waarop de machine geadverteerd kan worden.

- Neem hiervoor contact op met de helpdesk of consultant.

Het aantal websites waaraan de machines gekoppeld kunnen worden is uitgebreid naar maximaal 20 websites.

Op hoeveel websites kan ik mijn machine publiceren of te koop zetten?

Het is mogelijk om op maximaal 20 websites de machine te adverteren / zetten.

- Neem contact op met de planner om dit eenmalig in te stellen.

Wat kan ik allemaal met machine websites / online adverteren?

Het is ook mogelijk om de machineadministratie te koppelen aan een webshop/website, zodat de informatie op de website altijd accuraat en up-to-date is.

- Op tabblad Website / Commercieel kunnen website aangevinkt, informatie en foto's toegevoegd worden.
- Zie ook: Advertentiekoppeling (machines)
- Machine (website) export

Neem contact op met de planner / verkoper om dit in te stellen.

Welke machinegegevens kan ik opgeven, voor de website export?

Bij Onderhoud machines, tabblad Websites, kunnen de volgende gegevens opgegeven worden:

- Website(s)
- Categorie
- hoofd- en subgroepen
- Overige informatie
- Uitvoering
- Foto's

Voor meer informatie zie ook Machine (website) export.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Machines Advertentiekoppeling (machines)
- Onderhoud machines
- Zoek machines

Wat doe ik als de financiële voorraad niet aansluit met de  machines?

---
## Hoe kan ik kosten achteraf op een machine boeken zonder werkorder?

Nadat een machine afgeleverd is, komt het voor dat er toch nog facturen binnenkomen die betrekking hebben op een machine. Denk aan externe transportkosten of een uitkering van extra inkoop korting.

Om deze kosten te boeken, doorloopt u de volgende stappen:

1. Ga naar Boeken inkooporder machines (KI).
2. Vul de gegevens in.
3. Vink machinefactuur aan.
4. In de regels: Geef de machine in.
5. Bij kostensoort selecteer Kosten achteraf.
6. Geef eventueel de grootboekrekening in. Deze grootboekrekening moet kostendrager machine hebben.
7. Geef overige gegevens in.

Bij Opvragen machines, tabblad Financieel is gelijk te zien dat het kosten achteraf bedrag bijgewerkt is.

Kies voor de knop  Einde boekstuk.

De inkoopfactuur is geboekt.

#### FAQ

Hoe komt het dat ik geen grootboeknummer kan opgeven.

Nadat de machine en kostensoort achteraf opgegeven zijn, controleert Powerall Connect of bij de opgegeven grootboekrekening de kostendrager wel machine is.

Wat wordt er geboekt?

#### Grootboek

Bij Opvragen grootboekmutaties (GO) is de volgende journalisering te zien bij Info Boekstuk:

#### Machine transactie

De volgende machinetransactie wordt geboekt, deze is o.a. zichtbaar bij Opvragen machines (MO), tabblad Transacties.

#### Crediteuren

Bij Opvragen crediteurposten (KO) de openstaande post bij de crediteur.

Welke kostensoort kan ik selecteren?

De volgende kosten soort kan er geselecteerd worden, bij een machinefactuur, afhankelijk van de instelling:

- | Kostensoort | Optie voor kostensoort bij Boeken inkoopfacturen optioneel bij een machinefactuur:--VERKOOP--- Machine- BPM- Kosten achteraf (alleen geboekt op Kosten achter af bij Subadministratie machines is ja).- Overige kosten bij subadm. machine is ja ook geboekt op balans en inkoopwaarde, vanaf versie 3.28-- EXPLOITATIE-- vanaf versie 3.28:- Verzekering - Keuring- Afschrijving- OpbrengstInstelling: soort bedrijf is motorbranche:.- Korting, als machine nog op voorraad is, wordt de rekening voorraad marge ingevuld, en de balanswaarde verhoogd.- Overige kosten, geboekt op machine bij Overige kosten.NB Bij Machine / BPM verschijnt bij een machine met inkoopstatus Besteld/ Voorraad, de gekoppelde grootboekrekening, via de artikelgroep.Bij Machine adm. 2.0 is nee, zijn deze kosten zichtbaar bij F8 Tabblad Transacties | | --- | --- |

---
## FAQ Machinisten App

Belangrijk: De Machinisten app kan niet samen in één administratie draaien met de Werkbon App.

#### FAQ

Kan ik de werkorder regels wijzigen, die in de machinist App zijn aangemaakt?

- In de regel kan de omschrijving, aantal en prijs, niet gewijzigd worden.
- Wil je deze aanpassen, dan moet je een regel eronder toevoegen en daar de correctie in aanbrengen.

Hoe zit het als de monteur het werk gereed meld op de Werkbon App en iemand anders meldt dat het werk niet gereed is?

Als een monteur een Werk gereed stuurt dan wordt er gecontroleerd of er nog planrecords 'niet gereed' zijn. Zie Beheer servicemelding, tabblad Planning , kolom Status.

- Werkorder planstatus wordt pas op 'Werk gereed' gezet als alle planrecords diezelfde status hebben.

---
## Hoe zie ik dat er een nieuwe versie van Powerall Connect is?

In de menu balk van Powerall Connect verschijnt een melding:

- Nieuwe versie Powerall beschikbaar. Opmerking: Deze melding verschijnt alleen bij de gebruikers waarbij Update notificaties ontvangen op Ja staat.
- Of controleer bij het Powerall Connect informatie scherm, de nieuwste beschikbare versie. Ga naar een administratie.
- Klik in de bovenste balk op het i-tje .

#### Bijwerken/update

Zie voor vervolg van de update procedure Hoe installeer ik een Powerall update?

#### Verouderde versie op werkstation

Het kan ook voorkomen dat de Powerall Connect versie op de server al geüpdatet is, maar nog niet op het werkstation / thin client.

1. Bij het opstarten van Powerall Connect verschijnt dan de volgende melding:
2. Kies voor de knop OK om Powerall Connect bij te werken. Het scherm Nieuwe versie ophalen... verschijnt.
3. Bevestig de Windows gebruikersaccount melding.
4. Het scherm Installatie Powerall Werkstation. Bezig met installeren verschijnt.

Nadat de installatie beëindigd is, wordt het login scherm getoond en kan Powerall Connect weer gebruikt worden.

---
## FAQ Powerall Connect installatie, updates e.d.

In dit hoofdstuk staan de meestgestelde vragen over de Powerall Connect installatie en updates.

- Hoe, wat m.b.t. Powerall werkstation? Hoe installeer ik Powerall Werkstation / Planbord / Outlook Inbox?
- Hoe repareer of wijzig ik de Powerall werkstation installatie?

Hoe herstart ik de Service Host?

Hoe zie ik dat er een nieuwe versie van Powerall Connect is?

Hoe installeer ik een Powerall update?

Wat is er gewijzigd in de nieuwe versie van  Powerall Connect?

Hoe stel ik de Powerall Connect Outlook Inbox in?

Hoe maak ik het streepje t.b.v. sneltoetsen zichtbaar?

Wat zijn de virusscanner uitsluitingen of exceptions?

Welke instellingen zijn van belang bij het installeren van Powerall Connect?

Opmaak e-mail berichten/facturen  in .html formaat bij SMTP

#### Powerall Connect statusbalk

*Klik hier voor meer informatie over de statusbalk: De statusbalk wordt onderin, bij een programma standaard, weergegeven: 1. Programma naam 2. Versie 3. Gebruiker 4. Printer (standaard) 5. Datum, actuele 6. Aantal regels (is nog niet overal zichtbaar) 7. Aanvullende helptekst, afhankelijk van cursor/veld. Opmerking: 1, 6 en 7 zijn variabel #### Powerall Connect setup meldingen Wat doe ik bij de update melding: 'Updates voor versie 3.xx zijn geblokkeerd'?. Het is mogelijk dat bepaalde updates geblokkeerd zijn. - Wacht totdat de betreffende update online gezet wordt. - Laat iedereen uit loggen en herstart de server of pc opnieuw. Wat doe ik bij de installatie melding: 'Er is geen actie ondernomen omdat het systeem opnieuw moet worden opgestart?'. - Een herstart van het systeem is nodig. - Laat iedereen uit loggen en herstart de server of pc opnieuw. Wat doe ik bij de update-melding: 'De volgende processen (Firefox (PID: *) zijn nog actief en moeten worden afgesloten...'.

- Sluit de browser Firefox.
- Kies voor de knop Opnieuw.

Tijdens de installatie worden bepaalde barcode fonts bijgewerkt. Deze worden door Firefox gebruikt.

Wat doe ik bij de update-melding: 'De setup wordt uitgevoerd over een bestaande Powerall Connect-installatie. Hierin zijn beschadigde administraties aanwezig...'.

Controleer of de volgende administraties toegankelijk zijn:-

- Oorzaak: Uit de administratiemap waren de bestanden verwijderd.
- Oplossing: Verwijder deze administratie bij Onderhoud administraties.

Wat doe ik bij de update-melding: 'Deze installatie vereist minimaal Windows Server 2008 R2 of Windows 7 met Service Pack 1'?

Onderstaande melding verschijnt bij het updaten, het besturingssysteem / Windows is verouderd.

- Oorzaak: Verouderde hardware / software, bepaalde functionaliteit wordt in deze versie niet ondersteund.
- Oplossing:Neem hiervoor contact op met de helpdesk, de hardware moet vervangen worden.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## Wat doe ik bij de melding: 'Het maximaal aantal gebruikers is ingelogd'?

Als deze waarschuwing verschijnt, is het maximaal aantal gebruikers bereikt of ingelogd dat verbonden is aan de licentie van Powerall Connect. Dit kan bijvoorbeeld voortkomen als een actieve Powerall Connect sessie beëindigd of niet goed afgesloten wordt.

Om het de ingelogde gebruikers te controleren, doorloopt u de volgende stappen:

1. Ga in het systeemmenu naar Systeembeheer > Actieve taken.
2. Ga naar tabblad Verbindingen.
3. Wacht even totdat de actieve verbindingen verschijnen.
4. Een overzicht van actieve verbindingen met de betreffende gebruikers verschijnt. Selecteer de gebruiker die niet werkelijk actief is.
5. Kies voor de knop Verwijder.
6. Bij de pop-up Weet u zeker dat u de volgende verbinding wilt?. Kies voor de knop Ja.

Ga naar tabblad Taken.

1. Selecteer de gebruiker die niet werkelijk actief is.
2. Kies voor de knop Verwijder.
3. Bij de pop-up Weet u zeker dat u deze taak wilt verwijderen. Kies voor de knop Ja.

De ingelogde gebruiker is verwijderd en kan weer inloggen.

Opmerking: Bij tabblad Taken kunnen de gebruikers die niet bij Verbindingen voorkomen, verwijderd worden. Een actieve verbinding ontbreekt hierbij.

Let op! dat er geen actieve gebruikers uitgelogd worden.

---
## Wat doe ik bij de melding: 'Inboxpad is niet ingesteld...'?

#### Oorzaak

Bij het gebruik van de Powerall inbox plugin, via de optie Naar Factuurbox kan onderstaande melding voorkomen.

Als het Inboxpad niet ingesteld is, verschijnt deze melding:

#### Oplossing

Het inbox-pad verwijst naar de map of folder waar de inkomende e-facturen worden opgeslagen, om verwerkt te worden.

- Voor meer informatie zie Hoe stel ik de Powerall Connect Outlook Inbox in?

---
## Wat is er gewijzigd in de nieuwe versie van  Powerall Connect?

# Wat is er gewijzigd in de nieuwe versie van Powerall Connect?

Powerall Connect wordt continu aangepast aan de wensen van onze klanten en geoptimaliseerd waar nodig is.

- In elke nieuwe versie van Powerall Connect worden nieuwe - of gewijzigd functies doorgevoerd. Dit is beschreven in de Release notes.

Om de release notes te bekijken, doorloopt u de volgende stappen:

1. Start Powerall en login.
2. Kies een administratie.
3. Ga naar het Powerall Connect informatie symbool (i-tje) in de bovenste menubalk. Het scherm Powerall Connect informatie verschijnt.
4. Klik op de rechtsonder op de link Klik hier om de release notes te bekijken of ../release-notes. Per release zijn de nieuwe en gewijzigde functies te zien.

#### Zoeken in Release notes - nieuw -

Vanaf versie 3.29 kan staan de Release notes in deze documentatie

- Via de zoek knop kan er in de release notes gezocht worden.
- Selecteer vervolgens het onderwerp
- De gearceerde zoekterm(en) worden vervolgens weergegeven. Blader even door het onderwerp heen.

#### Zoeken in Release notes - oud -

Een handige functie is het zoeken op een bepaald woord of woorden in de release notes.

- Dit kan per module of in alle versies.
- Praktische informatie over een bepaald .

Opmerking: Release notes is een term die gebruikt wordt om aan te geven welke wijzigingen er zijn in een bepaalde versie (release) van de Powerall Connect software.

- Welkom bij de Online Help van Powerall Connect
- Powerall Connect help
- Veelgestelde vragen FAQ

---
## Wat doe ik bij de melding: 'There was a problem with one of the .NET support libraries'?

#### Vraag / opmerking

Hoe los ik dit probleem op? Neem hiervoor contact op met de helpdesk.

#### Foutmelding

De volgende foutmelding wordt weergegeven:

- There was a problem with one of the .NET support libraries..NET assemblies cannot be loaded.COBOL error at 010BFA in IIN71.ACU

#### Oorzaak

Problemen met Windows of Windows Updates.

#### Oplossing

Computer herstart en .NET installatie hersteld en Powerall installatie hersteld.

---
## Wat betekent de ... status?

Wat betekent de bonstatus?

De volgende bon statussen worden gebruikt:

1. = Openstaande bon, kan gewijzigd worden.
2. = Gefactureerde bon, met factuurnummer, maar nog NIET financieel doorverwerkt.
3. = Bon of factuur die van filiaal naar hoofdkantoor gesynchroniseerd is.
4. -
5. = Gefactureerde bon EN financieel doorverwerkt.De bon/factuur is doorverwerkt, d.w.z. de open posten en grootboekmutaties (kostenplaatsmutatie) zijn aangemaakt en de statistieken zijn bijgewerkt.

Wat betekent de offerte status?

De volgende offerte statussen worden gebruikt :

1. = OfferteOfferte verlopen = de offertedatum is voorbij.
2. = Opdr. (opdracht) bevestiging
3. = Inkoop
4. = Vrijgegeven
5. = Vervallen

Wat betekent de werkorder / werkbon status?

De volgende werkorder / bon statussen worden gebruikt:

1. = Openstaande werkorder, kan gewijzigd worden.
2. = Vrijgegeven, interne werkorder, maar nog NIET financieel doorverwerkt.
3. = Vrijgegeven externe werkorder
4. -
5. = Vrijgegeven en doorverwerkte interne werkorder EN financieel doorverwerkt en artikelstatistieken zijn bijgewerkt.

Op de Powerall CRM app worden bij de Machine transacties de Werkorder 'status' weergegeven, vanaf versie 3.28

Een werkorder heeft de volgende status:

- Open - bij geen artikelen en uren nieuw.
- In Uitvoering - bij artikelen of uren incl. bedragen nieuw.
- Gereed - de werkorder is vrijgegeven.

Hierdoor zijn de open - en lopende werkorders met de prijzen beter inzichtelijk.

Wat betekent de verkoopstatus?

De volgende verkoop statussen worden gebruikt:

1. = Openstaande verkooporderof Nieuw (bij weborders)

1. = Vrijgegeven verkooporder

Wat betekent de verhuurstatus?

De volgende verhuur 1.0 statussen worden gebruikt:

1. = Aanvraag
2. = Reservering
3. = Gekoppeld
4. = Lopend
5. = Afgemeld
6. = Retour
7. = Vrijgave / Factuur

De volgende Verhuur 2.0 statussen worden gebruikt:

1. = Offerte
2. = Open
3. = Lopend

1. = Afgemeld
2. = Retour
3. = Historisch
4. = Vervallen

Dit zijn de verhuurorderstatus(sen).

Wat betekent de contractstatus?

De volgende contract statussen worden gebruikt bij:

1. = Lopend

1. = Vervallen

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## FAQ Planbord werkorders

De meest gestelde vragen staan bij het planbord werkorders, zie:

- FAQ Planbord

---
## Wat doe ik bij de melding: 'Aanroep geweigerd door aangeroepene'?

#### Melding

Het volgende bericht kan verschijnen, bij het importeren van een Excel bestand.

- Bijv. bij inlezen van catalogus vanuit Excel.

Belangrijk: Bij de melding Class not registered, is Excel niet geïnstalleerd.

#### Oorzaak

Dit komt voor op een nieuwe pc, met een standaard Office Klik-en-Klaar licentie. Excel en Word functies zijn dan niet vanuit Powerall Connect te gebruiken (ActiveX, COM).

- De functionaliteit is hierbij beperkt.

Of Microsoft office is nog niet geregisteerd / aangemeld.

#### Oplossing

Activeer de juiste (Office) licentie van Excel, waardoor de import functionaliteit beschikbaar komt.

Opmerking: Anders neem contact op met de helpdesk.

#### Klik-en-Klaar office licentie

Melding; Office op dezelfde computer geïnstalleerd met Klik-en-Klaar en met Windows Installer wordt niet ondersteund.

- Klik hier voor meer info Klik-en-Klaar.

---
## Wat doe ik bij de melding: 'General socket error' of 'Communication socket closed unexpectedly'?

#### Vraag / opmerking

Hoe los ik het connectie probleem op?

#### Foutmelding

De volgende foutmelding wordt weergegeven:

1. General socket error.
2. Communication socket closed unexpectedly.

#### Oorzaak

De verbinding tussen de pc/client en de server is onderbroken.

#### Oplossing

1. Start Powerall Connect opnieuw.
2. Als dat niet helpt herstart, de betreffende pc of client.
3. Bij het gebruik van een server controleer of Powerall Connect op de server werkt.

---
## Wat doe ik bij de melding: 'Administratie 1 kan niet geopend worden. Mogelijk wordt er een update uitgevoerd'?

#### Oorzaak

Als deze waarschuwing verschijnt bij het openen van een administratie, is er een update actief van Powerall Connect. Het scherm aan de rechterkant verschijnt.

Links zie je dat de update gestart is en wacht op OK.

#### Oplossing

Wacht totdat de update voltooid is.

Opmerking: Als deze melding na enige tijd (afhankelijk van de database grootte) niet weggaat neem dan contact op met de helpdesk.

---
## FAQ Powerall Connect foutmeldingen

In dit hoofdstuk staan de meest gestelde vragen m.b.t. Powerall Connect foutmeldingen.

- Wat doe ik bij de melding: 'Aanroep geweigerd door aangeroepene'?
- Wat doe ik bij de melding: 'Administratie 1 kan niet geopend worden. Mogelijk wordt er een update uitgevoerd'?
- Wat doe ik bij de melding: 'General socket error' of 'Communication socket closed unexpectedly'?
- Wat doe ik bij de melding: 'Inboxpad is niet ingesteld...'?
- Wat doe ik bij de melding: 'Nieuwere of verouderde administratie of versie'?
- Wat doe ik bij de melding: 'Het maximaal aantal gebruikers is ingelogd'?
- Wat doe ik bij de melding: 'mqrt.dll: Programm missing or inaccessible'?
- Wat doe ik bij de melding: 'There was a problem with one of the .NET support libraries'?
- Wat doe ik bij de melding: 'Het maximaal aantal gebruikers is ingelogd'?
- Wat doe ik bij de melding: 'Verzenden naar Powerall Connect factuurinbox mislukt?'

Meldingen

Afdrukken

*Wat doe ik bij de melding: 'Wacht op vrijgave sorteerbestand'? Deze melding kan verschijnen bij het afdrukken van een overzicht (tegelijkertijd) op twee taken of sessies. - Het sorteer bestand wordt gebruikt om bij het weergeven van een uitgebreide lijst bij de Selecteren programma's of bij het printen om een sortering op bepaalde kolommen te maken. Oplossing - Wacht tot de eerst gestarte taak, die het sorteerbestand in gebruik heeft, gereed is.of - Druk op Stoppen. Wat doe ik bij de melding: 'Fout bij afdrukken...'? Bij een overzicht of afdruk kan de fout 'Fout bij afdrukken, layout X van niet gevonden'. verschijnen. Controleer of de juiste layout ingevuld is bij de betreffende Instellingen. Indien nodig maak eventueel een layout aan. Wat doe ik bij de melding: 'Bestandsfout PRDATA? Bij een overzicht of afdruk kan de fout 'Bestandsfout PRDATA, foutdetails 39,01 ... \\PRDATA.dat'. verschijnen. Neem hiervoor contact op met de helpdesk om dit op te lossen. Wat doe ik bij de melding: 'Waarde komt niet voor in referentietabel'? Bij een wijziging of bij het opslaan kan deze fout ' Waarde komt niet voor in referentietabel'. verschijnen. Controleer op alle tabbladen of de gegevens juist zijn. FAQ Wat doe ik bij de melding: 'Er is al een gebruiker met dezelfde gegevens ingelogd'? Bij het inloggen kan onderstaande melding voorkomen. Dit kan eveneens bij het starten van een administratie. De melding Gebruiker is al ingelogd verschijnt. #### Oorzaak / oplossing Dit kan een van de volgende oorzaken zijn. 1. Deze gebruiker is al ingelogd. Vraag aan de gebruiker om uit te loggen. De Powerall Connect sessie / taak is abnormaal beëindigd van deze gebruiker. 1. Beëindigd in Systeembeheer de taken die niet meer actief zijn. Voor meer info zie Hoe verwijder / disconnect ik een gebruiker(sessie)? Wat doe ik bij de melding: 'Code geblokkeerd op ander scherm'? Bij een selectie programma kan onderstaande melding voorkomen. In deze situatie wordt de betreffende instellingen gewijzigd, hierdoor kan er geen nieuw order aangemaakt worden. 1. Ga naar de betreffende partitie (bijv. druk op de toetsen ). 2. Sluit het betreffend instellingsprogramma af en probeer op nieuw. #### Licentie Wat doe ik bij de melding: 'De huidige softwarelicentie is ontoereikend voor dit programma'? De licentie geldt niet voor de betreffende module of dit programma. - Controleer de licentie van de betreffende administratie, deze kan namelijk gewijzigd zijn. - Geef het programma en module door en neem contact op met de helpdesk. Wat doe ik bij de melding: 'Ongeldige licentie' Het betreffend programma komt niet overeen met de licentie. - Neem hiervoor contact op met de helpdesk. Wat doe ik bij de melding: 'Uw demo licentie verloopt na X dagen?' De licentiedatum is bijna verlopen. - Neem hiervoor contact op met de helpdesk. Wat doe ik bij de melding: 'Het maximaal aantal gebruikers is ingelogd. U kunt niet meer inloggen'? Er zijn meer gebruikers ingelogd, dan is toegestaan volgens de licentie. - Vraag gebruikers om op niet actieve taken uit te loggen. NB Als dit regelmatig voorkomt kan het aantal gebruikers uitgebreid worden. - Belangrijk: Consequentie is wel dat een gebruiker die op twee partities inlogt in twee verschillende bedrijven ook twee gebruikers bezet houdt (1 voor ieder bedrijf). Wat doe ik bij de melding: 'Uw licentie is verlopen?' Bij de melding Uw licentie is verlopen is de licentiedatum verlopen. - Neem hiervoor contact op met de helpdesk. Wat doe ik bij de melding: 'Uw Licentie is verlopen' of 'Uw licentie is ongeldig'? De huidige licentie is verlopen of ongeldig. 1. Bij ongeldig, controleer de licentie key bij de administratie. 2. Vernieuw de licentie en/of neem contact op met de helpdesk.Bovenstaande melding kan in het nieuwe jaar verschijnen. Wat doe ik bij de melding: 'Het bijwerken van meerdere administraties met verschillende versies.... enz.'? Waarschijnlijk is het bijwerken/update van de administratie niet goed gegaan. - Neem hiervoor contact op met de helpdesk om dit op te lossen. Login Wat doe ik bij de melding: 'Deze versie van Powerall is verouderd'? Als er gebruik wordt gemaakt van een oude Powerall Connect versie, verschijnt na 10 maanden de melding: - Deze versie van Powerall Connect is verouderd! - Kies voor de knop Ja. Wat doe ik bij de melding: 'Leesfout systeempad in GPCCNT Foutcode: 23'? 1. Sluit alle Powerall Connect sessies. 2. Log opnieuw in. Het probleem is verholpen, anders raadpleeg de helpdesk. Wat doe ik bij de melding: 'Geen systeempad ingesteld*'?

Neem contact op met de helpdesk, om dit te verhelpen.

Overige

Wat doe ik bij de melding 'Code niet gevonden' bij Wijzigen?

Controleer of het programma niet openstaat / bezet is op een andere partitie.

- Deze melding verschijnt bij Wijzigen of Verwijderen van een item.

Wat doe ik bij de melding: 'Het administratie-pad is niet bereikbaar vanaf uw werkstation'?

Deze melding verschijnt als het administratie data-pad niet (goed) bereikbaar is vanaf een werkstation.

- Controleer of de verbinding met de aangegeven gedeelde map en probeer het opnieuw, of vraag de systeembeheerder wat er aan de hand kan zijn.

Wat doe ik bij de melding: 'Method Not Found'?

Deze fout kan voorkomen bijE-Inkoopfacturen inboeken bij het tonen van de PDF van de inkoopfactuur.

- Neem contact op met de helpdesk om dit op te lossen.

Wat doe ik bij de melding: 'FOUT MET EXCEL OPENEN'?

Er wordt bij deze toepassing gebruik gemaakt van de Excel functionaliteit.

1. Controleer of het programma Microsoft EXCEL geïnstalleerd is.

Als Excel al geïnstalleerd is, raadpleeg de helpdesk.

Wat doe ik bij de melding: 'Administratie <01> kan niet geopend worden. Mogelijk wordt er een update uitgevoerd'?

Onderstaande melding kan verschijnen:

Wacht totdat de administratie is bijgewerkt.

#### Update

Wat doe ik bij de melding: 'Kan geen exclusieve toegang tot Powerall Connect krijgen'?

Bij het updaten kan aan het einde de volgende melding verschijnen:

Kan geen exclusieve toegang tot Powerall Connect. Zorg dat alle gebruikers zijn uitgelogd voor de setup gestart wordt. (Details: Fout bij verwijderen van GPCCNT.dat)

- Kies voor de knop Opnieuw.

De setup wordt voortgezet en afgerond.

Wat doe ik bij de melding: 'Kan de Powerall Connect Taakplanner-services (PowerAllTaskScheduler) niet starten'?:

Druk op de knop Retry of Opnieuw.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## FAQ Prijsafspraken

In dit hoofdstuk staan de meestgestelde vragen over de in- of verkoop prijsafspraken.

Prijsafspraken

De volgende soorten prijsafspraken zijn mogelijk:

- Ordertype of ordersoort, zie Onderhoud ordertypes.
- Ordertype, kortingsgroep en kortingspercentage, zie Onderhoud relaties (BRR), tabblad Debiteuren of Crediteuren.
- Prijsniveau 1-2, zie Onderhoud artikelen (ABA), tabblad Algemeen.Verkoopprijs (niveau) 1 is de verkoopprijs.
- Verkoopprijs (niveau) 2 is de verkoopprijs en de adviesprijs (consumentenprijs) (instelling).

Per klant(groep) / per artikelgroep
Artikelcode (actieprijs)

Belangrijk: Als er een actieprijs ingevuld is, bij een artikel wordt er geen korting berekend, maar wordt deze prijs toegepast.

Per klant(groep) per artikel
Handmatig (in de regels)

Hierbij een overzicht:

FAQ

*In welke volgorde worden deze prijsafspraken toegepast? Bovengenoemde volgorde wordt gebruikt voor de prijsafspraken, bijv.: - De korting per klant / per artikel gaat boven/voor de korting per klant / artikelgroep. Opmerking: Neem contact op met de planner om de diverse kortingen in te stellen. Bij welke modules kan ik allemaal een prijsafspraak maken en instellen? In Powerall Connect is dit mogelijk bij de volgende modules: - Facturering - Verkooporders - Inkooporders - Offerte - Werkorder - Verhuur Welk type prijsafspraken zijn er? De volgende type prijsafspraken zijn mogelijk: - Eenvoudig. - Ordertypes, afhankelijk van het (inkoop/verkoop) ordertype. - Bijv. spoedorder geen korting en maandorder standaard korting. Staffels*, per hoeveelheid, hoe meer je afneemt hoe meer korting.
*Ordertypes + Staffels*, zie boven.

Hoe kan het komen dat de prijsafspraak niet wordt toepast?

Controleer bij de betreffende module of de prijsafspraak is ingesteld.

- Controleer of de hiërarchie (volgorde) van prijsafspraken.
- Zie ook de volgende vraag.

Wat moet er ingesteld zijn?

- Bij de instellingen van de betreffende module, tabblad Koppelingen, moeten de betreffende prijsafspraken op ja staan.
- De gewenste prijsafspraak moet ingesteld zijn.

Wat gebeurt er als ik bij een kassabon, naar een relatie (met een prijsafspraak) wissel?

- Er verschijnt dan een pop-up met de vraag: Wilt u de prijsafspraken van deze relatie toepassen op de bestaande orderregels?

Is het mogelijk om prijsafspraken inkoop te importeren?

Ja, dit is mogelijk, met een Excel-bestand, met ingave van leverancier catalogus en kortingspercentage factor . Dit bestand kan / moet de volgende kolommen bevatten:

- Hoofdgroep
- Hoofdgroep omschrijving
- Subgroep
- Subgroep omschrijving
- Kortingspercentage
- Opslagfactor groep
- Kortingspercentage factor

Optie voor de leveranciers artikelgroepen:

- Toevoegen & Bijwerken
- Geen actie
- Bijwerken
- Vervangen

Belangrijk: Bij de melding Class not registered, is Excel niet geïnstalleerd.

Intern KS: Intern, dit is mogelijk met programma PVP82.

- Inkoop prijsafspraken Hoe lees ik nieuwe kortingsafspraken van mijn leverancier in?

Verkoop prijsafspraken

- Hoe kan ik een opslag toepassen bij bepaalde artikelen, bij de kassa?

Onderhoud kortingsgroepen

Onderhoud ordertypes

Prijsafspraken rapportages

- Hoe lees ik nieuwe kortingsafspraken van mijn leverancier in?
- Hoe geef ik op mijn (winter)beurt xx% korting?

---
## FAQ Projecten

In dit hoofdstuk staan de meestgestelde vragen over de Project module.

*Hoe komt het dat ik de referentie 1 en 2* niet kan aanpassen van een project?

De oorzaak is dat het project al actief is.

- Projecten

---
## FAQ Inkoop(orders)

**FAQ Inkoop(orders) In dit hoofdstuk staan de meestgestelde vragen over de inkoop module. - FAQ Goederenmatching - Hoe haal ik mijn nieuwe inkoopfacturen op? - Hoe lees ik nieuwe kortingsafspraken van mijn leverancier in? - Hoe werkt de besteladvieslijst? Inkooporders e.d. Kan ik ook een minimum orderbedrag instellen? Ja, dit is mogelijk voor een inkooporder, d.w.z. een leverancier, een minimum order bedrag in te stellen. Om dit te doen, doorloopt u de volgende stappen: 1. Ga naar Onderhoud relaties (BRR). 2. Kies voor de knop Wijzig. 3. Ga naar tabblad Crediteurinfo. 4. Vul het minimum orderbedrag in. 5. Kies voor de knop Opslaan. De gegevens zijn opgeslagen. Opmerking: Bij een inkooporder verschijnt dan het minimum orderbedrag en het resterend bedrag in de gekleurde kopregel, daarnaast verschijnt er een melding als het orderbedrag niet bereikt is. Hoe koppel ik een inkooporder met een BTB verkooporder of werkorder? Om een inkooporder met een order te koppelen, doorloopt u de volgende stappen: 1. Geef de artikelcode en aantal in de regels in. 2. Vul in de kolom BTB VO of WO in: VO bij een verkooporder. 3. WO bij een werkorder. 4. Enter vervolgens door (tot eind van de regel). Het scherm Koppeling inkooporder met verkooporder verschijnt. 5. Geef de relatie en ordernummer in. 6. Kies voor de knop Opslaan. De inkooporder is gekoppeld met de order, waarop het artikel toegevoegd is. - Normaal wordt een verkoop - of werkorder gekoppeld/besteld met een BTB inkooporder.Zie Koppeling werk-/verkooporder met inkooporder. De uitgebreide / interne tekst van het artikel wordt niet** meegenomen op de verkoop of werkorder.
Het koppelen van een kleine machine artikel is mogelijk, bij de ontvangst worden de SN op de VO bijgewerkt.

Waar kan ik alle de inkooporders zien, dit ik ontvangen heb?

Het is mogelijk om een overzicht aan te vragen met alle inkooporders. Voor meer informatie zie:

- Overzicht voorraadmutaties (ALM) Selecteer bij mutatiesoort de optie inkoop.
- Selecteer eventueel bij sorteren op relatiecode. De inkooporders worden dan op leverancier gesorteerd.

Opvragen inkooporders (IO).

#### Inkoopprijzen

Is het mogelijk om de inkoopprijs te verbergen voor de gebruiker?

Ja het is mogelijk om een autorisatie voor de inkoopprijs in te stellen.

- In plaats van de inkoopprijs worden dan sterretjes *** getoond.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Is het mogelijk om bij een BtB order om de inkoopprijzen bij te werken in de gekoppelde regels?

Ja het is mogelijk om bij een gekoppelde BtB verkooporder of werkorder de inkoopprijzen bij te werken.

- Dit is mogelijk bij goederen ontvangst of bij matching of bij beide.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Inkoopfacturen e.d.

Hoe boek ik een factuur in waar je betaalkorting op krijgt als je binnen x dagen betaalt?

Wanneer er gewerkt wordt met automatisch betalen, moet de factuur ingeboekt worden.

- Bij het boeken van de inkoopfactuur moet de goede betaalconditie ingevuld worden. Wanneer bij het automatisch betalen de batch aangemaakt wordt, binnen de betaaltermijn waarvoor de korting geldt, dan wordt bijvoorbeeld 98% van het factuurbedrag overgemaakt naar de crediteur.
- De andere 2% wordt automatisch weggeboekt naar de grootboekrekening van de betaalkorting.

Hoe blokkeer ik een factuur voor betaling, zodat die niet per ongeluk meegaat in de betaalbatch?

- Daarna komt de mogelijkheid om aan te geven waarom de factuur geblokkeerd moet worden voor betaling.
- Bij Selecteren inkooporders verschijnt bij de status dan de tekst Geblokkeerd.

Hoe gebruik ik de knop Goederenmatching bij 'Boeken inkoopfacturen'.

Ga naar Onderhoud relaties, tabblad Crediteurinfo en controleer of goederenmatching op ja staat.

Hoe wijzig ik de relatie, als de factuur geboekt is op de verkeerde crediteur?

Wanneer een inkoopfactuur op een verkeerde crediteur geboekt is, kan dit gewijzigd worden zolang er geen betaling op zit.

1. Ga naar Inkoopfactuur boeken (KI).
2. Kies voor de knop Wijzig boekstuk. Achter de relatiecode verschijnt dan een pennetje.
3. Kies voor de pennetje-knop . De pop-up melding Wilt u de relatie van deze factuur wijzigen? verschijnt.
4. Kies voor de knop Ja.

Selecteer de nieuwe relatie.

1. De pop-up melding: Relatie succesvol aangepast verschijnt.
2. Kies voor de knop OK.

Opmerking: Wanneer tijdens het boeken geconstateerd wordt dat de verkeerde crediteur gekozen is dan moet de boeking ‘fout’ afgemaakt worden. Daarna kan via het wijzigen van het boekstuk de relatiecode aangepast worden.

Is het mogelijk om een inkoopfactuur boekstuk te verwijderen?

Nee het is niet mogelijk, om een aangemaakt boekstuk te verwijderen. De belastingdienst eist bijv. een opeenvolgend nummer, zie Factuureisen.

- Als er een onterecht boekstuk ingevoerd is, moet deze 'leeggemaakt' worden. Het is ook mogelijk om hiervoor een apart grootboeknummer te gebruiken (bijv. met + en - boeking).

Hoe wordt de BTW-code toegekend bij een inkoopfactuur?

Met behulp van de volgende methode wordt bijv. bij een e-factuur, een BTW code toegekend.

1. De voorkeurs BTW code van de leverancier wordt als uitgangspunt genomen.
2. Een check of land van het BTW nummer van de factuur overeenkomt met de landcode van de administratie. Indien dat niet het geval is, wordt op basis van de ISO landcode uit het BTW nummer bepaald of het een EU of non-EU factuur betreft en dan wordt afhankelijk daarvan de juiste BTW code uit de instellingen crediteuren gepakt.
3. Als de landcode van het BTW nummer van de factuur overeenkomt met de landcode van de administratie en er is BTW berekent op de factuur en bij de relatie staat een EU of non-EU BTW code ingesteld, dan wordt dit omgezet naar de standaard hoog tarief BTW code uit de Instellingen crediteuren.

Op dit moment is helder of het een binnenlandse, een EU of niet EU factuur betreft.

1. Vervolgens wordt voor binnenlandse facturen gecheckt welk percentage het BTW bedrag is. Indien het een factuur met 0% of 9% betreft, wordt deze BTW code geselecteerd in plaats van de standaard hoog (21%) tarief BTW code.
2. Als laatste kan je nog een variant hebben waarbij er meerdere BTW percentages op 1 factuur aanwezig zijn. Om deze direct goed te laten boeken is het noodzakelijk dat de scan/herken software er voor zorgt dat op regelniveau al het juiste BTW percentage is gevuld.
3. Als na het boeken van alle regels blijkt dat er toch een verschil is in de factuur én de automatische herkenning en boeking in Powerall Connect wordt er een popup getoond bij Boeken inkoopfacturen waarin de boeking aangevuld kan worden.

Opmerking: Voor gedeelde administraties tussen België en Nederland wordt eerst bepaald in welke administratie je zit en dan afhankelijk van de landcode van de klant bepaald of het een binnenlandse levering is of een EU.

Zien / zoeken

Hoe controleer ik of een factuur niet dubbel inboekt is?

- Wanneer bij het boeken van de inkoopfactuur bij het veld 'betaalkenmerk' het factuurnummer van de crediteur ingevuld wordt, vindt er een check plaats op het betaalkenmerk. Wanneer dit betaalkenmerk al eerder gebruikt is, komt er een melding waar dit kenmerk eerder gebruikt is. Zo is er te zien of een factuur dubbel ingeboekt wordt.

Hoe zie ik welke inkoopfacturen er geboekt zijn voor een crediteur?

Er kan vanuit het factuurregister crediteuren (KLF) een selectie afgedrukt worden op een crediteur.

- De relatiecode van de crediteur wordt ingevuld bij 'van' en bij 't/m'.
- Bij periodes van kan de periode gewijzigd worden, waarvan de facturen weergegeven moeten worden.

Hoe zie ik of een factuur al betaald is en wanneer?

Bij Opvragen crediteurposten (KO) kunnen per crediteur de openstaande posten bekeken worden. Standaard staan hier de actuele open posten.

- Wanneer de post er niet tussen staat, zal die in de meeste gevallen al betaald zijn. Dan kan er in het scherm geklikt worden op 'historisch' en is de datum selectie aan te passen.
- Selecteer de inkoopfactuur.
- Kies voor de knop Betaalinfo.
- Er opent dan een scherm met de gegevens wanneer en via welke bank de factuur betaald is.

Hoe zie ik de (grootboek) boeking van de factuur?

Bij het opvragen van Opvragen crediteurposten (KO) selecteert u de inkoopfactuur.

- Kies voor de knop Details boeking, om de boeking te bekijken.
- Er opent dan een scherm met de grootboekrekeningen waar op geboekt is en met welke bedragen.

Hoe zie ik welke inkooporder er gematcht is op een factuur?

Bij het opvragen van de Opvragen crediteurposten (KO) selecteert u de inkoopfactuur.

- De matching kan opgevraagd worden door op de knop Details matching te klikken.
- Er opent dan een scherm met de gegevens van de inkooporder en de artikelen die op de inkoopfactuur gematcht zijn.

Hoe zoek ik een factuur zoeken op bedrag?

Er kan via Overzicht mutaties per dagboek (GLD) gezocht worden op (boekingsbedrag) bedrag.

- Kies bij dagboek voor het inkoopboek.

Hoe zoek ik een factuur op het factuurnummer van de crediteur?

Het factuurnummer van de crediteur wordt bij het inboeken van de factuur ingevuld in het veld 'betaalkenmerk'.

- Hierop kan gezocht worden in het programma ‘Selecteren Inkoopfacturen’. Dit zijn alleen de nog niet betaalde inkoopfacturen.
- Wanneer er gezocht moet worden in alle inkoopfacturen kan dit gedaan worden via het factuurregister crediteuren (KLF). Het factuurnummer van de crediteur kan dan ingegeven worden bij het veld 'betaalkenmerk'.

Waarom zijn sommige bestelregels vet gedrukt?

Bij het programma Goedkeuren besteladvieslijst (IBA) is bij de vet gedrukte regels een goedkopere leverancier aanwezig in het artikelbestand.

- Deze kan bij kolom Leverancier geselecteerd worden. Zie ook Besteladvieslijst (goedkeuren).
- Deze leveranciers zijn terug te vinden via F7 of Onderhoud artikelen, tabblad Leverancier.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Inkoop
- FAQ Prijsafspraken
- Van welke leveranciers is een EDI koppeling beschikbaar?

---
## Hoe installeer ik een Powerall update?

Elke klant, die beschikt over een Powerall Connect Servicecontract, kan ten alle tijde de laatste update van Powerall Connect installeren.

- Het installeren van updates gebeurt op de server of de hoofdcomputer waarop Powerall Connect geïnstalleerd is.

Let op! Alle Powerall Connect gebruikers moeten de administratie en het Planbord verlaten, anders mislukt de update omdat Powerall Connect dan nog in gebruik is.

1. Open de snelkoppeling Powerall Updates op het bureaublad. Het scherm Powerall Updates verschijnt:
2. Belangrijk: Administrator - of beheersrechten zijn vereist om op deze pc/(terminal)server/werkstation Powerall Connect of andere software te installeren of bij te werken.
3. Kies voor de knop Start installatie. Het scherm Welkom bij Powerall Connect  verschijnt.
4. Klik hier voor meer informatie over de eenmalige melding vanaf 3.16 of hoger Vanaf versie 3.16 of hoger verschijnt éénmalig het volgend scherm: Let op: minimale Windows versie gewijzigd! Powerall vereist vanaf deze versie Windows 10 of hoger voor werkstations.
5. Kies voor de knop Volgende. Het scherm Onderdelen verschijnt.
6. Kies voor de knop Volgende. Let op! Het selectief uitschakelen van update onderdelen kan leiden tot een instabiel of niet werkend systeem. Gebruik deze functie alleen in overleg met onze medewerkers.
7. Het scherm Instellingen voor Powerall Connect (met het installatiepad) verschijnt.
8. Kies voor de knop Volgende. Het scherm Backup en upgrade verschijnt.
9. Kies voor de knop Volgende. Opmerking: De gedeelde administraties worden ook bijgewerkt naar een nieuwere versie.
10. Optioneel alleen bij PWS: Het scherm Instellingen voor de PWS verschijnt.
11. Kies voor de knop Volgende.
12. Optioneel Eerste keer of als Niet akkoord is aangevinkt: Het scherm Verzameling van Powerall Connect-instellingen verschijnt.
13. Kies voor de knop Volgende.
14. Klik hier voor meer informatie over het verzamelen van de Powerall Connect informatie: Akkoord staat standaard aangevinkt. Deze opties betekenen: Na akkoord: scherm wordt niet meer getoond .
15. Na niet akkoord: wordt dit scherm opnieuw getoond bij de volgende installatie en blijft de optie op niet akkoord staan.

- Het scherm Overzicht verschijnt.

1. Kies voor de knop Volgende. Bevestig de Windows gebruikersaccount melding.
2. Het scherm Installatie proces verschijnt, met informatie over het installatie proces: Bezig met installeren. Vanaf versie 3.31.
3. Het scherm Installatie voltooid verschijnt.
4. Optioneel: om te zien wat er gewijzigd is, in deze versie, klik op de link Klik hier om de Release notes te bekijken. De Powerall Connect release notes worden geopend in de browser.
5. Kies voor de knop Sluiten. Opmerking: Als de melding: een herstart is nodig verschijnt, is het aan te raden dit te doen, om mogelijke problemen in de werking van Powerall Connect te voorkomen.

De updates zijn geïnstalleerd en Powerall Connect kan weer gebruikt worden.

#### FAQ

Opmerking: Bij gebruik van werkstations moeten deze ook bijgewerkt worden, zie gerelateerde onderwerpen.

Wat wordt er bij het installeren van een nieuwe versie of update opgeschoond?

Bij een update wordt, per administratie, het volgende opgeschoond:

- Verouderde back-ups. De laatste 4 administratie back-ups blijven bewaard.
- De bestanden in de WRK-map met extensie .ppr / .txt / .xml / .html en datum gewijzigd ouder dan 14 dagen.
- Kopieën van oude Powerall Connect bestanden, (bijv. GUETXT-V03290.dat/vix) die ouder zijn dan 1 maand .

- Hoe update ik het Powerall Connect Werkstation?

---
## Hoe installeer ik Powerall Werkstation / Planbord / Outlook Inbox?

Powerall Connect werkstation wordt gebruikt op een werkstation of thin client. Het volgende kan geïnstalleerd worden:

- Powerall Connect Werkstation
- Powerall Connect PlanbordWerkorder planbord

Powerall Connect Outlook Inbox (plug-in)

Opmerking: In dit voorbeeld is Powerall Connect geïnstalleerd op een server .

Om Powerall Connect op een Werkstation te installeren, doorloopt u de volgende stappen:

1. Type onder bij zoeken Programma in.
2. Selecteer bovenaan Programma's installeren of verwijderen.
3. Zoek op Powerall Connect.
4. Kies voor de knop Wijzigen.
5. Kies voor de knop Volgende. (Welkom)
6. Kies voor de knop Volgende. (Onderdelen) Opmerking: Vink eventuele andere onderdelen (Planbord en/of Outlook Inbox) aan.
7. Kies voor de knop Volgende. (Overzicht)
8. Bevestig de Windows gebruikersaccount melding. De melding Powerall Connect is succesvol gewijzigdverschijnt.
9. Kies voor de knop Sluiten.

De installatie is voltooid.

#### Powerall Connect Outlook Inbox

Om de Powerall Connect Outlook Inbox in te stellen voor Outlook, zie:

- Hoe stel ik de Powerall Connect Outlook Inbox in?

- Hoe repareer of wijzig ik de Powerall werkstation installatie?
- Dubbelklik op Powerall Connect Werkstation. Het installatie programma wordt gestart.

Werkorder planbord

Welke instellingen zijn van belang bij het installeren van Powerall Connect?

---
## Hoe installeer ik een Powerall Connect update?

Elke klant, die beschikt over een Powerall Connect Servicecontract, kan ten alle tijde de laatste update van Powerall Connect installeren.

- Het installeren van updates gebeurt op de server of de hoofdcomputer waarop Powerall Connect geïnstalleerd is.

Let op! Alle Powerall Connect gebruikers moeten de administratie en het Planbord verlaten, anders mislukt de update omdat Powerall Connect dan nog in gebruik is.

1. Open de snelkoppeling Powerall Updates op het bureaublad. Het scherm Powerall Updates verschijnt:
2. Belangrijk: Administrator - of beheersrechten zijn vereist om op deze pc/(terminal)server/werkstation Powerall Connect of andere software te installeren of bij te werken.
3. Kies voor de knop Start installatie. Het scherm Welkom bij Powerall Connect  verschijnt.
4. Klik hier voor meer informatie over de eenmalige melding vanaf 3.16 of hoger Vanaf versie 3.16 of hoger verschijnt éénmalig het volgend scherm: Let op: minimale Windows versie gewijzigd! Powerall vereist vanaf deze versie Windows 10 of hoger voor werkstations.
5. Kies voor de knop Volgende. Het scherm Onderdelen verschijnt.
6. Kies voor de knop Volgende. Let op! Het selectief uitschakelen van update onderdelen kan leiden tot een instabiel of niet werkend systeem. Gebruik deze functie alleen in overleg met onze medewerkers.
7. Het scherm Instellingen voor Powerall Connect (met het installatiepad) verschijnt.
8. Kies voor de knop Volgende. Het scherm Backup en upgrade verschijnt.
9. Kies voor de knop Volgende. Opmerking: De gedeelde administraties worden ook bijgewerkt naar een nieuwere versie.
10. Optioneel alleen bij PWS: Het scherm Instellingen voor de PWS verschijnt.
11. Kies voor de knop Volgende.
12. Optioneel Eerste keer of als Niet akkoord is aangevinkt: Het scherm Verzameling van Powerall Connect-instellingen verschijnt.
13. Kies voor de knop Volgende.
14. Klik hier voor meer informatie over het verzamelen van de Powerall Connect informatie: Akkoord staat standaard aangevinkt. Deze opties betekenen: Na akkoord: scherm wordt niet meer getoond .
15. Na niet akkoord: wordt dit scherm opnieuw getoond bij de volgende installatie en blijft de optie op niet akkoord staan.

- Het scherm Overzicht verschijnt.

1. Kies voor de knop Volgende. Bevestig de Windows gebruikersaccount melding.
2. Het scherm Installatie proces verschijnt, met informatie over het installatie proces: Bezig met installeren. Vanaf versie 3.31.
3. Het scherm Installatie voltooid verschijnt.
4. Optioneel: om te zien wat er gewijzigd is, in deze versie, klik op de link Klik hier om de Release notes te bekijken. De Powerall Connect release notes worden geopend in de browser.
5. Kies voor de knop Sluiten. Opmerking: Als de melding: een herstart is nodig verschijnt, is het aan te raden dit te doen, om mogelijke problemen in de werking van Powerall Connect te voorkomen.

De updates zijn geïnstalleerd en Powerall Connect kan weer gebruikt worden.

#### FAQ

Opmerking: Bij gebruik van werkstations moeten deze ook bijgewerkt worden, zie gerelateerde onderwerpen.

Wat wordt er bij het installeren van een nieuwe versie of update opgeschoond?

Bij een update wordt, per administratie, het volgende opgeschoond:

- Verouderde back-ups. De laatste 4 administratie back-ups blijven bewaard.
- De bestanden in de WRK-map met extensie .ppr / .txt / .xml / .html en datum gewijzigd ouder dan 14 dagen.
- Kopieën van oude Powerall Connect bestanden, (bijv. GUETXT-V03290.dat/vix) die ouder zijn dan 1 maand .

- Hoe update ik het Powerall Connect Werkstation?

---
## Hoe maak ik het streepje t.b.v. sneltoetsen zichtbaar?

Bij bijna alle knoppen is het gebruik van sneltoetsen mogelijk. Om bijv. iets af te drukken, druk op ALT+P bij de knop Print.

Als het onder onderstrepingsteken (_) niet zichtbaar is, doorloopt u de volgende stappen:

#### Toegankelijkheidsinstelling aanzetten in Windows 8, 10 of 11.

1. Bij windows Start type in Toegankelijkheid.
2. Selecteer Toegankelijkheidsinstellingen voor toetsenbord.
3. Zet bij Overige instellingen onderstreping aan.
4. Windows 11 Zet Toegangstoetsen onderstrepen aan.

De sneltoetsen zijn onderstreept.

Klik hier voor meer informatie over deze instelling in Windows 7

#### Toegankelijkheidsinstelling aanzetten in Windows 7

1. Klik met de rechtermuisknop, links onderin, op de Windows Start knop.
2. Klik achtereenvolgens op Configuratiescherm > Toegankelijkheid > Toegankelijkheidscentrum > Het toetsenbord eenvoudiger in het gebruik maken.
3. Vink bij 'Toetsenbordsnelkoppelingen en sneltoetsen' onderstrepen aan.
4. Klik op OK.

De sneltoetsen zijn onderstreept.

- Tips & Tricks

---
## Hoe repareer of wijzig ik de Powerall werkstation installatie?

Belangrijk: Zorg er voor dat op het betreffend werkstation niemand is ingelogd in Powerall Connect.

Om de Powerall Connect installatie te repareren, doorloopt u de volgende stappen:

1. Klik, in de Windows taakbalk, op het vergrootglas.of Ga naar > Configuratiescherm > Programma’s en Onderdelen en ga verder met stap 4.
2. Type in .
3. Klik op Apps en onderdelen.
4. Blader naar en klik op Powerall Werkstation.
5. Klik op Wijzigen.
6. Kies Repareren. of Bij wijzigen, kies Wijzigen.
7. Kies voor de knop Volgende.
8. Kies voor de knop Volgende.
9. Bevestig de Windows gebruikersaccount melding.
10. Bij Reparatie voltooid: Kies voor de knop Sluiten.

De installatie is gerepareerd, Powerall Connect kan weer gebruikt worden.

- Hoe installeer ik Powerall Werkstation / Planbord / Outlook Inbox?

---
## Hoe stel ik de Powerall Connect Outlook Inbox in?

**Hoe stel ik de Powerall Connect Outlook Inbox in? Met de Powerall Connect Inbox plug-in kunnen e-mail facturen doorgezet worden naar de Powerall Connect administratie(s). #### Instellingen De Powerall Connect Outlook Inbox plug-in moet geïnstalleerd zijn, zie Hoe installeer ik Powerall Werkstation / Planbord / Outlook Inbox? #### Outlook inbox instellingen Het pad voor de inbox moet opgegeven worden in Outlook, open deze. Dit kan op 2 manieren a of b: 1. Per outlook map, deze optie wordt gebruikt als er facturen naar meerdere administraties moeten worden gezet: 2. Rechtermuisknop op de betreffende map > Eigenschappen. 3. Ga naar tabblad Powerall inbox. 4. Vul het inbox pad in of blader er naar toe. 5. Kies voor de knop OK. Voor alle mappen**, deze optie wordt gebruikt als de facturen naar **1 administratie** gezet moeten worden.

1. Klik op Bestand > Opties > Invoegtoepassingen > Powerall Connect Inbox > Opties invoegtoepassing.
2. Geef het Inbox pad op.
3. Kies voor de knop OK.

Het inbox-pad is ingesteld.

Opmerking: Hierbij een voorbeeld van het inbox pad op server : \\\pw\\INBOX\

Tip: facturen of administratie@ Om de administratie zo eenvoudig mogelijk te laten verlopen is het raadzaam om je inkomend/uitgaande facturen via bijv. bovenstaand e-mail adres te ontvangen/versturen. • Vragen over en reacties op facturen kunnen op deze manier gemakkelijk onderzocht worden. Daarnaast is het direct duidelijk waar de e-mail over gaat.

#### FAQ

Wat doe ik als de outlook plugin niet wil starten?

Het is mogelijk dat de outlook plug-in niet start op een oud systeem/server (in dit geval terminal server (2008 R2) met Office 2013 32-bits).

- De melding Er is een runtime fout opgetreden tijdens het laden van de COM-invoegtoepassing verschijnt:

#### Oplossing

VSTO runtime te (her)installeren, dat wil nog wel eens helpen bij dit soort oude systemen.

- https://download.microsoft.com/download/C/A/8/CA86DFA0-81F3-4568-875A-7E7A598D4C1C/vstor_redist.exe

- Powerall Connect Outlook Inbox

---
## Hoe update ik het Powerall Connect Werkstation?

Opmerking: Powerall Connect werkstation wordt gebruikt op een werkstation of thin client.

Als er een nieuwe versie van Powerall Connect geïnstalleerd is, moet ook de software op de werkstations bijgewerkt worden. Om dit te doen, doorloopt u de volgende stappen:

1. Bij het opstarten van Powerall Connect of het Planbord verschijnt dan de volgende melding: Belangrijk: Administrator - of beheersrechten zijn vereist om op deze pc/(terminal)server/werkstation Powerall Connect of andere software te installeren of bij te werken.
2. Kies voor de knop OK om Powerall Connect bij te werken. Het scherm Nieuwe versie ophalen verschijnt.
3. Bevestig de Windows gebruikersaccount melding.
4. Het scherm Installatie Powerall Werkstation. Bezig met installeren verschijnt.... Powerall Connect werkstation wordt geïnstalleerd

Nadat de installatie beëindigd is, wordt het login scherm getoond en kan Powerall Connect weer gebruikt worden.

- Hoe installeer ik een Powerall update?

---
## Wat doe ik bij de melding: 'Verzenden naar Powerall Connect factuurinbox mislukt?'

#### Outlook

In Microsoft Outlook is het mogelijk om bepaalde e-mails te verzenden naar Powerall Connect.

Bij het verzenden van een e-mail/factuur uit Outlook naar de Powerall Factuurinbox kan één van deze meldingen verschijnen:

of

Belangrijk: Dit komt hoofdzakelijk voor bij IMAP (Internet Message Access Protocol). Dit is het protocol voor het synchroniseren van e-mail, er wordt hierbij direct op de mailserver gewerkt. • Controleer dus het het email protocol. • Indien dit ook voorkomt bij Exchange of POP s.v.p. doorgeven!

Om dit op te lossen, doorloopt u de volgende stappen:

1. Open Outlook.
2. Rechtermuisknop op Postvak IN, selecteer > Eigenschappen. Het scherm Eigenschappen van Postvak IN verschijnt.
3. Ga naar tabblad Powerall Inbox.
4. Voltooid markeren moet hierbij uitgevinkt zijn.
5. Kies voor de knop OK.

Een email kan weer verzonden worden naar de Powerall Connect inbox.

#### “Verzenden naar Powerall Factuurinbox mislukt: Kan de functie niet uitvoeren omdat het bericht is gewijzigd”

Bovenstaand probleem kan voorkomen in de volgende situaties:

- Als er een trage verbinding is tussen de email client (bijvoorbeeld outlook) en de email server. IMAP vereist vaak een snelle internetverbinding.
- Als er een e-factuur naar een server geplaatst moet worden via de Powerall Connect Outlook Inbox, en de server staat op een remote locatie waar de verbinding tussen de Outlook Inbox en server niet stabiel of heel traag is, door bijv. een trage VPN verbinding).
- Hierbij een praktijk voorbeeld: Opmerking: Een e-mail werd vanaf een bepaalde pc via een (trage) VPN verbinding in een map op de server gezet. Het duurde waarschijnlijk te lang om de status te wijzigen, vandaar deze foutmelding.

## Foutmelding met inboeken e-facturen vanuit Outlook bij Powerall Connect Outlook Inbox

#### Probleem

Foutmelding: Verzenden naar Powerall Factuurinbox mislukt:

- Pdf-Sharp Kan bestand of assembly Pdfsharp, Version=1.50.4000.0, Culture=neutral, publickeytoken=yyyyy of een van de afhankelijkheden hiervan niet laden. De manifestdefinitie van de gevonden assembly komt niet overeen met de assembly-verwijzing. Uitzondering van HRESULT: 0x80131040

- Unexpected character ... in PDF stream. The file may be corrupted. Etc.

#### Oplossing

Repareer de Powerall Connect Werkstation installatie, zie:

- Hoe repareer of wijzig ik de Powerall werkstation installatie? Bij stap 6 kies i.p.v. wijzigen Repareer.

---
## Wat doe ik bij de melding: 'mqrt.dll: Programm missing or inaccessible'?

#### Oorzaak

De PWS van Powerall Connect is niet geïnstalleerd.

(Cobol error at 00122e in PW00.acu)

#### Oplossing

Installeer ook de PWS.

1. Start installatie (Powerall Setup .exe) > Wijzigen > Volgende.
2. Vink Powerall Web Synchronisatie (PWS) aan > Volgende.
3. Geef de  voor de PWS op > Volgende.
4. Etc.

De PWS services is geïnstalleerd. Start Powerall Connect opnieuw.

Opmerking: Mqrt.dll is een onderdeel van Message queuing MSMQ, die gelijktijdig met de PWS geïnstalleerd wordt.

---
## Wat doe ik bij de melding: 'Nieuwere of verouderde administratie of versie'?

#### Administratie is nieuwer dan programma versie!

Het volgende bericht verschijnt, bij het opstarten van een administratie (die verouderd was):

- De administratieversie  is nieuwer dan de programmaversie . Neem contact op met de helplijn.

Mogelijke oorzaak: De verouderde administratie is bijgewerkt naar een nieuwe versie en daarna krijg je deze melding.

Belangrijk: Neem contact op met de helpdesk om dit op te lossen.

#### Verouderde Powerall Connect versie

De melding Deze versie van Powerall Connect is verouderd, verschijnt als er gebruik gemaakt wordt van een Powerall Connect versie van meer dan één jaar oud.

Kies voor de knop Ja. Of

Installeer de nieuwste versie van Powerall Connect zie:

- Hoe installeer ik een Powerall update?

#### Verouderde administratie

Als een administratie een verouderde versie heeft dan actieve Powerall Connect versie, verschijnt de volgende melding:

Opmerking: Deze melding verschijnt bijv. als de laatste back-up teruggezet wordt.

Klik hier voor meer informatie over het bij werken van de 'verouderde' gegevens:

Om de administratie bij te werken, doorloopt u de volgende stappen:

1. Kies voor de knop Ja.
2. Het scherm Powerall Connect update verschijnt. Opmerking: Indien u geen back-up heeft, maak deze via een Schaduwkopie.
3. Kies voor de knop Ja.
4. Opmerking: Normaliter verschijnt er geen foutmelding.
5. Als de update gereed is, verschijnt het scherm:
6. Kies voor de knop Doorgaan.

De administratie is bijgewerkt en kan weer gebruikt worden.

Belangrijk: Bij een bestandsfout neem contact op met de helpdesk.

---
## FAQ&#160;Offerte en Word

# FAQ Offerte en Word

In dit hoofdstuk staan de meestgestelde vragen over de over de Offerte i.c.m. Microsoft office Word.

Hoe druk ik een offerte naar een nieuw Word document af?

Om een offerte naar een nieuw word document af te drukken, doorloopt u de volgende stappen:

1. Ga naar Selecteren offertes (OS).
2. Selecteer de offerte.
3. Kies voor de knop Wijzigen.
4. Kies voor de knop Print MS Word.
5. Dubbelklik om het betreffend Word sjabloon af te drukken.
6. Als het document gereed is, wordt deze geopend in Microsoft Word. Het programma Word licht op, in de Windows taakbalk.

De offerte wordt in Microsoft Word geopend.

Hoe druk ik een offerte in Word af?

Om een (laatste) offerte naar een Word document af te drukken, doorloopt u de volgende stappen:

1. Ga naar Selecteren offertes (OS).
2. Selecteer de offerte.
3. Kies voor de knop WORD offerte.

De laatste offerte wordt in Microsoft Word geopend en kan afgedrukt worden.

Hoe zie ik de diverse offerte versies?

Om van een offerte de diverse versies te bekijken, doorloopt u de volgende stappen:

1. Ga naar Selecteren offertes (OS).
2. Selecteer de offerte.
3. Kies voor de knop Word versies.

De map met de offerte versies wordt weergegeven met een volgnummer bijv. (00x).docx.

- FAQ Lay-outs / Word

---
## FAQ&#160;Offerte

# FAQ Offerte

In dit hoofdstuk staan de meestgestelde vragen over de over de Offerte module.

- Hoe werkt ondertekenen offerte i.c.m. Stiply?
- Hoe wijzig ik de relatie van een offerte of werkorder? vanaf versie 3.30
- FAQ Offerte en Word

Algemeen

*Hoe voeg ik de kolom Marge* in de regels, toe bij een offerte?

Het is mogelijk om de kolom Marge % toe te voegen in de offerte regels.

- Voor meer informatie zie Offerte calculatie.

Waar kan ik de offerte nog meer bekijken?

Het is mogelijk om de PDF-offertes te bekijken op de Powerall CRM App. Voor meer info zie:

- Powerall CRM App Offertes

Waar kan ik een compleet overzicht van de offertes vinden?

Bij Overzicht offertes uitgebreid / verkort (OLB of OLV) kan een overzicht aangevraagd worden van zowel lopende als vrijgegeven offertes. Bij Status vanaf selecteer:

- Alle inclusief vervallen offertes),of
- Vrijgegeven en vul 1 t/m 4 in, (exclusief vervallen).

Opmerking: Het is mogelijk om op de offerte de afleverdatum (veld SQA780) toe te voegen.

Machines

Hoe maak ik een offerte van een (nieuwe) machine die nog niet in Powerall Connect staat?

Het is mogelijk om een offerte te maken voor een machine die nog niet binnen is (nog niet geregistreerd in Powerall Connect).

Om dit te doen, doorloopt u de volgende stappen:

1. Geef de offerte in, zie Nieuwe offerte aanmaken.
2. Na ingave van het machineverkoop artikel kies, bij het scherm Verkoop transacties, voor de knop Overslaan.
3. Bij Vrijgeven offerte moet deze regel (later) gekoppeld worden aan een machine. Selecteer de machine.
4. Kies voor de knop Verder.

De offerte/order is gekoppeld aan de machine.

Kan ik ook de offerte(s) van de machine zien?

Ja, dit is mogelijk bij Opvragen machines (MO), tabblad Offertes.

- Offerte

---
## Hoe druk ik opnieuw mijn pakbon of leverbon af?

Het is mogelijk om de pakbon of leverbon opnieuw af te drukken van een verkooporder. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Selecteren verkooporders (VS).
2. Selecteer de verkooporder.
3. Kies voor de knop Details. Het scherm Verkooporder details verschijnt.
4. Kies voor de knop Print kopie.Selecteer layout de gewenst Lever- of Pakbon.
5. Kies voor de knop Leveringeninfo. Het scherm Verkooporder leveringen verschijnt.
6. Kies voor de knop Pakbon. of Kies voor de knop Leverbon.

De pakbon of leverbon wordt op het scherm weergegeven en kan afgedrukt worden.

---
## Hoe wijzig ik de bontekst op een offerte of verkooporder?

#### Tekst bij vrijgeven offertes en verkooporders

Als een offerte of verkooporder wordt vrijgegeven dan zijn er de volgende mogelijkheden:

- Standaard maakt Powerall Connect zelf de standaard tekst: Levering vk-ord 54546 D.D. 11/04/25
- Gebruik een artikel met een andere tekst met een tag voor datum en document bijv. 'levering verkooporder '.
- Gebruik een artikel zonder tekst. Dan wordt geen regel toegevoegd.

Deze tekst is vrij in te stellen via een tekst-artikel bij instelling offertes en verkooporders. Ook kan dit voor andere talen (bijv. Engels, Duits) ingesteld worden.

#### Tekst artikel

Om het tekst-artikel in te stellen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud artikelen (ABA).
2. Kies voor de knop Opvoer.
3. Geef de omschrijving in de vorm van Levering vk.order  D.D.  met een tag <> voor document en datum.
4. Bij soort artikel selecteer Tekst.
5. Kies voor de knop Opslaan.

Het artikel is opgeslagen.

Opmerking: Het is mogelijk om geen tekst weer te geven bij het vrijgeven van verkooporder. • Geef dan een artikel op zonder tekst, dan wordt er geen regel toegevoegd.

#### Instellingen offertes en verkooporders

Om het tekst-artikel in te stellen bij de offerte of verkooporder, doorloopt u de volgende stappen:

1. Ga naar Instellingen verkooporders (BIK) of Instellingen Offertes (BIO), tabblad Beheer.
2. Kies voor de knop Wijzig.
3. Geef bij tekstartikel t.b.v. vrijgave tekst de  in.
4. Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

Tip: Bij het vrijgeven van de offerte of verkooporder wordt deze tekst aangemaakt. Als er bij Selecteren bonnen (FS) dubbel geklikt wordt op de bon, wordt deze tekstregel getoond.

Belangrijk: Bij een aanbetaling wordt er altijd een tekst ter informatie afgedrukt.

---
## FAQ CRM App

**FAQ CRM App In dit hoofdstuk staan de meestgestelde vragen over de Powerall CRM App. - Hoe controleer ik de verbindingsstatus of versie op CRM App? - Wat doe ik bij de e-mail melding 'Powerall CRM for IOS is now available to test'? ### Installatie #### Waar kan ik deze app downloaden? De app kan in de App store of Playstore gedownload worden. Klik hier voor meer informatie over het downloaden van de Powerall CRM App - Voor Android: Powerall CRM. - Voor Apple op iTunes: Powerall CRM. Tip: Zoek op Powerall CRM App in de app store. Voor een beschrijving of versie informatie van deze app zie bovenstaande sites. Hoe installeer ik de Powerall CRM App? - Installatie CRM app ### FAQ en Meldingen #### Nieuw Wat is nieuw in de Powerall CRM App? #### Versie 3.01 2023 De layout is helemaal vernieuwd conform Powerall Connect 3.0. - Bij machines wordt het icoon van de betreffende branche getoond. #### Versie 2021 Het volgende functies zijn toegevoegd: ### Offertes Op het Dashboard is Mijn offertes toegevoegd. Mijn offertes: - Alle offertes van de gebruiker/verkoper zijn zichtbaar. - Offertes kunnen gebruikt worden. #### Autorisatie offertes - De gebruiker moet geautoriseerd worden voor Offertes bij Onderhoud personeelscode, tabblad CRM App. Het veld Offertes tonen moet op ja staan. Zie Ga naar Onderhoud personeelscodes (BTP). Indien niet geautoriseerd, zijn Mijn Offertes en tabblad Offerte niet zichtbaar. Bij Instellingen offertes, tabblad Uitvoer printer moeten de layout velden Standaard/Machine offerte PDF t.b.v. CRM app gevuld zijn: Bij de Relaties details is tabblad Offerte toegevoegd. De volgende gegevens worden weergegeven: - De offerte details (alleen de kop van de offerte, geen regels) - De status van de offerte - De relatie details - PDF offerte (incl. regels) - Word offerte De PDF en Word offerte kan gedeeld, verzonden en afgedrukt worden. Opmerking: Een PDF-offerte wordt pas gemaakt bij Einde offerte. Machines - Een Kleine machine is ook zichtbaar. #### Versie 2020 Het volgende functies zijn toegevoegd: - Relaties Bij tab Machines, kan je een machine zoeken. - Bij een nieuwe klant, kan je een land selecteren. Machines

- Prijstype (Vraagprijs, Op aanvraag, Notk e.d.) opgegeven en bewerkt worden.
- Vlootnummer is zichtbaar en zoekbaar.
- Bij klantweergave aan wordt de handelsprijs niet weergegeven.

#### Algemeen

*Hoe komt het dat ik de dichts bijzijnde buitenlandse klanten niet zie, als ik in Nederland in de grensstreek ben? Dit heeft te maken met de standaard instelling van de Powerall CRM App m.b.t. de plaatsbepaling. - Indien klant veel in het buitenland komt, of het bedrijf bevindt zich buiten Nederland, moet de afstandsbepaling uitgebreid worden naar het buitenland. - Daar zijn mogelijk kosten aan verbonden. - Neem hiervoor contact op met de helpdesk om dit te regelen. Wat doe ik bij een ongeldige licentie? Uw licentie is ontoereikend, 0 van maximaal 0 gebruikers(s) zijn al actief. - Neem contact op met de helpdesk, om dit aan te passen. Wat doe ik bij de melding 'De beta van Overall CRM*' is verlopen.

Na verloop van tijd verloopt de beta versie van de Powerall CRM App omdat deze verouderd is en er een nieuwe versie uit gekomen is. De nieuwste versie van de Powerall CRM App moet dan gedownload worden.

- Ga naar de app store en download de nieuwste versie, zie ook Waar kan ik deze app downloaden?

Wat doe ik bij de melding 'Licentie niet toereikend'?

De volgende aanvullende informatie wordt gegeven:

- Uw licentie is ontoereikend, 1 van maximaal gebruikers(s) zijn al actief. Neem contact op met de helpdesk, om dit aan te passen
- Login op het Webportal en controleer bij Modules > Seats Powerall CRM App welke gebruikers actief zijn. Indien nodig verwijder een (niet actieve) gebruiker.

Welk licentie model wordt gebruikt?

De werking van de Werkbon App is hetzelfde als de Powerall CRM App.

- De klant betaalt per gebruiker. Een gebruiker kan onbeperkt op meerdere devices inloggen.
- Een gebruiker gebruikt één seat.

Opmerking: In het Mijn Powerall / klantenportaal is het aantal gebruikte seats te zien, zie Seats gebruik. Ook kan hier een seat verwijderd worden.

Wat doe ik als de personeelscode niet gekoppeld is?

#### Oorzaak

Aan de betreffende gebruiker is geen personeelscode gekoppeld.

Opmerking: Je kunt dit zien op het dashboard, waar achter welkom de personeelsnaam staat.• Indien de personeelscode nog niet aanwezig is, voeg deze dan toe via Onderhoud personeelscodes.

#### Oplossing

Ga naar 4.c bij Onderhoud gebruikers.

#### Resultaat

De gebruiker is gekoppeld aan een personeelscode.In de App wordt bij Welkom de naam weergegeven.

Wat gebeurt er als ik klantweergave aan zet?

Als de klantweergave aangezet wordt, is bepaalde informatie niet zichtbaar. Dit geldt voor het volgende:

- Notities Deze zijn niet zichtbaar, er wordt niets getoond. Ook niet 'Mijn acties' of de melding Geen resultaten / notities.

Machines

- Op tabblad Algemeen wordt alleen de adviesprijs en niet de handelsprijs weergegeven.
- Op tabblad Transactie is het totaalbedrag artikelen en de artikelprijs niet zichtbaar. De bedragen van de werkorder regels zijn niet zichtbaar, alleen aantallen.
- De interne notities zijn niet zichtbaar.

#### Relaties

Hoe komt het dat ik bij relaties het aantal kilometers niet zie?

Bij de melding: Locatievoorziening uitgeschakeld moet de toegang tot de locatie aan staan. Ook er moet een actieve GPS -of Wifi verbinding zijn, anders kunnen de afstand in km's niet berekend worden.

- Ga naar Instellingen > Powerall CRM App > Locatie en controleer de toegang.

Hoe geef ik de CRM kenmerken op in de CRM app?

Om op te geven of te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Relatie details en scroll naar beneden.
2. Bij CRM kenmerken druk op de toets Bewerken.
3. Selecteer het CRM kenmerken, bijv. Soort bedrijf of Aantal machines: Waarde = N: Waarde = J: zie:
4. Kies voor de knop OPSLAAN.

De gegevens zijn opgeslagen.

Kan ik de machine(s) zien bij de eindverbruiker?

Ja, als bij Onderhoud machines (MBB), tabblad Service de eindgebruiker ingevuld is.

In de Powerall CRM App is deze bij de betreffende Relatie, tabblad Machine zichtbaar.

- Opmerking: Bij Opvragen machines, tabblad Machines, is het ook mogelijk om deze te zien, bij een speciale instelling. Neem hiervoor contact op met de helpdesk.

#### Artikel

Hoe kan ik een artikel(barcode) scannen?

1. Ga naar Artikelen.
2. Druk op het Scanner symbool, rechts boven.
3. Als de App om toestemming tot de camera vraag, geef dan akkoord.
4. Plaats de barcode in het midden van het scherm (op rode lijn).

De artikelcode wordt gescand (het scannen gebeurt automatisch).

#### Artikel / Machine

Wat voor soort foto's kan in toevoegen aan mijn artikel of machine?

Bij een artikel of machine, tabblad Afbeeldingen, kunnen de volgende foto's worden toegevoegd worden:

- Standaard
- Voor websiteArtikel: Machines:

Bij Machine, kan vervolgens gekozen worden voor:

- Foto maken
- Selecteren uit galerij

Hoe sorteer of verwijder ik een afbeelding?

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Machines of Artikelen.
2. Selecteer een machine of artikel
3. Ga naar tabblad Afbeeldingen.
4. Druk op Sorteren of verwijderen.
5. Sorteer: Druk op de afbeelding en sleep deze naar de juiste positie.
6. Verwijder: Druk op (prullenbak knop).
7. iOS: Kies voor de knop Opslaan. Andriod: Kies voor de knop Opslaan.

De gegevens zijn opgeslagen.

#### Machines

Hoe filter ik de machines op inkoop en/of verkoopstatus?

Het is mogelijk om de machines te filteren op de diverse in- en verkoop statussen. Om dit te doen, doorloopt u de volgende stappen:

1. Druk op het filter symbool (rechtsboven).
2. Vink de betreffende statussen aan op uit.
3. Kies voor de knop TOEPASSEN.

De betreffende machines worden weergeven.

- Onderaan verschijnt kort een melding dat er een filter wordt toegepast.

Hoe filter ik mijn machines op machinegroep?

Het is mogelijk om de machines te filteren op machine (hoofd)groep. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Machines.
2. Druk op Blader door groepen (bovenaan).
3. Selecteer een groep:
4. Kies voor de knop BEKIJK ALLES.

De machines van deze groep worden weergegeven.

Hoe worden de website foto's genoemd in Powerall Connect?

De website foto's in Powerall Connect worden als volgt ge- of hernoemd:

- -.jpg
- bijv. 5556.001.jpg

Opmerking: Deze website foto's staan in de betreffend dossier map van de machine.

#### Instellingen

Wat kan ik wijzigen bij de Powerall CRM App instellingen?

De volgende instellingen kunnen gebruikt worden.

- Ingelogd bij bedrijf / wisselen administratie(uitloggen)
- Ingelogd als gebruiker (uitloggen)
- Huidige locatie (Handmatig / GPS / Niet gebruiken)
- Taal (Nederland / Engels)
- Klantweergave (inschakelen / uitschakelen)

Hoe wissel ik van administratie?

Om van administratie te wisselen, doorloopt u de volgende stappen:

1. Ga naar Instellingen.
2. Bij administraties, druk op de gewenste administratie.
3. Bij melding Administratie switchen druk op Ja.

De geselecteerde administratie is actief.

Hoe wissel ik van taal (Engels/Nederlands)?

Om van taal te wisselen, doorloopt u de volgende stappen:

1. Ga naar Instellingen.
2. Bij taal, druk op Nederlands of English.
3. De CRM app gaat direct naar het Dashboard.

De CRM app wordt in de geselecteerde taal weergegeven.

Welke mogelijkheden zijn er m.b.t. de autorisatie voor de Powerall CRM App?

Het volgende kan geautoriseerd worden voor een gebruiker:

| Omschrijving | Gebruik | Aanmaken | Wijzigen |
| --- | --- | --- | --- |
| Gebruik Powerall CRM App | J/N |  |  |
| Relatie aanmaken / wijzigen | J/N | Ja | Ja |
| Contactpersoon aanmaken / wijzigen | J/N | Ja | Ja |
| Machine aanmaken / wijzigen | J/N | Ja | Ja |
| Inkoopprijzen tonen | J/N |  |  |
| Offertes tonen | J/N |  |  |

Dit kan bij Onderhoud personeelscodes (BTP) bij tabblad CRM app.

#### Beveiliging

Hoe is de Powerall CRM App beveiligd?

De beveiliging van de Powerall CRM App is als volgt:

- De app is beveiligd met een bedrijfs - en gebruikers account/login.
- De verbinding is beveiligd met het SSL (Secure Sockets Layer) protocol.
- Daarnaast wordt gebruikt gemaakt van een beveiligde Microsoft Azure omgeving.

#### Ondersteuning iOS apparaten

Welke iOS-versies worden ondersteund door de Powerall CRM App?

De ondersteuning voor een bepaalde iOS-versie eindigt zodra Apple de ondersteuning stopt. Hierbij enkele opmerkingen:

- Alleen apparaten worden ondersteund mits de laatste updates geïnstalleerd zijn.
- En alleen apparaten worden ondersteund die niet achterhaald of verouderd (Vintage of Obselete) zijn, zie:https://iosref.com/ios

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Powerall CRM app

---
## Wat doe ik bij de melding: 'Kan verkooporder &lt;x&gt; niet vrijgeven, inkoopprijzen zijn nog niet gecontroleerd bij matching!'?

# Wat doe ik bij de melding: 'Kan verkooporder  niet vrijgeven, inkoopprijzen zijn nog niet gecontroleerd bij matching!'?

#### Oorzaak

Als aan een verkooporder ook een inkooporder is gekoppeld, en de inkoopprijzen zijn nog niet gecontroleerd bij matching, is het nog niet mogelijk om deze vrij te geven.

#### Voorwaarde

Het volgende is dan ingesteld bij Instellingen artikelen:

- tabblad Voorraad/bestelmethodiek Prijs wijzigen bij goederen ontvangst/matching is Ja.

- tabblad Koppelingen Controle Btb-order inkoopprijzen of verkoopprijzen is Ja. Dan wordt de verkoop-/werkorder bijgewerkt.

Er moet eerst gematcht worden, want anders wordt er geen goede inkoopprijs of verkoopprijs berekend.

#### Oplossing

Om dit op te lossen, doorloopt u de volgende stappen:

1. Ga naar Goederenmatching (KI).
2. Geef de relatiecode in.
3. Kies voor de knop Nieuw boekstuk.
4. Geef de overige gegevens in.
5. Kies voor de knop Matchen goederen.
6. Match deze inkooporder, zie link bij punt 1.
7. Ga naar Verwerken artikelmutaties (AVF) om deze te verwerken.

De verkooporder kan vrijgegeven worden.

---
## FAQ Verkoop

In dit hoofdstuk staan de meestgestelde vragen over de Verkoop module.

- FAQ Offerte
- FAQ Facturatie
- FAQ Kassa
- FAQ Prijsafspraken
- Hoe druk ik opnieuw mijn pakbon of leverbon af?
- Hoe, wat kan ik ... m.b.t. het verkoopproces?
- Hoe, wat kan ik ... m.b.t. PostNL?
- Hoe, wat kan ik ... m.b.t. Webshoporders?
- Hoe, wat kan ik ... m.b.t. wijzigen van korting op regelniveau?
- Hoe werkt een vooruit- of aanbetaling bij een verkoop- of werkorder?
- Hoe wijzig ik de bontekst op een offerte of verkooporder?

#### Dropshipment verkooporder

*Dropshipment bij verkooporders Wat is dropshipping bij verkooporders? Van een verkooporder(s) kan in één keer een inkooporder(s) gemaakt worden. Het volgende is hierbij van toepassing: - Het verkoopordertype moet dropshipment zijn. Zie Onderhoud ordertypes (BTR). Artikelen moeten van één (zelfde) leverancier zijn. Artikelen moeten status actief hebben. Opmerking: Neem contact op met de planning om dit in te richten. Welke meldingen kan ik krijgen bij een verkooporder met type dropshipment? Bij Selecteren verkooporders (VS) is het mogelijk om, van de alle verkooporders op het scherm, BtB order aan te maken, via de knop > Meer functie > BtB aanmaken. De volgende meldingen mogelijk zijn hierbij mogelijk - Dropshipment aanmaken is niet mogelijk: artikel (order Y / regel Z) heeft een andere leverancier; - artikel heeft geen leverancier; - artikel is onbekend / niet leverbaar / uitlopend / op aanvraag. Opmerking: Neem contact op met de planning om dit in te richten. Overige Is het mogelijk dat een verkooporder niet meer gewijzigd kan worden? Ja, dit is mogelijk door het gebruik van de fiatteringscode in de verkooporder, vanaf versie 3.14. Bij Instellingen verkooporders, tabblad Beheer, kan hiervoor het veld autorisatie fiatteringscode gebruikt worden. - Boven een bepaalde fiatteringscode mogen alleen gebruikers met een in te stellen autorisatie level de order nog wijzigen. Een gebruiker met een autorisatie (bijv. K) lager dan het in de instellingen ingegeven autorisatieniveau (K) mag namelijk wel een order wijzigen met een fiatteringscode lager dan het in de instellingen ingegeven autorisatieniveau. D.w.z. verkooporders met fiattering van A t/m K mogen gewijzigd worden, L t/m Z niet. - Een gebruiker met een autorisatie hoger dan het in de instellingen ingegeven autorisatieniveau mag altijd de fiatteringscode / verkooporder wijzigen. NB Z is het hoogste autorisatie niveau. Is het mogelijk om bij Selecteren verkooporders alleen de standaard of machine orders te zien? Ja, dit is mogelijk bij het veld Welke orders weergeven. Neem hiervoor contact op met de helpdesk om dit in te stellen | Welke orders weergeven | Optie voor het weergeven van verkooporders (afhankelijk van instelling):- Alle (standaard) - Standaardorders - Machineorders- Retouren / RMA | | --- | --- | - Hierbij een voorbeeld: Hoe zet ik de kolom Geleverd* in de regels, bij een verkooporders?

Het is mogelijk om de kolom geleverd toe te voegen in de verkooporder regels. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Instellingen verkooporders tabblad Beheer.
2. Selecteer bij Gebruik Picken order Ja.
3. Eventueel met Controle bij Vrijgave Ja, (het vrijgave scherm verschijnt hierbij).

*Hoe is deelfacturering van verkooporder uit te voeren? Standaard staat bij Onderhoud relaties (BRR), tabblad Debiteurinfo, deellevering en deelfacturatie op ja. Als er in de regels de aantallen gereserveerd ingevuld worden, kunnen deze regels alvast gefactureerd worden. - Bij het vrijgeven van deze verkooporder, worden alleen de aantallen + tekstregels gereserveerd doorgezet naar de bonnen. Wat betekent BR / IO* in de kolom BtB (Back to back) bij Invoeren/wijzigen verkooporders?

Dit betekend meestal dat er onvoldoende op voorraad is en dat het artikel besteld wordt of in bestelling is.

- IO er ise een inkooporder (IO) aan deze regel is gekoppeld.
- BR er is een bestelregel (BR) aan deze regel is gekoppeld, er wordt gebruik gemaakt van Centraal inkooporders aanmaken.

Om het inkoopnummer te bekijken: Kies voor de knop Details.

- Zie ook Koppeling werk-/verkooporder met inkooporder.

*Wat betekent de kolom Excl.Bedrag* bij Opvragen relaties bij verkooporders?

- In de kolom Excl. bedrag wordt het bedrag dat nog gereserveerd staat (aantal gereserveerde orders x prijs) weergegeven.

- Verkoop
- Onderhoud leveringscondities

---
## Hoe, wat kan ik ... m.b.t. het verkoopproces?

## Marges

Op het scherm Marge op  is het mogelijk om de marges per artikel of totaal te bekijken.

Hoe en waar kan ik de marges bekijken?

- Er is een extra knop Toon marge toegevoegd bij de knop

Hoe wordt de bruto winstmarge berekend?

- Het margebedrag is de Verkoopprijs - Inkoopprijs, bijv. 12,00 - 7,50 = 4,50.
- Het marge% of brutowinstmarge in procenten van de verkoopprijs, bijv. (4,50 : 12,00) x 100= 37,5%.

Hoe kan ik de 'Toon marge' knop autoriseren?

Om de Toon marge te autoriseren, doorloopt u de volgende stappen:

1. Ga naar Instellingen modules / processen (BI).
2. Selecteer de gewenste module.
3. Ga naar tabblad Beheer.
4. Kies voor de knop Wijzigen.
5. Vul bij Autorisatie kostprijs de autorisatie in van de gebruikers.
6. Kies voor de knop Opslaan.

Alleen voor de gebruikers met deze autorisatie, is deze knop zichtbaar.

Opmerking: Indien nodig doe dit ook voor de andere modules.

## Deelleveringen en facturatie

Bij deelleveringen en facturatie zijn de al geleverde en gefactureerde artikelen te zien.

Opmerking: Als deelleveringen en facturatie niet zijn toegestaan, kan de order niet vrijgegeven of gefactureerd worden. Of een Magazijnpicklist aangevraagd worden.

Welke knop/ informatie is er toegevoegd bij verkooporders?

Bij Selecteren verkooporders (VS) en Opvragen verkooporders(VO) is de knop Leveringeninfo beschikbaar

Bij verkooporder leveringen is het mogelijk om een Pakbon (kopie), Leverbon (kopie) of Factuur (kopie) aan te vragen, indien beschikbaar.

## Instellingen

Wat moet ik instellen om het te gebruiken?

Bij Instellingen CRM procesnotities, kan de volgende instelling gebruikt worden:

- | Proces | Optie voor het CRM proces waarbij een CRM melding aangemaakt wordt:- Invoer notitie- Bezoeknotitie- Print offerte- Print opdrachtbevestiging- Invoer verkooporder- Print aanmaning 1 t/m 4- Print herinnering keuring 1 t/m 4- Supportmodule- Nieuwe relatie via CRM-app (notitie aanmaken is onzichtbaar) | | --- | --- |

Als notitie aanmaken op Ja staat, komt er CRM pop-up als er een nieuwe verkooporder wordt aangemaakt bij:

- Vrijgeven van offerte naar Verkooporder
- Importeren webshop orders
- BTB - inkoopkant
- Invoeren verkooporders

Bij Onderhoud relaties (BRR), Debiteureninfo, kan de volgende instelling gebruikt worden:

- | Deelleveringen | Optie voor deelleveringen. Bij een nieuwe relatie / verkooporder wordt deze waarde overgenomen:- Ja (standaard) - Nee - Standaard wordt deze overgenomen van Instellingen debiteuren. | | --- | --- | | Deelfacturatie | Optie voor deelfacturatie (gedeeltelijke factureren). Bij een nieuwe relatie / verkooporder wordt deze waarde overgenomen:- Ja (standaard) - Nee - Standaard wordt deze overgenomen van Instellingen debiteuren. | | --- | --- |

Opmerking: Per relatie is dit instelbaar.

Bij Instellingen verkooporders, tabblad Beheer, kan de volgende instelling gebruikt worden:

- | Gebruik picken order | Optie het gebruik van picken orders:- Nee (standaard)- Ja, werkorders kunnen ook gepickt worden bij Overzicht orders (te picken) 2.0. | | --- | --- | | Dashboard picken | Optie voor het gebruik van het dashboard picken orders: - Nee (standaard) - Ja, hierbij is ook Gebruik Picken order' ja nodig, zie Overzicht orders (te picken) 2.0Hierbij verschijnt bij een verkooporder de knop Picken Order onder Meer functies. | | --- | --- | Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.
- of | Controle bij vrijgave | Optie voor gebruiker bij het scherm Registratie vrijgave leveringen (van toepassing bij PostNL).- Nee (standaard)- Ja, als bij Controle bij vrijgave en Gebruik Picken order beide op ja staan, wordt er een pop-up getoond 'Registratie vrijgave leveringen'. Hierbij kan Vrijgegeven door en Expeditiecode opgegeven worden, zie .Bij Verkooporderregel leveringen worden dan de kolommen Door en Vervoerswijze getoond. | | --- | --- | | Laatste pakbonnummer | Dit is het laatste gebruikte pakbon nummer. Bij gebruik van de knop Picken order wordt dit nummer gebruikt, de instelling 'Picken order' moet 'ja' zijn. | | --- | --- |

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## Wat doe ik bij de melding: 'Het balie bestand bestaat al op de server...'?

#### Melding

Deze melding, op de Barcodescanner Datalogic Memor, kan voorkomen bij het verzenden van de gescande gegevens.

Het balie bestand bestaat al op de server. Probeer het later nog eens.

#### Oorzaak

Er bestaat al een balie bestand in de uitleesmap, mogelijk is een eerdere scanning niet verwerkt.

#### Oplossing

Om de barcodescanner uit te lezen (welke dan ook), doorloopt u de volgende stappen:

1. Ga naar Uitlezen barcodescanner (BXU). In Menu 3.0 onder Artikelen > Barcodering en EPC
2. Selecteer het Uitleesstation optioneel. Opmerking: Alleen zichtbaar bij de instelling gebruik meerdere stations is ja.
3. Kies voor de knop Uitlezen.
4. Afhankelijk van de soort ontvangen scanning, verschijnt het volgende bij: #### Balie Klik hier voor meer informatie over de balie functie: Bij de instelling verwerking via bonnen, verschijnt het pop-up scherm Invoeren/wijzigen bonnen. Geef de relatie in.
5. Na Enter worden de gescande artikelen toegevoegd in de regels.

Bij de instelling verwerking via kassa, worden de artikelen 'geparkeerd', zie Invoeren kassabonnen, er verschijnt geen pop-up scherm.

D.m.v. de knop Geparkeerd en Oppakken, kan de transactie, met referentie Barcode scanning, verder afgehandeld worden.

#### Bestellen

Klik hier voor meer informatie over Bestellen:

Het pop-pup scherm Verwerk barcode bestelling verschijnt.

1. Wijzig eventueel de magazijncode.
2. Kies voor de knop Verwerken.
3. De ingescande artikelen worden op een inkooporder gezet. Het overzicht Aanmaken inkooporder vanuit barcodescanner wordt weergegeven op het scherm.
4. Of Op de Goedkeuren bestaladvieslijst, hierbij verschijnt eerst onderstaand scherm instelling. Zie Besteladvieslijst stap 5a.

#### Overboeken

Klik hier voor meer informatie over overboeken:

Het scherm Barcodering overboeking verschijnt .

Als artikelen niet herkend worden, verschijnt onderstaand scherm.

#### Locatie Klik hier voor meer informatie over Locatie: Het pop-pup scherm Verwerk locatie scanningen verschijnt.

1. Wijzig eventueel de magazijncode.
2. Kies voor de knop Verwerken.
3. De locatie van het artikelen wordt bijgewerkt, van dit magazijn. Het overzicht Uitzonderingen locatiescanning wordt weergegeven op het scherm.

#### Tellen

Klik hier voor meer informatie over Tellen:

Het scherm Verwerk barcode tellingen verschijnt.

1. Geef de magazijncode in.
2. Kies voor de knop Verwerken.
3. Bij kleine machine artikelen verschijnt een melding, als de voorraad (serienummer) gecorrigeerd moet worden. Voor meer informatie zie: Kleine machines Voorraad correctie

Werkorder

De gescande artikelen worden direct toegevoegd op de werkorder.

Afhankelijk van de instelling werkorders bijwerken worden de artikelen getotaliseerd of toegevoegd.

Bij Verwerkt - specificatie is te zien, wat er verwerkt is.

Als er geen gegevens meer uitgelezen moeten worden:

- Kies voor de knop Stop. De melding Wilt u stoppen met het uitlezen van de barcodescanner? verschijnt.
- Kies voor de knop Ja.

Kies voor de knop Sluiten.

Het bestand wat al op de server stond, wordt verwerkt, daarna wordt ook het balie bestand wat op de scanner staat verwerkt.

---
## Hoe druk ik de gescande artikelen (niet) af?

Bij het uitlezen van de scanner van een werkorder verschijnt er een pop-up met de gescande artikelen.

Het vinkje achter 'Print lijst' zorgt ervoor dat de gescande artikelen wel of niet afgedrukt worden.

1. Ga naar Uitlezen barcode scanner (BXU).
2. Kies voor de knop Uitlezen. Afhankelijk van de scanningen verschijnt er een melding, bijv. Verwerk barcode bestelling.
3. Selecteer bij magazijncode het magazijn, bij meerdere magazijnen.
4. Kies voor de knop Gereed.

Zet het vinkje bij Print lijst aan of uit.(Deze instelling blijft staan in- of uitgeschakeld.)

Kies voor de knop Gereed.

Kies voor de knop Sluiten.

Afhankelijk van het vinkje worden de gescande artikelen wel of niet afgedrukt.

- Overzicht barcode scanningen

---
## Hoe pas ik de autorisatie aan voor het touchscreen, zodat de monteur een werkorder kan wijzigen?

De monteur kan een werkorder wijzigen, op het touchscreen, als hij hiervoor toegang heeft.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud personeelscodes (BTP).
2. Geef de personeelscode in.
3. Kies voor de knop Wijzig.
4. Ga naar tabblad Werkbon App.
5. Bij veld inplannen toestaan van kies voor Nieuw + bestaande WO. | Inplannen toestaan van | Optie voor het inplannen van een werkorder (WO): - Geen WO (standaard) - Nieuw WO - Nieuw, bestaande WO- Scannen WO op de Werkbon App, vanaf versie 3.24NB Dit geldt ook zonder de Werkbon App bijv. bij Urenregistratie touchscreen ook voor het uitnodigen van een collega. | | --- | --- |
6. Kies voor de knop Opslaan.

De monteur kan een werkorder wijzigen op het touchscreen.

Opmerking: De autorisatie voor de kostprijs is in te stellen bij Instellingen werkorders tabblad Beheer.

---
## Hoe mail ik de uren naar een personeelslid?

Het is mogelijk om een urenoverzicht te e-mailen naar een persoon.

Tip: Dit overzicht uren/persoon kan gestuurd worden ter controle of als er bijv. iemand ingehuurd wordt.

#### Voorwaarde

De volgende voorwaarden zijn van toepassing:

- Deze optie moet beschikbaar zijn. Opmerking: Indien dit niet het geval is, raadpleeg de helpdesk.
- Bij Onderhoud personeelscodes (BTP) moet bij de betreffende personeelscode een relatiecode met een e-mailadres gekoppeld zijn, anders krijg je de pop-up:
- Bij Instellingen documentbeheer, tabblad Uren, kan het ontwerp, standaard afzender, bijlage en verzendwijze ingevuld worden

#### Overzicht aanvragen / mailen

Om het uuroverzicht aan te vragen, doorloopt u de volgende stappen:

1. Ga naar Mailen uren per persoon (WUM).
2. Bij personeelscode vanaf en t/m selecteer de betreffende personeelscode. Belangrijk: Selecteer één personeelscode, anders krijgt iemand de uren van iemand anders te zien.
3. Selecteer de overige gegevens, zoals bijv. werkorderstatus alle.
4. Kies voor de knop Verzenden.
5. De e-mail vervolgens wordt geopend in Microsoft Outlook (het programma zal oplichten in de Windows taakbalk).
6. Kies voor de knop Verzenden. (Het onderwerp wordt overgenomen uit de documentinstellingen.)

De e-mail is verzonden.

---
## Hoe wijzig ik het uurtarief?

Het uurtarief wordt gebruikt om het bedrag aan uren te berekenen.

#### Opgave Uren per persoon

Bij Werkorder uren registreren kan het Tarief excl. bedrag in de regels handmatig gewijzigd worden.

Er zijn 2 opties van toepassing A of B:

#### A. Taaksoort is leidend

Om het uurtarief van een bepaalde taak te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud taaksoorten (BTT).
2. Geef de taaksoortcode in.
3. Kies voor de knop Wijzig.
4. Wijzig het Extern/Intern tarief prijs.
5. Kies voor de knop Opslaan.

Bij nieuwe uren opgaves, wordt dit tarief gebruikt.

Belangrijk: Wanneer de prioriteitscode tarief op ‘Personeel’ staat, dan moet bij iedere personeelscode het tarief aangepast worden, zie hieronder.

#### B. Personeelscode is leidend

Om het standaard tarief van een medewerker te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud personeelscodes (BTP).
2. Geef de personeelscode in.
3. Kies voor de knop Wijzig.
4. Wijzig het Extern/Intern tarief prijs.
5. Kies voor de knop Opslaan.

Bij nieuwe uren opgaves, wordt dit tarief gebruikt.

---
## Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties?

Er zijn twee soorten werkorders, met verschillende tarieven:

- Extern, voor de klant.
- Intern, voor eigen gebruik of doorbelasting.

## Controle / vrijgave werkorder/bon

D.m.v. de Controle knop is het mogelijk om te zien wat er op de werkbon/factuur komt te staan.

- Het is hierbij mogelijk om d.mv. de knop Print werkorder een 'proforma' werkbon factuur/status update van de werkorder te maken en te verzenden. De juiste werkorder layout kan geselecteerd worden.

Klik hier, voor meer informatie over dit onderwerp.

Onderstaande instelling moet op ja staan bij Instellingen werkorders, tabblad Beheer.

- | Gebruik controle bij vrijgeven | Optie om de werkorder te controleren, voordat deze vrijgeven wordt: - Nee, (standaard) - Ja, bij Invoeren/wijzigen werkorders, verschijnt de knop Controle i.p.v. Vrijgegeven, zie ook Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties?Bij het gebruik van de Controle knop, wordt een soort preview van de bon gemaakt ter controle. | | --- | --- |

Opmerking: Deze controle optie geldt alleen bij externe werkorders.

Bij Invoeren/wijzigen werkorder staat er de knop Controleren i.p.v. Vrijgeven.

1. Kies voor de knop Controleren.
2. Na controle verandert de knop(tekst) in Vrijgeven: 1 % van het werkorderbedrag is 60 + 10 = 70,00 is 0,70 klein materiaal kosten.
3. De werkbon kan zo gecontroleerd en vrijgegeven worden.

In de regels worden de volgende gegevens (indien aanwezig) toegevoegd ter controle:

- Uren opgegeven via de knop Urendetail zie Werkorder uren registreren.
- Doorbelasting klein materiaal.
- Bij optie Handhaven, opgave vaste prijs/bedrag.

Belangrijk: Bij het verlaten van het programma, verdwijnen deze regels.

In onderstaande voorbeelden zijn deze (toegevoegde) regels zijn groen gemarkeerd.

#### Tekst regel

De tekst in de eerste regel is de externe tekst in de tabblad Werkomschrijving en wordt pas aangemaakt bij het vrijgeven.

#### Prijsniveau uren extern

Het prijsniveau uren extern/intern bepaalt hoe de uren weergegeven worden op de werkorder bon.

Klik hier, voor meer informatie over dit onderwerp.

Alleen optie Werkordertotaal wordt nog in één regel weergegeven:

- Bij de andere opties worden de uren afzonderlijk weergegeven, indien de taaksoort, tarief of opslag verschilt.

| Prijsniveau uren extern / intern | Het prijsniveau voor het berekenen van de uren op een externe of interne werkorder:- Werkordertotaal, uren worden gecumuleerd in één regel. Uren/aantal 1 met totaal bedrag (uren x tarief gecumuleerd) bijv. (4uur x 50 tarief) aantal 1 verkoopprijs 200.- Aantal x tarief (afgerond) , Uren worden per tarief en per korting verzameld en berekend. Per tarief en korting wordt er een regel geschreven (hoeft niet 1 op 1 te zijn).- Aantal x tarief (niet afgerond) idem, niet afgerond.- Personeelscode, externe / interne uurtarief van de persoon, Uren worden per personeelscode / per tarief / per korting verzameld. Per personeelscode per tarief en korting wordt er een regel geschreven. (Externe / interne uurtarief van de persoon, artikelcode bij facturen, bij geen artikel: ARB).- Taaksoort, Uren worden per taaksoort / per tarief / per korting verzameld en verschijnen op de werkorder regel.Zie bijv. Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties? |
| --- | --- |

De volgende uren opgave en instelling gelden hierbij:

- Uren voorbeeld:
- Overige Instellingen

1. Werkordertotaal, De urenregels worden berekend en dan in één regel getotaliseerd. Uren/aantal 1 met totaal bedrag (uren x tarief gecumuleerd).
2. Aantal x tarief (afgerond) Uren worden per tarief en per korting verzameld en berekend.Per tarief en korting wordt er een regel geschreven (hoeft niet 1 op 1 te zijn).
3. Aantal x tarief (niet afgerond)Idem, zelfde als afgerond.
4. Personeelscode Uren worden per personeelscode/per tarief/per korting verzameld. Per personeelscode per tarief en korting wordt er een regel geschreven. (Externe / interne uurtarief van de persoon, artikelcode bij facturen, bij geen artikel: ARB).
5. Taaksoort, Uren worden per taaksoort, per tarief of per korting verzameld. Per taaksoort / tarief / korting wordt er een regel geschreven.

Opmerking: * Het regel bedrag = aantal x tarief (x Opslag %).• Korting wordt negatief weergegeven in de kolom korting. • Bij een Opslag % wordt het prijs verhoogd en is de korting 0.

#### Positie urenregels

Het is mogelijk de uren boven of onderaan de werkorder bon weer te geven.

Klik hier voor meer informatie over over deze instelling:

Hierbij is ingesteld dat de uren bovenaan de werkorder bon komen.

| Gegenereerde urenregels vrijgeven | De plaats waar de aangemaakt urenregels weergegeven worden, bij het controleren of vrijgeven van een werkorder.- Bovenaan (standaard)- Onderaan |
| --- | --- |

Gegenereerde urenregels vrijgeven is gewijzigd naar positie van vrijgegeven urenregels.

#### Doorbelasting klein materiaal

Het is mogelijk om automatisch klein materiaal door te belasten.

Klik hier voor meer informatie over dit onderwerp:

Er is hierbij ingesteld dat 1% van het werkorder bedrag wordt doorbelast.

|  | Het volgend is ingesteld bij Instellingen werkorders, tabblad Beheer: |
| --- | --- |

| Automatisch doorbelasten klein materiaal | Optie voor het automatisch doorbelasten kleinmateriaal (interne- of extern werkorder):- 0,00 % standaard (niets doorbelast)- > 0,00 t/m max. 9,99%Optie om door te klein materiaal door te belasten:- Werkorder (Materiaal + Uren standaard)- Materiaal- UrenDe artikelcode bij doorbelasten gevuld zijn, zie Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties? |
| --- | --- |

| Artikelcode bij doorbelasting | De artikelcode van het kleinmateriaal dat doorbelast, a.h.v. de instellingen, wordt aan de klant. |
| --- | --- |

- Voor een voorbeeld van de werkorderbon zie schermafdrukken hierboven.

#### Vast afgesproken bedrag (handhaven)

Het is mogelijk om een afgesproken - of vastbedrag, voor bijvoorbeeld een reparatie of bouw van een machine af te spreken.

Klik hier voor meer informatie over dit onderwerp:

De globale stappen zijn:

- Bij een werkorder moet een vast bedrag in/ex BTW in gegeven worden.
- Bij het vrijgeven of controleren wordt dan het verschil berekend.
- Op factuur komt dan één regel te staan, met het afgesproken bedrag.

Belangrijk: Bij vrijgave naar een werkorder i.c.m. aantal geleverd vullen is ja, wordt het offerte bedrag ingevuld bij vast bedrag bij de WO instelling afgesproken bedrag.

Instellingen

| Afgesproken bedrag 'handhaven' |  |
| --- | --- |

| Artikelcode bij correctie | De  bij correctie (bij handhaven). Het soort artikel is normaal. |
| --- | --- |

| Afdrukken regels op factuur | Optie voor het afdrukken van de regels op de factuur (bij handhaven):- Ja, alle regels op factuur.- Beperkt artikel + omschrijving en aantal, zonder bedragen. Het afgesproken bedrag = Totaalbedrag (onder de streep)- Nee, geen regels op factuur, alleen Aantal = 1  met afgesproken bedrag.Klik hier, voor meer informatie over dit onderwerp.Hierbij een voorbeeld afdrukken regels op factuur is nee:Het correctiebedrag is het totaal van de bovenliggende regels (in dit geval 2 t/m 8).Opmerking: Bij Controle werkorders, zijn deze regels wel te zien. |
| --- | --- |

Belangrijk: Een vrijgegeven werkorder met een vast bedrag, kan in de bonnen (regels) niet (meer) gewijzigd worden. Dit om mogelijke verschillen te voorkomen. Bij het wijzigen van de bon verschijnt een pop-up melding.

- Zorg dat er altijd een verschil is, tussen het totaal bedrag en het afgesproken 'vast bedrag excl. BTW', anders komt de 0 factuur op de open posten debiteuren.
- Bij de Werkorder details wordt het vast bedrag (handhaven) nog niet getoond, als deze nog niet vrijgegeven is.

#### Vanuit Werkbon App

Hoe zit de werkbon eruit, vanuit de Werkbon App?

Nadat de werkbon afgehandeld en getekend is, wordt de volgende tekst weergegeven op de werkbon:

In de dossier map wordt de werkbon en eventuele formulieren opgeslagen.

---
## FAQ Service / werkplaats

In dit hoofdstuk staan de meestgestelde vragen over de Service en Werkorder(plaats) module.

#### Servicemeldingen

- Servicemelding aanmaken vanuit keuringsherinnering
- Hoe, wat m.b.t. takenlijst i.c.m. Werkbon App nieuw vanaf versie 3.02
- Hoe kan ik de servicemeldingen zien, waarop nog artikelen staan die niet geleverd zijn? Het kan voorkomen dat een servicemelding niet afgewerkt kan worden, omdat er nog (op de werkorder) artikelen op staan met geleverd aantal 0. Om deze meldingen te zien, doorloopt u de volgende stappen: 1. Selecteren servicemeldingen (SS). 2. Kies bij status wacht op afh. (=afhankelijkheid). 3. Kies voor de knop Selecteren. De servicemeldingen met werkorders waarbij artikelen staan, die nog geleverd moeten worden, verschijnen op het scherm.

#### Overige

- Hoe druk ik de gescande artikelen (niet) af?
- Hoe mail ik de uren naar een personeelslid?
- Hoe pas ik de autorisatie aan voor het touchscreen, zodat de monteur een werkorder kan wijzigen?
- Hoe wijzig ik het uurtarief?

#### Werkorders

- FAQ Planbord werkorders
- Hoe geef ik op mijn (winter)beurt xx% korting?
- Hoe komt het dat artikelen 'verdwijnen' van de werkorders i.s.m. de Werkbon App?
- Hoe werkt de bestelkoppeling (OCI) i.c.m. werkorders? nieuw
- Hoe werkt picken / gereserveerd bij werkorders? nieuw
- Hoe werkt een vooruit- of aanbetaling bij een verkoop- of werkorder? nieuw
- Hoe wijzig ik de relatie van een offerte of werkorder?
- Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties?

Hoe krijg ik een artikel, dat ik demonteer, terug op voorraad bij een werkorder?

Voer een negatief aantal benodigd in en een negatief aantal geleverd.

- Bij het Vrijgeven komt het aantal weer op voorraad.

Opmerking: Het is niet mogelijk om een negatief aantal te picken.

Hoe kan ik ook de toekomstige werkorders te zien?

Bij Selecteren werkorders (WS) is het mogelijk om in te stellen, om X dagen vooruit de werkorders te zien, vanaf versie 3.19.

- Bij Instellingen werkorders (BIW) vul t/m werkorder datum dagen in.
- | T/m werkorder datum + .. dagen | Het aantal dagen dat bij het veld datum t/m wordt opgeteld in Selecteren werkorders (WS), vanaf versie 3.19.Bij bijv. 7 dagen, zijn de werkorders van volgende week zichtbaar.- 0 = Standaard | | --- | --- |

Hoe stel ik een toeslag in voor klein materiaal op de werkorder?

- Het is mogelijk om klein materiaal automatisch te laten doorbelasten voor de werkorder of materiaal of uren bedrag.
- Hiervoor moet een artikelcode voor de doorbelasting toegevoegd worden.NB Dit artikel moet op voorraad bijhouden Nee staan.
- Voor een voorbeeld zie de bovenstaande (laatste) vraag.

|  | Het volgend is ingesteld bij Instellingen werkorders, tabblad Beheer: |
| --- | --- |

| Automatisch doorbelasten klein materiaal | Optie voor het automatisch doorbelasten kleinmateriaal (interne- of extern werkorder):- 0,00 % standaard (niets doorbelast)- > 0,00 t/m max. 9,99%Optie om door te klein materiaal door te belasten:- Werkorder (Materiaal + Uren standaard)- Materiaal- UrenDe artikelcode bij doorbelasten gevuld zijn, zie Hoe ziet mijn werkorder bon eruit, na controle / vrijgave wat zijn de opties? |
| --- | --- |

| Artikelcode bij doorbelasting | De artikelcode van het kleinmateriaal dat doorbelast, a.h.v. de instellingen, wordt aan de klant. |
| --- | --- |

Hoe krijg ik een melding als ik een dubbel servicenummer gebruik?

Bij Selecteren werkorders (WS) is het mogelijk om in te stellen, als er een dubbel servicenummer ingegeven wordt, vanaf versie 3.19.

- Bij Instellingen werkorders (BIW) vul t/m werkorder datum dagen in.
- | Melding dubbel servicenummer | Optie voor een melding bij een dubbel servicenummer in Nieuwe werkorder aanmaken, vanaf versie 3.19.- Nee (standaard) - Ja Voor de motorbranche is dit standaard ja. Het scherm Dubbele werkorder voor machine verschijnt. | | --- | --- |

Hoe stel ik de e-mail werk gereed melding in voor een werkorder?

Om de e-mail gereed melding in te stellen, doorloopt u de volgende stappen:

1. Bij Instellingen documentbeheer (BIE), tabblad Werkorder e.a. ingesteld zijn o.a. de Mailbody. Opmerking: Aandachtspunt: Als je geen pop up krijgt of de mail wordt niet verstuurd, dan krijg je geen melding! Mogelijk is er geen mailadres bij de klant ingesteld bij tab E-document, Werkorder gereed.
2. OBA71 layout W is de layout die gebruikt wordt voor email werk gereed.

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Kan ik de werkorder ook volledig afdrukken?

Ja dit is mogelijk. Dit is handig als de werkorder over meerdere dagen verspreid is / duurt.

Bij Instellingen werkorders, tabblad Werkbon App kan dit bij het volgende veld ingesteld worden:

- | Werkorder volledig printen | Optie om de werkorder OBA71 / werkbon OBH71 volledig af te drukken, i.p.v. per planrecord (bij werk over meerdere dagen bij einde werk): - Nee (standaard) - Ja . | | --- | --- |

Kan ik ook op een werkorder de elementcodes van een machine afdrukken?

Ja dat is mogelijk, bijv. in twee kolommen,

- Alleen elementcodes met formaat tekst worden hierbij niet afgedrukt.

Neem hiervoor contact op met de helpdesk om dit in te stellen.

Waarom krijg ik de pop-up: Let op: Prijsniveau wordt gewijzigd?

Bij Invoeren/wijzigen werkorders kan onderstaande melding voorkomen.

- Bij een (nieuwe) werkorder krijg ik deze pop-up melding:
- Dit gebeurt als de type werkorder wijzigt van Extern naar Intern of andersom. Bij intern worden meestal de kostprijzen berekend.

Opmerking: Er zijn ook bedrijven die interne werkorders berekenen met verkoopprijzen. Dit geldt bijv. als van iedere afdeling het resultaat/winst bepaald wordt.

- Service

- FAQ Werkbon App

---
## Hoe, wat kan ik ... m.b.t. de voorraadaansluiting / artikelprijsmutaties?

**Hoe, wat kan ik ... m.b.t. de voorraadaansluiting / artikelprijsmutaties? In dit hoofdstuk staan de meest gestelde vragen over de voorraadaansluiting, artikelprijsmutaties en Herwaarderen voorraadwaarde. ### Doelstelling Het doel van de voorraadaansluiting is: - Na herwaardering is er altijd een complete financiële aansluiting. - Een exacte specificatie van de herwaardering op artikel/transactie niveau ter onderbouwing. - Een audit trail of traceerbaarheid mogelijkheid van tussentijdse mutaties, om vast te stellen wie, wanneer, welke wijzigingen door heeft gevoerd. - Consistentie bij een multi-administratie en met een gedeeld artikelbestand. - Mogelijkheid om de financiële voorraadlijst met terugwerkende kracht uit te draaien. Opmerking: Deze voorraadaansluiting kan op elk moment verwerkt worden. ### Audit trail Elke mutaties die betrekking heeft op een artikelprijswijziging, van een verkoop-, verrekenprijs of een artikelgroep wordt gelogd in het audit trail bestand. In de audit trail log kunnen de artikel/prijsmutaties bekeken worden: - Selecteren audit trail artikel mutaties - Audit trail (artikel) mutaties rapportages Waar kan ik de artikelprijsmutaties bekijken? Om van een artikel de mutaties te bekijken, doorloopt u de volgende stappen: 1. Ga naar Opvragen artikelen (AO) of F7. 2. Ga naar tabblad Mutaties. 3. Selecteer bij mutatiesoort optie Prijswijziging. #### Artikelmutaties Om artikelmutaties af te drukken, doorloopt u de volgende stappen: 1. Ga naar Overzicht voorraadmutaties (ALM). 2. Selecteer bij mutatiesoort Prijswijzigingen. 3. Kies voor de knop Afdrukken. Het overzicht verschijnt op het scherm. Waar worden de in- en verkoopprijzen allemaal gelogd in Powerall Connect? Deze prijzen worden in de audit trail logt in de volgende programma's: - Onderhoud artikelen (ABA) - Verwerk prijswijzigingen (AGV) - Verwerk artikel of serie verwijzingen (ABW) - Artikel verwijzing aanleggen (ABV) - Boeken goederenontvangst (AVO) ### Herwaardering Een herwaardering gebeurt bij een wijziging van de: - verrekenprijs / inkoopprijs - of de artikelgroep. NB bij een Belgische voorraadboeking wordt een extra boeking m.b.t. de voorraad mutatie rekening gebruikt, naast de voorraad nieuw rekening. De prijswaardering van de voorraad gebeurt a.d.h.v. ingestelde waarderingsmethodiek zie Instellingen. Belangrijk: De automatische (grootboek)boeking worden Periodiek uitgevoerd (niet meer per transactie), als bijv. een verrekenprijs of artikelgroep wordt aangepast. Opmerking: • Bij Instellingen artikelen, tabblad Koppelingen, moet Gebruik voorraad en Grootboekrekeningen beide Ja zijn.• De voorraad wordt alleen berekend bij artikelen met soort artikel 'Normaal' of 'Machineverkoop' en niet bij 'Vervangen' en 'Tekst' artikelen. Hoe verwerk ik handmatig** de herwaardering?

Periodiek (dagelijks, wekelijks of maandelijks) kan een herwaardering uitgevoerd worden.

Om dit handmatig te doen, doorloopt u de volgende stappen:

1. Ga naar Herwaarderen voorraadwaarde (GPV).
2. Kies voor de knop Verwerken.
3. Na het verwerken verschijnt een pop-up met hoeveel mutaties er verwerkt zijn, of dat er geen herwaarderingsmutaties aangemaakt zijn.
4. Kies voor de knop OK.

De herwaardering is verwerkt.

Wat doe ik bij de melding 'Standaard dagboek voor boekingen voorraad is niet ingevuld'?

Bij herwaarderen moet het voorraad dagboek ingevuld zijn.

- Vul het  in bij Instellingen artikelen, tabblad Koppelingen.

Hoe verwerk ik **automatische** de herwaardering?

Bij een financiële periodewissel kan de herwaardering verwerkt worden, wijzig hiervoor eenmalig de instelling Automatisch herwaarderen bij periodewissel naar Ja.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Instellingen financieel (BIG).
2. Ga naar tabblad Grootboek.
3. Kies voor de knop Wijzig.
4. Selecteer Ja bij Automatisch herwaarderen bij periodewissel.
5. Kies voor de knop Opslaan.

Bij een periodewissel financieel worden de prijs wijzigen automatisch verwerkt.

Opmerking: Standaard staat deze waarde op ja. Bij Herwaarderen voorraadwaarde wordt vermeld of dit automatisch ingesteld is of niet.

Hoe ziet de journaalpost van een herwaardering eruit?

Afhankelijk van de gebruikte grootboeknummers ziet de journaalpost er als volgt uit:

1. Ga naar Opvragen grootboekmutaties (GO).
2. Selecteer de grootboekrekening van de herwaardering.
3. Vul eventueel een periode in.
4. Hierbij een voorbeeld van een herwaardering:

Of

1. Ga naar Overzicht voorraadmutaties (ALM).
2. Selecteer bij mutatiesoort herwaardering.
3. Vul eventueel een boekstuknummer of mutatiedatum in.
4. Kies voor de knop Afdrukken.
5. Een gedetailleerd verslag van deze herwaardering wordt weergegeven.

1. Hierbij een voorbeeld van een artikelgroepswijziging (van 1 naar 86 en een prijswijziging van 5 naar 7,50):

Hoe komt het dat ik de journaalposten van de herwaardering nog niet zie?

De artikelmutaties moeten nog verwerkt worden. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Verwerken artikelmutaties (AVF).
2. Selecteer bij mutatiesoort herwaardering.

De mutaties zijn verwerkt en de grootboek boeking is aangemaakt.

Op welk grootboeknummer wordt de herwaardering geboekt?

De herwaardering wordt geboekt op het grootboeknummer van de artikelgroep van het artikel.

1. Ga naar Opvragen artikelen (AO) of F7.
2. Kijk welke artikelgroep bij het artikel behoort.

1. Ga naar Onderhoud artikelgroepen (ABG).
2. Geef de betreffende artikelgroep op.
3. Ga tabblad Voorraad.
4. Bij Herwaardering staat het grootboeknummer. (In bovenstaand geval 9100).

Hoe werkt de herwaardering bij een gedeelde artikeladministratie?

Bij een gedeelde artikelen worden alleen die magazijnen hergewaardeerd, waarvan de administratie de eigenaar is.

- De herwaardering moet per administratie verwerkt worden.

Wat doe ik bij de melding 'Standaard dagboek voor boekingen voorraad is niet ingevuld'?

Bij herwaarderen moet het voorraad dagboek ingevuld zijn.

- Vul het  in bij Instellingen artikelen, tabblad Koppelingen.

## Instellingen

Welke instellingen zijn van invloed hierop?

Bij Instellingen financieel, (BIG)

Bij tabblad Grootboek:

- | Automatisch herwaarderen bij periodewissel | Optie voor het automatisch herwaarderen bij een periodewissel financieel:- Nee- Ja, bij de Periodewissel financieel (GPP) wordt de artikelvoorraad ook automatisch hergewaardeerd.Bij Herwaarderen voorraadwaarde (GPV) wordt vermeld, of dit automatisch is ingesteld of niet. Ja (standaard) bij update, als klant Instellingen artikelen 'Gebruik voorraad' en 'Grootboekrekeningen' op Ja staan. | | --- | --- |

Bij Instellingen artikelen, (BIA)

Tabblad Printvoorkeuren:

- | Voorraadwaardelijst prijs | Optie voor welke prijs of waarde er gebruikt wordt bij de voorraadwaarde lijst:- Verrekenprijs (standaard) - Verkoopprijs - Voorraadwaarde Bij de Voorraadwaardelijst (ALW) wordt deze prijs/waarde overgenomen in veld Prijs voorraadwaarde en weergegeven op het overzicht. | | --- | --- |

Afhankelijk van bovengenoemde instelling, is het mogelijk om de financiële voorraadwaarde af te drukken. Hierdoor is er aansluiting met het grootboek.

Tabblad Voorraad/bestelmethodiek

- | Kostprijs bij doorboeken orders | Optie voor welke kostprijs er gebruikt wordt, bij de nacalculatie van bonnen/orders en de prijs waarbij een bon/order wordt doorgeboekt:- Actueel (standaard) - Invoer, de kostprijs die op het moment van invoer op een bon/order gebruikt wordt. | | --- | --- | Voor de voorraadwaardering:

- | Waarderings methodiek | Optie voor het waardering van de artikel voorraad:- Vaste VerrekenPrijs (standaard, VVP), alleen bij deze optie kan bij het updaten van de catalogi de verrekenprijs geüpdatet worden.NB De prijs is datum afhankelijk, zodat een aanpassing van de VVP zorgt voor een herwaardering van de voorraad.- Laatste InkoopPrijs (LIP)- Gemiddelde InkoopPrijs (GIP), zie Hoe werkt de Gemiddelde Inkoop Prijs (GIP) waardering?Let op! Wijzig alleen de waarderingsmethodiek in overleg met uw accountant. Wijziging moet door een consultant uitgevoerd worden. | | --- | --- |

Bij artikel mutatietype of soort mutatie worden hierbij gebruikt:

- Herwaardering
- Prijswijzigingen

Hoe controleer ik de voorraadwaarde controleren (na herwaardering)?

Om de voorraad te controleren, doorloopt u de volgende stappen:

1. Ga naar Voorraadwaardelijst (ALW).
2. Bij Prijsvoorraadwaarde selecteer Voorraadwaarde.
3. Kies voor de knop Afdrukken. Noteer het totaal.
4. Ga terug.
5. Bij Prijsvoorraadwaarde selecteer daarna Verrekenprijs op.
6. Kies voor de knop Afdrukken. Noteer het totaal.

De lijsttotalen moeten overeenkomen.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

---
## Van welke leveranciers is een EDI koppeling beschikbaar?

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

Van de volgende leveranciers is een EDI-koppeling of Digitale order beschikbaar in Powerall Connect:

| Omschrijving | Website (login) | Digitale order | EDI | F7 / EPC | Opmerking *=bijgewerkt |
| --- | --- | --- | --- | --- | --- |
| AGCO Mechan (AGC) | mechanshop.nl | Ja | - | EPC |  |
| Agroparts (AP) EVAX |  |  | Ja |  |  |
| Agroparts (AP) / Homburg |  |  | Ja |  |  |
| AVA | ava-cooling.com |  | Ja |  |  |
| Bepco (BEP) | bepcoparts.com | Ja | - | Ja |  |
| Bosta (BO) | bosta.nl |  | Ja |  | apr 2023 * |
| Brinkman (BR) | royalbrinkman.nl |  | Ja |  |  |
| Bulthuis | bulthuis.eu | Ja | - | Ja / EPC |  |
| Case NewHolland (CNH) | portal.cnh.com | Ja | - | Ja / EPC |  |
| Claas (CL) | claas.com |  | Ja |  |  |
| Combilift Ierland | combilift.com |  | Ja |  |  |
| DAF (DAF) |  | Ja |  |  |  |
| Deutz-Fahr (DF) | agricenter.com |  | Ja |  |  |
| DeLaval (DL) | delaval.com |  | Ja |  |  |
| De Lille (Merlo) | de lille (merlo) |  | Ja |  | sep 2022 |
| De Wulf (Belgie) | dewulf (BE) |  | Ja |  | Vanaf jan 2025 |
| Dulevo International (DI) |  |  | Ja |  |  |
| Duport | duport.nl/onderdelen_service | Ja | - | Ja |  |
| Eriks (EK) | eriks.nl |  | Ja |  |  |
| Fabory (FAB) | fabory.com |  | Ja |  |  |
| Fluiconnecto Benelux (FB / FLW) | fluiconnecto.nl |  | Ja |  |  |
| Festo (FO) | festo.com |  | Ja |  |  |
| Royal de Boer (GEA) | royal de boer |  | Ja | Ja |  |
| Gallager (GL) |  |  | Ja |  |  |
| Granit (GR) | granit-parts.nl | Ja |  | Ja |  |
| Grimme | grimme.com |  | Ja |  | jan 2023 * |
| Havam van Heck Harrems (HAV) |  |  | Ja |  |  |
| Hikoki (HIK) | hikoki-powertools |  | Ja |  |  |
| Hillaire van der Haeghe (HH) | hillaire van der haeghe |  | Ja |  |  |
| Jean Heybroek (HEY) | jeanheybroek.com |  | Ja |  |  |
| Hocoparts webshop (HO1) | hocoparts.com |  | Ja |  |  |
| Hofman Animal Care (HOF) | hofmananimalcare.nl |  | Ja |  |  |
| Homburg (HB) | homburg-holland.com |  | Ja |  |  |
| Honda (HO) | ecom.honda-eu.com |  | Ja |  |  |
| Husqvarna Webshop (HUW) |  |  | Ja |  |  |
| Indi (IN) | indi.nl |  | Ja |  |  |
| JCB (JCB) hoofddealers | jcb-bene.com | Ja | - | Ja |  |
| JCB subdealers |  |  | Ja |  | sep 2022 |
| John Deere (JD) | partscatalog.deere.com | Ja | Ja | Ja | Digitale order sep 2023 |
| John Deere Webshop (JDW) |  |  | Ja |  |  |
| Karcher (bestelsoftware) (KA) |  |  | Ja |  |  |
| Karcher (Belgie) KAR |  |  | Ja |  |  |
| Kellox |  | Ja | - |  |  |
| Kubota webshop (KB) |  |  | Ja |  |  |
| Kooijmans (KO) | kooijmansschijndel.nl |  | Ja |  | sep 2022 |
| Kramp / Webshop (KR/KRW) | kramp.com/shop-nl | Ja | - | Ja / EPC |  |
| KTM (KTM) | ktm-shop.nl |  | Ja |  |  |
| Kubota (KU) |  |  | Ja |  |  |
| Kverneland (KV) |  |  | Ja |  |  |
| Kverneland webshop (KVW) | kvgportal.com |  | Ja |  |  |
| Lasaulec (LA) |  |  | Ja |  |  |
| Leeuwtechniek (LT) |  |  | Ja |  |  |
| Manitou |  |  | Ja |  |  |
| Mechan Groep Webshop (MGW) | mechanshop.nl | Ja | Ja |  | juli 2022 |
| Motor Cycle Storehouse (MCS) |  |  | Ja |  |  |
| McHale (MH) |  |  | Ja |  |  |
| Middelwijk (MID) |  |  | Ja |  | aug 2022 |
| Nilfisk (NIL) | nilfisk.com |  | Ja |  |  |
| Granit Parts (MT/MTW) | granit-parts.nl | Ja | Ja | Ja / EPC | Vanaf 2022 |
| Nimag-Suzuki dealerportal (NIM) |  | Ja | - |  |  |
| NRF | webshop.nrf.eu |  | Ja |  |  |
| Oosterberg | oosterberg.nl | Ja | Ja | Ja | juli 2025 |
| Parts Direct (PD) |  |  | Ja |  |  |
| Parts Europe (PE) | partseurope.eu |  | Ja |  |  |
| Pols | Parts.pols/nl | Ja | Ja |  |  |
| Royal Reesink (REE) | parts.reesinkagri.com | Ja | Ja |  |  |
| Revaho (REH) | revaho.nl |  | Ja |  |  |
| Same (SAM) |  |  | Ja |  |  |
| SDF (SDF) | extranetsdf.com |  | Ja | Ja |  |
| Shell (SHL) | markethub.shell.com |  | Ja |  | april 2023 * |
| Shoei (SHO) |  |  | Ja |  |  |
| Sparex (SPA) | nl.sparex.com | Ja | - | Ja |  |
| Schmitter (ST) |  |  | Ja |  |  |
| Stierman De Leeuw | stiermandeleeuw.nl | Ja | - | Ja | maa 2021 |
| Stihl (STL) | stihl.com | Ja | Ja |  | mei 2024 * |
| Toro Belgie (TOB) | commerce.toro.com |  | Ja |  |  |
| Toro (TOR / TOW) |  |  | Ja |  |  |
| Transferro webshop (TR) | transferro.com |  | Ja |  |  |
| Technische Unie (TU) | technischeunie.nl | Ja | - | Ja |  |
| TVH (TVH) | tvh.com | Ja | - | Ja |  |
| VEEservice IDAC (Drunen) | veeserviceidac.nl |  | Ja |  |  |
| Wabco | wabco-customercentre.com |  | Ja |  |  |
| Westfalia (WF) |  |  | Ja |  |  |
| Wijlhuizen (WHN) |  | Ja |  | Ja |  |
| Wildkamp (WI) | wildkamp.nl |  | Ja |  |  |
| Wolf-Garten Nederland (WGN) |  |  | Ja |  |  |
| Yamaha (YAM) | my.yamaha-motor.eu |  | Ja | EPC |  |
| Zevij-Necomij (ZVN) | zevij-necomij.com |  | Ja |  | feb 2023 |
| Zuidberg staalservice (ZUS) |  |  | Ja |  |  |

Voor meer informatie over:

- EDI / Digitale ordersEDI / Digitale inkooporder aanmaken

F7
- zie Artikelen, online info leverancier

EPC
- EPC bestand importeren
- FAQ Elektronische Part Catalogus (EPC)

#### FAQ

Wat is het verschil tussen een EDI en een Digitale order?

Een digitale order is de opvolger van de EDI. Een digitale order heeft meer mogelijkheden en gebruikersvriendelijker en technisch beter.

- Bij een digitale order wordt geen EDI meer gebruikt.

Welke Powerall Connect module is hiervoor nodig?

Het volgende module is nodig voor:

- De EDI-koppeling de module Inkooporders EDI.
- De EPC-koppeling de module Artikel Parts Locator.

---
## Welke leveranciers integraties zijn er?

De volgende leveranciersintegraties zijn aanwezig in Powerall Connect:

- Artikelinformatie / PartsInquiry
- Voorraad upload / Partslocator
- Facturen ophalen / InvoiceInquiry
- Digitale order / DigitalOrder
- Pakbonnen ophalen / Dispatch note
- OCI / Bestelkoppeling

Het hangt van de leverancier af, of deze al of niet gebruikt kunnen worden.

| Leverancier | Afkorting |
| --- | --- |
| Autema | AUTE |
| BartParts | BRT |
| Beneparts | BENEP |
| Bihr | BIHR |
| Bepco | BEP |
| Bromach | BROMA |
| Bulthuis | BHS |
| Claas |  |
| CNH | CNH |
| DAF | DAF |
| Demo / Powerall Connect | DEMO |
| Granit | GR |
| Grimme | GI |
| Homburg | HOMB |
| IPS / NewHolland |  |
| John Deere | JD |
| Kellox | KLX |
| Kramp | KR |
| NIMAG | NIM |
| Oosterberg | OOSTB |
| Pols Zuidland | POLS |
| Reesink | RR |
| Same Deutz-Fahr (SDF) | SDF |
| Sparex / SP | SP |
| Stierman De Leeuw | SDL |
| Stihl | STIHL |
| Technische Unie | TU |
| TVH | TVH |
| Wijlhuizen | WHN |

- #### Parts inquiry Artikelen, online info leverancier / Parts inquiry

#### Digital order

- Van welke leveranciers is een EDI koppeling beschikbaar?

#### Invoice inquiry

- Hoe haal ik mijn nieuwe inkoopfacturen op?

Overige

- Integraties EPC bestand importeren
- Export productregistratie Stihl
- KrampHoe werkt partnershop order doorfacturering (Kramp / Granit)?
- Kramp catalogus update

---
## Welke barcodes plak ik op mijn tablet?

Hierbij enkele belangrijke barcodes om op de tablet te plakken, bij gebruik van de Opticon OPN2006 scanner, voor de Werkbon App.

Onderstaand bestand kan gebruikt worden om de barcode labels af te drukken.

- Open het bestand Barcodes.om.op.de.tablet.te.plakken.PDF.

#### Werkbon App barcode labels:

- Opnieuw koppelen
- Data naar App verzenden

---
## FAQ&#160;Werkbon App

# FAQ Werkbon App

In dit hoofdstuk staan de meestgestelde vragen over de Werkbon App.

- Hoe maak ik een nieuwe Werkbon App gebruiker aan?
- Welke barcodes plak ik op mijn tablet?
- Handleiding 1, Opticon OPN2006 scanner koppelen met Android
- Handleiding 2, Opticon OPN2006 scanner koppelen met de Werkbon App
- Handleiding 3, Opticon OPN2006 scanner troubleshooting met de Werkbon App

Opmerking: De Werkbon App kan alleen gebruikt worden op toestellen met Android 6 of hoger, voor meer informatie, zie Android-versies .

Top FAQ's

*Welke machine transacties* worden weergegeven op tabblad Transacties?

Op het tabblad Transacties worden de transacties / historie weergegeven.

- De werkorder transacties van de laatste 2 jaar of de laatste 10 transacties worden getoond.
- Zie ook Registratie en Orderdetails

*Wat gebeurt er als ik artikelen gescand heb met de bluetooth scanner, als mijn apparaat vergrendeld is? De artikelen die gescand zijn, worden getoond zodra de app weer geopend wordt. Meldingen Wat doe ik bij de melding: 'Gebruik app niet toegestaan*'?

De ingelogde gebruiker is in Powerall Connect nog niet geautoriseerd om de Werkbon App te gebruikenof de gebruiker is niet goed gekoppeld aan de persoon of personeelscode.

Controle gebruiker

Om dit te doen, doorloopt u de volgende stappen:

1. Ga in het systeemmenu naar Systeembeheer > Onderhoud gebruikers.
2. Geef het gebruikersnummer in.
3. Controleer of bij de betreffende administratie het juiste personeelscode staat (in de kolom Pers.).
4. Personeelscode 2 is aan deze gebruiker gekoppeld, zie

#### Controle autorisatie Werkbon App.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Onderhoud personeelscodes (BTP).
2. Geef de personeelscode in.
3. Ga naar tabblad Werkbon app.
4. Zet Gebruik werkbon app op Ja.
5. Kies voor de knop Opslaan.

Log opnieuw in.

*Wat doe ik bij de melding 'Webservice is niet bereikbaar.* ...'?

De melding Webservice is niet bereikbaar. Controleer uw internetverbinding.' verschijnt als er geen verbinding is met het Powerall Connect.

- Controleer of bij Service Host de status actief is.
- Controleer de WiFi of internetverbinding.

*Wat doe ik bij de melding 'Geen internetverbinding.* ...'?

De melding Geen internetverbinding. Planning kan niet worden bijgewerkt' verschijnt als er geen (wifi) verbinding is met het internet.

- Controleer de WiFi of internetverbinding.

*Wat doe ik bij de melding: 'Powerall Werkbon is gestopt*', bij het toevoegen?

Bij het toevoegen van een nieuwe servicemelding is het mogelijk dat je deze melding krijg.

1. Ga naar Instellingen (linksboven: ).
2. Blader naar beneden naar Offline-data (referentiedata).
3. Klik hierop om bij te werken. Offline data wordt opgehaald.

Zojuist ververst, verschijnt.

Als fout blijf terugkomen, neem contact op met de helpdesk.

*Wat doe ik bij de melding: 'Powerall Connect WerkbonApp is gestopt*', bij opstarten?

Deze melding kan bij het opstarten van de Powerall Werkbon app verschijnen.

- Neem contact op met de helpdesk.

*Hoe komt het dat een (gedeeltelijk) gereed gemelde werkorder op Werkbon App, niet binnen komt? Als deze servicemelding of werkorder openstaat, is het niet mogelijk om de status bij te werken. - Bij een volgende gereedmelding, wordt de servicemelding of werkorder, weer bijgewerkt. Werkbon App en serviceproces Klik hier voor meer informatie over het gebruik van de Werkbon App voor buitendienst met planner: In onderstaand proces wordt weergegeven welke stappen doorlopen worden, wanneer een planner een servicemelding inplant voor een (buitendienst) monteur, zie ook Werkverzoek . Werkbon App proces (met planner) De groene blokken geven de stappen weer die door de planner gedaan worden. In deze situatie is het proces zo ingesteld, dat de monteur op de Werkbon App alleen werkorders te zien krijgt die de status 'Gepland' hebben. PDF formulier Hoe kan ik een invulbaar PDF formulier maken? Het is mogelijk om een PDF formulier zelf (online) te maken. - Voor meer info zie pdfescape.com.Om dit direct te starten: pdfescape.com/open. Hoe ziet bijv. z'n PDF invulformulier eruit? Hierbij enkele voorbeelden van PDF formulier: - APK-formulier-basis.pdf - PDF.formulier.pdf Hoe voeg ik een invulformulier toe in Powerall Connect, voor de Werkbon App? Er zijn twee soort invul formulieren die op de Werkbon App gebruikt worden: 1. PDF invulformulier. zie Onderhoud PDF formulieren (per werkorder) (type Normaal) 2. Keuringsformulier zie Keuringen instellen (type Keuring). - Waar kan ik dit formulier zien in Powerall Connect? Dit formulier is zichtbaar bij het Dossier Werkbon App Hoe zorg ik er voor dat een PDF formulier zichtbaar is op de Werkbon App? De formulieren zijn gekoppeld aan de WO / Servicemelding d.m.v. keuring. - Op de Werkbon App kan deze ingevuld worden, er verschijnt dan de vraag of PDF formulier is ingevuld? - Zie Werkbon App Formulieren werkorder. Belangrijk: Voor PDF invulformulieren is de module keuringen nodig, om dit werkend te krijgen. Diverse Hoe kan ik de afgewerkte werkorders, die gereed/afgemeld zijn, zien voor verdere verwerking: Bij de Instellingen werkorders, tabblad Werkbon App de selectiecode bij Werk Gereed op H gezet. - Zodra op de tablet “werk gereed” wordt gedaan, dan komt bij de werkorder de H te staan. Op deze selectiecode kan dan geselecteerd worden. Nieuw opgevoerde artikelen (ook diverse bestaande artikelen niet) kunnen niet door tablet scanner gelezen worden. - Op te lossen door Referentie data opnieuw op te halen, bij Instellingen Werkbon App. Kan bv Vekoma opvoeren met pakbon nr dat dit als onderdeel gescand wordt en er dan later een bedrag aan gekoppeld wordt? - Als interne notitie registreren met het Pakbon nr. Werkorders als afgewerkt gemeld, kun je die ook nog weer activeren en een aanvullend klusje afronden? - Ja, dit kan maar dan moeten ze opnieuw ingepland worden. Uitgevoerd werk (als test geprobeerd) wijzigen als werk/werkdag is afgesloten kan dat? - Ja, door opnieuw in te plannen, wellicht is het dan sneller om de werkorder aan te passen in Powerall. Bestaat de mogelijkheid dat de orderbevestiging van bv. Kramp/ Granit in 1 keer omgezet wordt in artikel stickers zonder dat hiervoor het automatisch bestellen wordt gebruikt? - Ja, printen labels bij Boeken goederenontvangst (AVO) aangezet. Hoe sluit ik de werkorder af die alleen met service melding is gemaakt en op papier geprint wordt? . Dit gebeurde met omzetten van personeelscode 26 naar 99 (aangemerkt als “collega Werk gereed”. Als we overschakelen naar de tablet, staan deze er nog in als gepland. - Werkorder wijzigen en selectiecode X geven, zodat deze vrijgeven kan worden. Bij 'Invoeren/wijzigen werkorders' staat de kolom “Benodigd”. Waarvoor is dit bedoeld, wij vergeten soms het aantal in te voeren. - Is met name van belang als je met inkooporders werkt, dit werkt goed mits het magazijn op orde is. Indien nodig kan deze instelling uitgezet worden. Werkbon App Hoe leeg ik de app / Werkbon App chache? Om dit te doen, doorloopt u de volgende stappen: 1. Druk op de betreffende app > App-info. 2. Druk op Opslag en cache. 3. Druk op Cache wissen. 4. De Cache is gewist 5. Bij Opslag wissen: Bevestig de melding: "Alle gegevens van deze applicatie worden definitief gewist." Kies voor de knop OK. (De cache kan ook geleegd worden). Gegevens zijn gewist. Opmerking: Het legen van de cache wordt ook gebruikt om als bedrijf uit te loggen. Belangrijk: Bij Gegevens wissen moeten de bedrijfs- en login gegevens moeten opnieuw opgegeven worden. Hoe sluit ik de Werkbon App af, en start deze opnieuw? Om de Werkbon App af te sluiten, doorloopt u de volgende stappen: Opmerking: Zorg er wel voor dat alles goed geregistreerd is. 1. Druk onderaan, op de tablet zelf, op App-toets (of Recent-toets) . Een zwarte balk komt omhoog. Daarin staat een overzicht van alle actieve apps. 2. Druk bij Powerall Werkbon op het kruisje X om de app af te sluiten of Kies voor ALLE SLUITEN. De Werkbon App kan weer gestart worden. Hoe komt het dat op mijn werkorder, zoveel artikelen op benodigd 0 en geleverd 0 staan? Bij het inplannen worden de artikelen overgenomen naar de Werkbon App. - Als de artikelen (via de Werkbon App) geleverd worden, dan komen deze op de werkbon te staan. - Als deze artikelen niet geleverd worden via de Werkbon App, dan worden deze artikelen niet afgedrukt op de werkbon. Daarbij komen er in de werkorder regels voor deze artikelen te staan met aantal geleverd en benodigd op 0. Hoe plaats ik een spoed bestelling op de Werkbon App? Het is mogelijk om artikelen met spoed te bestellen. Voor meer info zie: - Spoed bestelling Kan ik met de Werkbon App artikelen inscannen? Ja, dat is mogelijk met een bluetooth (mini) scanner. - Met deze scanner scan je de artikelen die je nodig hebt. - Met bluetooth lees je deze artikelen in de Werkbon App, zie ook: Artikelen scannen Werkbon App Voor meer informatie raadpleeg de verkoopafdeling. Kan ik ook meerder werkorders op de Werkbon App in één keer aftekenen? Ja, dit is mogelijk bij een relatie met meerdere werkorders. - Aftekenen later is alleen mogelijk als er meerdere werkorders van dezelfde relatie aanwezig zijn. Controle / Aftekenen Hierbij is het mogelijk om in de kop de andere werkorders van de relatie te selecteren en te bekijken. Kan ik ook met een andere gebruiker inloggen op de Werkbon App? Ja dat kan in theorie, maar het is niet erg praktisch. - Log met de ene gebruiker uit, - en met de andere gebruiker weer in. Hoe zit het met de besteladvieslijst en de plankvoorraad als artikelen met de Werkbon App gescand worden? 1. De artikelen worden direct verwerkt in de besteladvieslijst. 2. Op het moment dat een artikel in de Werkbon App wordt gebruikt, wordt het aantal gereserveerd in app gevuld en gaat de plankvoorraad naar beneden. Belangrijk: De batchscanning svp direct verwerken omdat er met de artikelen die in de batch van de scanner zitten geen rekening wordt gehouden. Welke situaties ondersteunt de Werkbon App? Onderstaande situaties worden ondersteund door de Werkbon App: - ZZP-er. - Buitendienst met meewerkend voorman. - Buitendienst met planner. - Werkplaats. - Werkplaats in combinatie met buitendienst. Welk licentie model wordt gebruikt? De werking van de Werkbon App is hetzelfde als de Powerall CRM App. - De klant betaalt per gebruiker. Een gebruiker kan onbeperkt op meerdere devices inloggen. - Een gebruiker gebruikt één seat. Opmerking: In het Mijn Powerall / klantenportaal is het aantal gebruikte seats te zien, zie Seats gebruik. Ook kan hier een seat verwijderd worden. Navigeren Hoe navigeer ik het beste met de Werkbon App? 1. Hometoets Met deze knop ga je altijd terug naar het startscherm. 2. Menutoets / optietoets, Druk hierop om te zien welke acties beschikbaar zijn. 3. Terugtoets Hiermee ga je terug naar het vorige scherm of sluit je een dialoogscherm of menu. De terugtoets zit vaak links of rechts van je toestel en lijkt op een omgekeerd pijltje. 4. Multitask-toets Geeft je een overzicht van je recente apps, die je met een swipe kunt afsluiten. De multitask-toets die is te herkennen aan de twee vierkantjes die elkaar gedeeltelijk overlappen. #### Zien / zoeken Waar kan ik de uitgebreide artikelteksten zien op de Werkbon App? De uitgebreide artikelteksten zijn te zien als je een regel aanklikt. - Interne referentie (veld ordergegevens) Waarom verschijnt de werkorder niet in de dagplanning op de Werkbon App? In de dagplanning in de Werkbon App verschijnen ingeplande werkorders. Wanneer deze niet verschijnt kan er het volgende aan de hand zijn: - De werkorder is niet ingepland. De servicemelding heeft dan de status 'te plannen' of 'herplannen'. Alleen servicemeldingen met status 'gepland' of 'wacht op afhankelijkheid' verschijnen in de dagplanning op de Werkbon App. Oplossing: Neem contact op met de planner om de werkorder in te plannen. Het werk is wel ingepland, maar op het planbord nog niet aangemerkt als 'definitief*'. Bij '*definitief*' wordt de werkorder doorgestuurd naar de Werkbon App.
- Oplossing: Neem contact op met de planner om de werkorder definitief in te plannen.

Het werk is wel (definitief) ingepland, maar er is geen verbinding met het internet waardoor de actuele planning niet kan worden opgehaald.
- Oplossing: Maak contact met wifi of met het mobiele internet en herlaad de planning door bovenaan de planning met de vinger naar beneden te schuiven.

De werkorder is voor iemand anders ingepland.
- Oplossing: Neem contact op met de planner om de werkorder aan u toe te wijzen.

De werkorder is wel voor u ingepland, maar u bent als iemand anders ingelogd (bijv. doordat u de tablet van een collega gebruikt).
- Oplossing: Log uit en meld u opnieuw aan met uw eigen  en .

De werkorder is wel ingepland maar op een andere dag.
- Oplossing: Neem contact op met de planner om de werkorder de werkorder op de juiste dag in te plannen.

Welke machine gegevens zie ik?

Bij de machine gegevens/ingave, worden de volgende gegevens getoond op de Werkbon App:

- Omschrijving
- Servicenummer
- Vlootnummer
- Kenteken
- Serienummer

#### Android-versies

Welke Android-versies worden ondersteund door de Werkbon App?

Opmerking: De Werkbon App kan alleen gebruikt worden op toestellen met Android 6 of hoger, voor meer informatie, zie Android-versies .

De ondersteuning voor een bepaalde Android-versie eindigt zodra Google de ondersteuning stopt. Hierbij enkele opmerkingen:

- Google brengt beveiligingsupdates voor sommige oudere Android-versies uit, zodat apparaten met deze verouderde software toch nog veilig gebruikt kunnen worden.
- Na enkele jaren (als er inmiddels nieuwere versies zijn) worden er geen beveiligingsupdates meer uitgebracht. Op dat moment eindigt de support van Google voor beveiligingsupdates en daarmee ook de support voor de Werkbon App.

Klik op de volgende link voor de actuele status van alle Android Versies. Onderstaande bekende versies worden na de einddatums niet meer ondersteund door de Werkbon App:

| Android versie | Einddatum ondersteuning | Opmerking | | --- | --- | --- | | 5.1 of lager | 1 april 2024 | |

#### Installatie

Voor meer info zie:

- Installatie Werkbon App

Hoe installeer ik de Werkbon App?

Om dit te doen, doorloopt u de volgende stappen:

1. Login op de Google Play store.
2. Zoek op Powerall Werkbon.
3. Kies voor de knop Installeer.
4. Start de Werkbon App.
5. Bij pop-up Werkbon App wil telefoongegevens uitwisselen. Kies voor de knop Sta toe.
6. Geef de bedrijfsgegevens op (éénmalig).
7. Geef de login gegevens in.

De Werkbon App kan gebruikt worden.

Hoe wissel ik van taal, bijv. Nederlands naar Engels?

Stel de standaard taal in of voeg een andere taal toe, op het apparaat:

1. Ga naar Instellingen.
2. Druk op Algemeen beheer > Taal.
3. Druk op het + symbool.
4. Voeg taal Engels toe. Vanaf versie 3.29 wordt het Duits ook ondersteund.

Log opnieuw in de Werkbon App.

#### Beveiliging

Hoe is de Werkbon App beveiligd?

De beveiliging van de Werkbon App is als volgt:

- De app is beveiligd met een bedrijfs - en gebruikers account/login.
- De verbinding is beveiligd met het SSL (Secure Sockets Layer) protocol.
- Daarnaast wordt gebruikt gemaakt van een beveiligde Microsoft Azure omgeving.

#### Snapshot / kopie

Hoe maak ik een snapshot van de Werkbon App gegevens?

Het is mogelijk om een snapshot (moment opname/ 'tijdelijke backup' database) te maken.

Belangrijk: Doe dit alleen als een supportmedewerker dit aangeeft!

Om en snapshot te maken, doorloopt u de volgende stappen:

1. Ga naar Instellingen.
2. Druk op Deel app-data. Het scherm Deel app-data verschijnt.
3. Geef de Extra opmerkingen in (optioneel).
4. Kies voor de knop VERZENDEN.

De Werkbon App snapshot (app-data) wordt direct geüpload naar het Dealer Portal en beveiligd opgeslagen met een wachtwoord.

- Het gebruik van de Werkbon App is gekoppeld aan de servicemeldingen module.

Opmerking: Er kan maar 1 App per licentie gebruikt of gekoppeld worden.

Tip: Gebruik de uitvouw knop (boven U bent hier:) om alle vragen uit - of in te vouwen.

- Powerall Werkbon App

---
## Hoe maak ik een nieuwe Werkbon App gebruiker aan?

Om een nieuwe Werkbon App gebruiker aan te maken, doorloopt u de volgende stappen:

#### Stap 1 Toevoegen personeelscode

1. Ga naar Onderhoud personeelscodes (BTP).
2. Kies voor de knop Opvoer.
3. Geef de personeelscode op.
4. Vul gegevens volledig in. Datum in dienst is nodig voor planbord.
5. Afdeling
6. Tabblad Werkbon App Gebruik Werkbon App Ja en Inplannen toestaan van: Aanmaken WO: Ja.
7. Kies voor de knop Opslaan.

De personeelscode voor de gebruiker is aangemaakt.

#### Stap 2 Toevoegen gebruiker

1. Ga in het systeemmenu naar Systeembeheer > Onderhoud gebruikers. Zie ook Nieuwe gebruiker aanmaken.
2. Kies voor de knop Opvoer.
3. Geef de gebruikersgegevens in. Vul de autorisatie A in.
4. Selecteer de juiste administratie.
5. Koppel de personeelscode en de juiste magazijncode aan deze gebruiker.
6. Kies voor de knop Toevoegen.
7. Kies voor de knop Opslaan.

De gebruiker is aangemaakt.

#### Stap 3 Werkbon App ingave bedrijfslogin.

Als je de eerste keer inlogt in de Werkbon App wordt het volgende gevraagd:

1. De bedrijfslogin gegevens.
2. De gebruikerslogin gegevens.

Na invoer van beide logins kan betreffende medewerker aan de slag, zie ook:

- Inloggen Werkbon App.

---
## Hoe komt het dat artikelen 'verdwijnen' van de werkorders i.s.m. de Werkbon App?

Voorwaarde

Dit komt voor als het volgende ingesteld is bij Instellingen werkorders tabblad Werkbon App:

1. Toon voorbereide artikelen is ja
2. Verwerking naar werkorders is per artikelsoort.
3. Tabblad Orderpicken, Gebruik orderpicken is nee.
4. NB er wordt gebruik gemaakt van servicemeldingen.

#### Voorbereide artikelen

Dit zijn artikelen die eerst op de werkorder worden gezet. Daarna wordt deze servicemelding planning 'definitief' zodat ze op de Powerall Werkbon App komen, waar ze verder afgehandeld worden.

#### Optie 2 verwerking: per artikelsoort

Indien werk niet gereed, blijft regel op besteld staan en wordt deze elke keer getoond in de Werkbon App:

- Opmerking: Bij de optie Werk niet gereed op de Werkbon App wordt niet gevraagd wat er met de voorbereidende artikelen moet worden gedaan. * Ze zijn wel inzichtelijk bij Registratie onder kop Materiaal verbruik.

Indien je toch kiest bij Einde werk voor Werk gereed dan wordt de melding getoond: Let op: niet alle benodigde artikelen zijn gebruikt. Deze artikelen worden hierdoor gemarkeerd als ‘niet meer nodig’.

Het resultaat is dat deze artikelen verwijderd worden van de werkorder:

- Op dat moment wordt ook de BTB koppeling uit de regel gehaald. De bestelling blijft bestaan die is immers al verzonden. Daar staat nog steeds dat die benodigd is voor deze werkorder en dat klopt ook, want zo is het origineel besteld.

- Powerall Werkbon App Werk controleren en aftekenen
- Materiaalverbruik

---
## Hoe geef ik op mijn (winter)beurt xx% korting?

#### Situatie

Ik wil op werkorders bij winterbeurten bijv. 10% korting geven.

#### Oplossing

Om kortingen op bepaalde werkorders te geven, moet het volgende ingesteld zijn:

#### Instellingen modules

*Klik hier voor meer informatie over de eenmalige module Instellingen: #### Instellingen artikelen 1. Ga naar Instellingen artikelen (BIA), tabblad Prijsmethodiek. 2. Selecteer bij Type prijsafspraken Ordtypes+ (Staffels). In dit voorbeeld is er ook sprake van staffelkorting m.b.t. het aantal benodigd. | Type prijsafspraken | Optie voor het type prijsafspraken:- Eenvoudig (standaard), alleen regel / staffel 1 wordt gebruikt zie *- Ordertypes - Staffels *- Ordtypes + Staffels ** = Verkoop prijsafspraken | | --- | --- | #### Instellingen werkorders 1. Ga naar Instellingen werkorders (BIW), tabblad Koppelingen. 2. Selecteer bij Prijsafspraken kortingsgroep Ja. #### Onderhoud kortingsgroepen 1. Ga naar Onderhoud kortingsgroepen (APO). 2. Voeg onderstaand kortingsgroep toe: #### Onderhoud werkordersoorten 1. Ga naar Onderhoud werkordersoorten (BTW). 2. Voeg onderstaand werkordersoort toe: 3. Belangrijk: Gebruik bij interne/externe WO mag niet intern zijn #### Onderhoud verkoop prijsafspraken 1. Ga naar Verkoop prijsafspraken (APA). 2. Selecteer kortingsgroep. 3. Geef de (bijv. 4) in. 4. In combinatie met nvt 5. Geef het en in (de regels). Staffel In bovenstaand voorbeeld is er ook sprake van een staffel als aantal >5 of > 10 is. #### Invoeren/wijzigen werkorders Hierbij een voorbeeld van een werkorder, waarbij bovengenoemde korting berekend wordt. 1. Ga naar Selecteren werkorders (WS). 2. Kies voor de knop Nieuw. 3. Voer de werkorder in. 4. Bij werkordersoort kies . 5. Bij de artikelregels verschijnt dan de korting(en). 6. In bovenstaand voorbeeld is er ook sprake van staffelkorting bij regel 2 en 3. #### FAQ Hoe zit het als er nog andere prijsafspraken zijn? De volgende regels gelden bij prijsafspraken, deze (1-3) moet wel ingesteld zijn bij Instellingen werkorder. 1. Handmatig kan altijd de korting aangepast worden. 2. De prijsafspraak per artikel of per klant en artikel.De prijsafspraak per artikelgroep of per klant en groep. De prijsafspraak per klantgroep of per artikel groep.De korting per werkordersoort. Hoe komt het dat ik geen* korting zie bij een artikel op de werkorder?

Controleer het volgende:

- Is de juiste werkordersoort geselecteerd.

Bij de modules moet de prijsafspraken goed ingesteld zijn.

- Voor de juiste module instellingen, zie Instellingen artikelen.
- Controleer verder bovengenoemde instellingen.

Is prijsafspraken werkordersoort i.c.m. hoofd- en subgroep mogelijk?

Ja, dit werkt, mits goed ingesteld. De korting wordt dan toegepast op de artikelen die vallen onder deze hoofd en subgroep.

- Ga naar Instellingen werkorders (BIW), tabblad Koppelingen.
- Controleer / stel het volgende (in):

- Hierbij de overige instellingen, werkordersoort, verkoop prijsafspraak en artikelen het resultaat bij een werkorder:

Opmerking: Neem contact op met onze helpdesk om te inventariseren of dit binnen uw organisatie toepasbaar is. Zij schakelen in overleg de planning in, om een consultant in te plannen.

---
## Veelgestelde vragen FAQ

Hierbij een top '10' van veelgestelde vragen:

1. Hoe maak in een nieuwe bon aan?
2. Hoe, wat m.b.t. de bankkoppeling
3. Lay-out wijzigen
4. Hoe, wat m.b.t. Peppol
5. Barcode scanner nieuwe barcode software update vanaf versie 3.25 en 3.27.
6. Catalogus & leveranciers Download catalogus
7. Tips & Tricks
8. Barcode scanner
9. Wat is nieuw in Powerall Connect? Release notes 3.29 en voor de beta klanten: Release notes 3.30 - Beta
10. Wat is de historie van de online documentatie? De documentatie is voor het laatst bijgewerkt op donderdag 11 juni 2026.

Dit hoofdstuk heeft dezelfde opbouw als het Powerall Connect help menu.

- FAQ Algemeen FAQ Apps

FAQ Powerall Connect installatie, updates e.d.

FAQ Powerall Connect foutmeldingen

- FAQ Relaties FAQ CRM

FAQ Artikelen

- FAQ Voorraad / magazijn
- FAQ Inkoop(orders)

FAQ Machine

- FAQ Financieel

- FAQ Verkoop FAQ Offerte
- FAQ Facturatie
- FAQ Kassa

- FAQ Service / werkplaats

- FAQ Verhuur & contract
- FAQ Projecten

- Welkom bij de Online Help van Powerall Connect
- Powerall Connect help
- Wat is nieuw in Powerall Connect?

---
