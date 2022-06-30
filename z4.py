class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(3, 4)
p2 = Point(3, 4)
print(hash(p1), hash(p2), sep='\n')
print(p1 == p2)