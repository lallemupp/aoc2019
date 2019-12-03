import math

if __name__ == '__main__':
    mass = int(input('mass of module:'))
    rounded = math.floor(mass / 3)
    neededFuel = rounded - 2
    print("fuel needed = ", neededFuel)
