
Fram tills nu har de flesta haft svårigheter med att hantera filer. I denna
uppgift ska du öva på att läsa filer och skapa dictionaries.



# Uppgift


Skapa en funktion som tar emot en lista av namn och ger tillbaka en dictionary
med en tuple för varje persons favorita numer och färg, som på följande vis,

```python
d = {
    'lucas': ('red', 8),
    'ava': ('pink', 5),
}
```


Funktionen ska kunna hantera felaktiga namn utan att avbryta (exempelvis via
`os.path.isfile()`). Se till att du kör din kod från rätt ställe så att den har
tillgång till båda `fav_colors/` och `fav_numbers/` mapparna.

