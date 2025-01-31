import math
import numpy as np



def circle_area(radius):
    area = math.pi * radius**2
    return(area, 2)


def compound_interest(principal, rate, time, times_per_year=12):
    amount = principal * (1 + rate/times_per_year)**(times_per_year*time)
    return round(amount, 2)

def distance_between_points(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    round(distance, 2)

def exp_growth(start, rate, time):
    return round(start * math.exp(rate * time), 4)


def trig_calc(angle):
    rads = math.radians(angle)
    sin = math.sin(rads)
    cos = math.cos(rads)
    tan = math.tan(rads)
    return round(sin, 4), round(cos, 4), round(tan, 4)


def np_random_array(length):
    arr = np.random.rand(length)
    squared = arr**2
    mean = np.mean(squared)
    return round(mean, 3)


def np_random_matrix_squaring():
    matrix1 = np.random.uniform(0, 10, (2, 2))
    matrix2 = np.random.uniform(0, 10, (2, 2))
    result = np.round(matrix1**matrix2, 2)
    return(result)



def main():
    print(circle_area(5))

    p = 1000
    r = 0.05
    t = 10
    print(compound_interest(p, r, t))


    x1, y1 = 1, 2
    x2, y2 = 4, 6
    print(distance_between_points(x1, y1, x2, y2))


    y0 = 10
    k = 0.1
    t = 5
    print(exp_growth(y0, k, t))

    print(trig_calc(45))


    print(np_random_array(10))

    print(np_random_matrix_squaring())

if __name__ == '__main__':
        main()
