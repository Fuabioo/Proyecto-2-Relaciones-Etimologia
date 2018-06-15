"""
Testing module
"""
import pytest
import tec.ic.ia.pc2.g08 as g08


def get_two_carrot_input():
    """
    Obtains pre-defined testing base genetic that is assured not to fail
    """
    args = g08.get_args()
    args.genetico = True
    args.derecha = True
    args.individuos = 3
    args.generaciones = 100
    args.vision = 4
    args.zanahorias = 2
    args.tablero_inicial = "_generated_inputs_/4x4(2).txt"
    result = g08.get_result(algorithm="Genetic", args=args)
    return result


def get_one_carrot_input():
    """
    Obtains pre-defined testing base genetic that is assured not to fail
    """
    args = g08.get_args()
    args.genetico = True
    args.derecha = True
    args.individuos = 3
    args.generaciones = 100
    args.vision = 4
    args.zanahorias = 2
    args.tablero_inicial = "_generated_inputs_/4x4(1).txt"
    result = g08.get_result(algorithm="Genetic", args=args)
    return result


class TestGeneral(object):
    """ Test object for proof that the algorithm actually CAN finish """

    def test_comparation(self):
        """
        Comparation between indiviuals that gives a 5
        """
        result = get_two_carrot_input()
        individual_1 = [['>', 'C', ' ', '<'],
                        [' ', 'Z', ' ', ' '],
                        [' ', ' ', ' ', ' '],
                        [' ', ' ', 'Z', ' ']]
        individual_2 = [[' ', 'C', ' ', '<'],
                        [' ', 'Z', ' ', ' '],
                        [' ', ' ', ' ', ' '],
                        [' ', ' ', 'Z', ' ']]
        assert 5 == result.compare(individual_1, individual_2)

    def test_completeness(self):
        """
        Tests if the algorithm gives a result that can be called a result
        """
        result = get_two_carrot_input()
        res = result.run()
        assert res[-1] > 10000

    def test_population_generation(self):
        """
        Tests if the generation of the first population acts correctly
        """
        result = get_two_carrot_input()
        res = result.generate_first_population(12)
        assert len(res) == 12

    def test_bad_fitness(self):
        """
        Tests if the generation of the first population acts correctly
        """
        result = get_two_carrot_input()
        individual_1 = [['>', 'C', ' ', '<'],
                        [' ', 'Z', ' ', ' '],
                        [' ', ' ', ' ', ' '],
                        [' ', ' ', 'Z', ' ']]
        res = result.fitness(individual_1)
        assert res < 0

    def test_good_fitness(self):
        """
        Tests if the generation of the first population acts correctly
        """
        result = get_two_carrot_input()
        individual_1 = [['>', 'C', ' ', 'v'],
                        [' ', 'Z', ' ', ' '],
                        [' ', ' ', ' ', ' '],
                        [' ', ' ', 'Z', '<']]
        res = result.fitness(individual_1)
        assert res > 0

    def test_comparation(self):
        """
        Comparation between indiviuals that gives a 5
        """
        result = get_two_carrot_input()
        individual_1 = [['v', 'C', ' ', '<'],
                        [' ', 'Z', ' ', ' '],
                        [' ', ' ', ' ', ' '],
                        [' ', ' ', 'Z', ' ']]
        individual_2 = [[' ', 'C', ' ', 'v'],
                        [' ', 'Z', ' ', ' '],
                        [' ', ' ', ' ', ' '],
                        [' ', ' ', 'Z', '<']]
        child = result.new_child(individual_1, individual_2)
        assert child != individual_1 or child != individual_2
