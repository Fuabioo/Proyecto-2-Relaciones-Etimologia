"""
A Star Algorithm related stuff module
"""

import shutil
import time
import random

from tec.ic.ia.pc2.data_structures import Graph, PriorityQueue
from tec.ic.ia.pc2.utils import parse_input_a_estrella, load_input, print_console, get_node, hms_string
from tec.ic.ia.pc2.utils import get_direction, write_output_file, format_path, check_root, check_folder


def heuristic(node_1, node_2):
    """ Heuristic when only 4 directions are posible (Manhattan) """
    (x_node_1, y_node_1) = node_1
    (x_node_2, y_node_2) = node_2
    return abs(x_node_1 - x_node_2) + abs(y_node_1 - y_node_2)


class AStar:
    """
    A star algorithm implementation class
    """

    def __init__(self, args=None, enviroment=None, app_root=""):
        self.args = args
        enviroment, graph = parse_input_a_estrella(
            load_input(self.args.tablero_inicial))
        self.enviroment = enviroment or {}  # Estado del (todo) ambiente
        self.graph = graph or Graph()  # Grafo de todo el ambiente

        self.app_root = format_path(app_root)
        self.folders = ["Output"]
        check_root(self.app_root, self.folders)

        self.counter = 0
        self.last = ""

    def set_enviroment(self, enviroment):
        """
        Sets the enviroment variable
        """
        if enviroment:
            self.enviroment = enviroment
        else:
            raise ValueError(
                "enviroment variable must be a non-empty dictionary")

    def a_star_search(self, goal, accesible_nodes):
        """
        Backbone of the algorithm
        """
        initial = self.enviroment["bunny"]
        frontier = PriorityQueue()
        frontier.push(element=initial, priority=0)

        accumulated_cost = {initial: 0}
        paths = {}

        result = {}

        end = False
        while frontier:
            current = frontier.pop()

            if current == goal or end:
                break

            for node in self.graph.neighbors(current):
                if node in accesible_nodes:  # Node in vision field?
                    # cost from current to neighbor = 1
                    current_cost = accumulated_cost[current] + 1
                    if node not in accumulated_cost or current_cost < accumulated_cost[node]:
                        accumulated_cost[node] = current_cost
                        # f(n) = g(n) + h(n)
                        priority = current_cost + heuristic(goal, node)
                        # if self.graph.nodes[node].carrot:
                        #    priority = 1
                        if self.args.debug:
                            print(
                                current,
                                "->",
                                node,
                                ' >>> ',
                                priority,
                                ' = ',
                                current_cost,
                                ' + ',
                                priority -
                                current_cost)
                        result[get_direction(current, node)] = priority
                        paths[current] = node
                        frontier.push(element=node, priority=priority)
        return result, paths

    def get_cost_direction(self, node, accesible_nodes):
        """
        Executes a search for a given goal and gets the result direction
        """
        costs, path = self.a_star_search(node, accesible_nodes)
        next_node = path[self.enviroment["bunny"]]
        next_dir = get_direction(self.enviroment["bunny"], next_node)
        if costs[next_dir] == 0:
            costs[next_dir] = 1
        next_node = min(costs, key=costs.get)
        next_node = get_node(self.enviroment["bunny"], next_node)
        return costs, next_node

    def get_neighbour_costs(self):
        """
        Obtains the cost of the neighbors
        """
        accesible_nodes = self.graph.get_scope_keys(
            self.enviroment["bunny"], self.args.vision)
        all_costs = {}
        next_node = None
        for valid_node in accesible_nodes:
            if self.graph.nodes[valid_node].carrot:
                all_costs, next_node = self.get_cost_direction(
                    valid_node, accesible_nodes)
                break
        if all_costs == {}:
            posibilities = self.graph.neighbors(self.enviroment["bunny"])
            index = random.randint(0, len(posibilities) - 1)
            key = list(posibilities)[index]
            all_costs, next_node = self.get_cost_direction(
                key, accesible_nodes)

        return all_costs, next_node

    def step(self):
        """
        Step execution
        """
        current_pos = self.enviroment["bunny"]
        costs, next_node = self.get_neighbour_costs()

        best_direction = get_direction(current_pos, next_node)

        if best_direction == self.last:
            self.counter += 1
        if self.counter > 15:
            access = self.graph.neighbors(current_pos)
            access.pop(next_node)
            next_node = access[random.randint(0, len(access)-1)]
            best_direction = get_direction(current_pos, next_node)

        # Move bunny and eat if there is a carrot
        self.enviroment["bunny"] = next_node
        if self.graph.nodes[next_node].consume_carrot():
            self.enviroment["carrot"].remove(next_node)
            self.args.zanahorias -= 1

        costs["MOVIMIENTO"] = best_direction
        return costs

    def check_enviroment(self):
        """ Checks that the enviroment is full of necesary variables"""
        enviromental_variables = ["bunny", "carrot", "size"]
        for key in enviromental_variables:
            if key not in self.enviroment:
                raise ValueError(key + " not present in the enviroment")
            value = self.enviroment[key]
            if not value:
                raise ValueError(key + "'s value must not be None")
            if not isinstance(value, list) and not isinstance(value, tuple):
                raise ValueError(key + "'s value must be a list or tuple")
            if isinstance(value, list) and not value:
                raise ValueError(key + "'s value must not be empty")

    def run(self):
        """
        Runs the algorithm
        """
        start = time.time()

        # Check that everything is fine with the enviroment
        self.check_enviroment()

        # Output directory for this run
        curr_out_dir = self.app_root + 'Output/AStar/'
        shutil.rmtree(curr_out_dir, ignore_errors=True)
        check_folder(curr_out_dir)
        print("OUTPUT DIRECTORY", curr_out_dir)

        step_no = 0
        maximum_steps = self.args.limite

        # Initial amount of carrots
        carrot_amount = len(self.enviroment["carrot"])

        # Initial state
        formated_step = format(step_no, '05d')
        write_output_file(
            formated_step,
            curr_out_dir,
            self.enviroment,
            self.args.debug)
        step_no += 1

        result_string = ""

        while True:
            formated_step = format(step_no, '05d')

            if carrot_amount < self.args.zanahorias:
                result_string = "Menos zanahorias de las que conejo ocupa  |  "
            if self.args.zanahorias == 0:
                print("PASO:", formated_step, "FINAL")
                result_string += "Conejo satisfecho!  |  "
                break
            if step_no == maximum_steps:
                print("PASO:", formated_step, "FINAL")
                result_string += "Imposible terminar: Maxima cantidad de pasos  |  "
                break
            scores = self.step()
            print_console(formated_step, scores)
            write_output_file(
                formated_step,
                curr_out_dir,
                self.enviroment,
                self.args.debug)
            step_no += 1

        if result_string != "":
            print(result_string[:-3])
        duration = time.time() - start
        print("Duracion:", hms_string(duration))
        return step_no, duration, result_string
