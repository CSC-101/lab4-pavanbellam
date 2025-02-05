import data
import math
# Write your functions for each part in the space below.

# Part 1
def first_element(l1):
        return[ ele[0] for ele in l1]


# Part 2
def x_coordinates(l1):
        return [i.x for i in l1]

# Part 3
def are_in_positive_quadrant(l1):
        return[ i for i in l1 if i.x >= 0 and i.y >= 0]

# Part 4
def distance(p1, p2):
        return math.sqrt(((p1.x - p2.x)**2)-((p1.y - p2.y)**2))

# Part 5
def manhattan_distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Part 6
def distance_all(l1):
        return[((i.x)**2 + (i.y)**2)**0.5 for i in l1]

