
Se föreläsning 2, "Program design and functions".


# Abstraction, Modularity, Maintainability

Du och din vän sammarbetar på ett skolprojekt. På er gemensamma projektmapp
laddar din vän upp en fil med namnet [`program.py`](program.py). Öppna filen
och testa att köra den. Kan du indentifera och fixa de misstag som gör det
otydligt exakt vad koden har för uppgift?


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




# Eval

Vad gör `eval` funktionen? Varför bör man undvika den?


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


