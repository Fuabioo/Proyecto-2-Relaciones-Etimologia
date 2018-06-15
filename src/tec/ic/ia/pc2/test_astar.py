"""
Testing module
"""
import pytest
import tec.ic.ia.pc2.g08 as g08


def get_rectangle_input():
    """
    Obtains pre-defined testing base astar that is assured not to fail
    """
    args = g08.get_args()
    args.a_estrella = True
    args.vision = 2
    args.zanahorias = 2
    args.tablero_inicial = "_generated_inputs_/5x4.txt"
    result = g08.get_result(algorithm="AStar", args=args)
    return result


def get_two_carrot_input():
    """
    Obtains pre-defined testing base astar that is assured not to fail
    """
    args = g08.get_args()
    args.a_estrella = True
    args.vision = 2
    args.zanahorias = 2
    args.tablero_inicial = "_generated_inputs_/5x4.txt"
    result = g08.get_result(algorithm="AStar", args=args)
    return result


def get_one_carrot_input():
    """
    Obtains pre-defined testing base astar that is assured not to fail
    """
    args = g08.get_args()
    args.a_estrella = True
    args.vision = 2
    args.zanahorias = 2
    args.tablero_inicial = "_generated_inputs_/4x4(1).txt"
    result = g08.get_result(algorithm="AStar", args=args)
    return result


def get_25_by_25_input():
    """
    Obtains pre-defined testing base astar that is assured not to fail
    """
    args = g08.get_args()
    args.a_estrella = True
    args.vision = 10
    args.zanahorias = 10
    args.tablero_inicial = "_generated_inputs_/25x25(50).txt"
    result = g08.get_result(algorithm="AStar", args=args)
    return result


class TestCompletness(object):
    """ Test object for proof that the algorithm actually CAN finish """

    def test_completeness_one(self):
        """
        Two present carrots and bunny needs two carrots
        """
        result = get_two_carrot_input()
        result.run()
        assert result.args.zanahorias == 0

    def test_completeness_two(self):
        """
        One present carrots but bunny needs two
        """
        result = get_one_carrot_input()
        result.run()
        assert result.args.zanahorias > 0

    def test_completeness_three(self):
        """
        One present carrots but bunny needs two
        """
        result = get_25_by_25_input()
        result.run()
        assert result.args.zanahorias == 0


class TestEnviroment(object):
    """ Test object for enviromental variables """

    def test_enviroment_one(self):
        """
        Test for carrot not present in the enviroment
         -> ValueError: carrot not present in the enviroment
        """
        enviroment = {"bunny": (0, 0)}
        result = get_two_carrot_input()
        result.set_enviroment(enviroment)
        with pytest.raises(ValueError):
            result.run()

    def test_enviroment_two(self):
        """
        Test for bunny not present in the enviroment
         -> ValueError: bunny not present in the enviroment
        """
        enviroment = {"carrot": [(0, 2), (2, 1), (3, 2)]}
        result = get_two_carrot_input()
        result.set_enviroment(enviroment)
        with pytest.raises(ValueError):
            result.run()

    def test_enviroment_three(self):
        """
        Test for incorrect bunny
         -> ValueError: bunny's value must not be None
        """
        enviroment = {"bunny": 0, "carrot": [(0, 2), (2, 1), (3, 2)]}
        result = get_two_carrot_input()
        result.set_enviroment(enviroment)
        with pytest.raises(ValueError):
            result.run()

    def test_enviroment_four(self):
        """
        Test for incorrect carrot
         -> ValueError: carrot's value must not be None
        """
        enviroment = {"bunny": (0, 0), "carrot": []}
        result = get_two_carrot_input()
        result.set_enviroment(enviroment)
        with pytest.raises(ValueError):
            result.run()

    def test_enviroment_five(self):
        """
        Test for correct enviroment, no error shoud be encountered
        """
        result = get_two_carrot_input()
        try:
            result.run()
        except ValueError:
            raise pytest.fail("ValueError encountered")
