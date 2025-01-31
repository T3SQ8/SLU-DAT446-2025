
Se föreläsning 3, "Number representations and Arithmetics". Se till att även ta
hänsyn till det som vi har lärt oss tidigare om modularity, reusability, mm.

# Grundläggande floating-point arithmetic

Skriv en Pythonfunktion som beräknar arean av en cirkel givet dess radie.
Använd formeln:

$$
Area = \pi \cdot r^2
$$

* Använd `math` bibloteket för att hämta värdet på $\pi$.
* Avrunda till två decimaler med `round()`




# Ränta på ränta-beräkning

Skriv ett Python-program för att beräkna ränta på ränta för en given
huvudsumma, årlig räntesats och tidsperiod i år. Använd formeln:

$$
A = P \cdot (1 + \frac{r}{n})^{n \cdot t}
$$


där:

* `A` är det slutliga beloppet,
* `P` är huvudsumman,
* `r` är den årliga räntesatsen (som ett decimaltal),
* `n` är antalet gånger räntan beräknas per år (använd 12 gånger men gör så att användaren kan ändra
  detta värde utan att skriva om koden.
  [HINT](https://www.geeksforgeeks.org/default-arguments-in-python/)),
* `t` är tiden i år.
* Avrunda det slutliga beloppet till 2 decimaler med `round()`.



# Avstånd mellan två punkter

Skriv ett Python-program för att beräkna avståndet mellan två punkter
$(x_1,y_1)$ och $(x_2,y_2)$. Använd formeln:

$$
d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
$$

* Använd funktionen `math.sqrt()` för att beräkna kvadratroten.
* Avrunda resultatet till 2 decimaler med `round()`.


# Simulering av exponentiell tillväxt



Skriv ett Python-program för att simulera exponentiell tillväxt med formeln:

$$
y = y_0 \cdot e^{k \cdot t}
$$


där:

* $y$ är det slutliga värdet,
* $y_0$ är startvärdet,
* $k$ är tillväxttakten,
* $t$ är tiden.
* Använd funktionen `math.exp()` för att beräkna exponentialtermen.
* Avrunda det slutliga värdet till 4 decimaler med `round()`.


# Trigonometriska beräkningar

Skriv ett Python-program som:

1. Tar en vinkel i grader som indata från användaren.
2. Omvandlar vinkeln till radianer med `math.radians()`. Se
   [dokumentationen](https://docs.python.org/3/library/math.html#math.radians)
3. Beräknar sinus, cosinus och tangens för vinkeln med `math`-biblioteket.
4. Avrundar varje resultat till 4 decimaler med `round()`.

# Lösning av andragradsekvation

Skriv ett Python-program för att lösa en andragradsekvation av formen:

$$
ax^2 + bx + c = 0
$$

Använd formeln:

$$
x = \frac{-b \pm \sqrt{b^2 -4ac}}{2a}
$$


Hantera fall där diskriminanten $b^2-4ac$ är negativ genom att skriva ut "Inga reella rötter."



# NumPy-arrayoperationer (Svårare)

Du kommer att behöva läsa i NumPy dokumentationen för
[`numpy.random.rand`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html),
[`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html).

Skapa ett Python-program som:

1. Genererar en NumPy-array med X antal (testa med 10 st) slumpmässiga flyttal mellan 0 och 1.
2. Kvadrerar varje element i arrayen med exponentiering.
3. Beräknar medelvärdet av de kvadrerade värdena.
4. Avrundar medelvärdet till 3 decimaler med `round()`.



# NumPy-matrisoperationer (Svårare)


På samma sätt som ovan, sök i NumPy dokumentationen efter funktioner som kan uppfylla denna roll.
(HINT: `numpy.random.uniform`, hur kan man justera dimensionerna?)

Skapa ett Python-program som:

1. Genererar två $2 \times 2$-matriser slumpmässiga flyttal mellan 0 och 10 med NumPy.
2. Beräknar elementvis exponentiering av den första matrisen upphöjd till den andra matrisen.
3. Avrundar varje element i den resulterande matrisen till 2 decimaler med `round()`.


