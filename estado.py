
from car import *

class Estado:
    def __init__(self, player, cars, spaces, board_exit, board_size):
        self.player = player
        self.cars = cars
        self.spaces = spaces
        self.board_exit = board_exit
        self.board_size = board_size


    def percept(self, car):
        perceptions = {

        }

        not_empty = []
        for car in self.cars:
            not_empty += car.positions()
        not_empty += [self.player.positions()]
        

        if car.direction == 'H':
            for each in [self.player] + cars:
                if car != each:
                    if car.begin.y == each.begin.y:
                        if car.begin.x + 1 == car.begin

                if each.end.y == car.end.y and each.end.x ==


    def get_empty_spaces(self):
        spaces = []
        for car in self.cars:
            spaces[]


    def __lt__(self,state):
        pass

    def __eq__(self,state):
        pass

    def __hash__(self):
        pass

    def __str__(self):
        board = [ ['' for x in range(self.board_size-1)] for y in range(self.board_size-1) ]
        for car in self.cars:
            print(car.positions())
            for position in car.positions():
                print(position)
                board[ position.y][ position.x ] = car.name+" "

        for position in self.player.positions():
            board[ position.y][ position.x ] = "? " 
    
        board[self.board_exit.point.y][self.board_exit.point.x] = "* " 
        
        for row in range(self.board_size-1):
            for col in range(self.board_size-1):
                if board[row][col] == '':
                    board[row][col] = '# '

        str_board = [ " ".join(row) for row in board]
        str_board = "\n\n".join(str_board)

        return str_board       




def from_file(file_name):

    cars = {}
    empty_spaces = []
    player = Car('?')
    board_size = 0
    board_exit = None

    with open(file_name, 'r') as f:
        y = 0
        for row in f.readlines():

            x = 0
            for col in row:
                if col == "#":
                    space = Space(x, y)
                    empty_spaces.append(space)
                
                elif col == "?":
                    if not player.begin:
                        player.set_begin(x, y)
                    else:
                        player.set_end(x, y)

                elif col == "S":
                    board_exit = Space(x, y)

                elif col == " " or col == '\n':
                    x -= 1

                else:
                    car = Car(col)
                    if col not in cars:
                        car.set_begin(x, y)
                        cars[col] = car
                    else:
                        cars[col].set_end(x, y)

                x += 1

            y += 1

    return Estado(player, list(cars.values()), empty_spaces, board_exit, y+1)

    
                    

estado = from_file("examples.txt")
print(estado)
estado.cars[0].move_left(1)
print(estado)
estado.player.move_down(1)
print(estado)