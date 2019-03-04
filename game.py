

from car import *
from estado import Estado
from search import *
from copy import deepcopy

class Game(Problem):
    def __init__(self,inicial,goal = None):
        super().__init__(inicial)
        self.goal = goal

    
    
    def actions(self,estado):
        """
        :param state: an instance of state
        :return:
        {
            carA: [left1, left2, right1],
            carB: [left1, right1],
            carC: [up1, up2, up3],
        }

        """
        actions = []
        for each in estado.all.values():
            perception = estado.percept(each)
            for percept in perception:
                valid = 1
                distances = list(map(lambda x:each.distance(x,percept), perception[percept]))
                isValid = True
                if len(distances) > 0:
                    while isValid:
                        if valid < min(distances):
                            actions.append((each,percept,valid))
                        else:
                            isValid = False
                        valid+=1
                else:
                    distanceToWall = each.distanceToWall(percept,estado.boardSize)
                    for x in range(distanceToWall):
                        actions.append((each,percept,x + 1))
        return actions



    def result(self,state,action):
        """

        :param state: an instance of state
        :param action:
        :return:
        """
        newState = deepcopy(state)
        car = action[0]
        direction = action[1]
        distance = action[2]
        if direction == "down":
            newState.all[car.name].move_down(distance)
        elif direction == "up":
            newState.all[car.name].move_up(distance)
        elif direction == "esq":
            newState.all[car.name].move_left(distance)
        elif direction == "dir":
            newState.all[car.name].move_right(distance)
        return newState


    def goal_test(self,state):
        """

        :param state: an instance of state
        :return: true if is the final state
        """
        if state.all["?"].end.y == state.exit.point.y and state.all["?"].end.x == state.exit.point.x:
            return True
        return False


    def path_cost(self,c,state1,action,state2):
        pass


    def h1(self,no):
        """
        valorizar mais se consegui andar, segundo se abrir caminho
        :param no: is a node
        :return: returns the value of the state (a bigger return is a better state)
        """
        actions = self.actions(no.state)
        h = 5
        for action in actions:
            if action[0].name == "?":
                h-=1
        return h


    def h2(self,no):
        h = 0
        for each in filter(lambda x:x.name != "?",no.state.all.values()):
            if no.state.inCorner(each):
                h+=1
        return h


    def h3(self,no):
        distanceToExit  = no.state.getPlayer().distanceToWall("dir",no.state.boardSize)
        return distanceToExit


    def h4(self,no):
        h = self.h1(no)
        h+= self.h3(no)
        return h

def from_file(file_name):
    board_size = 0
    player = Car("?")
    exit_space = None
    all = {}
    with open(file_name, 'r') as f:
        y = 0
        for row in f.readlines():
            x = 0
            for col in row:
                if col == "?":
                    if not player.begin:
                        player.set_begin(x, y)
                    else:
                        player.set_end(x, y)
                        all[col] = player
                elif col == "S":
                    exit_space = Space(x, y,col)
                elif col == " " or col == '\n':
                    x -= 1
                elif col != "?" and col != "#" and col != "S":
                    car = Car(col)
                    if col not in all:
                        car.set_begin(x, y)
                        all[col] = car
                    else:
                        all[col].set_end(x, y)
                x += 1

            y += 1
    return Estado(all, exit_space,6)


car = Car("B")
car.set_begin(0,0)
car.set_end(0,2)
car.move_down(1)

estado = from_file("examples.txt")
#print(estado)
game = Game(estado)
print(estado)
#print(estado.inCorner(car))
#print(game.h1(estado))
#print(estado.percept(car))
#print(game.actions(estado))
#print(game.result(estado,(car,"down",1)))
#############################

#res = depth_first_tree_search(game)
#res = depth_first_graph_search(game)
#res = uniform_cost_search(game)
#res = iterative_deepening_search(game)
#res = depth_limited_search(game,10)
res = best_first_graph_search(game,game.h3)
#print(res.path())
#print(res.solution())
#res = best_first_graph_search(game,game.h3)
#res = astar_search(game,game.h3)
#Para correr tem descomentar o algoritmo que quer
