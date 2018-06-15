"""
Genetic Algorithm module
"""


import random
import time
import copy
import shutil
import os

import functools
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

from tec.ic.ia.pc2.utils import hms_string, format_path, check_root, parse_input_a_estrella, load_input


def print_graph(scores):
    """
    Displays a plot
    """
    plt.title("Algorithm evolution between generations")
    plt.ylabel('Algorithm result')
    plt.xlabel('Generation')
    graph_x = [i for i in range(len(scores))]
    graph_y = scores
    plt.plot(graph_x, graph_y)
    plt.show()


class Genetic:
    """Genetic Algorithm Class"""

    def __init__(self, args=None, enviroment=None, app_root=""):
        self.args = args
        enviroment, _ = parse_input_a_estrella(
            load_input(self.args.tablero_inicial))
        self.enviroment = enviroment or {}  # Estado del (todo) ambiente
        self.app_root = format_path(app_root)
        self.folders = ["Output"]
        check_root(self.app_root, self.folders)

        # Setting the first direction
        if args.arriba:
            self.direction = "up"
        elif args.derecha:
            self.direction = "right"
        elif args.abajo:
            self.direction = "down"
        elif args.izquierda:
            self.direction = "left"

        # Board definition
        self.matrix = [[" " for _ in range(self.enviroment['size'][0])] for _ in range(
            self.enviroment['size'][1])]
        self.bunny = self.enviroment['bunny']
        self.carrots = len(self.enviroment['carrot'])
        self.matrix[self.bunny[0]][self.bunny[1]] = 'C'
        for carrot in self.enviroment['carrot']:
            self.matrix[carrot[0]][carrot[1]] = 'Z'

        # Hyper Params
        # Costs
        self.complete_reward = 10000
        self.carrot_reward = 50
        self.movement_pen = 1
        self.directioner_pen = 5

        # Evolve
        self.size_of_population = args.individuos
        self.mutation_rate = args.taza_mutacion
        self.number_of_child = 20
        self.generations = args.generaciones
        self.policy = args.politica

        # Debug
        self.save_files = args.guardar_archivos
        self.print_result = args.show_graphic

        if self.save_files:
            self.clear_directory()

    def __str__(self):
        string = ""
        string += "----- Algoritmo genetico -----"
        string += "\nConejo " + str(self.bunny)
        string += "\nZanahorias "
        for carrot in self.enviroment["carrot"]:
            string += str(carrot) + ' '
        string += "\nMatriz " + str((len(self.matrix), len(self.matrix[0])))
        string += "\nTamano poblacion " + str(self.size_of_population)
        string += "\nGeneraciones " + str(self.generations)
        string += "\nPolitica de cruce " + str(self.policy)
        string += "\nGuardar archivos " + str(self.save_files)
        string += "\nMostrar grafico " + str(self.print_result)
        string += "\n------------------------------"
        return string

    def run(self):
        """ Run the algorithm """
        start = time.time()

        _, scores = self.evolve(self.size_of_population, self.number_of_child)

        print("Duracion:", hms_string(time.time() - start))
        if self.print_result:
            print_graph(scores)
        return copy.deepcopy(scores)

    def generate_first_population(self, size_of_population):
        """
        Generates the first population (is the first matrix without directions)
        """
        population = []
        index = 0
        while index < size_of_population:
            population.append(self.matrix)
            index += 1
        return population

    def fitness(self, individual):
        """
        Scores the aptitude por each "person"
        """
        gens = ["<", ">", "^", "v"]
        dirs = ["left", "right", "up", "down"]
        bunny_x, bunny_y = self.bunny[0], self.bunny[1]
        individual[bunny_x][bunny_y] = individual[bunny_x][bunny_y][:-1]
        if individual[bunny_x][bunny_y] == "":
            individual[bunny_x][bunny_y] = " "

        carrots = self.carrots
        direction = self.direction
        moves = 0
        states = []
        while carrots > 0:
            state = direction[0] + str(bunny_x) + str(bunny_y)
            if state in states:
                break
            states.append(state)
            moves += 1
            if direction == "up":
                if bunny_x == 0:
                    break
                else:
                    bunny_x -= 1
            elif direction == "down":
                if bunny_x == len(individual) - 1:
                    break
                else:
                    bunny_x += 1
            elif direction == "left":
                if bunny_y == 0:
                    break
                else:
                    bunny_y -= 1
            else:
                if bunny_y == len(individual[0]) - 1:
                    break
                else:
                    bunny_y += 1

            if individual[bunny_x][bunny_y] == "Z":
                carrots -= 1
                individual[bunny_x][bunny_y] = " "
            elif individual[bunny_x][bunny_y] != " ":
                direction = dirs[gens.index(individual[bunny_x][bunny_y])]

        signals = 0
        for i in range(len(individual)):
            for j in range(len(individual[0])):
                if individual[i][j] != " " and individual[i][j] != "Z":
                    signals += 1

        result = 0
        if carrots == 0:
            result = self.complete_reward
        result += (self.carrots - carrots) * self.carrot_reward
        result -= moves * self.movement_pen
        result -= signals * self.directioner_pen

        return result

    def compare(self, individual1, individual2):
        """
        Compares two individuales
        """
        return self.fitness(copy.deepcopy(individual2)) - \
            self.fitness(copy.deepcopy(individual1))

    def sort_population_by_fitness(self, population):
        """
        Sorts the populations by their fitness
        """
        sorted_population = sorted(
            population, key=functools.cmp_to_key(self.compare))
        return sorted_population

    def evolve(self, size_of_population, number_of_child):
        """
        Evolves an individual
        """
        # temps_init = time.time()
        result = []
        scores = []
        population = self.generate_first_population(size_of_population)
        for i in range(self.generations):
            children = self.new_generation(population, number_of_child)
            population += children
            bck = copy.deepcopy(population)
            _, to_mute, _, _ = train_test_split(
                bck, bck, test_size=self.mutation_rate)
            population += self.mute(to_mute)
            population = self.sort_population_by_fitness(population)
            population = population[:size_of_population]
            result.append(population[0])
            scores.append(self.fitness(copy.deepcopy(population[0])))
            if self.save_files:
                self.create_file(population, i)
                
            print("GENERACION: "+str(i).zfill(5))
            bck = copy.deepcopy(population)
            for i in range(size_of_population):
                print("INDIVIDUO "+str(i).zfill(5)+ " APTITUD:" + str(self.fitness(bck[i])))
        return result, scores

    def new_generation(self, population, size_of_population):
        """
        Returns the children of the current population
        """
        kids = []
        index = 0
        while index < size_of_population:
            kids.append(self.new_child(random.choice(
                population), random.choice(population)))
            index += 1
        return kids

    def mute(self, to_mute):
        """
        Mutates and individual
        """
        gens = ["<", ">", "^", "v", " "]
        directions = []
        for person in to_mute:
            x, y = random.randint( 0, len(person) - 1), random.randint(0, len(person[0]) - 1)
            mutation = random.choice(gens)
            if person[x][y] != "C" and person[x][y] != "Z":
                person[x][y] = mutation
        return to_mute

    def new_child(self, mother, father):
        """
        Obtains a child given two parents
        """
        result = None
        if self.policy == "gen":
            result = self.gen_policy(mother, father)
        else:
            result = self.row_policy(mother, father)
        return result

    def gen_policy(self, mother, father):
        """
        Mating policy gen by gen
        """
        result = copy.deepcopy(mother)
        for i in range(len(result)):
            for j in range(len(result[0])):
                if random.choice((True, False)):
                    result[i][j] = father[i][j]
        return result

    def row_policy(self, mother, father):
        """
        Mating policy for rows
        """
        index = random.randint(0, len(mother))
        return mother[:index] + father[index:]

    def clear_directory(self):
        """ Clears a directory """
        shutil.rmtree(self.app_root + 'Output/Genetic/' +
                      self.direction, ignore_errors=True)

    def create_file(self, population, generation):
        """
        Creates a file for the population
        """
        for i in range(len(population)):
            filename = self.app_root + 'Output/Genetic/' + self.direction + "/" + \
                str(generation).zfill(5) + "/" + str(i).zfill(5) + ".txt"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            string = ""
            for j in range(len(population[i])):
                string += "".join(population[i][j]) + '\n'
            with open(filename, "w") as file:
                file.write(string)
                file.close()
