Preparation inför Lab 2.

Se till att du har installerat NumPy och Matplotlib.

```bash
pip3 install numpy matplotlib # lägg till --user om det behövs
```


Kör möljnade kod för att generera och plotta slumpmässig data:

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
X = 2 * np.random.rand(100, 1)
Y = 4 + 3 * X + np.random.randn(100, 1)

plt.plot(X,Y, 'o')
plt.show()
```


Matplotlib är ett stort biblotek som har många sätt att visa data på. (Se några
exempel [här](docs-examples).) Leta i [dokumentationen](docs-plot) efter hur du
kan ändra utseendet av diagramet som `plot()` ritar.

[docs-examples]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#examples-using-matplotlib-pyplot-plot
[docs-plot]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib-pyplot-plot


I Lab 2 ska du testa på att implementera några NumPy funktioner i Python
istället för NumPys optimerade C kod. Kör följande kod för att se skillnaden.
Koden räknar tiden det tar kvadrera 10 milioner tal med Python listor samt
NumPy vektorer.

```python
import numpy as np
import time

# Using NumPy (vectorized)
arr = np.arange(10_000_000)
start = time.time()
arr_squared = arr ** 2  # Fast, happens in C
end = time.time()
print("NumPy time:", end - start)

# Using native Python (loop-based)
arr_list = list(range(10_000_000))
start = time.time()
arr_squared_list = [x**2 for x in arr_list]  # Slow, happens in Python
end = time.time()
print("Python list time:", end - start)
```
