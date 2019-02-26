class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Space:

    def __init__(self, x, y):
        self.point = Point(x,y)

    def _str_(self):
        return "({0},{1})".format(self.point.x, self.point.y)

    def _repr_(self):
        return "({0},{1})".format(self.point.x, self.point.y)

class Car:

    def __init__(self, name):
        self.begin = None
        self.end = None
        self.name = name
        self.direction = None

    def set_begin(self, x, y):
        self.begin = Point(x,y)

    def set_end(self, x, y):
        self.end = Point(x,y)
        if self.begin.x != self.end.x:
            self.direction = 'v'
        self.direction = 'H' 

    def positions(self):
        if self.size() == 2:
            print('ss')
            return (self.begin, self.end)
        else:
            print('ssss')
            print(self.size())
            return (self.begin, self.middle(), self.end)

    def size(self):
        if self.direction == 'V':
            return abs(self.begin.x - self.end.x) + 1
        return abs(self.begin.y - self.end.y) + 1

    def middle(self):
        if self.direction == 'V':
            return Point(self.begin.x - self.end.x, self.begin.y)
        return Point(self.begin.x, self.end.y - self.begin.y)

    def move_down(self, moves):
        self.set_begin(self.begin.x, self.begin.y + moves)
        self.set_end(self.end.x, self.end.y + moves)

    def move_up(self, moves):
        self.set_begin(self.begin.x, self.begin.y - moves)
        self.set_end(self.end.x, self.end.y - moves)

    def move_left(self, moves):
        self.set_begin(self.begin.x - moves, self.begin.y)
        self.set_end(self.end.x - moves, self.end.y)

    def move_right(self, moves):
        self.set_begin(self.begin.x + moves, self.begin.y)
        self.set_end(self.end.x + moves, self.end.y)

    def __str__(self):
        return  "[({0},{1}), ({2},{3})] : Car {4}".format(
            self.begin.x, self.begin.y, self.end.x, self.end.y, self.name
            )

    def __repr__(self):
        return  "[({0},{1}), ({2},{3})] : Car {4}".format(
            self.begin.x, self.begin.y, self.end.x, self.end.y, self.name
            )

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end
