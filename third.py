import math
from enum import Enum

first_route = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
second_route = ["U62","R66","U55","R34","D71","R55","D58","R83"]


class Direction(Enum):
    UPP = 'U'
    LEFT = 'L'
    DOWN = 'D'
    RIGHT = 'R'


class Path:
    def __init__(self, route):
        self.position = (0, 0)
        self.positions = []
        for step in route:
            direction = step[0]
            distance = int(step[1:])
            if direction == Direction.UPP.value:
                self.upp(distance)
            elif direction == Direction.LEFT.value:
                self.left(distance)
            elif direction == Direction.DOWN.value:
                self.down(distance)
            elif direction == Direction.RIGHT.value:
                self.right(distance)

    def upp(self, distance):
        for i in range(0, distance):
            (x, y) = self.position
            y += 1
            self.position = (x, y)
            self.positions.append(self.position)

    def left(self, distance):
        for i in range(0, distance):
            (x, y) = self.position
            x -= 1
            self.position = (x, y)
            self.positions.append(self.position)

    def down(self, distance):
        for i in range(0, distance):
            (x, y) = self.position
            y -= 1
            self.position = (x, y)
            self.positions.append(self.position)

    def right(self, distance):
        for i in range(0, distance):
            (x, y) = self.position
            x += 1
            self.position = (x, y)
            self.positions.append(self.position)

    def closest_intersection_with(self, other):
        intersections = list(set(self.positions) & set(other.positions))
        shortest_distance = float('nan')
        for intersection in intersections:
            (x, y) = intersection
            distance = (abs(x) + abs(y))
            if math.isnan(shortest_distance) or distance < shortest_distance:
                shortest_distance = distance
        return shortest_distance


if __name__ == '__main__':
    first = Path(first_route)
    second = Path(second_route)
    print(first.closest_intersection_with(second))
