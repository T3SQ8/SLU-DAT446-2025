Se föreläsning 9: Object-Oriented programming eller `intro-till-oop.md`

# Uppgift 1: Rektangeln

I några tidigare uppgifter blev ni tillfrågade att skapa lite geometriska funktioner. Nu ska vara göra en liknande sak men istället ska vi använda en klass.

## Del A: Skapandet av klassen

1. Skapa en klass `Rectangle`
2. Lägg till en konstruktor (alltså en `__init__()`). Rektangeln ska ha instansvariabler bredd & höjd samt position i x & y-led. Denna position beskriver rektangelns nedre vänstra hörn. (Antingen sparas x&y som enskilda variabler eller med en hjälpklass `Punkt()` som den beskrevs i `intro-till-oop.md`)

## Del B: Några enkla metoder

1. Skapa en metod `get_perimeter` som ska svara med rektangelns omkrets
2. Skapa en metod `get_area` som ska svara med rektangelns area
3. Skapa en metod `get_middle` som ska svara med rektangels mittpunkt (antingen som en lista (x,y) eller som en instans av klassen punkt)

## Del C: Fler metoder

1. Skapa en metod `intersects` som ska undersöka om de två rektanglarna skär varandra. Metodskalet ska se ut så här:

```python
def intersects(self, rectangle_2: Rectangle) -> bool:
    # rectangle_2: Rectangle ser till att datatypen som tas in är en instans av Rectangle och inte något annat
    # -> bool säkerställer att funktionen returnerar en bool (alltså True/False)
    pass

```

> Tips för ifall du har svårt att veta var du ska börja: Rita upp två generella trianglar och undersök först problemet matematiskt. När du vet hur du löser problemet matematiskt kan du sedan översätta det det till kod. 
