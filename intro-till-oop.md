# Objektivt orienterad programmering (OOP)

## Vad är en klass? 

En klass är ett så kallat objekt, eller en sak. Kort sagt går det att beskriva en klass som ett strukturerat sett att lagra data samt att operera på, alltså förändra eller omformatera den datan. Programmeringsmässigt kan klassen i din kod ses som en 'mall'. När du vill använda klassen skapar du (vanligtvis, för specialfall se *statiska klasser*) behöver du ha en instans. Exempelvis, om vi har en klass som heter 'bil' kanske vi har en instans av den klassen som heter 'Volvo V70' som har vissa specifika mått & specifikationer (variabler). Däremot är sättet vi vill operera på datan densamma (exempelvis att uppdatera bränslemängden när vi kör).

> Ett annat sätt att se på klasser är som en datatyp (vilket de är). I vårt exempel skapar vi alltså datatypen Bil med tillhörande information och klassfunktioner (som vanligtvis kallas för metod) precis som att datatypen String har tillhörande information och metoder. 

```python

class Bil():
    def __init__(self, length, fuel, efficiency):
        self.length = length
        self.fuel = fuel
        self.efficiency = efficency 

    def drive(self, distance):
        # <Nånting som borde hända när bilen kör>
        pass

```

### Init-funktionen (Konstruktorn)

Alla klasser (som inte är statiska) behöver en så kallad konstruktor (`__init__()`-funktion). Denna funktion körs när en instans av en klass skapas. Om konstruktorn har funktionsparametrar (i vårt fall length, fuel och efficiency) skrivs de in när instansen skapas av klassen.

```python

volvo_v70 = Bil("3m", 100, 0.5)

```

### Vad är 'self'
#### Variabler
Inuti en klass används keywordet 'self' väldigt mycket. Det innebär att du försöker komma åt någonting från instansen av klassen som anropade metoden. Exempelvis om du vill komma åt hur mycket bränsle en viss instans av klassen bil har kvar.

```python

def get_fuel_percentage(self):
    return self.fuel

```

I exemplet med funktionen drive innebär det att också att metoden endast påverkar instansen som anropade funktionen och inte hela klassen. 

#### Metoder

Om du inuti din klass vill anropa en metod från klassen ska även här keywordet 'self' användas. Ett exempel kan vara i vår drive-metod

```python
def drive(self, distance):
    old_fuel = self.fuel # Går även att använda self.get_fuel_percentage()

    usage = distance*efficiency

    self.fuel = old_fuel - usage # Uppdaterar fuel-variabeln för den specifika instansen av Bil som anropade drive()
```

> **OBS**: När du anropar en metod utanför klassens kod använder du {instansnamn}.{metodnamn}. Om du anropar metoden från inuti klassens egna kod anropar du med metoden med self.{metodnamn}.

## Varför ska vi använda klasser?

Klasser är ett sätt att strukturera & gruppera data sådant att data hänger ihop med varann. Ett exempel på detta är som i Laboration 2 där en grupp av punkter ska plottas. För att plotta dessa används 2 listor som innehåller X-koordinater respektive Y-koordinater. Problemet med detta är då alltså att de olika listorna innehåller data som ska hänga ihop men de gör de inte i praktiken.
 
Istället använder vi en klass, som vi kaller för Punkt

```python
class Punkt():
    def __init__(x_position, y_position):
        self.x_pos = x_position
        self.y_pos = y_position

```

Om vi nu återigen vill lagra en lista med punkter kan vi istället för att ha två separata listor för X & Y krävs endast en lista.

```python

points = list()

points.append(Punkt(1, 2))
points.append(Punkt(2, 3))
points.append(Punkt(3, 4))
points.append(Punkt(4, 5))

```

Om vi nu vill hitta punkt nr 3 (räknat från 0) skriver vi då:

```python
chosen_point = points[3]

print("X:", chosen_point.x_pos, "Y:" chosen_point.y_pos)
```

En annan fördel med att använda klasser är att om vi exempelvis nu skulle vilja bygga en funktion som beräknar avståndet mellan 2 punkter. Inuti vår klass Punkt skriver vi då en ny funktion avstånd som ger avståndet mellan den givna punkten som anropar metoden och en valfri punkt vi skriver in.

> Notera, koden `other_point: Punkt` innebär att vi tar en variabel som vi kallar för other_point, det som är efter :-tecknet är vilken klass (datatyp) som det måste vara. Detta innebär alltså att vi **vet** att variabeln som skickas in en är en punkt.

```python

def avstånd(self, other_point: Punkt):
    return math.sqrt((self.x_pos - other_point.x_pos)**2 + (self.y_pos - other_point)**2)

```

Alltså fungerar klassen som ett sätt att gruppera kod. Vi kan *abstraktera* kod och ge data en slags kontext, som att vi gör om 2 stycken tal till en punkt. Därefter gör vi något med datan, antingen som bara ger någonting men vi kan även vilja flytta datan och då är fördelaktigt att den är gruperad / kopplad.

Tänk nu att vi våran punkt exempelvis skulle beskriva pingis-bollen i en variant av det klassiska spelet Pong. För att flytta på punkten ska vi skapa en ny funktion som förändrar informationen i vår punkt.

Funktionen flytta ska ta in en hastighet, alltså en fart och en riktning (vinkel).

```python
def flytta(self, fart, riktning):
    # Först vill vi ta reda på hur snabbt punkten rör sig i x & y-led
    x_velocity = fart*math.cos(riktning)
    y_velocity = fart*math.sin(riktning)

    # Därefter vill vi uppdatera, alltså förändra tillståndet av vår punkt
    self.x_pos = self.x_pos + x_velocity
    self.y_pos = self.y_pos + y_velocity

```

Nu har ni fått en grundlig genomgång i vad en klass är och varför vi ska använda dem. Detta är grunderna till OOP men detta är ett väldigt djupt kaninhål som går att fastna i. Några ytterligare koncept inom OOP är:

1. Arv. Klasser som är en variant / specialfall av en annan klass. Exempelvis kan klassen 'Hund' ärva metoder och instansvariabler klassen 'Däggdjur'. Detta kommer det mer information om i en kommande 
2. Statiska metoder & variabler. En metod/variabel som inte beror på klassens instans utan för 'hela klassen'. Exempel kan vara en statisk variabel 'antal_användare' som ökar varje gång en ny instans av klassen 'Användare' skapas.
3. Privata metoder & variabler. En funktion som endast kan användas av klassen som äger metoden/variabeln. Detta är inte särskilt vanligt i python och går inte att göra på 'riktigt' men anses vara best-practice (men är inte inom kursen)
