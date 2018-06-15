"""
Pytest for Logic Idiom-Word Module
"""

from model import Model
import logic_i_w


class Dummy:
    """Dummy console, this prevents modifying the code for the logic_w_w"""

    def __init__(self):
        self.dummy = ""  # Dummy variable

    def print(self, *args):
        """dummy function"""
        self.dummy = args


class TestLogicIW(object):
    """ Test object validation for the logic"""

    def test_related_1(self):
        """Test Case: hijo is related to primo? -> Yes"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" abuelo",spa," padre",spa)',
            '+ etymological_origin_of(" abuelo",spa," tio",spa)',
            '+ etymological_origin_of(" padre",spa," hijo",spa)',
            '+ etymological_origin_of(" tio",spa," primo",spa)']
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
        result = logic_i_w.related(
            "hijo",
            "spa",
            "primo",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_related_2(self):
        """Test Case: hijo is related to primo? -> No"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" abuelo",spa," padre",spa)',
            '+ etymological_origin_of(" abuelo",spa," tio",spa)',
            '+ etymological_origin_of(" padre",spa," hijo",spa)',
            '+ etymological_origin_of(" tio",rus," primo",rus)']
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
        result = logic_i_w.related(
            "hijo",
            "spa",
            "primo",
            "rus",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result
