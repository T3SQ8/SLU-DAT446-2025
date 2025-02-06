
Se föreläsning 2, "Program design and functions".


# Abstraction, Modularity, Maintainability

Du och din vän sammarbetar på ett skolprojekt. På er gemensamma projektmapp
laddar din vän upp en fil med namnet [`program.py`](program.py). Öppna filen
och testa att köra den. Kan du indentifera och fixa de misstag som gör det
otydligt exakt vad koden har för uppgift?

> - [x] Filens namn är inte beskrivande. Det kan inte heller vara då programmet
>   har flera olika orelaterade uppgifter.
> - [x] Variabelnamn står i både engelska och svenska. I detta fall är det
>   tänkt att användaren ska interagera med programmet på svenska men jag
>   väljer att variabelnamnen ska vara på engelska. Variabelnamnen står i
>   camelCase istället för snake\_case. Det är okej om en specifik stil har
>   bestämts i förväg, men för Python är snake\_case
>   vanligare.
> - [x] Vissa variabelnamn, `v`, `q`, etc. är för korta och inte beskrivande.
> - [x] Ingen IPO separation. Input/output sker runt processen, jag kan fixa
>   det till viss del men framöver ska vi separera outputen genom att
>   `return`:a från funktioner.
> - [x] Ingen abstraktion/moduläritet. De olika uppgifterna kan delas upp i
>   flera funktioner.
> - [x] Programmet har ingen felhantering. Den kraschar inte om man skriver en
>   sträng istället för ett nummer, men programmet bör testa att inputen är av
>   typen den förväntar sig. Framöver ska vi felhantera ordentligt genom `try`,
>   `except`, `finally`.
>
> Jag skriver om programmet och döper den till
> [`lab_computation.py`](lab_computation.py).


# If statments

Vad kommer att ske i följande `if`-statements?

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the event.")
```

```python
is_raining = False
has_umbrella = True

if is_raining or has_umbrella:
    print("You're good to go outside.")
```

```python
is_sunny = False

if not is_sunny:
    print("It's not sunny today.")
```

```python
is_weekend = True
is_holiday = False
work_due = True

if (is_weekend or is_holiday) and not work_due:
    print("You can relax!")
else:
    print("You have work to do.")
```

```python
temperature = 30
humidity = 80

if temperature > 25 and (humidity < 60 or not temperature > 35):
    print("The weather is okay.")
else:
    print("It's either too hot or too humid.")
```

```python
username = ""

if not username:
    print("Please enter a username.")
```


# Top-down design

Designa ett online checkout system. Den ska ta in läsa in en kunds kundvagn
från [`customers.py`](customers.py) och skriva ut de artiklar som vagnen
innehåller och vad varje artikel kostar. I slutet ska den skriva ut vad totala
beloppet är. Använd `range` för att numrera artiklarna när den skrivs ut.


> Exempellösning finns i [`checkout.py`](checkout.py)


# Eval

Vad gör `eval` funktionen? Varför bör man undvika den?

> `eval` är en inbyggd funktion i Python som exekverar en sträng. t.ex.
> ```python
> x = 10
> result = eval("x + 5")
> print(result)  # Output: 15
> ```
> 
> Innehållet i denna sträng kan ibland vara osäker och farlig, t.ex. kan det vara
> ett komando för att rensa alla filer på systemet.


# Return


Fram tills nu har vi inte använt `return` i någon av våra funktioner. Kör
följande kod. Varför skrivs inte resultatet ut? Vad finns det för fördelar med
`return` över att skriva ut resultatet varje gång?


```python
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
```

> Med `return` kan jag spara funktionen värde till en variabel, som i exemplet
> ovan. Jag kan skicka den `return`:ade värdet till en annan funktion, t.ex.
> `int(input("Ange ett nummer: "))`. I andra fall kan jag `return`:a t.ex.
> object, funktioner eller annat som inte kan/bör visas för användaren.


# Scope


```python
x = 10

def func():
    y = 5
    print("x:", x)
    print("y:", y)

func()

print("x:", x)
print("y:", y)
```

Varför får jag ett felmeddelande som säger att variabeln `y` är odefinerad. Hur
kan jag fixa detta?


> Variabeln `y` har definerats inom `func`, dvs att den har en local scope till
> funktionen och kan inte nås utanför den. `x` däremot är inte definerad inom
> någon funktion och kan därför nås i slutet av filen. För att göra `y`
> tillänglig kan vi returna den från `func` och assigna den till en variablel
> med `=`.
