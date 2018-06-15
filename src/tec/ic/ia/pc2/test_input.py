"""
Testing module
"""
from tec.ic.ia.pc2.utils import load_input, get_characters, parse_input_a_estrella


class TestInput(object):
    """ Test object for validation of the utils module"""

    def test_input(self):
        """
        Tests an arbitrary input of 4x5 and checks that the dimensions are correct
        """
        table = load_input("_generated_inputs_/5x4.txt")
        assert len(table) == 4 and len(table[0]) == 5 + 1  # EOL character

    def test_input_consistency_1(self):
        """
        Tests an arbitrary input of 4x5 and checks that it has indeed 2 carrots
        """
        table = load_input("_generated_inputs_/5x4.txt")
        assert sum(row.count("Z") for row in table) == 2

    def test_input_consistency_2(self):
        """
        Tests an arbitrary input of 4x5 and checks that it has a bunny
        """
        table = load_input("_generated_inputs_/5x4.txt")
        assert sum(row.count("C") for row in table) == 1

    def test_input_consistency_3(self):
        """
        Checks that the input table is according to the default valid characters
        """
        result = True

        valid_characters = get_characters()

        # Valid table
        table = load_input("_generated_inputs_/5x4.txt")
        for row in table:
            for character in row:
                result = result and character in valid_characters.values()
        assert result

    def test_enviroment_generation_1(self):
        """
        Checks if the enviroment dictionary size is fine
        """
        table = load_input("_generated_inputs_/5x4.txt")
        enviroment, _ = parse_input_a_estrella(table)
        assert len(list(enviroment.keys())) == 3

    def test_enviroment_generation_2(self):
        """
        Checks if the enviroment dictionary has "bunny" key
        """
        table = load_input("_generated_inputs_/5x4.txt")
        enviroment, _ = parse_input_a_estrella(table)
        assert "bunny" in enviroment.keys()

    def test_enviroment_generation_3(self):
        """
        Checks if the enviroment dictionary has "carrot" key
        """
        table = load_input("_generated_inputs_/5x4.txt")
        enviroment, _ = parse_input_a_estrella(table)
        assert "carrot" in enviroment.keys()

    def test_enviroment_generation_4(self):
        """
        Checks if the enviroment dictionary has "size" key
        """
        table = load_input("_generated_inputs_/5x4.txt")
        enviroment, _ = parse_input_a_estrella(table)
        assert "size" in enviroment.keys()
