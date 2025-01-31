
from customers import *

def checkout(customer):
    total_cost = 0
    # TODO: kan skrivas bättre via enumerate()
    for i in range(len(customer)):
        # TODO: kan skrivas bättre mha f-strings
        print(str(i+1) + ": " + customer[i][0] + ", " + str(customer[i][1]))
        total_cost += customer[i][1]
    print("Total:", total_cost)

# koden i denna if-statement körs endast när filen kallas som ett
# skript, och inte om den importeras
if __name__ == '__main__':
    checkout(bob)
    checkout(alice)
