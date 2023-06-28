from catalog_points.points import Point
from catalog_points.figures import Line, Square

if __name__ == '__main__':
    point_a = Point(1, 1)
    point_b = Point(2, 3)
    print(point_a, point_b)
    Line_1 = Line(point_a, point_b)
    print(Line_1)
    print(Line_1.distance())
    sguare_1 = Square(point_a, point_b)
    pass