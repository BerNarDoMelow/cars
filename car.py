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

    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Space:

    def __init__(self, x, y,name):
        self.point = Point(x,y)
        self.name = name

    def positions(self):
        return (self.point)

    def _str_(self):
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
            self.direction = 'H'
        else:
            self.direction = 'V'

    def positions(self):
        if self.size() == 1:
            return (self.begin, self.end)
        else:
            return (self.begin, self.middle(), self.end)

    def size(self):
        if self.direction == 'V':
            return abs(self.begin.y - self.end.y)
        return abs(self.begin.x - self.end.x)

    def middle(self):
        if self.direction == 'V':
            return Point(self.end.x, self.begin.y + 1)
        return Point(self.begin.x + 1,self.begin.y)

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

    def distance(self,car,position):
        if self.direction == "V" and position == "up":
            return abs(self.begin.y - car.end.y)
        elif self.direction == "V" and position == "down":
            return abs(self.end.y - car.begin.y)
        elif self.direction == "H" and position == "esq":
            return abs(self.begin.x - car.end.x)
        elif self.direction == "H" and position == "dir":
            return abs(self.end.x - car.begin.x)


    def distanceToWall(self,position,boardSize):
        if self.direction == "V" and position == "up":
            return self.begin.y
        elif self.direction == "V" and position == "down":
            return boardSize - self.end.y - 1
        elif self.direction == "H" and position == "esq":
            return self.begin.x
        elif self.direction == "H" and position == "dir":
            return boardSize - self.end.x - 1

    def __eq__(self,car):
        return self.begin.x == car.begin.x and self.end.x == car.end.x

    def __str__(self):
        return  "[({0},{1}), ({2},{3})] : Car {4}".format(
            self.begin.x, self.begin.y, self.end.x, self.end.y, self.name
            )

    def __repr__(self):
        return "[({0},{1}), ({2},{3})]".format(self.begin.x,self.begin.y,self.end.x,self.end.y)

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end
