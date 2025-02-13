Se föreläsning 5: Files & Dictionaries

# Hantering av spelinformation
En viktig del av programmering är förmågan att konvertera data från olika format och denna uppgift handlar just om att formatera om transkriberad rådata till ett format som lättare används vid programmering. Vi kommer att användas av .json-formatet, vilket i python motsvaras av en 'Dictionary'. Detta är en utav de enklaste varianterna av en strukturerad databas & kallas ibland för 'document database' & baseras på tanken av ett 'Key-value'-par. Tanken är då alltså att din dataset ska ha samma struktur & att du istället för vid exempelvis en nästlad lista (lista med listor) där du måste använda endast sifferindex kan du använda naturligt språk för att 'referera' till din 'nyckel' där datan (value) du är intresserad av finns.   

Du är en del av ett företag som ska göra om ett kortspel för att digitalisera det. Din kollega har redan börjat med att skriva ned kortens egenskaper och spara de i separate filer. Däremot finns det fortfarande lite att göra. I denna uppgift ska vi:
- Läsa in den transkriberade texten & lägga in det i en dictionary
- Spara dictionarien i en .json-fil för att spara den på ett sätt s.a datan är lätthanterbar.

## Del A: Inläsning av data
- Börja med att skriva en funktion som läser in en fil med formatet som finns i `transkiberad-data/charizard.txt`
  - Funktionen ska ge (returnera) en dictionary med samma format `konverterad-data/template.json`
- Skriv ytterligare en funktion som läser in alla data som finns i `transkriberad-data` & som konverterar datan med hjälp av den tidigare funktionen.
  -  Funktionen ska returnera en lista med alla dictionaries som innehåler den konverterade datan från `transkriberad-data`
  
> Vissa moves kan ha mer än kostnad, se `transkriberad-data/pikchu.txt`. Se till att ditt program kan hantera detta.

## Del B: Spara ned datan
- Skriv en funktion som givet en lista av dictionaries skriver en .json-fil, där varje dictionary ska sparas som en separat fil med samma namn som dictionaryt har attributet 'name'