Se föreläsning 5: Data validation, control flow, exceptions and generators

# Förbättring av tidigare problem

**Vi utgår nu från funktionerna som vi skrev för förra föreläsningens uppgifter.**

1. Din funktion som beräknar medelvärde har ett problem, nämligen att den kan ta in vad som helst men endast listor & tuples som innehåller tal kan ha ett medelvärde. Skriv om funktionen sådan att listan endast kan innehålla tal samt att funktionen ska ge ett felmeddelande ifall listan/tuplen är felaktig.

2. Repetera samma sak fast för medianvärdesfunktionen. 

Filerna `average.py` & `median.py` är uppdaterade med den nya funktionen `validate_data.py`. Det är en generell funktion som fungerar på både. 

**Förbättring av extrauppgiften**
- Se till att endast ett naturligt tal kan anges som valet av n (samt att det inte är 0) och ge ett felmedellande ifall fel input ges
- Vad händer ifall listan är tom?
- Vad händer ifall n är större än listans längd?

Lösningen finns i filen `nth_largest.py`. Det är en modifierad variant av uppgiften från den tidigare föreläsningen.