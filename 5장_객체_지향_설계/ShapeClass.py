import math


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x # 데이터 속성(attribute)
        self.y = y
    
    def distance_from_origin(self): # 메서드 속성
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return "point ({0.x!r}, {0.y!r})".format(self)
    
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x,y) # 생성 및 초기화
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)
    
    def area(self):
        return math.pi*(self.radius**2)
    
    def circumference(self):
        return 2*math.pi*self.radius
    
    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)
    
    def __repr__(self):
        return "circle ({0.radius!r}, {0.x!r})".format(self)
    
    def __str__(self):
        return repr(self)


# >>> import ShapeClass as shape
# >>> a = shape.Point(3,4)
# >>> a
# point (3, 4)
# >>> repr(a)
# 'point (3, 4)'
# >>> str(a)
# '(3, 4)'
# >>> a.distance_from_origin()
# 5.0
# >>> c = shape.Circle(3,2,1)
# >>> c
# circle (3, 2)
# >>> repr(c)
# 'circle (3, 2)'
# >>> str(c)
# 'circle (3, 2)'
# >>> c.circumference()
# 18.84955592153876
# >>> c.edge_distance_from_origin()
# 0.7639320225002102
