import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def euclidean_distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

# Take user input for the coordinates of the first point
x1 = int(input("Enter the x-coordinate of the first point: "))
y1 = int(input("Enter the y-coordinate of the first point: "))
point1 = Point2D(x1, y1)

# Take user input for the coordinates of the second point
x2 = int(input("Enter the x-coordinate of the second point: "))
y2 = int(input("Enter the y-coordinate of the second point: "))
point2 = Point2D(x2, y2)

# Calculate and print the Euclidean distance
distance = point1.euclidean_distance(point2)
print(f"The Euclidean distance between ({point1.x}, {point1.y}) and ({point2.x}, {point2.y}) is: {distance}")
