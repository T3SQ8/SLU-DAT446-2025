from math import sqrt, pi

def get_triangle_info(sideA: float, sideB: float, sideC: float): 
    perimeter = sideA+sideB+sideC

    # This uses something known as 'Heron's Formula'
    sp = perimeter/2
    area = sqrt(sp*(sp-sideA)*(sp-sideB)*(sp-sideC))

    print(f"Omkrets: {perimeter}")
    print(f"Area: {area}")

def get_circle_info(radius: float):
    perimeter = pi*2*radius
    area = pi*(radius**2) 

    print(f"Omkrets: {perimeter}")
    print(f"Area: {area}")


def get_rectangle_info(sideA: float, sideB: float):
    perimeter = 2*sideA + 2*sideB
    area = sideA*sideB

    print(f"Omkrets: {perimeter}")
    print(f"Area: {area}")

def get_pentagon_info(side: float, apothem: float):
    perimeter = 5*side
    area = (1/2) * perimeter * apothem

    print(f"Omkrets: {perimeter}")
    print(f"Area: {area}")


def menu():
    while True:
        print("Välkommen till den geometriska miniräknaren! Välj vad vad för typ av figur du vill undersöka eller om du vill avsluta:")
        print("1. Triangel")
        print("2. Cirkel")
        print("3. Rektangel")
        print("4. Pentagon")
        print("5. Avsluta")
        
        selection = int(input().strip())

        if selection == 1:
            sideA = float(input("Vad är triangelns första sida? "))
            sideB = float(input("Vad är triangelns andra sida? "))
            sideC = float(input("Vad är triangelns tredje sida? "))
            get_triangle_info(sideA, sideB, sideC)

        elif selection == 2:
            radius = float(input("Vad är cirkelns radie? "))
            get_circle_info(radius)

        elif selection == 3:
            sideA = float(input("Vad är rektangelns första sida?"))
            sideB = float(input("Vad är rektangelns andra sida?"))
            get_rectangle_info(sideA, sideB)

        elif selection == 4:
            side = float(input("Vad är pentagonens sidlängd? "))
            apotheme = float(input("Vad är pentagonens apothem? "))
            get_pentagon_info(side, apotheme)

        elif selection == 5:
            break
menu()