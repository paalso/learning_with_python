def intertsect_segments(segment1, segment2):
    left1, right1 = segment1
    left2, right2 = segment2

    return left1 <= left2 <= right1 or left2 <= left1 <= right2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, topleft, width, height):
        self.topleft = topleft
        self.width = width
        self.height = height

    def get_topleft(self):
        return self.topleft

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_vertices(self):
        x, y = self.topleft.get_x(), self.topleft.get_y()
        topright = Point(x + self.width, y)
        bottomleft = Point(x, y - self.height)
        bottomright = Point(x + self.width, y - self.height)
        return (self.topleft, topright, bottomleft, bottomright)

    def get_x_projection(self):
        return (self.topleft.get_x(), self.topleft.get_x() + self.width)

    def get_y_projection(self):
        return (self.topleft.get_y() - self.height, self.topleft.get_y())

    def point_inside(self, point):
        x, y = point.get_x(), point.get_y()
        x_left, y_upper = self.topleft.get_x(), self.topleft.get_y()
        x_right, y_lower = x_left + self.width, y_upper - self.height
        return x_left <= x <= x_right and y_lower <= y <= y_upper


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f'({self.center}, radius: {self.radius})'

    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius

    def point_in_circle(self, point):
        return self.center.dist(point) <= self.radius

    def rect_in_circle(self, rect):
        return all(map(lambda p: self.point_in_circle(p), rect.get_vertices()))

    def get_x_projection(self):
        return (self.center.get_x() - self.radius,
                self.center.get_x() + self.radius)

    def get_y_projection(self):
        return (self.center.get_y() - self.radius,
                self.center.get_y() + self.radius)

    def rect_circle_overlap(self, figure):

        if figure.point_inside(self.center):
            return True

        figure_vertices = figure.get_vertices()
        if all(map(lambda p: not self.point_in_circle(p), figure_vertices)):
            return False

        fig_x_projection = figure.get_x_projection()
        fig_y_projection = figure.get_y_projection()

        x_intertsection = \
            intertsect_segments(self.get_x_projection(), fig_x_projection)
        y_intertsection = \
            intertsect_segments(self.get_y_projection(), fig_y_projection)

        return  x_intertsection and y_intertsection
