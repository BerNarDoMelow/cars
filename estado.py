
from car import *
from copy import deepcopy


class Estado:
    def __init__(self, all, exit, boardSize):
        self.all = all
        self.boardSize = boardSize
        self.exit = exit


    def percept(self, car):
        search_board = deepcopy(self.all)
        del search_board[car.name]
        if car.direction == "H":
            return {
                "esq": list(filter(lambda x:x.end.x < car.begin.x and (x.begin.y == car.begin.y or x.end.y == car.end.y or x.middle().y == car.end.y),list(search_board.values()))),
                "dir": list(filter(lambda x:x.begin.x > car.end.x and (x.begin.y == car.end.y or x.end.y == car.end.y or x.middle().y == car.end.y),list(search_board.values()))),
            }
        else:
            return {
                "up": list(filter(lambda x:(x.begin.x == car.begin.x or x.begin.x == car.end.x or x.middle().x == car.begin.x) and x.end.y < car.begin.y,list(search_board.values()))),
                "down": list(filter(lambda x: (x.end.x == car.end.x or x.begin.x == car.end.x or x.middle().x == car.begin.x) and x.begin.y > car.end.y,list(search_board.values()))),
            }


    def getPlayer(self):
        return list(filter(lambda x: x.name == "?",self.all.values()))[0]

    def is_empty_space(self,position):
        """

        :param position: tipo Point
        :return:
        """
        for each in self.all.values():
            if position in each.positions():
                return False
        return True

    def findInBoard(self,position):
        for each in self.all.values():
            if position in each.positions():
                return each
        return False

    def inCorner(self,car):
        if car.direction == "V":
            return car.begin.y == 0 or car.end.y == self.boardSize - 1
        else:
            return car.begin.x == 0 or car.end.x == self.boardSize - 1

    def __lt__(self,state):
        pass

    def __eq__(self,state):
        pass

    def __hash__(self):
        return hash(str(self.all))

    def __str__(self):
        string = ""
        for y in range(self.boardSize):
            for x in range(self.boardSize):
                if self.is_empty_space(Point(x,y)):
                    string+="# "
                else:
                    string += self.findInBoard(Point(x,y)).name + " "
                if x == self.boardSize-1:
                    string += "\n"
        return string
