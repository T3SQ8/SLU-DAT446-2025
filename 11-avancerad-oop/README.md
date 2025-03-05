Se föreläsning 11: Advanced Object-Oriented programming

Fokus på denna uppgift är att få en grundläggande förståelse för arv eller *inheritance*.

> Disclaimer: OOP generellt och arv är ett djupt kaninhål och är något du kan spendera oräkneliga timmar på att lära dig allt omkring, denna uppgift (och demot) ska täcka grunderna. 

# Programskal för datorspel

Du jobbar på ett bolag som håller på att utveckla ett spel, mer specifikt ett zeldaliknande RPG á la gammalt. För speldesignern är det väldigt viktigt att kunna spara, hantera & använda olika typer av föremål. Din uppgift blir därför alltså att bygga ett programskal som ska kunna hantera stora mängder olika föremål.

## Tre typer av föremål

Programmet ska kunna hantera tre olika typer av föremål: Vapen, Mat och Rustning.

Alla föremål ska hå:
- Ett namn
- En sällsynthet 
- En vikt (odefinierad enhet)
- En modell (en bild i form av en filsökväg)
- Ägare (ska vara `None` från initiering)

För grundläggande datatyper (string, int, float etc) är det tydligt vad som det innebär att skriva ut ett objekt. Men för andra klasser, såsom de vi själva implementerar är det inte helt tydligt. 

```python

print(testItem) # ger <__main__.Item object at 0x0000027EC5276900>

```

För att lösa detta problem vill vi implementera en såkallad dundermetod (såsom `__add__`, `__init__` etc, oroa er inte för mycket hur dessa fungerar "i grunden"). Denna gång är det `__repr__`-metoden. Denna skall returnera en sträng som kommer att ge svaret på vad som händer när jag kör kodstycker ovan. 

```python
# __repr__-metoden implementerad

print(testItem) # Test, Common item: 5 kg, Model: path.jpg, Owner: None 
```

## Mat

Utöver alla attribut (instansvariabler) som alla föremål har ska all mat ha:
- En ättid (i sekunder)
- Hur mycket hälsa användaren får tillbaka från maten

Implementera även funktionen `__repr__` för klassen. Om du vill komma åt den funktion för klassen "Item" anropar du metoden genom `super().__repr__()`. 

## Vapen 

Utöver alla attribut (instansvariabler) som alla föremål har ska alla vapen ha:
- En räckvidd (i pixlar)
- En minimiskada
- En maximumskada

Vapnet ska även ha en funktion `get_damage` som ge ett slumpmässigt heltal som ska vara i intervallet mellan minimiskadan & maximumskadan.

Implementera även funktionen `__repr__` för klassen. 
## Rustning

Utöver alla attribut (instansvariabler) som alla föremål har ska all rustning ha:

- En absorptionschans (i %, vilken chans rustningen har att absorbera en träff )
- Maximal utthållighet (i antal absorptioner)
- Nuvarande Uthållighet (i antal absorptioner). Vid initiering ska denna vara densamma som den maximala utthålligheten

En klassmetod `hit` som ska returnera huruvida en inkommande träff kommer att träffa användaren eller rustningen. Metoden ska:
- Utvärdera om träffen går igenom eller träffar rustningen
- Om träffen går igenom (alltså INTE absorberas) ska den inkommande skadan returneras
- Om träffen absorberas (alltså inte går igenom) ska den nuvarande utthålligheten uppdateras (minskas med 1) och skadan 0 ska returneras. 

Implementera även funktionen `__repr__` för klassen. 