
class Game(Problem):
    def __init__(self,inicial,goal = None):
        pass

    
    
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
        action = {}
        for x in estado.carros + [estado.player]:
            percept = estado.percept(x)
            for direction in percept.keys():
                if not percept[direction]:





    def result(self,state,action):
        """

        :param state: an instance of state
        :param action:
        :return:
        """
        pass


    def goal_test(self,state):
        """

        :param state: an instance of state
        :return: true if is the final state
        """
        pass


    def path_cost(self,c,state1,action,state2):
        pass

    def h1(self,no):
        """

        :param no: is a node
        :return: returns the value of the state (a bigger return is a better state)
        """
        pass


#############################

#res = depth_first_tree_search(game)
#res = depth_first_graph_search(game)
#res = uniform_cost_search(game)
#res = iterative_deepening_search(game)
#res = depth_limited_search(game,10)
#res = best_first_graph_search(game,game.h2)
#res = best_first_graph_search(game,game.h3)
#res = astar_search(game,game.h3)
#Para correr tem descomentar o algoritmo que quer
