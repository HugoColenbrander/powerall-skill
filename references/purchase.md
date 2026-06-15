# Powerall - PURCHASE

## Inkoop

Algemeen processchema inkoopproces

Vanuit deze module kunnen er inkoopoffertes / orders aangemaakt en versturen worden. Vervolgens is het mogelijk om deze aanvragen eenvoudig om te zetten naar een inkooporder.

De volgende onderwerpen worden behandeld:

- Inkooporder
- Koppeling werk-/verkooporder met inkooporder
- Inkooporderregels in backorder
- Inkoop prijsafspraken
- EPC bestand importeren
- Relaties

- Artikelen
- FAQ Inkoop(orders)

- Inkoopfacturen

---
## Goederenmatching

#### Doel

Goederen ontvangst inkoop matching heeft de volgende doelen:

- Afstemmen dat er alleen betaald wordt, wat ook daadwerkelijk geleverd is.
- Aansluiting van de voorraad ontvangsten met de inkopen in de financiële administratie.Goederenmatching 3.0 met dagboek Matching.

Ervoor zorgen dat de prijs waarvoor ingekocht is, ook daadwerkelijk gefactureerd wordt.

De volgende onderwerpen worden behandeld:

- Boeken inkoopfacturen met goederenmatching Matching mogelijkheden

Selecteren matching manco's

Overzicht matching controlelijst

Klik hier voor meer informatie over de functie en het gebruik:

Deze functie heeft twee raakvlakken:

1. De financiële administratie met de inkoopfacturen.
2. Het logistiek gedeelte met de goederen ontvangst.

#### Gebruik

Goederenmatching is een combinatie van goederenontvangst en inkoop. Voor wat betreft de goederenontvangst hebben we dan een keuze uit twee opties :

1. Goederenontvangst wordt uitgevoerd door logistiek, aantallen worden ingeboekt.
2. Goederenontvangst wordt uitgevoerd door logistiek, zowel aantallen als prijzen worden hier ingegeven.

De inkoop wordt vervolgens door de administratie gedaan. De inkoopfactuur wordt ingeboekt, de goederenontvangsten erbij gezocht en vervolgens wordt de factuur goedgekeurd. Eventueel kan administratie de prijzen nog aanpassen. Ontvangst aantallen kunnen niet gewijzigd worden.

### Boeken inkoopfacturen goederenmatching

Om de inkoopfacturen met goederenmatching te boeken, doorloopt u de volgende stappen:

1. De inkopen worden op de gebruikelijke manier geboekt, zie Inkoopfactuur boeken.of Ga naar Selecteren inkoopfacturen (KS). Kies voor de knop Wijzig openpost.of
2. Kies voor de knop Matchen. Wanneer krijg ik de Matching knop te zien? Deze knop is beschikbaar indien bij Instellingen crediteuren, tabblad Beheer de matching (gebruik goederen facturen) aan staat en als de relatie van de leverancier op tabblad Crediteuren goederenmatching op Ja staat.
3. Kies voor de knop Matchen goederen. De eerste regel wordt automatisch ingevuld met het factuurbedrag excl. BTW.
4. Het scherm Goederen ontvangst matching verschijnt. Opmerking: Bij de gekozen leverancier is goederenmatching ja opgegeven.
5. Selecteer één of meerder ontvangstbonnen (voor één factuur, bedragen in eigen valuta).
6. Vervolgens wordt de volgende actie ondernomen (zie processchema): De gehele ontvangst komt overeen en wordt geheel goedgekeurd, de ontvangst kan ook op artikelniveau goedgekeurd worden. Opmerking: Bij een verschil tussen factuur - en ontvangst aantal moet reden verschil geselecteerd worden, zie ook matchings mogelijkheden. Tip: In het bovenste Goederen ontvangst matchings venster kan gesorteerd worden op kolom en gezocht worden (d.m.v. CTR+F op bijv. ontvangstnummer).• Bij ingave van Reden verschil maak gebruik van de pijltjes-naar-beneden/boven-toets om de reden te selecteren.
7. Controle en ingeven van prijzen. Om zo nodig het artikelbestand bij te werken.
8. Transportkosten en orderkosten kunnen apart aangegeven worden.

Kies voor de knop Definitief, om definitief te boeken.Of

- Kies voor de knop Proforma, om weer terug te gaan en de boeking tijdelijk op te slaan.

Het scherm Boeken inkoopfacturen verschijnt weer.

- zie Boeken inkooporder machines

FAQ

Hieronder een uitleg van de velden van scherm  Goederen matching:

| Kop |  |
| --- | --- |

| Ontvangst relatie | De relatiecode van de inkoopfactuur of ontvangst- Standaard is deze gelijk aan de inkoopfactuur. |
| --- | --- |

| Magazijncode | De code van het magazijn. |
| --- | --- |

| Regels: |  |
| --- | --- |

| Ontvangst | Het ontvangstnummer of ontvangstbon. |
| --- | --- |

| Inkoop | Het inkoopnummer. |
| --- | --- |

| Referentie | De betreffende referentie. |
| --- | --- |

| Bedrag | Het (factuur)bedrag. |
| --- | --- |

Als er een ontvangst wordt aangevinkt, verschijnen de artikelen van deze ontvangst in de regels

| Regels: |  |
| --- | --- |

| Rgl. | Het regelnummer, wordt automatisch doorgenummerd. |
| --- | --- |

| Artikelcode | De betreffende artikelcode. |
| --- | --- |

| Grootboek | Selecteer of vul de grootboekrekening in, waarop geboekt moet worden. Bij directe afboeking of bijboeking op een grootboekrekening (in plaats van via een openstaande post). |
| --- | --- |

| Omschrijving | Bij een artikel: de omschrijving van het artikelBij een grootboek: de boekingstekst. |
| --- | --- |

| Ontv. aantal | Het aantal ontvangen. |
| --- | --- |

| Fact. aantal | Het aantal op de (inkoop)factuur. |
| --- | --- |

| Ontv. bedrag | Het bedrag ontvangen. |
| --- | --- |

| Fact. bedrag | Het bedrag op de (inkoop)factuur. |
| --- | --- |

| Fact. bruto | Het factuurbedrag bruto of verkoopprijs (per stuk). |
| --- | --- |

| Kostenplaats | Wilt u de kosten van een totale bon of factuur kunnen doorboeken naar één bepaalde kostenplaats, dan kunt u hier die specifieke kostenplaats ingeven, zie Onderhoud kostenplaatsen.Gebruikt u deze code niet, dan worden de uren en onderdelen naar de standaard ingevoerde grootboekrekeningen doorgeboekt, zonder uitsplitsing van kostenplaats. |
| --- | --- |

| Kostendrager | Dit is de kostendrager. |
| --- | --- |

| Reden verschil | Optie bij reden verschil (ontvangen aantal is ongelijk aan factuuraantal):- Geen- Te veel ontvangen (positief verschil)- Andere factuur (positief)- Credit verwacht / factuur (negatief verschil)- Nalevering volgt (negatief)- Verschil akkoord (beide) |
| --- | --- |

Op basis van de bij de artikelcode gekoppelde artikelgroep wordt bepaald op welke tussenrekeningen geboekt moet worden. Deze regels worden automatisch aangemaakt, samen met de transport- en/of orderkosten regels. Eventuele inkoopverschillen worden naar een daarvoor in de instellingen opgegeven grootboekrekening geboekt.

Opmerking: - Als bij instellingen artikelen 'Bijwerken prijs goederenontvangst' op 'Ja' of 'Verkoop' staat, wordt er een waarschuwing getoond bij Definitief boeken matching, als er een artikelregels is zonder verkoopprijs.- Gedeelde omgeving: Alleen de ontvangsten worden getoond van de magazijnen waarvan de administratie eigenaar is.

#### Matchings mogelijkheden

Klik hier voor meer informatie over de matchings mogelijkheden:

De volgende mogelijkheden zijn er m.b.t. het factuuraantal en ontvangstaantal bij matching:

| Optie | Factuur en ontvangst aantal | Oorzaken | Reden verschil | Opmerking, na boeken | Oplossen door |
| --- | --- | --- | --- | --- | --- |
| 1 | Factuur = Ontvangst |  |  |  |  |
| 2 / 3 |  |  |  |  | Bij Selecteren matching manco's wijzig reden naar Verschil akkoord |
| 2a | Factuur  ontvangst | De (na) levering is nog niet ontvangen/geregistreerd | - Nalevering volgt | - Artikel verschijnt bij Selecteren matching manco's, als artikel ontvangen wordt kan het handmatig gematcht worden bij Selecteren matching manco's | - 1 Ontvangen artikel Boeken goederenontvangst- 2 Handmatig matchen bij Selecteren matching manco's. zie punt 4, boekingen: |
| 3b |  | Teveel gefactureerd (te weinig ontvangen): verrekening op andere factuur. | - Credit verwacht | - Ontvangstbon, met negatief factuuraantal.Regel gesplitst met negatief factuuraantal. | - 1 Negatieve inkoopfactuur, zie Goederenmatching boekingen: |
| 3c |  | Te veel gefactureerd (te weinig ontvangen): | - Verschil akkoord | - Negatief verschil geboekt op grootboekrekening voorraad correctie |  |

Hierbij een voorbeeld van optie 2b andere factuur:

Tip: Voor grote bedrijven waar bijv. de inkoopfactuur door de administratie geboekt worden en de goederen matching door de magazijnmedewerker gedaan wordt, is er een apart optie AVM beschikbaar. Deze medewerker boekt de Proforma en de administratie boekt dan Definitief.Neem hiervoor contact op met de helpdesk om dit in te stellen.

#### Doorboeking

- De volgende journaalpost wordt dan bijv. geboekt: | Grootboek | Omschrijving | Debet | Credit | | --- | --- | --- | --- | | 3100 | Voorraad onderdelen (in magazijn) | 100,00 | | | aan 7100 | Voorraad onderdelen verschillen | | 100,00 |
- De journalisering kan gecontroleerd worden bij Overzicht mutaties per dagboek (GLD).

De grootboekrekening van de betreffende artikelgroep tabblad Voorraad van het artikel/machine wordt hiervoor gebruikt.

-  bij Voorraad nieuw.
- Aan  bij Voorraad correctie.

### Overzicht matching controlelijst

- Overzicht matching controlelijst

#### Goederenmatching 3.0

#### Wat is goederen matching 3.0?

- Klik hier voor meer informatie over de werking: Iedere ontvangst krijgt een uniek ontvangstnummer.
- Matching in eerdere periode geeft geen verandering van cijfers maar een boeking in de actuele periode en direct een voorraadboeking zonder verwerken artikelmutaties.
- aflettering van deze mutaties.
- in nieuw dagboek matching.
- Machine inkopen en machinedeel worden ook automatisch afgeletterd.
- Opmerking: Een Definitieve boeking wordt gejournaliseerd in dagboek Matching een Proforma boeking niet, alleen in dagboek Inkopen.

Financiële voorraad boeking bij ontvangst.

- Bij Boeken goederenontvangst (AVO) worden de ontvangsten na het inboeken direct financieel verwerkt worden, zodat er niet meer gewacht behoeft worden op de matching.

Matching achteraf.

- Bij matching Definitief worden de goederen afgeletterd, zie Afletteren grootboekmutaties.

Matchen bij één ontvangst met meerdere inkoopfacturen is mogelijk, zie voorbeeld 2.

Nieuwe instelling voor moment van het bijwerken van de inkoopprijzen moment prijswijziging:

1. Inkoop / goederenontvangst
2. Twee keer (bij inkoop en matching)

Hiervoor is een kolom Prijsupd nee / ja toegevoegd bij Boeken goederenontvangst.

Bij de volgende instelling prijswijziging bij goederenontvangst is de optie Inkoop toegevoegd:

1. Ja (zowel inkoop als verkoop)
2. Nee, geen prijzen
3. Verkoop (alleen verkoop)
4. Inkoop (alleen inkoop)

Bij Goederen ontvangst matching is het volgende gewijzigd:

1. Nieuwe (matchings)reden: Verschil akkoord. Hierbij wordt in het dagboek Matching het boekhoudkundig verschil gecorrigeerd op de tussenrekening en de correctierekening.
2. De kolom Ontv. bedrag is toegevoegd.
3. Als het factuur aantal of bedrag verschilt, wordt deze in het rood / rode kleur weergegeven. Bijv. het ontvangst bedrag verschilt met de factuur.
4. Het notitie icoon is toegevoegd, voor een interne notitie inkoopfactuur.

Belangrijk: Eénmalig moet Verwerken artikelmutaties (AVF) gedraaid worden. Als dit niet gedaan wordt, verschijnt er een pop-up melding bij matching.

Klik hier voor meer informatie over de oude werking:

- Ontvangst geen boeking
- Matching in een vorige periode geeft verandering van cijfers
- Voorraadboeking na AVF (na matching)

#### Instellingen

Wat is er ingesteld voor Goederen matching 3.0?

Het volgende is ingesteld:

#### 1 Nieuw dagboek matching

Er is een dagboek Matching (het eerste vrije nummer na dagboek Voorraad) voor goederen matching aangemaakt bij:

- Onderhoud dagboeken (GBD). Het dagboektype is Standaard.
- Het dagboek grootboekrekening moet 9999 zijn.
- Belangrijk: Geldt alleen als bij Instellingen crediteuren Gebruik goederen facturen op Matching goederen staat.

#### 2 Nieuw dagboek matching & Instellingen artikelen

Bij Instellingen artikelen, tabblad Koppelingen is het dagboek voor Matching51 (standaard).

#### Voorbeeld matching boeking

Hierbij een voorbeeld van een boeking in verschillende periodes:

1. De goederen zijn ingekocht en besteld in periode 08.
2. Worden ontvangen in periode 08. De goederen worden op voorraad geboekt.
3. De inkoopfactuur wordt later ontvangen en gematcht in periode 09. Grootboekrekening 2720 Nog te matchen valt zo tegen elkaar weg.
4. Deze boekingen vinden plaats in periode 09.

1 Inkooporder

De volgende inkooporder wordt ingegeven:

2 Dagboek Voorraad

De goederen worden ontvangen en op geboekt bij Boeken goederenontvangst.

- Bijv.:

In dagboek 50 Voorraad artikelen wordt het volgende gejournaliseerd:

- Zie Overzicht mutaties per dagboek (GLD) .

3 Dagboek Inkopen en Matching

De inkoopfactuur wordt geboekt bij Inkoopfactuur boeken (KI) en gematcht, in volgende periode 09.

Journalisering in dagboek 30 Inkopen en 51 Matching:

Voorbeeld 1, mutaties per dagboek(en) in periode 08 en 09.

Bij Afletteren grootboekmutaties is te zien dat de matching (grootboekrekening 2720) afgeletterd is.

#### Boekingen

- Bij goederen ontvangt worden de goederen gelijk op de voorraad geboekt.

| Boeking / proces | Grootboekrekening | Debet | Credit | Dagboek |
| --- | --- | --- | --- | --- |
| Goederenontvangst | 3000 Voorraad artikelen | 16,10 |  | 50 Voorraad |
|  | Aan 2700 Te ontvangen facturen |  | 16,10 |  |
| Inkoopfactuur | Aan 1600 Crediteuren |  | 19,48 | 30 Inkopen |
|  | 1523 Voorheffing BTW | 3,38 |  |  |
|  | 2720 Nog te matchen | 16,10 |  |  |
| + Matchen | Aan 2720 Nog te matchen |  | 16,10 | 51 Matching |
|  | 2700 Te ontvangen facturen | 16,10 |  |  |

Klik hier voor meer informatie over een voorbeeld met meerdere facturen:

In dit voorbeeld is er één keer een ontvangst geboekt en er zijn drie facturen ontvangen, verder komen aantallen en prijzen overeen.

- Van één artikel zijn er drie besteld en ontvangen. Drie keer wordt er een inkoopfactuur met 1 artikel ingeboekt.
- Om de (ontvangst) details te bekijken, doorloopt u de volgende stappen: 1. Ga naar Selecteren inkoopfacturen (KS). 2. Kies voor de knop Details.Het scherm Inkooporder details verschijnt. 3. Kies voor de knop Ontvangt gegevens > Meerdere. 4. Het scherm Inkooporderregel matching gegevens verschijnt:
- Bij matching is bij redenandere factuur gekozen.
- Na het inboeken en matchen van deze 3 facturen zien de grootboek-boekingen als volgt uit: Voorbeeld 2, mutaties per dagboek(en) van meerdere facturen.
- Bij Afletteren grootboekmutaties is het volgende afgeletterd:

Klik hier voor meer informatie over een voorbeeld van een machine matching:

Er wordt een inkooporder ingekocht en ontvangen van:

1. Machine
2. Artikel met machinedeel (voor machine)
3. Artikel

- Na de matching (en doorverwerking) is het volgende in het grootboek geboekt: Voorbeeld 3, matching machines Boekstuk: 65 machine
- 66 machine deel
- 1000020 artikel

Opmerking: Er is hierbij vanuit gegaan van de instelling machines dat de machine transactie direct verwerkt worden, dit kan ook handmatig via Doorverwerken machine-transacties (MVD).

Hoe ziet de Belgische variant eruit bij matching?

In België wordt er gebruik gemaakt van standaard rekeningen MAR (Minimumindeling van het Algemeen Rekeningstelsel).

Hierbij een voorbeeld van de boekingen:

| Boeking / proces | Grootboekrekening | Debet | Credit | Dagboek |
| --- | --- | --- | --- | --- |
| Goederenontvangst | 340000 Goederenontvangst | 100 |  | 50 Voorraad |
|  | aan 608100 Prijsverschillen |  |  |  |
|  | aan 444100 Te ontvangen facturen * |  | 100 |  |
|  | 604001 Aankopen | 100 |  |  |
|  | aan 609400 Voorraad mutatie |  | 100 |  |
| Inkoopfactuur | aan 440000 Crediteuren |  | 100 | 30 Aankopen |
|  | 411000 BTW | 21 |  |  |
|  | aan 451300 BTW Intracom |  | 21 |  |
|  | 499001 Nog te matchen * | 100 |  |  |
| Matchen | 444100 Te ontvangen facturen * | 100 |  | 51 Matching |
|  | aan 499001 Nog te matchen * |  | 100 |  |

Opmerking: * Het saldo van deze rekeningen is 0,

Opmerking: Bij Overzicht voorraadmutaties (ALM) wordt aangegeven of een inkoopfactuur gematcht of een pro-forma is.

Opmerking: Als bij een afgeletterde grootboekmutatie het bedrag wordt gewijzigd, bij matching boekingen, dan wordt de afletteringscode verwijderd.

#### FAQ

Hoe zit het als de voorraad eenheid wijzigt bij een artikel?

Bij Goederen ontvangst matching wordt er rekening gehouden met het wijzigen van de voorraadeenheden van een artikel. Bij (het tonen van) de matching wordt er gerekend met de historische aantal en waarde. Dit gebeurt bij:

- Goederenmatching
- Selecteren matching manco's
- Overzicht matching controlelijst

Wat doe ik als bij matching het artikel niet op de inkoopfactuur staat?

Bij goederen ontvangst matching kan:

- Het artikel verwijderd worden uit de betreffende matching (via rechter-muis-knop op de regel).

Bij het boeken van een nieuwe inkoopfactuur (volgende matching) verschijnt het betreffende artikel op het inkoopnummer.

- FAQ Goederenmatching

- Afletteren grootboekmutaties
- Goederenmatching Overzicht matching controlelijst

Boeken goederenontvangst

---
## Selecteren matching manco's

Bij matching manco's worden alle inkoopfacturen en ontvangsten getoond waarin manco’s zijn, d.w.z. die nog niet gematcht zijn. Deze moeten nog opgelost of verwerkt worden.

- Als er bij Goederenmatching een reden verschil opgegeven is, verschijnen deze factuur regels.
- Factuurregels en ontvangsten kunnen aangevinkt en vervolgens opgeslagen worden. Zodat deze naleveringen alsnog gematcht worden.
- Bij een ontvangst en een credit ontvangst kunnen deze tegen elkaar weggeboekt worden, door ze te laten vervallen.
- Een boekhoudkundige voorraad correctie wordt in het dagboek Matching geboekt bij: Wijzigen reden naar reden verschil akkoord.
- Bij het laten vervallen van een regel, wordt er geen (directe) correctie gedaan op de plankvoorraad. Opmerking: Overleg met het magazijn of de voorraad al is gecorrigeerd (in de praktijk is dit meestal het geval). Klik hier voor meer informatie over een voorbeeld boeking: Een artikel met een positief aantal (2) is vervallen 2 x 70.67 (vvp) = 141.34. Het volgende wordt hierbij geboekt:

Als bij Instellingen artikelen koppeling grootboek op nee, staat, wordt er niets geboekt.

Om naar de matching manco's te gaan doorloopt u de volgende stappen:

1. Ga naar Selecteren matching manco's (AVS).
2. Geef een selectie op.
3. Kies voor de knop Selecteren.
4. De volgende acties zijn mogelijk: Vink een ontvangst - en factuurregel aan. Opmerking: De regels worden gematcht op Leverancier, Cataloguscode, Artikel en Aantal. - Deze moet bij de ontvangst, met de factuur overeenkomen.- Het cumulatief aantal van de geselecteerde regels moet 0 zijn (ontvangst +factuur = 0).- Het matchen is mogelijk bij 1 factuurregel en meerdere ontvangstregels. Bijv.:
5. Kies voor de knop Wijzig reden om de reden te wijzigen.
6. Voor vervallen zie Laten vervallen.

Kies voor de knop Opslaan.

De naleveringen zijn (alsnog) gematcht.

Opmerking: Er vindt geen aflettering meer plaats.

#### Laten vervallen oude ontvangsten

Het is mogelijk om (oude) ontvangsten zonder reden te laten vervallen.

Klik hier voor meer informatie om dit te doen:

Om ontvangsten te verwijderen, doorloopt u de volgende stappen:

1. Ga naar Selecteren matching manco's (AVS).
2. Geef een selectie op, met bijv. een leverancier en een t/m datum.
3. Vink de vervallen regels aan. Belangrijk: Regels waarin een reden van verschil in aantal is opgegeven of regels die gesplist zijn, kunnen niet vervallen, dit veroorzaakt een foutieve boeking.
4. Kies voor de knop Vervallen.

De ontvangsten zijn direct vervallen.

Opmerking: Matching manco's met aantal 0 worden, niet getoond.

- FAQ Goederenmatching

---
## EDI / Digitale inkooporder aanmaken

#### Voorwaarden

Digital order of EDI (layout) moet ingesteld zijn voor de leverancier en bij de relatiecode.

#### Taak

Om een EDI-order of Digitale order aan te maken, doorloopt u de volgende stappen:

1. Ga naar Selecteren inkooporders (IS).
2. Selecteer de inkooporder.
3. De volgende acties zijn mogelijk: (Deze zijn afhankelijk van de communicatie instellingen.) Instelling Kies voor de knop EDI. Klik hier voor meer informatie om dit te doen: Het scherm Aanmaken EDI-bestand verschijnt.
4. Controleer de gegevens.
5. Kies voor de knop Aanmaken. Opmerking: Bij sommige layouts kan ook een Afleverdatum ingevuld worden.De bestandsnaam wordt gevuld vanuit het betreffende EDI-layout.

Instelling Kies voor de knop Digitale order.

of

Instelling Kies voor de knop Proforma order, bij instelling proforma is ja.

- Het scherm Digitale order verzenden verschijnt. Opmerking: De 'verzend' velden worden opgehaald afhankelijk van de leverancier (dit kan even duren).

1. Geef de ordersoort in. Technische Unie:
2. Kies voor de knop Versturen. Het scherm Overzicht digitale order verschijnt. Bij Digitale order met het digitale order nummer en de opmerking Order succesvol geplaatst, als alles goed gegaan is. In bovengenoemd voorbeeld is de netto prijs tegelijkertijd bijgewerkt.
3. Bij Proforma order met het proforma nummer.

Bij Digital order (a) controleer de gegevens/ opmerkingen of druk op de link Bekijk online.

Bij Proforma order optie (b)

*Klik hier voor meer informatie overeen proforma order: 1. Kies voor de knop Order plaatsen. De opmerking Order succesvol geplaatst. verschijnt bovenaan. Kies voor de knop Sluiten. - Een digitale order zorgt voor de status ophoging zodat de knop Digitale status beschikbaar wordt. - Als een leveranciers de juiste inkoopprijs teruggeeft, wordt het totaalbedrag inkoop bijgewerkt. Kies voor de knop Sluiten. De digitale / EDI-order is verzonden / aangemaakt. #### FAQ Hoe activeer ik de knop EDI bij Selecteren inkooporders. Om van een inkooporder een EDI-order te maken, moet dit ingesteld zijn bij de leverancier. Om dit te doen, doorloopt u de volgende stappen: 1. Ga naar Onderhoud relaties (BRR) 2. Ga naar tabblad E-document. 3. Kies voor de knop Wijzigen. 4. Vink bij Inkooporder EDI het vakje Actief aan. 5. Kies voor de knop Opslaan. De knop EDI of Digitale order is beschikbaar. Hoe worden de EDI inkooporder bestanden verder verwerkt? - Het inkooporder EDI bestand kan handmatig geïmporteerd worden, bijv. ingelezen op de website. - Ook is het mogelijk om deze EDI bestanden automatisch te verwerken, afhankelijk van de leverancier. Bijv. bij Mechan of TU. Hoe zit het bij het versturen van een Digitale order m.b.t. prijs en aantal? Bij versturen van een Digitale (inkoop) order is het volgende mogelijk: M.b.t. aantal, vanaf versie 3.10: - De leverancier kan aan- of teruggeven dat de bestelhoeveelheid gewijzigd is. De opmerking 'Let op bestelde hoeveelheid is gewijzigd naar X', wordt hierbij weergegeven. De leverancier heeft de bestelde artikelcode vervangen en geeft een vervangend artikel terug. - Hierbij dan het artikel al of niet vervangen worden d.m.v. pijltjes (links/rechts) toetsen. M.b.t. prijs: - De leverancier kan de juiste prijs teruggeven, als deze afwijkt wordt deze gemarkeerd. Klik hier voor meer informatie over een voorbeeld van een EDI-order voor Mechan: Bij Mechan kan automatisch de (12345678) ingevuld worden. Klik hier voor meer informatie over een voorbeeld van een Digitale order / EDI-order voor Technische Unie (TU): Bij Selecteren inkooporders verandert de knop EDI in Digitale order, Proforma order: 1. Selecteer de inkooporder. 2. Kies voor de knop Digitale order. 3. Hierbij kunnen de volgende (TU) opties afhalen / kladorder gekozen worden: Opmerking: Kladorder is geen definitieve order, meer een soort prijsaanvraag. Deze optie werkt nu nog niet naar behoren; dus voorlopig niet gebruiken. 4. Kies voor de knop Versturen. Het scherm Overzicht digitale order verschijnt, met het ordernummer van de TU. 5. Kies voor de knop Sluiten. De order is verzonden. #### Inkooporder details Het ordernummer van de Technische Unie staat ook bij de inkooporder details bij Extern nr. Bij een digitale order: #### FAQ Worden de netto prijzen in de inkooporder aangepast op het moment dat deze afwijken van de TU prijzen? Ja, de prijzen worden bijgewerkt. Kan het ordernummer van de leverancier / TU terug gesynchroniseerd worden naar de inkooporder? Ja dit is te zien in de kolom Digitale order. - Bij een Proforma order aanvraag verschijnt hier het ordernummer van de leverancier. - In de map Dossier wordt een tekst bestand aangemaakt met response date, van de inkooporder. Wat doe ik bij de melding GLN is niet numeriek*?

Controleer of het juiste GLN nummer ingevuld is bij veld Extra waarde 2.

Wat is een GLN nummer precies?

Een Global Location Number (GLN) is een nummer van 8, 12, 13 of 14 posities lang (afhankelijk van het land), waarmee een fysieke locatie van bijvoorbeeld een kantoor, winkel of magazijn als uniek adres geïdentificeerd wordt.

Een GLN nummer is een EAN-code.

- GLN = GS1 locatiecodes, zie ook www.gs1.nl
- Zie ook Hoe krijgt u een GS1 adrescode?

Wat is het verschil tussen EDI - en Digitale order?

Bij Selecteren inkooporders (IS) wordt deze knop gebruikt.

- EDI is de oude benaming die nog bij 99% van de klanten zo werkt.
- Digital order gaat via de Powerall dealer services. Hierbij zijn er meer mogelijkheden (prijzen, ordernummers terug synchroniseren etc.).

- Een digitale order zorgt voor de status ophoging, zodat de knop Digitale status beschikbaar wordt.
- Als een leveranciers de juiste inkoopprijs teruggeeft, wordt het totaalbedrag inkoop bijgewerkt.

- Welke leveranciers integraties zijn er?

---
## Selecteren inkooporders

Voor meer informatie over de algemene mogelijkheden bij de selecteren programma's zie:

- Selecteren

Voor het dashboard inkooporders, doorloopt u de volgende stappen:

1. Ga naar Selecteren inkooporders (IS). Alle openstaande inkooporders verschijnen op het scherm.
2. De volgende acties zijn mogelijk: Geef een selectie op. Kies voor de knop Selecteren.
3. Geef direct het ordernummer in. Kies voor de knop .
4. De inkooporder verschijnt in de eerste regel.
5. Kies voor de knop Bestelregels. instelling Goedkeuren besteladvieslijst (centraal bestellen)
6. Kies voor de knop Importeren. EPC bestand importeren
7. Kies voor de knop Nieuw. Nieuwe inkooporder aanmaken (artikelen)
8. Machine inkooporder
9. Kies voor de knop Wijzigen. Inkooporder wijzigen of verwijderen
10. Kies voor de knop Details. Inkooporder details
11. Kies voor de knop Dossier.
12. Kies voor de knop Bestelbon.
13. Kies voor de knop Prijsaanvraag. Print prijsaanvraag
14. Kies voor de knop EDI. Inkooporder versturen
15. Kies voor de knop Digitale order. optioneel EDI / Digitale inkooporder aanmaken
16. Kies voor de knop Proforma order. optioneel Geldt alleen als bij Instellingen externe communicatie Proforma op ja staat.
17. Kies voor de knop Digitale status. optioneel Het scherm Overzicht digitale order verschijnt.
18. Kies voor de knop E-mail. Inkooporder versturen
19. Bij productie: Aanmaken bestelbon bijlage voor zippen tekeningen e.d.
20. Kies voor de knop Ontvangen. optioneel Boeken goederenontvangst De artikelen worden op voorraad geboekt.

#### FAQ

Wat betekenen de kleuren in de kolom Totaal?

Het orderbedrag in de kolom Totaal geeft aan of het minimum orderbedrag wel of niet bereikt is. En kan ook groen of rood zijn. Deze kleuren hebben de volgende betekenis:

- Rood = Het minimum orderbedrag is niet bereikt, bij status Openstaand. Bij het gebruik van de knoppen Bestelbon / Email / EDI wordt er een melding gegeven: Minimum orderbedrag = . Wilt u doorgaan?

Groen = Het minimum order is niet bereikt bij orderstatus Besteld.

Zwart = Minimum orderbedrag is bereikt of niet ingesteld.

Bijv.

Bij Onderhoud relaties, tabblad Crediteurinfo, kan een minimum orderbedrag ingegeven worden.

Welke inkooporder statussen zijn er?

De volgende inkooporder statussen zijn er:

- Openstaand, er is nog geen bestelbon afgedrukt.
- Bestelbon, besteld. De bon is aangevraagd.
- Ontvangen, inkooporder is ontvangen en verschijnt niet meer in dit overzicht.

Hoe komt het dat de knop EDI of E-mail niet geactiveerd wordt als ik een inkooporderregel selecteer?

De bestelmethode is afhankelijk van de leveranciers instellingen bij Onderhoud relaties als er niets is aangevinkt blijven deze knoppen grijs.

- Controleer op tabblad E-document wat er is aangevinkt bij documentsoort Inkooporder. Het volgende kan bijv. gebruikt worden als deze is aangevinkt bij: E-mail / PDF de knop E-mail.
- EDI de knop EDI.

Hoe komt het dat ik de knop Ontvangen niet kan gebruiken?

Als de knop Ontvangen uitgegrijsd is, is deze knop niet bruikbaar of niet geautoriseerd.

- Bij de inkoop status Bestelbon is de knop te gebruiken.
- Bij Instellingen inkooporders kan deze knop geautoriseerd zijn. De gebruiker moet deze autorisatie hebben.

- FAQ Inkoop(orders)

---
## Besteladvieslijst (goedkeuren)

Met de besteladvieslijst wordt het aantal te bestellen artikelen berekend, aan de hand van de voorraden, minimum en maximum etc. bestelmethode.

- Voor meer informatie zie: Hoe werkt de besteladvieslijst?
- Besteladvieslijst in het inkoopproces schema

Om de besteladvieslijst aan te vragen, doorloopt u de volgende stappen:

1. Ga naar Besteladvieslijst (ALB). Het scherm Besteladvieslijst verschijnt.
2. De pop-melding Er zijn nog oude bestelregels aanwezig, die misschien ten onrechte eerder niet verwijder zijn. Deze kunnen invloed hebben op de besteladvieslijst.... kan verschijnen. Deze kunnen verwijderd worden, zie Verwijderen bestelregels (IBV).
3. Geef eventueel een selectie in. Bij Centraal inkooporders aanmaken is nee. | Inkoopregels aanmaken | Optie voor het aanmaken van een inkooporder regels:- Ja (standaard) - Nee - Toevoegen, inkoopregel wordt toegevoegd, indien inkooporder met datum vandaag bestaat.- Goedkeuren, bestelregels worden aangemaakt (tussenstap) en het programma Goedkeuren besteladvieslijst verschijnt. De aangevinkte regels kunnen via de knop Goedkeuren besteld worden. Er wordt dan een inkooporder(s) aangemaakt. | | --- | --- |
4. Bij Centraal inkooporders aanmaken is ja. Bij Bestelregels aanmaken selectie Ja of Goedkeuren, is het mogelijk om direct inkooporderregels aan te maken.
5. | Bestelregels aanmaken | Optie voor het aanmaken van bestelregels:- Nee (standaard) alleen een overzicht wordt weergegeven.- Ja, (standaard bij Central Warehouse) bestelregels worden aangemaakt, zie Goedkeuren besteladvieslijst (IBA).- Goedkeuren, bestelregels worden aangemaakt (tussenstap) en het programma Goedkeuren besteladvieslijst verschijnt. De goedgekeurde bestelregels kunnen definitief besteld worden, d.w.z. van de geselecteerde regels worden inkooporders aangemaakt. | | --- | --- |

Kies voor de knop Afdrukken.
De artikelen worden opgezocht en gecontroleerd of deze voldoen aan de selectie criteria.

De besteladvieslijst wordt aangemaakt.

## Goedkeuren besteladvieslijst

Bij de optie goedkeurenbesteladvieslijst zijn er twee mogelijkheden:

1. Bij de instelling centraal inkooporders aanmaken is ja. Blijven de bestelregels staan.
2. Als de optie bestelregels aanmaken is goedkeuren gebruikt wordt bij de besteladvieslijst, (zie stap 2 hierboven) wordt 1 (IS) hieronder overgeslagen. De bestelregels die niet zijn goedgekeurd, worden verwijderd.

Als er besteladvies gegevens / regels zijn aangemaakt, dan kunnen deze aangepast en (definitief) besteld worden. Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Selecteren inkooporders (IS). Kies voor de knop Bestelregels.
2. Bij Goedkeuren besteladvieslijst (IBA). Selecteer in de kop de eventuele selecties.
3. Kies voor de knop Selecteren.

Het aantal, te bestellen artikelen en de leverancier kan aangepast worden.

Vink de te bestellen regels aan.

Tip: Het vinkje / optie toon goedkoopste leverancier is toegevoegd. Vink deze aan, en druk op Selecteren om de goedkoopste leverancier(s) te tonen.Deze optie kan ook standaard aangevinkt worden, via de instellingen.

Instelling Centraal inkooporders aanmaken is nee.

1. Kies voor de knop Goedkeuren.
2. Kies voor de knop Bestellen & sluiten. Als de knop Goedkeuren niet gebruikt worden de Regels die niet zijn goedgekeurd verwijderd.

Instelling Centraal inkooporders aanmaken is ja.

Kies voor de knop Definitief bestellen.

Van deze artikelen is een inkooporder aangemaakt.

#### FAQ

*Hieronder een uitleg van de velden van scherm Goedkeuren besteladvieslijst*:

| Kop |  |
| --- | --- |

| Sorteren op | Optie om te sorteren op:- Artikelcode (standaard) - Locatie - Leverdatum - Back-to-back (BTB) - Hoofdlocatie |
| --- | --- |

| Leverancier | De relatiecode van de leverancier. |
| --- | --- |

| Leverancier vanaf | Leverancier selectie vanaf .. t/m ... |
| --- | --- |

| Artikelgroep vanaf | Artikelgroep selectie vanaf .. t/m ... |
| --- | --- |

| ABC-analyse vanaf | ABC-analyse selectie vanaf .. t/m ... |
| --- | --- |

| Magazijn vanaf | Magazijn selectie vanaf .. t/m ... |
| --- | --- |

|  | Rechter kolom: |
| --- | --- |

| BtB-type | Selecteer het BtB-type (B ack to Back), bestellingen aangemaakt vanuit:- N.v.t. (standaard) alle types- Verkooporder- Werkorder- Project |
| --- | --- |

| BTB-order vanaf | Kostenplaats selectie vanaf .. t/m ... NB. Als hier dezelfde kostenplaats wordt ingevuld, wordt deze overgenomen op de inkooporder. |
| --- | --- |

| Creatiedatum vanaf | De aanmaakdatum van de order vanaf en t/m.- Leeg .... t/m  |
| --- | --- |

| Kostenplaats vanaf | Kostenplaats selectie vanaf 0 t/m 999. NB. Als hier dezelfde kostenplaats wordt ingevuld, wordt deze overgenomen op de inkooporder bij een BtB optioneel. |
| --- | --- |

| Toevoegen aan bestaande orders | Optie om een bestelling toe te voegen aan een bestaande inkooporder: - Nee (standaard) - Ja, ordernummer verschijnen en kan geselecteerd worden. |
| --- | --- |

| Bron | De 'plaats'waar deze inkoop bestlregel is aangemaakt.:- N.v.t. / alle (standaard) - EPC- picklijst - Besteladvies / H - Barcodering - Projecten - Back-to-Back (BTB) - SlimStock |
| --- | --- |

| Toon goedkoopste leverancier | Vink deze aan, om de goedkoopste leverancier te tonen, in een aparte kolom Goedkoopste leverancier en inkoopprijs die zichtbaar worden, deze regel is vet.- NB. Bij Instellingen inkooporders tabblad Koppelingen kan deze standaard aangevinkt worden. |
| --- | --- |

Opmerking: Bij een wijziging in de kopgegevens, druk op de knop Selecteren om deze te activeren.

| Regels: |  |
| --- | --- |

| Rgl. | Het regelnummer, wordt automatisch doorgenummerd. |
| --- | --- |

| Magazijncode | De code van het magazijn. |
| --- | --- |

| Magazijn oms. | De magazijnomschrijving. |
| --- | --- |

| Locatie | De fysieke locatie waar het artikel te vinden is in het magazijn. Vaak wordt dit opgebouwd uit verdiepings-gangpad-kast-plank, bijv. 01-A-01-01. |
| --- | --- |

| Voorraad | De beschikbare voorraad. |
| --- | --- |

| Artikelcode | Het artikel, zie Onderhoud artikelen.Ingave of zoeken op een omschrijving / kenmerk via Zoek artikelen. |
| --- | --- |

| Omschrijving | De 'betreffende' omschrijving. |
| --- | --- |

| Aantal | Het betreffend aantal. |
| --- | --- |

| Inkoopaantal | Het inkoopaantal dat ontvangen wordt. |
| --- | --- |

| Leverancier | De relatiecode van de leverancier. |
| --- | --- |

| Inkoopprijs | De inkoopprijs |
| --- | --- |

| Datum | Datum dat de order(regel) ingegeven is. |
| --- | --- |

Onderstaande velden verschijnen alleen bij de optie Toon goedkoopste leverancier: Selecteer deze in de kolom leverancier.

| Goedkoopste leverancier | De goedkoopste leverancier |
| --- | --- |

| Inkoopprijs | De inkoopprijs |
| --- | --- |

Opmerking: De velden aantal en de leverancier zijn wijzigbaar.

Opmerking: • Als de leverancier niet de bestelvoorkeursleverancier is van dit artikel, krijg je de vraag: Toch bij deze leverancier bestellen? Ja of Nee. • Door de BtB-type selectie te maken, is het mogelijk te zien, vanwaar de bestellingen zijn aangemaakt, zie ook kolom BTB.• Alleen artikelen uit je eigen artikelbestand komen in de bestelregels terecht en niet de catalogus artikelen. Deze kunnen aan de inkooporder toegevoegd worden.• Als het aantal 0,0 is, verschijnt er een melding bij Definitief bestellen.

Hoe kan ik een bestelregel verwijderen?

Het is mogelijk om een bestelregel te verwijderen, bijv. een uitlopend artikel. Om dit te doen, doorloopt u de volgende stappen:

1. Selecteer de regel.
2. Rechtermuis knop in de kolom Rgl -> Verwijderen

Het artikel is verwijderd van de bestellijst.

Is het mogelijk om een bestelling toe te voegen aan een bestaande inkooporder?

Ja, dit is mogelijk. Om dit te doen, doorloopt u de volgende stappen:

1. Selecteer de leverancier (in de kop).
2. Selecteer bij Toevoegen aan bestaand orders Ja.
3. Selecteer bij Toevoegen aan specifieke orders de , indien er meerdere orders aanwezig zijn.

Belangrijk: Alleen regels voor hetzelfde magazijn als van de inkooporder worden hierop toegevoegd.

Wordt het minimum orderbedrag gecontroleerd?

Ja, als dit ingesteld is bij de leverancier.

- Als er op de knop Definitief bestellen wordt gedrukt, wordt gecontroleerd of het totale inkoopbedrag van de geselecteerd regels voldoet aan het minimum orderbedrag. Dit geldt als er is één leverancier geselecteerd is, of alle (geselecteerde) regels voor 1 leverancier zijn.

Instelling Centraal inkooporders aanmaken is nee

Wat gebeurt er als ik 'Goedkeuren besteladvieslijst' afsluit of annuleer?

Als de goedkeuren besteladvieslijst geannuleerd wordt of bij 'Bestellen' & sluiten, verschijnt er een melding:

- De regels die niet zijn goedgekeurd, worden verwijderd.

Bij veel bestelregels verschijnt in het scherm Besteladvieslijst nog de volgende melding:

- Belangrijk: Wacht hierbij totdat de verwerking gereed is, anders blijven artikelen 'hangen'.

Is het mogelijk om de bestelregels eerst goed te keuren?

Het is mogelijk om de bestelregels eerst goed te keuren, voor dat deze in een inkooporder komen, door de optie Goedkeuren d.m.v. onderstaande instelling:

- | Besteladvies inkoop order maken | Optie voor de Besteladvieslijst, voor het veld inkooporder aanmaken: - Ja (standaard)- Nee- Toevoegen (niet mogelijk bij centraal bestellen)- Goedkeuren (dit geldt ook voor Barcode app bestellen, hierbij moet Ga naar Uitlezen barcode scanner (BXU). aan staan). | | --- | --- |

Zie punt 5a.

Instelling Centraal inkooporders aanmaken is ja

Is het mogelijk om bij definitief bestellen ook gelijk de bestelbon af te drukken?

Ja, dit is allen mogelijk bij Centraal inkooporders aanmaken ja. Om dit te doen, doorloopt u de volgende stappen:

1. Selecteer één  bij van en t/m.
2. Vink de artikelen aan.
3. Kies voor de knop Definitief bestellen.
4. Bij de melding Direct inkooporder afdrukken kies: Ja, bestelbon wordt afgedrukt en inkoopstatus wordt bestelbon (definitief).
5. Nee, de inkoopstatus blijft openstaan.

Is het mogelijk om verwijderde inkooporder regel weer terug te zetten in de 'Goedkeuren besteladvieslijst'?

Ja, dit is alleen mogelijk bij Centraal inkooporders aanmaken ja bij een gekoppelde verkooporder.

- Het kan immers zijn dat de leveranciers de goederen op backorder heeft / niet kan leveren. Hierdoor is het mogelijk om de artikelen bij een andere leverancier te bestellen.
- Bij het verwijderen van een gekoppelde inkooporder regel verschijnt (ook) de melding: Wilt u de gekoppelde regel uit de verkooporder in de bestellijst terugzetten.

Hoe komt het dat de knop 'Definitief bestellen' niet beschikbaar is?

Als de knop Definitief bestellen grijs is, selecteer dan bij Leverancier waarbij beide staat:

- Extern of
- Intern

Hoe verwijder ik bestelregels?

Om bestelregels te verwijderen, doorloopt u de volgende stappen:

1. Ga naar Verwijderen bestelregels (IBV).
2. Vink de te verwijderen regels aan.
3. Kies voor de knop Regels verwijderen.

De bestelregels zijn verwijderd.

Opmerking: Dit programma staat niet standaard in het menu.

- Nieuwe inkooporder aanmaken
- Inkooporder versturen
- Hoe werkt de besteladvieslijst?

---
## Nieuwe inkooporder aanmaken

**Nieuwe inkooporder aanmaken Inkoopproces schema Om een inkooporder in te voeren, doorloopt u de volgende stappen: 1. Ga naar Selecteren inkooporders (IS). Een overzicht van openstaande inkooporders verschijnt. 2. Kies voor de knop Nieuwe order.Het scherm Invoeren/wijzigen inkooporders verschijnt. 3. Geef de relatiecode en inkoop ordergegevens in. 4. Bij de order regels geef de Cataloguscode of de Artikelcode(s) in, met het aantal. 5. Kies voor de knop Einde order. De inkooporder is opgeslagen. Opmerking: Bij gebruik van een leverdatum in de regels is de gewenste leverdatum in de kop, altijd gelijk aan de laagste leverdatum in de regels. ### Inkooporder invoeren #### Instelling bestelregels De (dagelijkse) inkopen worden hierbij verzameld in de bestelregels, vervolgens worden er dan inkooporders aangemaakt. Zie ook Besteladvieslijst (goedkeuren) instelling. #### Importeren EDI inkoopordergegevens Klik hier voor meer informatie over het importeren van inkoopordergegevens vanuit via een webshop of bestelsysteem: Om inkoopordergegevens vanuit de webshop of het bestelsysteem van de leverancier te importeren, doorloopt u de volgende stappen: 1. Ga naar Selecteren inkooporders (IS). 2. Geef de relatiecode en inkoop ordergegevens op. 3. Kies voor de knop Importeer. Het scherm EDI orders ophalen verschijnt. 4. Kies voor de knop Importeren order. of 5. Kies voor de knop Alles importeren. Controleer de geïmporteerde EDI order(s). Opmerking: Bij Selecteren inkooporders, kan d.m.v. de knop Ontvangen direct de artikel / regels ingeboekt worden, van de betreffende inkooporder, met status Bestelbon. #### FAQ Hieronder een uitleg van de velden van scherm Invoeren/wijzigen inkooporders: | Kop | | | --- | --- | | Relatiecode | De relatie code, zie Onderhoud relaties. | | --- | --- | | Inkoopordernummer | Het ordernummer van de inkoop. | | --- | --- | | | | --- | | Inkooporderdatum | De datum van de inkooporder. | | --- | --- | | Selectiecode | Bij dit veld kan een waarde (A t/m Z, 1-9) opgeven worden, waarop later bij het controleren, afdrukken of vrijgeven op geselecteerd kan worden. Een handig hulpmiddel voor het maken van selecties. | | --- | --- | | Fiattering | Hier kunt u een letter opgeven van A t/m Z. Bij gebruik van fiatteringscode zijn er afspraken over welke letter aan welke autorisatie is gekoppeld. NB Bij een verkooporder kan de fiattering als autorisatie voor het wijzigen functioneren. | | --- | --- | | Kostenplaats | Wilt u de kosten van een totale bon of factuur kunnen doorboeken naar één bepaalde kostenplaats, dan kunt u hier die specifieke kostenplaats ingeven, zie Onderhoud kostenplaatsen.Gebruikt u deze code niet, dan worden de uren en onderdelen naar de standaard ingevoerde grootboekrekeningen doorgeboekt, zonder uitsplitsing van kostenplaats. | | --- | --- | | Inkoopordertype | Het inkoop ordertype (1 - 5), zie Onderhoud ordertypes.- Bijv. Inkoop order en Inkoop spoed. | | --- | --- | | | | --- | | Referentie | Hier geeft u een korte duidelijke omschrijving van de order.NB De (externe) referentie kan automatisch gevuld wordt a.h.v. instellingen werkorders van dit veld. | | --- | --- | | Ordergegevens | Hier vult u bijvoorbeeld de contactpersoon of opdrachtgever in. | | --- | --- | | | | --- | | Rayon | De rayoncode bepaalt het afzetgebied of regio. Deze kan gebruikt worden om verkoopstatistieken te genereren. | | --- | --- | | Relatiecode | De relatie code, zie Onderhoud relaties. | | --- | --- | | Servicenummer | Het machine nummer, zie Onderhoud machines. | | --- | --- | | Inkoper | De personeelscode van de inkoper, zie Onderhoud personeelscodes.NB Inkoopstatistieken kunnen geraadpleegd worden | | --- | --- | | Magazijn (orderkop) | Het magazijn voor deze order, zie Onderhoud magazijnen. De artikelmutaties vinden plaats in dit magazijn.- De magazijncode wordt overgenomen op de orderregels. Kan handmatig aangepast worden. | | --- | --- | | | Rechter kolom: | | --- | --- | | Post adres | Invulbaar bij instellingen centraal inkooporders aanmaken. | | --- | --- | | Relatiecode | De relatie code, zie Onderhoud relaties. | | --- | --- | | Factuuradres | Dit is standaard het adres van de relatie. - Wilt u standaard een adres van een andere relatie gebruiken? Dan kunt u deze instellen bij Onderhoud relaties, tabblad Debiteureninfo, bij het veld factuurrelatie (order). | | --- | --- | | Aflever adres | | | --- | --- | | Afleveradres | Het adres waar de goederen / diensten geleverd worden. - Standaard gevuld met de algemene adresgegevens. Dit kunt u wijzigen door handmatig het afleveradres in te voeren of door één van de afleveradressen te selecteren, bij het volgnummer, die bij de relatie bekend zijn. | | --- | --- | | Volgnummer | Het volgnummer van het afleveradres d.w.z een ander afleveradres van de relatie. - Kan bij Zoek afleveradressen geselecteerd worden. | | --- | --- | | Regels: | | | --- | --- | | Rgl. | Het regelnummer, wordt automatisch doorgenummerd. | | --- | --- | | Cat. cd. (Catalogus code) | Als u over de optie ‘gegevensuitwisseling’ beschikt, kunt u opgeven of u een artikel uit een bepaalde catalogus wilt invoeren. U geeft aan uit welke catalogus u het artikel wilt invoeren door de twee letters in te vullen die voor de desbetreffende catalogus zijn. Bijv. KR voor Kramp. Door dit veld leeg te laten kunt u een artikel uit het eigen artikelbestand invoeren. Weergave van dit veld is optioneel.V = is voor een vrij artikel. Dan kunt u zelf een code of de code van de leverancier opgegeven bij de artikelcode. | | --- | --- | | Artikelcode | Het artikel, zie Onderhoud artikelen.Ingave of zoeken op een omschrijving / kenmerk via Zoek artikelen. | | --- | --- | | Omschrijving | Omschrijving van het artikel. - Dit veld wordt automatisch gevuld vanuit het artikelbestand. Kan handmatig aangepast worden. | | --- | --- | | Besteld | Het aantal besteld. | | --- | --- | | Geleverd | Het aantal geleverd.Als goederen ontvangen worden (d.w.z opgeboekt op de voorraad), wordt dit aantal bijgewerkt | | --- | --- | | Verkoopprijs | Dit is de verkoopprijs, Incl. of Excl. BTW (over deze prijs wordt de klant korting berekend). | | --- | --- | | Korting | Het kortingspercentage op de brutoverkoopprijs van het artikel. NB Standaard gevuld met de kortingsafspraken die zijn vastgelegd. Kan handmatig aangepast worden. | | --- | --- | | BTW | De BTW code wordt ook uit het artikelbestand en van de relatie overgenomen. In de order is deze handmatig aan te passen, bijvoorbeeld bij marge-artikelen. | | --- | --- | | Code | Dit optioneel veld betreft de factuurregelcode. Factuurregel codes kunnen bij de facturering, offertes, verkooporders en bij de werkorders ingegeven worden. U kunt er bedragen mee weglaten (onderdrukken) of van een tekst voorzien in de bedrag kolom, terwijl achterliggend het bedrag in tellingen en boekingen wel een rol speelt. | | --- | --- | | Artikelgroep | De artikelgroep van het artikel / machine. Dit is de financiële groep en bepaalt de financiële boekingen. | | --- | --- | | BTB | Als er sprake is van een back-to-back BtB koppeling voor deze orderregel, wordt in dit veld het ordernummer van de gekoppelde inkooporder weergegeven. | | --- | --- | | | Vinkje om de inkoopprijs bij te werken instelling.- Afhankelijk van de instelling wordt de inkoop- of verrekenprijs van het artikel bij Boeken goederenontvangst en/of Goederenmatching bijgewerkt. | | --- | --- | | Type | Het merk type van de machine. | | --- | --- | | Leverdatum | De (afwijkende) leverdatum van het artikel in de regels (bij een inkooporder). | | --- | --- | #### Inkooporder machine - Zie hiervoor Machine inkooporder Hoe werk ik de inkoopprijzen bij? Bij een leveranciers-koppeling / parts inquiry, is het mogelijk om de inkoopprijzen bij te werken. Om dit te doen, doorloopt u de volgende stappen: 1. Kies voor de knop Prijzen bijwerken. De pop-up melding Prijzen zijn bijgewerkt verschijnt. 2. Kies voor de knop OK. NB als de adviesprijs niet bekend is, wordt deze niet bijgewerkt (alleen het kortings % indien gevuld). Opmerking: Bij Digitale orders is de knop Prijzen bijwerken niet zichtbaar, maar de knop Digital status. Wat doe ik bij de melding: Fout bij prijs opvraag**?

Probeer eerst opnieuw.

- Neem hiervoor contact op met de helpdesk.

Hoe wordt standaard de inkoopprijs berekend in de regels?

De inkoopprijs wordt als volgt berekend, bij Invoeren/wijzigen inkooporders op het scherm, in de regels.

- De inkoopprijs van de leverancier is de basis / uitgangspunt van de berekening:
- De advies-/verkoopprijs en korting zijn hierbij zichtbaar in de regels.

| Adviesprijs | Korting | Inkoopprijs | Opmerking |
| --- | --- | --- | --- |
| leverancier |  | Inkoopprijs leverancier |  |
| 30,00 | 50% | 15,00 | 30 -15 = 15 (is 50% van 30)Korting wordt berekend |
|  |  |  |  |
|  |  | Wijziging naar: |  |
| 30,00 | 33,33% | 20,00 | Korting herberekend |
|  |  |  |  |
|  | Wijziging naar: |  |  |
| 30,00 | 25,00 | 22.50 | Inkoopprijs herberekend |
|  |  |  |  |
| Wijziging naar: |  |  |  |
| 40,00 | 25,00 | 30,00 | Inkoopprijs herberekend |

Belangrijk: Bij een kortingsregeling wordt deze korting toegepast.

Wat doe ik bij de melding 'Minimum orderbedrag niet bereikt'?

Als er een minimum orderbedrag bij de leverancier ingesteld is, verschijnt er een melding als het order bedrag kleiner is, als de order opgeslagen wordt.

- Pas eventueel de order aan / of wacht op meer artikelen / of bestel met mogelijke extra kosten.

Wat is er mogelijk met de knop Besteladvies?

Bij een inkooporder is het mogelijk om artikelen, die nodig zijn, toe te voegen voor deze leverancier. Om dit te doen, doorloopt u de volgende stappen:

1. Kies voor de knop Besteladvies.De Besteladvieslijst verschijnt op het scherm.
2. Ga terug, d.m.v. kruisje of druk de besteladvieslijst af.

Het artikel is toegevoegd in de regels.

Belangrijk: De inkooporder wordt ook aangevuld met artikelen waarvan deze leverancier niet de voorkeurleverancier is!

Is het mogelijk om verwijderde inkooporder regel weer terug te zetten in de 'Goedkeuren besteladvieslijst'?

Ja, dit is alleen mogelijk bij Centraal inkooporders aanmaken ja bij een gekoppelde verkooporder.

- Het kan immers zijn dat de leveranciers de goederen op backorder heeft / niet kan leveren. Hierdoor is het mogelijk om de artikelen bij een andere leverancier te bestellen.
- Bij het verwijderen van een gekoppelde inkooporder regel verschijnt (ook) de melding: Wilt u de gekoppelde regel uit de verkooporder in de bestellijst terugzetten.

Hoe koppel ik een inkooporder met een BTB verkooporder of werkorder?

Om een inkooporder met een order te koppelen, doorloopt u de volgende stappen:

1. Geef de artikelcode en aantal in de regels in.
2. Vul in de kolom BTB VO of WO in: VO bij een verkooporder.
3. WO bij een werkorder.
4. Enter vervolgens door (tot eind van de regel). Het scherm Koppeling inkooporder met verkooporder verschijnt.
5. Geef de relatie en ordernummer in.
6. Kies voor de knop Opslaan.

De inkooporder is gekoppeld met de order, waarop het artikel toegevoegd is.

- Normaal wordt een verkoop - of werkorder gekoppeld/besteld met een BTB inkooporder.Zie Koppeling werk-/verkooporder met inkooporder.

De uitgebreide / interne tekst van het artikel wordt **niet** meegenomen op de verkoop of werkorder.
Het koppelen van een kleine machine artikel is mogelijk, bij de ontvangst worden de SN op de VO bijgewerkt.

Wat gebeurt er als ik de valutacode wijzig bij een inkoopfactuur - of verkoopfactuur boeken?

De bedragen worden weergegeven in het scherm in de gekozen valuta.

- Deze bedragen worden omgerekend naar de eigen valuta.

- Koppeling werk-/verkooporder met inkooporder
- EPC bestand importeren
- Inkooporder versturen
- Hoe kan ik kosten achteraf op een machine boeken zonder werkorder?
- Boeken goederenontvangst

---
## Inkooporder details

Om de inkooporder details te bekijken, doorloopt u de volgende stappen:

1. Selecteren inkooporders (IS).
2. Selecteer de inkooporder.
3. Kies voor de knop Details.
4. Het scherm Inkooporder details verschijnt.
5. Bij een koppeling met een order, kan er in de kolom Bestemd voor doorgeklikt worden om de verkooporder (VO) of werkorder (WO) te bekijken.

#### FAQ

Waaruit kan ik de inkooporder details bekijken?

Dit is mogelijk vanuit de volgende programma's

- Opvragen inkooporders of Selecteren inkooporders via de knop Details.

Opvragen artikelen, tabblad Inkopen, of

Opvragen artikelen, tabblad In inkooporders,

- dubbel klik op de artikel inkooporder regel.

Wat zie ik bij de bon- of orderdetails?

Voor de (order) details wordt in vervolg XXX details gebruikt, het volgende weergegeven:

| XXX details | Order / datum | XXX status |
| --- | --- | --- |
| Relatiecode NAW gegevens Factuuradres / Afleveradres Contactpersoon | Referentie Ordergegevens Betalingsconditie Leveringsconditie Expeditiecode Verkoper / Inkoper Magazijn / kostenplaats | Factuur/datum of WO soort Ordertype Selectiecode Machine- of Projectdetails e.d.of Productie gegevens + structuur + aantal |

In de voet is het volgende te zien:

- Orderbedrag excl. BTW
- Notitie
- Print kopie
- Leveringeninfo instelling
- Dossier
- De oorspronkelijke XXX order (indien aanwezig).

Opmerking: De bedragen worden alleen getoond in de eigen valuta.

- Inkooporder

---
## Inkooporder

Het is mogelijk om inkopen handmatig op te geven of aan de hand van de besteladvieslijst de benodigde artikelen te laten berekenen.

#### Inkoopproces schema

Hieronder een schema van het inkoopproces.

De volgende onderwerpen worden behandeld:

- Selecteren inkooporders Inkooporder details

Besteladvieslijst (goedkeuren)

Nieuwe inkooporder aanmaken

Inkooporder wijzigen of verwijderen

Machine inkooporder

EDI / Digitale inkooporder aanmaken

Inkooporder versturen

Opvragen inkooporders

Inkoop rapportages

- Boeken goederenontvangst
- E-Inkoopfacturen inboeken
- Inkoopfactuur boeken

---
## Boeken inkooporder machines

#### Inkooporder ontvangen

Om inkoopfactuur te boeken, moet eerst de inkooporder ontvangen zijn.

*Klik hier voor meer informatie over het boeken van de goederenontvangst: Om dit doen, doorloopt u de volgende stappen: 1. Ga naar Selecteren inkooporders (IS). of Machines inkooporders (IM) vanaf versie 3.23. 2. Zoek en selecteer de inkooporder (met status Bestelbon). Opmerking: Geef de gewenste leverdatum, referentie en ordergegevens en inkoper op, ter herkenning van de order in de historie. • Met de toets ‘Page Down’ toets ga je direct door naar de regels. 3. Kies voor de knop Ontvangen. Het scherm Boeken goederenontvangst verschijnt. 4. Controleer het aantal en bedrag. 5. Kies voor de knop Einde Ontvangst. De inkooporder is ontvangen en de machine komt op voorraad te staan. Belangrijk: Een machine ontvangst mag niet via Machine ontvangst / levering (MVO) ontvangen worden, als deze op een inkooporder staat. #### Boeken inkoopfactuur Om een machine inkoopfactuur in te boeken, doorloopt u de volgende stappen: Indien de inkoopfactuur via de mail binnenkomt, wordt een van de volgende opties gebruikt: - E-facturen inboeken (eenvoudig) (KEI) of E-inkoopfacturen (geavanceerd) (KE). 1. Nadat hierbij de inkoopfactuur geselecteerd en de gevraagde gegevens ingegeven zijn. 2. Vink aan handmatig. 3. Kies voor de knop Boeken. 4. Het scherm Boeken goederenontvangst verschijnt. 5. Ga verder met stap 4. 1. Ga naar Boeken inkoopfacturen (KI). 2. Geef de relatie in. 3. Geef de factuurbedragen in. Opmerking: Indien er vanuit ander EU landen wordt ingekocht, dient er i.p.v. BTW-code 11, BTW-code 18 geselecteerd te worden. 4. Vink aan Machinefactuur. 5. Geef het betaalkenmerk en boekingstekst in. 6. Bij matchen: Kies voor de knop Matchen goederen. Het scherm Goederen ontvangst matching verschijnt. 7. Zie verder Goederenmatching. Geef de in en eventuele kostensoort. Controleer de gegevens of pas deze aan. Kies voor de knop Einde boekstuk. De machine is ingeboekt. #### FAQ - Alleen bij een inkoop grootboekrekening met kostendrager machine verschijnt het scherm Kostendrager, waarbij de balanswaarde verhoogd kan worden, vanaf versie 3.28. - Bij een machinefactuur, wordt bij het bijwerken van machinegegeven; chassisnummer of kenteken, ook deze machinegegevens bij een eventuele verkooporder bijgewerkt voor de Motor branche instelling, vanaf versie 3.27. Welke kostensoorten kan ik inboeken? De volgende kostensoorten kunnen ingeboekt worden bij een machine: - | Machine | Het servicenummer van de machine i.c.m. machinefactuur. optioneel. | | --- | --- | | Kostensoort | Optie voor kostensoort bij Boeken inkoopfacturen optioneel bij een machinefactuur:--VERKOOP--- Machine- BPM- Kosten achteraf (alleen geboekt op Kosten achter af bij Subadministratie machines is ja).- Overige kosten bij subadm. machine is ja ook geboekt op balans en inkoopwaarde, vanaf versie 3.28-- EXPLOITATIE-- vanaf versie 3.28:- Verzekering - Keuring- Afschrijving- OpbrengstInstelling: soort bedrijf is motorbranche:.- Korting, als machine nog op voorraad is, wordt de rekening voorraad marge ingevuld, en de balanswaarde verhoogd.- Overige kosten, geboekt op machine bij Overige kosten.NB Bij Machine / BPM verschijnt bij een machine met inkoopstatus Besteld/ Voorraad, de gekoppelde grootboekrekening, via de artikelgroep.Bij Machine adm. 2.0 is nee, zijn deze kosten zichtbaar bij F8 Tabblad Transacties | | --- | --- | Deze kosten zijn zichtbaar bij de Machine op tabblad Transacties. Wat gebeurt er bij het inboeken? Bij Einde boekstuk wordt de machine ingeboekt. - Bij Onderhoud machines (MBB), tabblad Financieel wordt de inkoopstatus voorraad. - De volgende transacties zijn geboekt bij Matching: Zonder matching wordt alleen Inkoopfactuur geboekt: - Er is hierbij sprake van een machine Subadministratie, met de volgende instellingen: - Bij een 'kostendrager' boeking, zijn de Boekstuk details te zien, als je dubbel klikt op de betreffende regel. Ik zie de optie machinefactuur* niet, hoe komt dat?

Bij Instellingen financieel, tabblad Grootboek moet Gebruik kostendragers op ja staan.

- Een kostendrager is een machine of dienst , waarop de gemaakte kosten toegerekend worden.
- Dit is een aparte module naast de kostenplaatsen.

Opmerking: Neem contact op met de planning om dit in te richten.

Hoe kan ik de machines controleren die ingekocht zijn?

1. Ga naar Controle machine inkopen (MVC). Het scherm Controlelijst machine inkoop verschijnt.
2. Geef een selectie op.
3. Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

Kan ik ook direct een kostendrager ingeven?

Een kostendrager kan ook direct op een machine of servicenummer geboekt worden.

1. Geef een grootboek in, waaraan een kostendrager is gekoppeld (in de regels). Als het vinkje machinefactuur uit staat, wordt deze pop-up alleen getoond als die overeenkomt met de inkooprekening van de artikelgroep, vanaf versie28.
2. Enter door.
3. Het scherm Kostendrager verschijnt.
4. Geef het servicenummer in. De inkoopstatus mag niet nvt of besteld zijn
5. Vink eventueel Nieuw (Overschrijven) aan. Belangrijk: Bij een niet gesloten machine administratie komt een al verkochte machine weer op voorraad te staan als je nieuw (overschrijven) kiest. * Controleer de status van de machine via F8.
6. Kies voor de knop Opslaan.Hierbij een voorbeeld van een kostendrager met een werkorder:
7. Op de betreffende werkorder wordt het artikel toegevoegd.

Klik hier voor meer informatie over het inkoopproces.

Het inkoopproces:

Het boeken van de inkoopfacturen is de laatste stap van het inkoopproces.

- Boeken goederenontvangst
- E-Inkoopfacturen inboeken
- Inkoopfactuur boeken

---
## Inkooporder versturen

- Inkoopproces schema

Als een inkooporder goed gekeurd is, wordt de bestelling verstuurd naar de leverancier. Dit gaat meestal per e-mail of via een EDI-order.

Om een inkooporder te versturen, doorloopt u de volgende stappen:

1. Ga naar Selecteren inkooporders (IS).
2. Selecteer de inkooporder.
3. Kies voor de knop E-mail.of Kies voor de knop EDI. Het volgende scherm verschijnt:Kies voor de knop Aanmaken.
4. De EDI order is aangemaakt.

Kies voor de knop Einde order.

De order is verzonden naar de leverancier

- De inkoopstatus gewijzigd van Openstaand naar Bestelbon.

Opmerking: Bij Selecteren inkooporders, kan d.m.v. de knop Ontvangen direct de artikel / regels ingeboekt worden, van de betreffende inkooporder, met status Bestelbon.

- Boeken goederenontvangst

---
## Inkooporder wijzigen of verwijderen

#### Wijzigen

Om een inkooporder te wijzigen, doorloopt u de volgende stappen:

1. Ga naar Selecteren inkooporders (IS).
2. Selecteer de inkooporder.
3. Kies voor de knop Wijzigen. Bij status Besteld verschijnt de melding Let op: Inkooporder is al definitief, toch doorgaan met wijzigen?
4. Kies voor de knop Ja.

Wijzig de benodigde gegevens.

Kies voor de knop Einde order.

De inkooporder is gewijzigd.

Opmerking: Bij een wijziging wordt gecontroleerd of alle artikelen/regels zijn geleverd. Als alles geleverd is, wordt de status van de inkooporder ontvangen. De order is dan niet meer zichtbaar op het inkooporder overzicht.

#### Orderbevestiging leverancier

Klik hier voor meer informatie over de orderbevestiging of wijzigen leverdatum:

Bij een order bevestiging door de leverancier, kan de gewenste leverdatum in de kop aangepast worden.

Als de inkooporder de status bestelbon heeft, verschijnt er bij het wijzigen van de gewenste leverdatum een pop-up, met de vraag: Wilt u de leveringsdatum van alle regels bijwerken?

- Opmerking: Als bij Ja handmatig nog een leverdatum in de regels, aangepast moet worden, sla dan eerst de order op en wijzig dan afwijkende leverdatum.

#### Verwijderen

Om een inkooporder te verwijderen, doorloopt u de volgende stappen:

1. Ga naar Selecteren inkooporders (IS).
2. Selecteer de inkooporder.
3. Kies voor de knop Wijzigen. Kies voor de knop Verwijderen.
4. Kies voor de knop Ja.
5. Bij elke gekoppelde BtB regel verschijnt de melding Wilt u de gekoppelde regel uit de order ook verwijderen.
6. Kies voor de knop Nee of Ja. Als alle regels uit een order verwijderd zijn, wordt de order zelf ook verwijderd.

De inkooporder is verwijderd.

#### Verwijderen meerdere inkooporders

Voor het verwijderen van meerdere inkooporders, doorloopt u de volgende stappen:

1. Ga naar Verwijderen inkooporders (IVV).
2. Geef een selectiecriteria in.
3. Kies voor de knop Verwijderen. Bij print verslag 'Ja' verschijnt er een overzicht van de verwijderde gegevens.

De inkooporders zijn verwijderd.

---
## Inkoop prijsafspraken

In de meeste gevallen is de inkoopkorting mede afhankelijk van de wijze van bestellen. Daarom kan per leverancier voor maximaal 5 verschillende ordersoorten of types, zoals spoed-, week- en seizoenorders of het kortingspercentage worden ingegeven. Deze leveranciersafspraken worden voor de artikelen vastgelegd per hoofd- en subgroep en per leverancierscatalogus. Bij het aanmaken van een bestelbon wordt op basis van het inkoop ordertype automatisch het juiste kortingspercentage voorgesteld.

### Inkoop prijsafspraken

De inkoop prijsafspraken kunnen ingegeven worden per leverancier.

Opmerking: De inkoop prijsafspraken gelden niet per artikel maar per hoofd- en subgroepen.• De hoofd- en subgroepen moeten overeenkomen met die van de leverancier.• Als bij de catalogus update instellingen prijsafspraken toepassen op ja staat, duurt het downloaden wat langer omdat de prijsafspraak door berekend wordt.

Om dit te doen, doorloopt u de volgende stappen:

1. Ga naar Inkoop prijsafspraken (API).
2. Kies voor de knop Wijzigen. of Kies voor de knop Opvoer.
3. Selecteer de leverancier, met de combinatie: Hoofd-/Subgroep.
4. Geef in de matrix de kortingsafspraken op. Opmerking: Korting 1 en Marge 1 t/m 5 zijn de ordertypes, zie Onderhoud ordertypes.
5. Kies voor de knop Opslaan.

De korting is actief, vanaf de startdatum t/m de einddatum als deze zijn ingegeven.

FAQ

- De regels, staffels 1 t/m 5 kunnen voor staffelkorting gebruikt worden (horizontaal).
- De kolommen korting 1 t/m 5 kunnen voor de ordertypes gebruikt worden (verticaal).

### Inlezen catalogi/prijsbestanden leverancier

Bij het automatisch inlezen van catalogi van leveranciers kunnen de prijzen 1:1 worden overgenomen, of met een factor worden omgerekend naar de inkoopprijs.

Het kortingspercentage van de leverancier kan in Powerall Connect middels een factor per productgroep worden vastgelegd, zodat de bruto verkoopprijs of advies verkoopprijs van de leverancier bij import automatisch wordt omgerekend naar de juiste netto inkoopprijs. Zodra een nieuwe prijscatalogus wordt ingelezen, worden de inkoopprijzen via deze factor aan het nieuwe prijspeil aangepast.

Dit stelt u in bij Onderhoud catalogi (AGT) op de betreffende catalogus.

Let op! Bij Onderhoud catalogi (AGT) tabblad Algemeen, mag je geen vaste kostprijs factor invullen, omdat anders de complete prijslijst een vast percentage korting berekend krijgt. De kostprijsfactoren bij de artikelen worden ook gebruikt bij goederen matching, en zorgen dan voor een foutieve matching.

- FAQ Prijsafspraken
- Offerte calculatie
- Onderhoud ordertypes
- Prijsafspraken rapportages
- Verkoop prijsafspraken

---
## Inkoop rapportages

Van de Inkoopgegevens is het mogelijk om een uitgebreide of verkort overzicht met selecties aan te vragen. Daarnaast kunnen Bestelbonnen (opnieuw) worden afgedrukt via 'Printen bestelbon'.

Om een overzicht aan te vragen, doorloopt u de volgende stappen:

1. Ga naar Overzichten inkooporders (IL).
2. Selecteer het overzicht:Inkooporders uitgebreid (ILB): Overzicht van de inkopen met uitgebreid informatie, zoals artikelen en teksten, (totaal)bedragen.
3. Inkooporders verkort (ILV): Overzicht van de inkooporders met beperkte gegevens incl. orderdatum, referentie, betaalconditie, totaalbedrag, selectiecode en status (leeg is openstaand en 1 is bestelbon).
4. Printen bestelbon (ILD): Dit zijn alle bestelbonnen van de openstaande inkooporders.

Geef een selectie op.

Kies voor de knop Afdrukken.

Het overzicht verschijnt op het scherm.

- Wat kan ik allemaal doen met een overzicht?

---
