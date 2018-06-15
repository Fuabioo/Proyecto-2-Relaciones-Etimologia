"""
Pytest for Logic Idiom-Idiom Module
"""

from model import Model
import logic_i_i


class Dummy:
    """Dummy console, this prevents modifying the code for the logic_w_w"""

    def __init__(self):
        self.dummy = ""  # Dummy variable

    def print(self, *args):
        """dummy function"""
        self.dummy = args


class TestLogicIW(object):
    """ Test object validation for the logic"""

    def test_common_amount_1(self):
        """Test Case: spa is related to primo? -> Yes"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" taco",spa," burrito",spa)',
            '+ etymological_origin_of(" taco",eng," burrito",eng)',
            '+ etymological_origin_of(" taco",deu," burrito",deu)']
        model_test.append_data(data_pool)
        model_test.load(Dummy())
        relations = {
            'derived': False,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': True,
            'is_derived_from': False,
            'variant': False}
        result = logic_i_i.common_amount(
            "-",
            "-",
            "eng",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result
