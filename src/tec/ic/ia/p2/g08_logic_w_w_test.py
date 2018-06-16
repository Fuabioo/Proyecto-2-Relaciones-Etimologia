"""
Pytest for Logic Word-Word Module
"""

from tec.ic.ia.p2.g08_model import Model
from tec.ic.ia.p2 import g08_logic_w_w


class Dummy:
    """Dummy console, this prevents modifying the code for the logic_w_w"""

    def __init__(self):
        self.dummy = ""  # Dummy variable

    def print(self, *args):
        """dummy function"""
        self.dummy = args


class TestLogicWW(object):
    """ Test object validation for the logic"""

    def test_brothers_1(self):
        """Test Case: tio(esp) is brother of abuelo(esp)? -> No"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.brother(
            "tio",
            "esp",
            "abuelo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_brothers_2(self):
        """Test Case: tio(esp) is brother of padre(esp)? -> Yes"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.brother(
            "padre",
            "esp",
            "tio",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_child_1(self):
        """Test Case: padre(esp) is child of abuelo(esp)? -> Yes"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.child(
            "padre",
            "esp",
            "abuelo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_child_2(self):
        """Test Case: tio(esp) is child of yo(esp)? -> No"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.child(
            "tio",
            "esp",
            "yo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_uncle_1(self):
        """Test Case: tio(esp) is uncle of primo(esp)? -> No"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.uncle(
            "tio",
            "esp",
            "primo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_uncle_2(self):
        """Test Case: primo(esp) is uncle of yo(esp)? -> No"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.uncle(
            "primo",
            "esp",
            "yo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_uncle_3(self):
        """Test Case: "tio" is uncle of "sobrino"? -> Yes"""
        model_test = Model()
        data_pool = [
            '+ etymological_origin_of(" abuelo",spa," padre",spa)',
            '+ etymological_origin_of(" abuelo",spa," tio",spa)',
            '+ etymological_origin_of(" padre",spa," sobrino",spa)']
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
        result = g08_logic_w_w.uncle(
            "tio",
            "spa",
            "sobrino",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_cousin_1(self):
        """Test Case: tio(esp) is cousin of primo(esp)? -> No"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.cousin(
            "tio",
            "esp",
            "primo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_2(self):
        """Test Case: tio(esp) is cousin of yo(esp)? -> No"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.cousin(
            "tio",
            "esp",
            "yo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_3(self):
        """Test Case: hijo is cousin of primo? -> Yes"""
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
        result = g08_logic_w_w.cousin(
            "hijo",
            "spa",
            "primo",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result

    def test_cousin_level_1(self):
        """Test Case: tio(esp) cousin level of abuelo(esp)? -> Not cousins"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.cousin_level(
            "tio",
            "esp",
            "abuelo",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_level_2(self):
        """Test Case: yo(esp) cousin level of tio(esp)? -> Not cousins"""
        thread = "esp_derived_esp.cl"
        model_test = Model()
        model_test.set_cl_file(thread)
        model_test.parse_file()
        model_test.load(Dummy())
        relations = {
            'derived': True,
            'etymologically': False,
            'etymology': False,
            'etymologically_related': False,
            'has_derived_form': False,
            'etymological_origin_of': False,
            'is_derived_from': False,
            'variant': False}
        result = g08_logic_w_w.cousin_level(
            "yo",
            "esp",
            "tio",
            "esp",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = False
        assert result == expected_result

    def test_cousin_level_3(self):
        """Test Case: hijo cousin level of primo? -> 1"""
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
        result = g08_logic_w_w.cousin_level(
            "hijo",
            "spa",
            "primo",
            "spa",
            Dummy(),
            model_test.get_logic(),  # data
            relations)
        expected_result = True
        assert result == expected_result
